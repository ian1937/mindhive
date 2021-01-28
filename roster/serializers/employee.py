from rest_framework import serializers
from roster.models import Role, Employee, Availability


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