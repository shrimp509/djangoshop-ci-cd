from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home_view(request):
	return HttpResponse("Hi Django on GAE, I am updated when push to github,\nand deployed by CircleCI~~")