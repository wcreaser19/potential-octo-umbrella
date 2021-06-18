import math

print("Enter values for the two known sides of a right angle triangle")

# input
a = input("Enter the first side")
b = input("Enter the second side")
c = input("Enter the hypotenuse")

# process
if a == "" and b == "" or a == "" and c == "" or b == "" and c == "" or a == "" and b == "" and c == "":
  print("Sorry, you did not enter enough data.")

elif a == "":
  a = float(c) ** 2 - float(b) ** 2
  a = math.sqrt(a)
  round_a = round(a, 2)
  print("The side a is equal to " + str(round_a) + ".")

elif b == "":
  b = float(c) ** 2 - float(a) ** 2
  b = math.sqrt(b)
  round_b = round(b, 2)
  print("The side b is equal to " + str(round_b) + ".")

elif c == "":
  c = float(a) ** 2 + float(b) ** 2
  c = math.sqrt(c)
  round_c = round(c, 2)
  print("The hypotenuse is equal to " + str(round_c) + ".")

else:
  print("Sorry, you entered too much data.")