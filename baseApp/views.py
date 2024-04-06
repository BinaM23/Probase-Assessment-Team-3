from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from .models import Payment
from django.http import HttpResponseBadRequest


# Create your views here.
def index(request):
    return render(request, 'index.html')

def payment(request):
    return render(request, 'payment.html')

def paymentSuccess(request):
    if request.method == 'POST':
        # Extract form data from the request
        cardholder = request.POST.get('cardholder')
        cardnumber = request.POST.get('cardnumber')
        expirydate = request.POST.get('expirydate')
        cvc = request.POST.get('cvc')
        amount = request.POST.get('amount')

        # Validate input
        if not cardholder or not cardnumber or not expirydate or not cvc or not amount:
            return HttpResponseBadRequest('Missing required fields')

        if not cardnumber.isdigit() or len(cardnumber) != 16:
            return HttpResponseBadRequest('Invalid card number, card number should be 16 characters long')

        if len(expirydate) != 5 or not expirydate[:2].isdigit() or not expirydate[3:].isdigit() or expirydate[2] != '/':
            return HttpResponseBadRequest('Invalid expiry date format')

        if not cvc.isdigit() or len(cvc) != 3:
            return HttpResponseBadRequest('Invalid CVC, cvv/cvc should be 3 charactes long')

        try:
            amount = float(amount)
            if amount <= 0:
                raise ValueError
        except ValueError:
            return HttpResponseBadRequest('Invalid amount')

        # Create a new Payment object and save it to the database
        payment = Payment.objects.create(
            cardholder=cardholder,
            cardnumber=cardnumber,
            expirydate=expirydate,
            cvc=cvc,
            amount=amount
        )

        # Optionally, you can redirect to a success page after recording the payment
        return render(request, 'paymentSuccess.html')  # Assuming 'payment_success' is the name of your success page URL pattern
    else:
        # Handle GET requests if needed
        return render(request, 'payment.html')
    
def payment_success(request):
    return render(request, 'paymentSuccess.html')