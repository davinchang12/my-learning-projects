import copy
import random
from collections import Counter
# Consider using the modules imported above.

class Hat:
	def __init__(self, **kwargs):
		contents = []
		for key, num in kwargs.items():
			for i in range(num):
				contents += key.split()
		self.contents = contents

	def draw(self, num_balls):
		x_choice = []
		contents = self.contents

		if(num_balls >= len(contents)):
			return contents

		for i in range(num_balls):
			choice = random.choice(contents)
			contents.remove(choice)
			x_choice.append(choice)

		self.contents = contents
		return x_choice


def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
	expected_list = []
	for key, value in expected_balls.items():
		for i in range(value):
			expected_list.append(key)

	prob = 0
	for i in range(num_experiments):
		temp = copy.deepcopy(hat)
		x = temp.draw(num_balls_drawn)
		result = list((Counter(expected_list) - Counter(x)).elements())
		if not result:
			prob += 1
	prob = prob / num_experiments
	return prob

if __name__ == "__main__":
	hat = Hat(blue=4, red=2, green=6)
	probability = experiment(
	    hat=hat,
	    expected_balls={"blue": 2,
	                    "red": 1},
	    num_balls_drawn=4,
	    num_experiments=3000)
	print("Probability:", probability)
	
	hat = Hat(red=3, blue=2)
	actual = hat.contents
	print(actual)

	hat = Hat(red=5, blue=2)
	print(hat.draw(2))