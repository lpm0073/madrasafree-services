#!/usr/bin/env python
# -*- coding: utf-8 -*-

from tempfile import tempdir
from django.http.response import HttpResponse
from django.views.decorators.http import require_POST
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
from django.views.decorators.clickjacking import xframe_options_exempt
from django.conf import settings
import json
#from edxmako.shortcuts import render_to_response
from django.urls import reverse
from django.template import loader
from django import template
from django.shortcuts import render

import requests

#from madrasafree_services.models import ExtraInfo


# @login_required off for testing
@csrf_exempt
@require_POST
def icredit_get_url(request):
    client_data = json.loads(request.body.decode('utf-8'))
    amount = client_data['Item']['UnitPrice']
    data = {
        'GroupPrivateToken': settings.ICREDIT_GROUP_PRIVATE_TOKEN,
        'Items': [{
            'Quantity': '1',
            'UnitPrice': amount,
            'Description': '',
        }],
        'RedirectURL': settings.REDIRECT_URL+'?name='+client_data.get('name','')+'&email='+client_data.get('email',''),
        'EmailAddress': client_data.get('email',''),
        'CustomerFirstName': client_data.get('name',''),
        'CustomerLastName': client_data.get('last_name',''),
        'ExemptVAT': 1,
    }
    if data['CustomerFirstName'] == '':
        del data['CustomerFirstName']
    if data['CustomerLastName'] == '':
        del data['CustomerLastName']
    if data['EmailAddress'] == '':
        del data['EmailAddress']
    if client_data['CreateRecurringSale']:
        data['SaleType'] = 2
        data['CreateRecurringSale'] = True
        data['RecurringSaleAutoCharge'] = True
        data['RecurringSaleDay'] = 15
        data['RecurringSaleCycle'] = 3
        data['RecurringSaleStep'] = 1
        data['RecurringSaleCount'] = 0
       # extra_info.support_is_periodical = True
        data['Items'][0]['Description'] = 'תמיכה חודשית במדרסה'
    else:
        data['SaleType'] = 1
       # extra_info.support_is_periodical = False
        data['Items'][0]['Description'] = 'תמיכה חד פעמית במדרסה'

   # extra_info.save()
    response = requests.post(
        settings.ICREDIT_API_URL,
        headers={
            'User-Agent': 'PostmanRuntime/7.26.8',
        },
        json=data,
    )
    url = '"{}"'.format(response.json()['URL'])
    return HttpResponse(url)

@xframe_options_exempt
def payment_success(request):
    return HttpResponse(render(request,'madrasafree_services_plugin/payment_success.html',{'name':request.GET.get('name',''),'email':request.GET.get('email','')}))
