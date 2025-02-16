from rest_framework import serializers
from .models import Product, Material, ProductMaterial, Warehouse

class MaterialSerializer(serializers.ModelSerializer):

  class Meta:
      model = Material
      fields = ['id', 'name']

class ProductMaterialSerializer(serializers.ModelSerializer):
  material = MaterialSerializer()

  class Meta:
      model = ProductMaterial
      fields = ['material', 'quantity']

class WarehouseSerializer(serializers.ModelSerializer):
  material = MaterialSerializer()

  class Meta:
      model = Warehouse
      fields = ['id', 'material', 'remainder', 'price']

class ProductSerializer(serializers.ModelSerializer):
  materials = ProductMaterialSerializer(many=True, read_only=True)

  class Meta:
      model = Product
      fields = ['id', 'name', 'code', 'materials']