from django.http import HttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from roster.models import Role, Shift, Employee, Availability
from roster.serializers import RoleSerializer, ShiftSerializer, EmployeeSerializer, AvailabilitySerializer


@api_view(['GET', 'POST', 'DELETE'])
def roles(request):
    if request.method == 'GET':
        roles = Role.objects.all()
        serializer = RoleSerializer(roles, many=True)
        return Response(serializer.data, status=200)
    elif request.method == 'POST':
        serializer = RoleSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
    elif request.method == 'DELETE':
        roles = Role.objects.all()
        roles.delete()
        return Response(status=204)
    return HttpResponse(status=404)


@api_view(['GET', 'POST', 'DELETE'])
def shifts(request):
    if request.method == 'GET':
        shifts = Shift.objects.all()
        serializer = ShiftSerializer(shifts, many=True)
        return Response(serializer.data, status=200)
    elif request.method == 'POST':
        serializer = ShiftSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
    elif request.method == 'DELETE':
        shifts = Shift.objects.all()
        shifts.delete()
        return Response(status=204)
    return HttpResponse(status=404)


@api_view(['GET', 'POST', 'DELETE'])
def employees(request):
    if request.method == 'GET':
        employees = Employee.objects.all()
        serializer = EmployeeSerializer(employees, many=True)
        return Response(serializer.data, status=200)
    return HttpResponse(status=404)


def availabilities(request):
    return HttpResponse('Hello availabilities')
