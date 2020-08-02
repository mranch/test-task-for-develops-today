from django.shortcuts import render


# Create your views here.
def home(request):
    return render(request, '<h1>Home</h1>')
