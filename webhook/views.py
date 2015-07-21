from django.shortcuts import render, redirect, render_to_response
from django.template import RequestContext
from django.http import HttpResponseRedirect, HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json

@csrf_exempt
def home(request):
    ctype = request.META['CONTENT_TYPE']
    event = request.META['X-Github-Event']
    signature = request.META['X-Hub-Signature']
    uid = request.META['X-Github-Delivery']
    if ctype == 'application/json' and signature :
    	data=json.loads(request.body)
    	return JsonResponse({'result':'pass','event':event})
    else:
        return JsonResponse({'result':'fail'})
