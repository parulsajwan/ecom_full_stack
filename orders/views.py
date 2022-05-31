from django.shortcuts import render, redirect
from django.core.exceptions import ObjectDoesNotExist
from django.contrib import messages
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from rest_framework import generics
from django.views.generic import View
from django.urls import reverse_lazy
from .models import Order
from .serializers import OrderSerializer
from django.views.generic.edit import DeleteView

from django.urls import reverse


@method_decorator(csrf_exempt, name='dispatch')
class OrderListView(generics.ListAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

    def get(self, request, *args, **kwargs):
        queryset = Order.objects.filter(user=request.user)
        serializer = OrderSerializer(queryset, many=True)
        context = {
            'data': serializer.data
        }
        return render(request, 'user/order.html', context)


class OrderCreateView(View):
    def post(self, *args, **kwargs):
        try:
            if self.request.user.is_authenticated:
                user = self.request.user.id
                product_id = self.request.POST['id']
                order = Order.objects.create(
                    user_id=user, product_id=product_id)
                order.save()
                messages.success(self.request, "Successfully ordered")
                return redirect("orders_list")
            messages.error(self.request, "Not a authenticated user")
            return redirect('login')
        except ObjectDoesNotExist:
            messages.info(self.request, "There is some error in your order")
            return redirect("orders_list")


class OrderDestroyView(DeleteView):
    model = Order
    template_name = 'user/order.html'
    success_url = reverse_lazy('orders_list')
