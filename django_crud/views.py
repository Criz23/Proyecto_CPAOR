from django.shortcuts import render
from employee.models import Employee
from django.http import HttpResponse

# Create your views here.
def registro(request):
    return render(request, 'registro.html')

def guardar(request):
    if request.method == 'GET':
        nombre = request.GET['nombre']
        direccion = request.GET['direccion']
        email = request.GET['email']
        Employee.objects.create(name=nombre, address=direccion, email=email)
        empleados = Employee.objects.all()
        return render(request, 'mostrar.html', {'empleados':empleados})
    else:
        return render(request, 'registro.html')