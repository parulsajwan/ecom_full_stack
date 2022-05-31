from django.shortcuts import render, redirect
from django.core.exceptions import ObjectDoesNotExist
from django.views.generic import View
from django.contrib import messages
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from rest_framework import generics
from rest_framework.renderers import TemplateHTMLRenderer
from .models import Product
from .serializers import ProductSerializer


def ProductView(request):
    return render(request, 'products/add_product.html')


@method_decorator(csrf_exempt, name='dispatch')
class ProductListView(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'products/listing.html'

    def get(self, request, *args, **kwargs):
        serializer = ProductSerializer(self.get_queryset(), many=True)
        context = {
            'listings': serializer.data
        }
        return render(request, 'products/listings.html', context)


@method_decorator(csrf_exempt, name='dispatch')
class ProductCreateView(View):
    def post(self, *args, **kwargs):
        try:
            if self.request.user.is_superuser:
                user = self.request.user.id
                product_name = self.request.POST['product_name']
                product_description = self.request.POST['product_description']
                product_price = self.request.POST['product_price']
                product_stock = self.request.POST['product_stock']

                product = Product.objects.create(
                    name=product_name,
                    description=product_description,
                    price=product_price,
                    stock=product_stock
                )
                product.save()
                messages.success(self.request, "Successfully added a product")
                return redirect("listings")
            messages.error(
                self.request, "Don't have permission to add a product")
            return redirect('login')
        except ObjectDoesNotExist:
            messages.info(self.request, "There is some error")
            return redirect("products/listing.html")


@method_decorator(csrf_exempt, name='dispatch')
class ProductRetrieveUpdateDestroyView(generics.RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'products/listing.html'

    def get(self, request, *args, **kwargs):
        pk = self.kwargs.get('pk')
        queryset = Product.objects.filter(id=pk)
        serializer = ProductSerializer(queryset, many=True)
        context = {
            'listing': serializer.data
        }
        return render(request, 'products/listing.html', context)
