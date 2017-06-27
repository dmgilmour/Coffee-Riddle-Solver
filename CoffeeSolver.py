import random
from random import shuffle
import sys

if len(sys.argv) != 3:
	print("Wrong arguments")

num_simulations = int(sys.argv[1])
num_employees = int(sys.argv[2])
diff = 1.0 / num_employees

employees = [[(diff * i), 0] for i in range(1, num_employees)]

for i in range(num_simulations):
	shuffle(employees)

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

employees.sort()
for employee in employees:
	print(round(employee[0], 2), "\t:", employee[1])



