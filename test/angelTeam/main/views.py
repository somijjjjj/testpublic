from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect

# Create your views here.

def main(request):
    return render(request, 'main/main.html')