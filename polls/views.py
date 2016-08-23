from django.shortcuts import render, render_to_response
from django.http import HttpResponse
from WebScraper import scraper

# Create your views here.
def index(request):
	scraper()
	# return HttpResponse("Hello World!")
	return render_to_response('test.html')