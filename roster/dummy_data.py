python manage.py shell

from roster.models import Role
from roster.tests.test_roles import roles_list
for role in roles_list:
    role_obj = Role(name=role["name"])
    role_obj.save()

from roster.models import Shift
from roster.tests.test_shifts import shifts_list
for shift in shifts_list:
    shift_obj = Shift(day=shift["day"], start_time=shift["start_time"], end_time=shift["end_time"])
    shift_obj.save()

from roster.models import Role, Employee
from roster.tests.test_roles import roles_list
from roster.tests.test_employees import employees_list
for count, employee in enumerate(employees_list):
    role = Role(name=roles_list[count]["name"])
    employee_obj = Employee(name=employee["name"], role=role)
    role.save()
    employee_obj.save()

exit()

