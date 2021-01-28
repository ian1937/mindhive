from django.http import HttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from roster.models import Employee
from roster.serializers import EmployeeSerializer


@api_view(["GET", "POST", "DELETE"])
def employees(request):

    if request.method == "GET":
        employees = Employee.objects.all()
        serializer = EmployeeSerializer(employees, many=True)
        return Response(serializer.data, status=200)

    elif request.method == "POST":
        serializer = EmployeeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)

    elif request.method == "DELETE":
        shifts = Employee.objects.all()
        shifts.delete()
        return Response(status=204)

    return HttpResponse(status=404)


def employee(request, id):
    return HttpResponse(f"Hello {id}")
    