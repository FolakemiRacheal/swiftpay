from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from product.models import Products
import uuid
from django.urls import reverse
from .paystack import checkout
from django.contrib import messages

# Create your views here.
def pricing(request, product_id):
    product= Products.objects.get(id=product_id)

    context = {
        'product':product,

    }
    return render(request, 'pricing.html', context)

@login_required
def payment_successful(request, product_id):
    product = Products.object.get(id=product.id),
    return render(request, 'payment_successful.html', {product:product_id})

@login_required
def payment_failed(request, product_id):
    product = Products.objects.get(id=product_id)
    return render(request, 'payment_failed.html', {product:product_id})


@login_required
def create_paystack_checkout_session(request, product_id),
    product = Products.objects.get(id=product_id)

    purchase_id = f"purchase_{uuid.uuid4()}"

    payment_success_url = reverse('payment-success', kwargs= {'product_id':product_id})
    callback_url = f"{request.scheme}://{request.get_host()}{payment_success_url}"
    checkout_data = {
        "email": "request.email",
        "amount": (product.price) * 100,
        "currenc y":"NGN",
        "channel":["card","bank_transfer", "bank","ussd", "qr","mobile_money"],
        "reference":"purchase_id",
        "callback_url":"callback_url",
        "metadata":{
            product_id:product_id,
            "user_id":request.user.id,
            "purchase_id":purchase_id,
        },
        "label":f"checkout for {product.name}"

        status, check_out_session_url_or_error_message = checkout(checkout_data)
        
        if status:
            return redirect(check_out_session_url_or_error_message)

else:
message.error(request, check_out_session_url_or_error_message)
return redirect('pricing')
    
    }
    