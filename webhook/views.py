from django.shortcuts import render, redirect, render_to_response
from django.template import RequestContext
from django.http import HttpResponseRedirect, HttpResponse, JsonResponse, Http404
from django.views.decorators.csrf import csrf_exempt
from django.utils.crypto import constant_time_compare
from django.conf import settings
import json, hmac, base64, hashlib, os



#Checking for IP for now.
#TODO : validate hash.minor.
def verify(ip):
	ip = ip.split('.')
	if ip[0]=='192' and ip[1]=='30':
		if int(ip[2])>=252 and int(ip[2])<=255:
			if int(ip[3])>=0 and int(ip[3])<=255:
				return True
			else:
				return False
		else:
			return False
	else:
		return False


@csrf_exempt
def home(request):
	if request.META.get('CONTENT_TYPE') == 'application/json':
		if verify(request.META.get('HTTP_X_FORWARDED_FOR')):
			cmd = settings.BASE_DIR+"/update.sh"
			os.system('%s'%(cmd))
			return HttpResponse("All done!")
		else:
			raise Http404
	else:
		raise Http404
