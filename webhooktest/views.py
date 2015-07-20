from django.shortcuts import render, redirect, render_to_response
from django.template import RequestContext
from django.http import HttpResponseRedirect, HttpResponse
from django.core.context_processors import csrf

# Create your views here.

def home(request):
	return HttpResponse("Hello")