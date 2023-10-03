from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.http import require_http_methods
from django.views.decorators.csrf import csrf_exempt
from django.template import loader
from .models import *
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
import requests
from django.contrib import messages
import pprint
import uuid
import iyzipay
import json


api_key = 'your_api_key'
secret_key = 'your_secret_key'
base_url = 'api.iyzipay.com'

#
# api_key = 'sandbox-api_key'
# secret_key = 'sandbox-secret_key'
# base_url = 'sandbox-api.iyzipay.com'


options = {
    'api_key': api_key,
    'secret_key': secret_key,
    'base_url': base_url
}

sozlukToken = list()
uid = uuid.uuid4()
print(uid)

def index(request):

    template = loader.get_template('help/index.html')
    about = About.objects.all().first()
    menu = Menu.objects.order_by('order').all()
    home = Home.objects.all().first()
    others = Others.objects.all().first()
    helpings = Helping.objects.all()
    fonds = Fond.objects.all()
    blogs = Blogs.objects.all()
    ids = []
    for m in menu:
        ids.append(m.href)

    context = {
        'about': about,
        'menu': menu,
        'home': home,
        'helpings': helpings,
        'fonds': fonds,
        'blogs': blogs,
        'ids': ids,
        'others': others
    }

    return HttpResponse(template.render(context, request))

def detail(request, pk):

    template = loader.get_template('help/blog_details.html')
    blog = Blogs.objects.filter(pk=pk).first()

    about = About.objects.all().first()
    menu = Menu.objects.order_by('order').all()
    home = Home.objects.all().first()
    blogothers = BlogDetailsOther.objects.all().first()
    others = Others.objects.all().first()
    helpings = Helping.objects.all()
    fonds = Fond.objects.all()
    blogs = Blogs.objects.all()
    ids = []
    for m in menu:
        ids.append(m.href)

    context = {
        'about': about,
        'menu': menu,
        'home': home,
        'helpings': helpings,
        'fonds': fonds,
        'blogs': blogs,
        'ids': ids,
        'others': others,
        'blog': blog,
        'bothers': blogothers,
    }

    return HttpResponse(template.render(context, request))

def payment(request, query=None):
    context = dict()
    fond_id = request.GET.get('fond_id')
    payment_value = request.GET.get('payment_value')
    toleg = Payments(fond_id=int(fond_id), value=float(payment_value), message='garashylyar', conversationId=uuid)
    toleg.save()

    payment_card = {
        'cardHolderName': 'John Doe',
        'cardNumber': '5528790000000008',
        'expireMonth': '12',
        'expireYear': '2030',
        'cvc': '123',
        'registerCard': '0'
    }

    buyer = {
        'id': 'BY789',
        'name': 'John',
        'surname': 'Doe',
        'gsmNumber': '+905350000000',
        'email': 'email@email.com',
        'identityNumber': '74300864791',
        'lastLoginDate': '2015-10-05 12:43:35',
        'registrationDate': '2013-04-21 15:12:09',
        'registrationAddress': 'Nidakule Göztepe, Merdivenköy Mah. Bora Sok. No:1',
        'ip': '85.34.78.112',
        'city': 'Istanbul',
        'country': 'Turkey',
        'zipCode': '34732'
    }

    address = {
        'contactName': 'Jane Doe',
        'city': 'Istanbul',
        'country': 'Turkey',
        'address': 'Nidakule Göztepe, Merdivenköy Mah. Bora Sok. No:1',
        'zipCode': '34732'
    }

    basket_items = [
        {
            'id': uid,
            'name': 'Binocular',
            'category1': 'Collectibles',
            'category2': 'Accessories',
            'itemType': 'PHYSICAL',
            'price': str(payment_value)
        }
    ]

    request1 = {
        'locale': 'en',
        'conversationId': uid,
        'price': str(payment_value),
        'paidPrice': str(payment_value),
        'currency': 'USD',
        'installment': '1',
        'basketId': uid,
        'paymentChannel': ['WEB', 'MOBILE', 'MOBILE_WEB', 'MOBILE_IOS', 'MOBILE_ANDROID', 'MOBILE_WINDOWS', 'MOBILE_TABLET', 'MOBILE_PHONE'],
        'paymentGroup': 'PRODUCT',
        "callbackUrl": "http://localhost:8008/result/",
        'paymentCard': payment_card,
        'buyer': buyer,
        'shippingAddress': address,
        'billingAddress': address,
        'basketItems': basket_items
    }

    payment = iyzipay.Payment().create(request1, options)

    checkout_form_initialize = iyzipay.CheckoutFormInitialize().create(request1, options)

    #print(checkout_form_initialize.read().decode('utf-8'))
    page = checkout_form_initialize
    header = {'Content-Type': 'application/json'}
    content = checkout_form_initialize.read().decode('utf-8')
    json_content = json.loads(content)
    print(type(json_content))
    print(json_content)
    print(json_content["checkoutFormContent"])
    print("************************")
    print(json_content["token"])
    print("************************")
    sozlukToken.append(json_content["token"])
    return HttpResponse(json_content["checkoutFormContent"])



@require_http_methods(['POST'])
@csrf_exempt
def result(request):
    context = dict()

    url = request.META.get('index')

    request = {
        'locale': 'en',
        'conversationId': uid,
        'token': sozlukToken[0]
    }
    checkout_form_result = iyzipay.CheckoutForm().retrieve(request, options)
    print("************************")
    print(type(checkout_form_result))
    result = checkout_form_result.read().decode('utf-8')
    print("************************")
    print(sozlukToken[0])   # Form oluşturulduğunda
    print("************************")
    print("************************")
    sonuc = json.loads(result, object_pairs_hook=list)
    #print(sonuc[0][1])  # İşlem sonuç Durumu dönüyor
    #print(sonuc[5][1])   # Test ödeme tutarı
    print("************************")
    for i in sonuc:
        print(i)
    print("************************")
    print(sozlukToken)
    print("************************")
    if sonuc[0][1] == 'success':
        context['success'] = 'Başarılı İŞLEMLER'
        return HttpResponseRedirect(reverse('success'), context)

    elif sonuc[0][1] == 'failure':
        context['failure'] = 'Başarısız'
        return HttpResponseRedirect(reverse('failure'), context)

    return HttpResponse(url)

def success(request):
    context = dict()
    context['success'] = 'İşlem Başarılı'
    py = Payments.objects.filter(conversationId=uid).first()
    if py:
        py.message = 'ustunlikli'
        py.status = True
    template = 'help/ok.html'
    return render(request, template, context)


def failure(request):
    context = dict()
    context['fail'] = 'İşlem Başarısız'
    py = Payments.objects.filter(conversationId=uid).first()
    if py:
        py.message = 'kemchilikli'
        py.status = False
    template = 'help/fail.html'
    return render(request, template, context)

def subscribe(request, query=None):
    print(request.GET.get('email'))
    email = request.GET.get('email')
    sb = Subscribe(email=email)
    sb.save()
    return HttpResponse()