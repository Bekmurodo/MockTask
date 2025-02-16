from django.core.management.base import BaseCommand
from warehouse.models import Product, Material, ProductMaterial, Warehouse

class Command(BaseCommand):
    help = 'Seed the database with initial data'

    def handle(self, *args, **kwargs):
        # Mahsulotlar
        shirt = Product.objects.create(name="Ko'ylak", code="238923")
        pants = Product.objects.create(name="Shim", code="238924")

        # Xomashyolar
        fabric = Material.objects.create(name="Mato")
        button = Material.objects.create(name="Tugma")
        thread = Material.objects.create(name="Ip")
        zipper = Material.objects.create(name="Zamok")

        # Mahsulot-Xomashyo
        ProductMaterial.objects.create(product=shirt, material=fabric, quantity=0.8)
        ProductMaterial.objects.create(product=shirt, material=button, quantity=5)
        ProductMaterial.objects.create(product=shirt, material=thread, quantity=10)
        ProductMaterial.objects.create(product=pants, material=fabric, quantity=1.4)
        ProductMaterial.objects.create(product=pants, material=thread, quantity=10)
        ProductMaterial.objects.create(product=pants, material=zipper, quantity=1)

        # Omborxona
        Warehouse.objects.create(material=fabric, remainder=24, price=1500)
        Warehouse.objects.create(material=fabric, remainder=12, price=1600)
        Warehouse.objects.create(material=button, remainder=150, price=300)
        Warehouse.objects.create(material=thread, remainder=300, price=500)
        Warehouse.objects.create(material=thread, remainder=260, price=550)
        Warehouse.objects.create(material=zipper, remainder=20, price=2000)

        self.stdout.write(self.style.SUCCESS('Database seeded successfully'))