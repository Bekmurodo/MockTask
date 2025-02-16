from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Product, ProductMaterial, Warehouse
from .serializers import ProductSerializer, WarehouseSerializer

class ProductMaterialsView(APIView):
    def post(self, request):
        product_code = request.data.get('product_code')
        quantity = request.data.get('quantity')

        try:
            product = Product.objects.get(code=product_code)
        except Product.DoesNotExist:
            return Response({"error": "Product not found"}, status=status.HTTP_404_NOT_FOUND)

        product_materials = ProductMaterial.objects.filter(product=product)
        materials_needed = []

        for pm in product_materials:
            total_needed = pm.quantity * quantity
            warehouses = Warehouse.objects.filter(material=pm.material).order_by('id')
            allocated = []

            for warehouse in warehouses:
                if total_needed <= 0:
                    break
                allocated_qty = min(warehouse.remainder, total_needed)
                allocated.append({
                    "warehouse_id": warehouse.id,
                    "material_name": pm.material.name,
                    "qty": allocated_qty,
                    "price": warehouse.price
                })
                total_needed -= allocated_qty

            if total_needed > 0:
                allocated.append({
                    "warehouse_id": None,
                    "material_name": pm.material.name,
                    "qty": total_needed,
                    "price": None
                })

            materials_needed.extend(allocated)

        response_data = {
            "product_name": product.name,
            "product_qty": quantity,
            "product_materials": materials_needed
        }

        return Response({"result": [response_data]}, status=status.HTTP_200_OK)