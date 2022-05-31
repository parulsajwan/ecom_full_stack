# ###
# URL patterns for Product
# ###

from django.urls import path, include

from . import views 

# for  Products
urlpatterns = [
   path('list/',views.ProductListView.as_view(), name="listings"),
   path('add/', views.ProductCreateView.as_view(), name="add_product"),
   path('', views.ProductView, name="add"),
   path('<int:pk>', views.ProductRetrieveUpdateDestroyView.as_view() ,name="listing"),
]
