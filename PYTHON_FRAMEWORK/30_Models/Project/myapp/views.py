from django.shortcuts import render,HttpResponse

# Create your views here.

def index(request):
    # return HttpResponse("Hello, world. You're at the homepage.")
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')