from django.conf import settings
from django.core.mail import send_mail


def send_order_notification(order):
    send_mail(
        subject=f"Order #{order.id} Confirmation",
        message=f"""
Hello {order.user.username},

Your order #{order.id} has been placed successfully.

Subtotal: ₹{order.subtotal}
Tax: ₹{order.tax_amount}
Grand Total: ₹{order.grand_total}

Thank you for shopping with CJCMART.
""",
        from_email=settings.DEFAULT_FROM_EMAIL,
        recipient_list=[order.user.email],
        fail_silently=False,
    )