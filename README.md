# mindhive


Run the command below to install the app to your local computer:
	git clone -b master https://github.com/ian1937/mindhive
	
Create and activate virtual environment:
	cd mindhive
	python -m venv venv
	venv\Scripts\activate.bat
	
Install the requirements (Make sure to have python 3.6 or above on your machine):
	pip install -r requirements.txt
	
Run the program (make sure venv is activated):
	python manage.py runserver
	
Setup data (Database should already be occupied by data):
	Copy and paste all dummy_data.txt file to the command line

See test coverage report (make sure venv is activated):
	coverage report
	
API endpoints:
							
roles/ GET all roles, POST a role, DELETE all roles
shifts/ GET all shifts, POST a shift, DELETE all shifts
employees/ GET all employees, POST an employee, DELETE all employees
availabilities/ GET all availabilities, POST an availability, DELETE all availabilities

roles/<int:id> GET a role, PUT edit a role, DELETE a role
shifts/<int:id> GET a shift, PUT edit a shift, DELETE a shift
employees/<int:id> GET an employee, PUT edit an employee, DELETE an employee
availabilities/<int:id> GET an availability, PUT edit an availability, DELETE an availability
