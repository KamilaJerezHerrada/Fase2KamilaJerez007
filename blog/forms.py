from django import forms
from django.forms import ModelForm
from .models import Contacto
from .models import Producto
from django.contrib.auth.forms import UserCreationForm
from .models import Cliente 

class ContactoForm(forms.ModelForm):

    class Meta:
        model = Contacto
        fields = '__all__'

class ProductoForm(ModelForm):

    model = Producto
    fields = ['idProducto','nombreProducto', 'precio', 'cantidad', 'stock']

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = Cliente
        fields = ['nombre', "apellido", "correoElectronico", "direccion", "cuidad", "region", "comuna", "codigoPostal", "numeroTelefono"]


