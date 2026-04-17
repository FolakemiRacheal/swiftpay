# from django.db import models
# import uuid
# from django.contrib.auth.models import User
# from product.models import Products as Product

# # Create your models here.

# class Payment(models.Model):
#     user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
#     transaction_id = models.CharField(max_length=100, default=uuid.uuid4())
#     amount = models.DecimalField()
#     payment_status = models.BooleanField(default=False)
#     product = models.ForeignKey(Product, on_delete=models.CASCADE)
#     created_at = models.DateTimeField(auto_now_add=True)



from django.db import models

# Create your models here.
# payments/models.py

from product.models import Order


class Payment(models.Model):
    STATUS_CHOICES = (
        ("pending", "Pending"),
        ("successful", "Successful"),
        ("failed", "Failed"),
    )

    PAYMENT_METHOD_CHOICES = (
        ("paystack", "Paystack"),
        # ("stripe", "Stripe"),
        # ("nova", "Nova Payment"),
        # ("payaza", "Payaza"),
    )

    CURRENCY_CHOICES = (
        ("NGN", "Nigerian Naira"),
        ("USD", "US Dollar"),
    )

    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name="payments")
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    currency = models.CharField(max_length=3, choices=CURRENCY_CHOICES, default="NGN")
    reference = models.CharField(max_length=100, unique=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default="pending")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    payment_method = models.CharField( max_length=50,choices=PAYMENT_METHOD_CHOICES, default="paystack",
    )
    metadata = models.JSONField(default=dict)

    def __str__(self):
        return f"Payment #{self.reference} for Order #{self.order.order_number}"
