from django.db import models

class Employee(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)

class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)

class Customer(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)

class Bill(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

class BillItem(models.Model):
    bill = models.ForeignKey(Bill, on_delete=models.CASCADE, related_name='items')
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)