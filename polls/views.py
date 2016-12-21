from django.shortcuts import render, render_to_response
from django.http import HttpResponse
from WebScraper import scraper

# Create your views here.
def index(request):
	wd = scraper()
	# return HttpResponse("Hello World!")
	return render_to_response('ti_test.html', wd)
	
def app(request):
	return render_to_response('app_page.html')