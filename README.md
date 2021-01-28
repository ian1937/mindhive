# mindhive


Run the command below to install the app to your local computer:
  git clone https://github.com/ian1937/mindhive/tree/master
	
	
Run the program:
	python manage.py runserver
	
Setup data (Database should already be occupied by data):
	Copy and paste dummy_data.py file to the command line
	
API endpoints:
							
roles/ GET all roles, POST a role, DELETE all roles
shifts/ GET all shifts, POST a shift, DELETE all shifts
employees/ GET all employees, POST an employee, DELETE all employees
availabilities/ GET all availabilities, POST an availability, DELETE all availabilities

roles/<int:id> GET a role, PUT edit a role, DELETE a role
shifts/<int:id> GET a shift, PUT edit a shift, DELETE a shift
employees/<int:id> GET an employee, PUT edit an employee, DELETE an employee
availabilities/<int:id> GET an availability, PUT edit an availability, DELETE an availability
