from django.shortcuts import render, redirect, render_to_response
from django.template import RequestContext
from django.http import HttpResponseRedirect, HttpResponse, JsonResponse, Http404
from django.views.decorators.csrf import csrf_exempt
from django.utils.crypto import constant_time_compare
import json, hmac


def verify(signature, payload):
    digest = hmac.new('KEYHERE') #Just for testing. In production, we'll import from settings or use an ENV
    digest.update(payload)
    key = digest.hexdigest()
    key = 'sha1=' + key
    return constant_time_compare(key, signature)

@csrf_exempt
def home(request):
    try:
        headers = request.META
	signature = headers['HTTP_X_HUB_SIGNATURE']
	delivery = headers['HTTP_X_GITHUB_DELIVERY']
	ctype = headers['CONTENT_TYPE']
	if ctype=='application/json':
	    payload = request.body
	    if verify(signature, payload):
    	        return HttpResponse('TRUE')		
    except:
        raise Http404
