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
        item_name = req.POST.get('item_name')
        print(type(price))
        amount = float(price)*100
        data = { "amount": amount, 
                "currency": "INR", 
                "receipt": "order_rcptid_11",
                "notes":{
                    "item_name":item_name,
                } 
                }
        client = razorpay.Client(auth =("rzp_test_pr99iascS1WRtU" , "UTDIzPGwICnAssu3Q3lk7zUi"))
        payment = client.order.create(data=data)
        print(payment)
        Order.objects.create(
            Order_id = payment.get('id'),
            Amount= int(price),
        )
    return render(req,'landing.html',{'payment':payment,'amount':price,'item_name': item_name})


def order_status(req):
    print(req.POST)
    rpi = req.POST.get('razorpay_payment_id')
    roi = req.POST.get('razorpay_order_id')
    print(rpi)
    print(roi)
    old_roi = Order.objects.get(Order_id=roi)
    old_roi.Razorpay_Id = rpi
    old_roi.Status = True
    old_roi.save()
    return render(req,'success.html')