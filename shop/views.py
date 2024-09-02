from django.shortcuts import render
from django.http import HttpResponse
from .models import Product,Contact,Orders
from math import ceil
# Create your views here.



def index(request):
    # products= Product.objects.all()
    # n= len(products)
    # nSlides= n//3 + ceil((n/3) + (n//3))

    # print(products)
    # print(n, nSlides,range(1,nSlides))

    # allprod=[[products,nSlides,range(0,nSlides)],
    #          [products,nSlides,range(0,nSlides)]]


    allProd=[]
    category = Product.objects.values('category','id')

    catdict = {item['category'] for item in category} 
    print(catdict)

    for cat in catdict:
        prod = Product.objects.filter(category=cat)
        n= len(prod)
        nSlides= n//3 + ceil((n/3) + (n//3))
        allProd.append([prod,nSlides,range(nSlides)])
        
    # params={'no_of_slides':nSlides, 'range':range(1,nSlides), 'product': products}
    params={'allprod': allProd}
    return render(request,"shop/index.html", params)




def about(request):
    # return HttpResponse("We are at about")
    return render(request, 'shop/about.html')

def contact(request):
    if(request.method == "POST"):
            
        name=request.POST.get('name' , '')
        email=request.POST.get('email', '')
        phone=request.POST.get('phone', '')
        desc=request.POST.get('desc', '')

        contact = Contact(name=name,email=email,phone=phone,desc=desc)
        contact.save()



        # print(name,email,phone,desc)


    # return HttpResponse("We are at contact")
    return render(request, 'shop/contact.html')


def tracker(request):
    return HttpResponse("We are at tracker")
    # return render(request, 'shop/index.html')

def search(request):
    return HttpResponse("We are at search")
    # return render(request, 'shop/index.html')

def productview(request,myid):
    # return HttpResponse("We are at productview id")
    product = Product.objects.filter(id=myid)
    
    return render(request, 'shop/productView.html',{'product':product[0]})

def checkout(request):
    if request.method=="POST":
        items_json= request.POST.get('itemsJson', '')
        name=request.POST.get('name', '')
        email=request.POST.get('email', '')
        address=request.POST.get('address1','')
        city=request.POST.get('city', '')
        state=request.POST.get('state', '')
        pincode=request.POST.get('pincode', '')
        phone=request.POST.get('phone', '')

        order = Orders(items_json= items_json, name=name, email=email, address= address, city=city, state=state, pincode=pincode, phone=phone)
        order.save()
        thank=True

        id=order.order_id
        return render(request, 'shop/finalpage.html', {'thank':thank, 'id':id})

    return render(request, 'shop/checkout.html')


# def finalpage(request):
#     return render(request, 'shop/finalpage.html')
