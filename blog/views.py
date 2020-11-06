from django.shortcuts import render
from .models import Producto
from .forms import  ContactoForm, CustomUserCreationForm, ProductoForm
from django.contrib.auth import login, authenticate

# Create your views here.
def index(request):
    return render(request, "index.html")

def productos(request):
    productos = Producto.objects.all()
    
    return render(request, "productos.html", {"listaProductos":productos})

def estilo(request):
    return render(request, 'estilo.html', {})

def accesorios(request):
    return render(request, 'accesorios.html', {})

def contacto(request):
    data = {
        'form': ContactoForm()
    }

    if request.method == 'POST':
        formulario = ContactoForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            data["mensaje"] = "Mensaje enviado"
        else:
            data["form"] = formulario

    return render(request, 'contacto.html', data)

def registrar(request):
    data = {
        'form': CustomUserCreationForm()
    }
    if request.method == 'POST':
        formulario = CustomUserCreationForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            user = authenticate(username=formulario.cleaned_data["username"], password=formulario.cleaned_data["password1"])
            login(request, user)
            #Se redirige al inicio
        data ["form"] = formulario
    return render(request, 'registrar.html', data)


def listado_productos(request):
    productos = Producto.objects.all()
    data = {
        'productos': productos
    }
    
    return render(request, 'listado_productos.html', data)

def nuevo_producto(request):
    data = {
        'form': ProductoForm()
    }
    return render(request, 'nuevo_producto.html', data)



