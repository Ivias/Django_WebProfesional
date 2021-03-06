from django.shortcuts import render, HttpResponse

"""
Inicio home/
Historia about/
Servicios services/
Visítanos store/
Contacto contact/
Blog blog/
Sample sample/ (esta es para páginas de prueba)

Es temporal puesto que cada view debera pasar a su correspondiente app 
y dejaremos únicamente las páginas staticas en core
"""

# Create your views here.
def home(request):
     return render(request,'core/home.html')

def about(request):
     return render(request,'core/about.html')

def services(request):
     return render(request,'core/services.html')

def store(request):
     return render(request,'core/store.html')

def contact(request):
     return render(request,'core/contact.html')

def blog(request):
     return render(request,'core/blog.html')

def sample(request):
     return render(request,'core/sample.html')
