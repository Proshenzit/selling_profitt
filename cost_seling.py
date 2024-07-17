cp = float(input("enter your  cost price : "))
sp = float(input("enter your seling price : "))
if cp >sp:
  amount = cp-sp
  print("loss",amount)
else:
  amount = sp-cp
  print("profit",amount)