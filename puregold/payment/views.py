from django.shortcuts import render, get_object_or_404, redirect
from .models import Payment
from django.contrib import messages
from django.contrib.auth.decorators import login_required
# from paypal.standard.forms import PayPalPaymentsForm
from django.shortcuts import render
from django.urls import reverse

# def paypal_payment(request):
#     paypal_dict = {
#         "business": "your-paypal-business-email@example.com",
#         "amount": "10.00",
#         "item_name": "Test Product",
#         "invoice": "unique-invoice-id-001",
#         "currency_code": "USD",
#         "notify_url": request.build_absolute_uri(reverse('paypal-ipn')),
#         "return_url": request.build_absolute_uri('/payment-done/'),
#         "cancel_return": request.build_absolute_uri('/payment-cancelled/'),
#     }

#     form = PayPalPaymentsForm(initial=paypal_dict)
#     context = {"form": form}
#     return render(request, "payment.html", context)

@login_required(login_url='/login/')
def gcash_payment_view(request, id):
    payment = get_object_or_404(Payment, id=id)

    if request.method == 'POST':
        uploaded_image = request.FILES.get('image')
        if uploaded_image:
            payment.image = uploaded_image
            payment.status = 'pending' 
            payment.save()
            messages.success(request, "Your GCash proof has been submitted.")
            return redirect('order:thank-you')

    context = {
        'payment': payment
    }
    return render(request, 'gcash.html', context)
