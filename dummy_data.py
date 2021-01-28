python manage.py shell

from roster.models import Role
from roster.tests.test_roles import roles_list
for role in roles_list:
    role_obj = Role(name=role["name"])
    role_obj.save()

from roster.models import Role, Employee
from roster.tests.test_roles import roles_list
from roster.tests.test_employees import employees_list
for count, employee in enumerate(employees_list):
    role = Role.objects.filter(name=roles_list[count]["name"]).first()
    employee_obj = Employee(name=employee["name"], role=role)
    role.save()
    employee_obj.save()

from roster.models import Shift, Employee
from roster.tests.test_shifts import shifts_list
from roster.tests.test_employees import employees_list
for count, shift in enumerate(shifts_list):
    employee = Employee.objects.filter(name=employees_list[count]["name"]).first()
    shift_obj = Shift(day=shift["day"], start_time=shift["start_time"], end_time=shift["end_time"], worked_by=employee)
    shift_obj.save()

from roster.models import Availability, Employee
from roster.tests.test_availabilities import availabilities_list
from roster.tests.test_employees import employees_list
for count, availability in enumerate(availabilities_list):
    employee = Employee.objects.filter(name=employees_list[count]["name"]).first()
    availability_obj = Availability(day=availability["day"],
                                    start_time=availability["start_time"],
                                    end_time=availability["end_time"],
                                    employee=employee)
    employee.save()
    availability_obj.save()

exit()
