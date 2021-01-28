from django.http import HttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from roster.models import Role
from roster.serializers.role import RoleSerializer


@api_view(["GET", "POST", "DELETE"])
def roles(request):

    if request.method == "GET":
        roles = Role.objects.all()
        serializer = RoleSerializer(roles, many=True)
        return Response(serializer.data, status=200)

    elif request.method == "POST":
        serializer = RoleSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)

    elif request.method == "DELETE":
        roles = Role.objects.all()
        roles.delete()
        return Response(status=204)

    return HttpResponse(status=404)


@api_view(["GET", "PUT", "DELETE"])
def role(request, id):

    try:
        role = Role.objects.get(id=id)
    except Role.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == "GET":
        serializer = RoleSerializer(role)
        return Response(serializer.data, status=200)

    elif request.method == "PUT":
        serializer = RoleSerializer(role, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)

    elif request.method == "DELETE":
        role.delete()
        return Response(status=204)

    return HttpResponse(status=404)