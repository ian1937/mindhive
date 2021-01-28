from rest_framework import serializers
from roster.models import Role, Shift, Employee, Availability


class EmployeeSetSerializer(serializers.ModelSerializer):

    class Meta:
        model = Employee
        fields = ["id", "name"]


class RoleSerializer(serializers.ModelSerializer):
    employee_set = EmployeeSetSerializer(many=True, read_only=True)

    class Meta:
        model = Role
        fields = ["id", "name", "employee_set"]


class ShiftSerializer(serializers.ModelSerializer):
    worked_by = EmployeeSetSerializer(read_only=True)

    class Meta:
        model = Shift
        fields = ["day", "start_time", "end_time", "worked_by"]


class AvailabilitySetSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Availability
        fields = ["day", "start_time", "end_time"]


class RoleSetSerializer(serializers.ModelSerializer):

    class Meta:
        model = Role
        fields = ["id", "name"]


class EmployeeSerializer(serializers.ModelSerializer):
    availability_set = AvailabilitySetSerializer(many=True, read_only=True)

    class Meta:
        model = Employee
        fields = ["id", "name", "role", "availability_set"]

    """ see https://stackoverflow.com/questions/50256852/django-rest-framework-post-foreign-key for details"""
    def to_representation(self, instance):
        self.fields["role"] =  RoleSetSerializer(required=False)
        return super(EmployeeSerializer, self).to_representation(instance)


class EmployeeNameSerializer(serializers.ModelSerializer):

    class Meta:
        model = Employee
        fields = ["id", "name"]


class AvailabilitySerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Availability
        fields = ["id", "day", "start_time", "end_time", "employee"]
        
    def to_representation(self, instance):
        self.fields["employee"] =  EmployeeNameSerializer(required=False)
        return super(AvailabilitySerializer, self).to_representation(instance)
