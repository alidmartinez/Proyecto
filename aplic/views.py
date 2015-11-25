from django.http import HttpResponse,HttpResponseRedirect
from aplic.models import *
from aplic.forms import  UsuarioForm
from aplic.forms import  TerceroForm
from aplic.forms import  KardexForm
from aplic.forms import  ProductoForm
from django.template import RequestContext
from django.shortcuts import get_object_or_404, render_to_response,redirect
from django.contrib.auth import authenticate, login
def index(request):
	if request.user.is_authenticated():
	    return render_to_response("aplic/index.html",{},
	    context_instance=RequestContext(request))  
	else: 
	   return redirect("/login")

def prueba(request,id):
    x="<h1>"+id+"</h1>"
	#return render_to_response("login",{})
    return HttpResponse(x)


def usuarios(request):
	usuarios=Usuario.objects.all()
	"""x="<h1>Lista de Usuarios </h1><br>"
	x+="<br>".join(["id:%s,RazonSocial: %s,nombreCompleto:%s %s," %(c.id,c.RazonSocial,c.Nombres,c.Apellidos) for c in usuarios ])
	return HttpResponse(x)"""
	return render_to_response("aplic/listarUsuarios.html",{'usuarios':usuarios},
		context_instance=RequestContext(request))

def kardex(request):
	kardex=Kardex.objects.all()
	"""x="<h1> Kardex </h1><br>"
	x+="<br>".join(["id:%s,CodKardex:%s,TipoMovimiento:%s,Fecha:%s,CodTercero:%s,CodProduc:%s,CantProduc:%s,ValorUnitario:%s,EstadoKardex:%s,ValorPublico:%s %s" %(c.id,c.CodKardex,c.TipoMovimiento,c.fecha,c.CodTercero,c.CodProduc,c.CantProduc,c.ValorUnitario,c.EstadoKardex,c.ValorPublico) for c in kardex ])
	return HttpResponse(x)"""
	return render_to_response("aplic/Kardex.html",{'kardex':kardex},
		context_instance=RequestContext(request))

def terceros(request):
	terceros=Tercero.objects.all()
	"""x="<h1>Lista de Terceros </h1><br>"
	x+="<br>".join(["id:%s,RazonSocial: %s,Email:%s %s," %(c.id,c.RazonSocial,c.Email) for c in terceros ])
	return HttpResponse(x)"""
	return render_to_response("aplic/listarTercero.html",{'terceros':terceros },
		context_instance=RequestContext(request))

def productos(request):
	productos=Producto.objects.all()
	"""x="<h1>Lista de Productos </h1><br>"
	x+="<br>".join(["id:%s,RazonSocial: %s,Email:%s %s," %(c.id,c.RazonSocial,c.Email) for c in productos ])
	return HttpResponse(x)"""
	return render_to_response("aplic/listarProducto.html",{'productos':productos },
		context_instance=RequestContext(request))



def Crear_tercero(request):
	if request.method =="POST":
		form=TerceroForm(request.POST)
		if form.is_valid():
			form.save()
			return HttpResponseRedirect("/terceros")
	else:
		form=TerceroForm()
		return  render_to_response("aplic/CrearTercero.html",
							  	  {'form':form},
							  	  context_instance=RequestContext(request))

def Crear_kardex(request):
	if request.method =="POST":
		form=KardexForm(request.POST)
		if form.is_valid():
			form.save()
			return HttpResponseRedirect("/kardex")
	else:
		form=KardexForm()
		return  render_to_response("aplic/AdicionarAlKardex.html",
							  	  {'form':form},
							  	  context_instance=RequestContext(request))

def Crear_usuario(request):
	if request.method =="POST":
		form=UsuarioForm(request.POST)
		if form.is_valid():
			form.save()
			return HttpResponseRedirect("/usuarios")
	else:
		form=UsuarioForm()
		return  render_to_response("aplic/CrearUsuario.html",
							  	  {'form':form},
							  	  context_instance=RequestContext(request))

def Crear_producto(request):
	if request.method =="POST":
		form=ProductoForm(request.POST)
		if form.is_valid():
			form.save()
			return HttpResponseRedirect("/productos")
	else:
		form=ProductoForm()
		return  render_to_response("aplic/CrearProducto.html",
							  	  {'form':form},
							  	  context_instance=RequestContext(request))


def Crear_parametro(request):
	if request.method =="POST":
		form=ParametroForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect("/parametro")
	else:
		form=ParametroForm()
		return  render_to_response("aplic/CrearParametro.html",
							  	  {'form':form},
							  	  context_instance=RequestContext(request))
		