from rest_framework import generics
from models import Employee, Product, Customer, Bill, BillItem
from serializers import EmployeeSerializer, ProductSerializer, CustomerSerializer, BillSerializer, BillItemSerializer

class EmployeeListCreate(generics.ListCreateAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer

class EmployeeRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
  
