from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from roster.models import Role
from roster.serializers import RoleSerializer


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
    return HttpResponse(status=404)


def shifts(request):
    return HttpResponse('Hello shifts')


def availabilities(request):
    return HttpResponse('Hello availabilities')


def employees(request):
    return HttpResponse('Hello employees')