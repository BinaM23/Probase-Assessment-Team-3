from django.shortcuts import render
from .models import Payment
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