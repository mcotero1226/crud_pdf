from django import forms  # Importa el módulo de formularios de Django
from .models import categoria # Importa el modelo Producto
from django.contrib.auth.forms import UserCreationForm  # Formulario estándar para crear usuarios
from django.contrib.auth.models import User  # Modelo de usuarios de Django

# Formulario para productos
class categoriaForm(forms.ModelForm):
    class Meta:
        model = categoria
        fields = '__all__'  # Incluye todos los campos del modelo Producto

# Formulario personalizado para registro de usuarios
class RegistroUsuarioForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']
