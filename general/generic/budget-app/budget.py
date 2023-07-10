class Category:

  def __init__(self, category):
    self.category = category
    self.ledger = []

  def __str__(self):
    title = f"{self.category:*^30}\n"
    amount = 0
    format_items = ""

    for item in self.ledger:
      format_items += f"{item['description'][0:23]:23}" + f"{item['amount']:>7.2f}\n"
      amount += item['amount']
    total = f"Total: {amount}"

    return title + format_items + total

  def deposit(self, amount, description=""):
    if description == "":
      self.ledger.append({"amount": amount, "description": ""})
    else:
      self.ledger.append({"amount": amount, "description": description})

  def withdraw(self, amount, description=""):
    current_funds = self.get_balance()
    if current_funds >= amount:
      if description == "":
            self.ledger.append({"amount": -amount, "description": ""})
      else:
        self.ledger.append({"amount": -amount, "description": description})
      return True
    else:
      return False

  def get_balance(self):
    balance = 0
    for item in self.ledger:
      balance += item['amount']
    return balance

  def transfer(self, amount, category):
    current_funds = self.get_balance()
    if current_funds >= amount:
      category.ledger.append({"amount": amount, "description": "Transfer from " + self.category})
      self.ledger.append({"amount": -amount, "description": "Transfer to " + category.category})
      return True
    else:
     return False

  def check_funds(self, amount):
    current_funds = self.get_balance()
    return current_funds >= amount

def create_spend_chart(categories):
  title = "Percentage spent by category\n"
  format_chart = ""
  format_categ = ""
  space = len(categories) * 3 + 1
  x_chart = f"{' ':>3} {'':-^{space}}\n"
  total_spent_categ = []
  percentage_spent = []

  for category in categories:
      spent = 0
      for item in category.ledger:
        if item['amount'] < 0:
          spent += abs(item['amount'])
      total_spent_categ.append(spent)

  total_spent = round(sum(total_spent_categ), 2)
  percentage_spent =  [int((spent/total_spent)*100) for spent in total_spent_categ]

  max_category_len = max([len(category.category) for category in categories])
  category_list = [category.category for category in categories]

  for x in range(100, -10, -10):
    format_chart += f"{x:>3}|"
    for percentage in percentage_spent:
        if percentage >= x:
            format_chart += " o "
        else:
            format_chart += "   "
    format_chart += " \n"

  for y in range(max_category_len):
    format_categ += f"{' ':>5}"
    for item in category_list:
      if len(item) > y:
        format_categ += f"{item[y]}  "
      else:
        format_categ += "   "
    format_categ += f"\n"

  return title + format_chart + x_chart + format_categ.rstrip("\n")
