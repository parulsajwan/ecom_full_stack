# ###
# URL patterns for Order
# ###

from django.urls import path, include

from .views import OrderListView, OrderCreateView, OrderDestroyView

# for  Products
urlpatterns = [
    path('list/', OrderListView.as_view(), name="orders_list"),
    path('', OrderCreateView.as_view(), name="orders"),
    path('delete/<int:pk>', OrderDestroyView.as_view(), name="order_by_id"),
]
