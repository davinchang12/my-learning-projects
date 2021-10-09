class Category:
	name = ""
	def __init__(self, category):
		self.name = category
		self.ledger = []
	def deposit(self, amount, description=""):
		self.temp = {}
		self.temp['amount'] = amount
		self.temp['description'] = description
		self.ledger.append(self.temp)

	def withdraw(self, amount, description=""):
		self.check = self.check_funds(amount)
		if(self.check == True):
			self.temp = {}
			self.temp['amount'] = -(amount)
			self.temp['description'] = description
			self.ledger.append(self.temp)
			return True
		else:
			return False
	def get_balance(self):
		self.balance = 0
		for i in range(len(self.ledger)-1):
			self.balance +=self.ledger[i]['amount'] + self.ledger[i+1]['amount']
		return round(self.balance, 2)

	def transfer(self, amount, category):
		cat_name = category.name	
		w_check = self.withdraw(amount, "Transfer to {}".format(cat_name))
		depo = category.deposit(amount, "Transfer from {}".format(self.name))

		if(w_check==True):
			return True
		else:
			return False
	def check_funds(self,amount):
		self.funds = 0
		self.length = len(self.ledger)
		
		for i in range(self.length):
			self.funds += self.ledger[i]['amount']

		if (self.funds < amount):
			return False
		else:
			return True

	def __str__(self):
		title = self.name.center(30, "*") + "\n"
		length = len(self.ledger)
		total = 0
		for i in range(length):
			title += f"{self.ledger[i]['description'][0:23]:23}" + f"{self.ledger[i]['amount']:>7.2f}" + '\n'
			total += self.ledger[i]['amount']

		output = title + "Total: " + str(total)
		return output


def create_spend_chart(categories):
	title = "Percentage spent by category\n"
	out = ""
	cat = []
	spending = []
	spent = 0

	for cats in categories:
		cat.append(cats.name)
		spent = 0
		for i in range(len(cats.ledger)):
			if cats.ledger[i]['amount'] < 0 :
				spent += abs((int(cats.ledger[i]['amount'])))

		spending.append(spent)
	print(spending)
	total = sum(spending)
	print(total)
	for i in spending:
		spending[spending.index(i)] = int((i / total) * 10) * 10

	longest = len(max(cat, key=len))

	for cats in cat:
		cat[cat.index(cats)] = cats.ljust(longest)

	catString = "     "
	for i in range(0, longest):
		if i < longest - 1:
			for cats in cat:
				catString += cats[i] + "  "
			catString += "\n     "
		else:
			catString += "      " + cats[longest-1] + "  "

	graph = ""
	for i in range(100, -10, -10):
		bar = " "
		line = str(i).rjust(3) + "|"
		for x in spending:
			if x >= i:
				bar += "o  "
			else :
				bar += "   "
		line += bar
		graph += line + '\n'
		dash = "    " + (len(cat) * 3) * "-" + "-" + "\n"

	out = title + graph + dash + catString
	return out

if __name__ == "__main__":
	food = Category("Food")
	food.deposit(1000, "initial deposit")
	food.withdraw(10.15, "groceries")
	food.withdraw(15.89, "restaurant and more food for dessert")
	print(food.get_balance())
	clothing = Category("Clothing")
	food.transfer(50, clothing)
	clothing.withdraw(25.55)
	clothing.withdraw(100)
	auto = Category("Auto")
	auto.deposit(1000, "initial deposit")
	auto.withdraw(15)

	print(food)
	print(clothing)

	print(create_spend_chart([food, clothing, auto]))