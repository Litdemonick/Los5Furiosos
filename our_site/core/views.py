from django.shortcuts import render

from django.shortcuts import render

def index(request):
    return render(request, "manual/index.html")

def control_versiones(request):
    return render(request, "manual/control_versiones.html")

def metodologias_agiles(request):
    return render(request, "manual/MetodologiaAgiles.html")  # Quita "templates/"

def documentacion(request):
    return render(request, "manual/documentacion.html")  # Quita "templates/"

def testing(request):
    return render(request, "manual/testing.html")  # Quita "templates/"

def trabajo_equipo(request):
    return render(request, "manual/trabajo_equipo.html")  # Quita "templates/"

def recursos(request):
    return render(request, "manual/recursos.html")  # Quita "templates/"