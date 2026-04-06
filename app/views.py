from django.shortcuts import render
from django.http import HttpResponse
import razorpay
from .models import *
# Create your views here.
def landing(req):
    return render(req,'landing.html')

def pay_amount(req):
    if req.method=='POST':
        price = req.POST.get('amount')
        print(type(price))
        amount = float(price)*100
        client = razorpay.Client(auth =("rzp_test_pr99iascS1WRtU" , "UTDIzPGwICnAssu3Q3lk7zUi"))
        data = { "amount": amount, "currency": "INR", "receipt": "order_rcptid_11" }
        payment = client.order.create(data=data)
        print(payment)
        Order.objects.create(
            Order_id = payment.get('id'),
            Amount= int(price),
        )
    return render(req,'landing.html',{'payment':payment,'amount':price})