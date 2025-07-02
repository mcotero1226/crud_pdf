from django.shortcuts import render, redirect
from .forms import categoriaForm, RegistroUsuarioForm
from .models import categoria
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.template.loader import get_template  # Importa la función para cargar plantillas
from xhtml2pdf import pisa  # Importa la librería para generar PDFs
from django.http import HttpResponse  # Importa la clase HttpResponse
from .models import categoria 

# from django.contrib.auth.decorators import login_required
# from django.shortcuts import render
# from .models import categoria# Ya está importado arriba


# Create your views here.
#vista de inicio
def home(request):
    return render(request, 'home.html')

#Registro de usuarios 
def registro(request):
    if request.method == 'POST':
        form = RegistroUsuarioForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = RegistroUsuarioForm()
    return render(request,'registro.html', {'form':form})

def iniciar_sesion(request):
    if request.method == 'POST':
        usuario = request.POST['username']
        clave = request.POST['password']
        user = authenticate(request, username=usuario, password=clave)
        if user: 
            login(request, user)
            return redirect('lista_categoria')
    return render(request, 'login.html')

def cerrar_sesion(request):
    logout(request)
    return redirect('login')




@login_required
def lista_categoria(request):
    categoriaModel = categoria.objects.all()
    return render(request, 'productos/lista.html', {'categoria' : categoriaModel})

@login_required
def agregar_categoria(request):
    form = categoriaForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('lista_categoria')
    return render( request, 'productos/forms.html', {'form' : form})

@login_required
def editar_categoria(request,id):
    categoriaModel =  categoria.objects.get(id=id)
    form = categoriaForm(request.POST or None, instance=categoriaModel)
    if form.is_valid():
        form.save()
        return redirect('lista_categoria')  
    return render( request, 'productos/forms.html', {'form': form})



@login_required

def eliminar_categoria(request, id):
    categoriaModel = categoria.objects.get(id=id)
    categoriaModel.delete()
    return redirect('lista_categoria')

# ...código existente...

@login_required
def dashboard_productos(request):
    categorias = categoria.objects.all()  # Usa otro nombre para la variable
    nombres = [p.nombre for p in categorias]
    # Cambia 'precio' por un campo existente, por ejemplo 'id' o cualquier otro campo numérico
    datos = [p.id for p in categorias]  # Reemplaza 'id' por el campo adecuado si existe

    return render(request, 'productos/dashboard.html', {
        'labels': nombres,
        'data': datos
    })

def generar_reporte_pdf(request):
    categorias = categoria.objects.all()  # Usa otro nombre para la variable
    template_path = 'productos/reporte_pdf.html'
    context = {'categoria': categorias}  # Corrige el nombre en el contexto

    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="reporte_productos.pdf"'

    template = get_template(template_path)
    html = template.render(context)

    pisa_status = pisa.CreatePDF(html, dest=response)
    if pisa_status.err:
        return HttpResponse('Hubo un error al generar el PDF', status=500)
    return response

# ...elimina la segunda definición de dashboard_productos y los imports duplicados...

# (Eliminadas las definiciones duplicadas y los imports innecesarios)
    
    
    
