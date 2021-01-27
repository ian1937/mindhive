from rest_framework import serializers
from roster.models import Role, Shift, Employee, Availability


class RoleSerializer(serializers.ModelSerializer):

    class Meta:
        model = Role
        fields = ('name',)