from rest_framework import serializers
from roster.models import Role, Employee


class EmployeeSetSerializer(serializers.ModelSerializer):

    class Meta:
        model = Employee
        fields = ["id", "name"]


class RoleSerializer(serializers.ModelSerializer):
    employee_set = EmployeeSetSerializer(many=True, read_only=True)

    class Meta:
        model = Role
        fields = ["id", "name", "employee_set"]