from django.db import models

# Create your models here.

class Payment(models.Model):
    cardholder = models.CharField(max_length=255)
    cardnumber = models.CharField(max_length=16)  # Assuming a typical credit card number length
    expirydate = models.CharField(max_length=5)   # Assuming MM/YY format
    cvc = models.CharField(max_length=3)
    amount = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f'Payment - Cardholder: {self.cardholder}, Card Number: {self.cardnumber}'
