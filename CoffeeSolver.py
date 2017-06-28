import random
from random import shuffle
import sys

def findMax(employees):
	max_employee = employees[0]
	for employee in employees:
		if employee[1] > max_employee[1]:
			max_employee = employee
	
	return max_employee



if len(sys.argv) != 4 or len(sys.argv) != 6:
	print("Invalid arguments")
	print("Usage: CoffeeSolver.py  [num_simulations]  [optimal_solution_precision]  [fake_mean_precision]  [<lower_range_to_test>] [<upper_range_to_test>]")
	exit(1)


num_simulations = int(sys.argv[1])
num_employees = int(sys.argv[2])
fake_mean_precision = int(sys.argv[3])

if len(sys.argv) >= 6:
	lower_range = float(sys.argv[4])
	upper_range = float(sys.argv[5])
else:
	lower_range = 0
	upper_range = 1


# How much to separate each standard test employee by
employee_diff = 1.0 / num_employees

# How much to increase the fake mean by each time
fake_mean_diff = (upper_range - lower_range) / fake_mean_precision

# Construct the list of fake means to iterate over
fake_mean_list = [round(fake_mean_diff * i + lower_range, 8) for i in range(fake_mean_precision)]

output = open("pyoutput.txt", "w")

# Run a full set of simulations for each fake mean tested
for fake_mean in fake_mean_list:

	# Construct the set of employees of size num_employees differing by
	# the previously calculated employee_diff
	employees = [[(employee_diff * i), 0] for i in range(1, num_employees)]

	# Add 4 times as many fake employees as real employees to outweigh
	# the employees even as optimal solution precision changes
	for i in range(num_employees * 4):
		employees.append([fake_mean, 0])

	# Run the number of simulations requested
	for i in range(num_simulations):
		shuffle(employees)

		# The actual simulation, initialize pot before each run
		coffee_pot = 1.0;
		for employee in employees:
			# Remove desired amount of coffee
			coffee_pot -= employee[0]
			if coffee_pot <= 0:
				# If we break the pot, refill it
				coffee_pot = 1
			else:
				# If not store coffee
				employee[1] += employee[0]


	# Find the best performing employee
	max_employee = findMax(employees)

	output.write(str(fake_mean))
	output.write("\t")
	output.write(str(round(max_employee[0], 4)))
	output.write("\n")

