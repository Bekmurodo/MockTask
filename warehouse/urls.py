from django.urls import path
from .views import ProductMaterialsView

urlpatterns = [
    path('product-materials/', ProductMaterialsView.as_view(), name='product-materials'),
]