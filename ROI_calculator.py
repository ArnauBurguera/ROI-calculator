Income = float(input("Income: "))
Expenses = float(input("Expenses :"))

def bnfts():
  Benefits = Income - Expenses
  print(f"Benefits: {Benefits}")

def bnfts_expns_ratio():
  ratio = (((Income / Expenses) * 100) - 100)
  print(f"Benefits/Expenses ratio: {ratio}")

def roi():
  ROI = ((Benefits / Expenses) / Expenses) * 100
  print(f"Roi: {ROI}")

bnfts()
bnfts_expns_ratio()
roi()