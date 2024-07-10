from django.shortcuts import render
from mvc.models import Departamento


# Create your views here.
def index(request):
    dept = Departamento()
    listadept = dept.listardptos()
    print("Me llega:", listadept)
    contexto = {
        'lista_dept': listadept
        }
    return render(request, 'mvc/index.html', contexto)


def toaltadept(request):
    return render(request, 'mvc/alta.html')


def altadeptexe(request):
    numdpt = request.POST['dptnum']
    nom = request.POST['nom']
    loc = request.POST['loc']
    dept = Departamento()
    dept.altadept(numdpt, nom, loc)
    listadept = dept.listardptos()
    contexto = {
        'lista_dept': listadept
    }
    return render(request, 'mvc/index.html', contexto)


def toeditardept(request):
    numdpt = request.GET['dptnum']
    dept = Departamento()
    datos = dept.datosdept(numdpt)
    contexto = {
        'datos_dept': datos
    }
    print("Mando editar.html:", contexto)
    return render(request, 'mvc/edicion.html', contexto)


def editardeptexe(request):
    numdpt = request.POST['dptnum']
    nom = request.POST['nom']
    loc = request.POST['loc']
    dept = Departamento()
    dept.editadept(numdpt, nom, loc)
    listadept = dept.listardptos()
    contexto = {
        'lista_dept': listadept
    }
    return render(request, 'mvc/index.html', contexto)


def borrardept(request):
    numdpt = request.GET['dptnum']
    dept = Departamento()
    dept.bajadept(numdpt)
    listadept = dept.listardptos()
    contexto = {
        'lista_dept': listadept
    }
    return render(request, 'mvc/index.html', contexto)
