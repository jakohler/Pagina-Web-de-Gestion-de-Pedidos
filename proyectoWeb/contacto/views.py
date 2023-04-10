from django.shortcuts import render, redirect
from .forms import FormularioContacto
from django.core.mail import EmailMessage

# Create your views here.

def contacto(request):

    if request.method == 'POST':
        formulario = FormularioContacto(data = request.POST)
        if formulario.is_valid():
            nombre = request.POST.get("nombre")
            email = request.POST.get("email")
            descripcion = request.POST.get("descripcion")
            email = EmailMessage("Web Gestion pedidos",
                                 "El usuario con nombre {} con la direccion {} escribe lo siguiente:\n\n {}".format(nombre, email, descripcion),
                                 "", ['jaelkohler@gmail.com'], reply_to=[email])
            
            try:
                email.send()
                return redirect("/contacto/?valido")
            except:
                return redirect("/contacto/?incorrecto")
    else:
        formulario = FormularioContacto()

    return render(request, "contacto/contacto.html", {'formularios': formulario})