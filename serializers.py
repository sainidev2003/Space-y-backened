from rest_framework import serializers
from models import Employee, Product, Customer, Bill, BillItem

class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = '__all__'

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'

class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = '__all__'

class BillSerializer(serializers.ModelSerializer):
    items = ProductSerializer(many=True)

    class Meta:
        model = Bill
        fields = '__all__'

class BillItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = BillItem
        fields = '__all__'