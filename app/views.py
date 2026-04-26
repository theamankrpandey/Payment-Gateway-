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




# views.py

# def add_item(req):
#     if req.method == "POST":
#         item = req.POST.get('item')   # user se item lena

#         cart = req.session.get('cart', [])   # old cart
#         cart.append(item)                   # new item add

#         req.session['cart'] = cart         # save in session

#     return redirect('home')

def add_item(req):
    cart ={}
    if req.method == "POST":
        item = req.POST.get("item")
        products = {
            "Shirt": 500,
            "Shoes": 1200,
            "Watch": 2500,
            "Bag": 900,
            "Mobile Cover": 300
        }

        if item in products:
            cart[item] = products[item]

    return render(req, "index.html", {"cart": cart})