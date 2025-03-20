from django.shortcuts import render

# Create your views here.

# hey

def home_view(request):
  
  return render(request, "home.html", {})