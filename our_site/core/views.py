from django.shortcuts import render

def index(request):
    return render(request, "manual/index.html")

def control_versiones(request):
    return render(request, "manual/control_versiones.html")

def metodologias_agiles(request):
    return render(request, "manual/metodologias_agiles.html")

def documentacion(request):
    return render(request, "manual/documentacion.html")

def testing(request):
    return render(request, "manual/testing.html")

def trabajo_equipo(request):
    return render(request, "manual/trabajo_equipo.html")

def recursos(request):
    return render(request, "manual/recursos.html")
