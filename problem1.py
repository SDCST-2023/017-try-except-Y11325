#python3
# Quadratic Equation
# Have the user enter in the coefficients of a quadratic equation in the
# format: ax^2 + bx + c = 0 and calculate the solutions of the equation
# rounded to 2 decimal places. Use a try...except block to catch if there
# is no solution
# incorporate a while loop to keep having the user enter in values for a,b,c
# until they are valid
# incorporate a second while loop to keep repeating the program without
# having to rerun it.

""" Sample output:
Enter in the coefficients for a quadratic equation in the format:
  ax^2 + bx + c = 0
a:3
b:d
c:1
Those are not valid values for a, b or c
a:3
b:2
c:1
There are no real roots to the equation
a:2
b:-3
c:-6
The roots are 2.64 and -1.14
a:1
b:8
c:16
The roots are -4.0 and -4.0
"""
import os
import math
os.system('cls')
while True:
  while True:
    try:
      print("\nEnter in the coefficients for a quadratic equation in the format: \nax^2 + bx + c = 0\n")

      a = (input("Enter a: "))
      a = int(a)
      b = (input("Enter b: "))
      b = int(b)
      c = (input("Enter c: "))
      c = int(c)
      dis = math.pow(b,2) - 4 * a * c
      dis = int(dis)

      x1 = (-b + math.sqrt(math.pow(b,2) - 4 * a * c))/(2*a)
      x2 = (-b - math.sqrt(math.pow(b,2) - 4 * a * c))/(2*a)
      print(f"\nThe roots are {round(x1,2)} and {round(x2,2)}\n")
      break

    except:
      if a == str(a) or b == str(b) or c == str(c):
        print("\nThose are not valid values for a, b or c\n")
      elif dis < 0:
        print("\nThere are no real roots to the equation\n")
        break
  
  again = input("Again?(y/n): ")
  if again == "y":
    continue
  elif again == "n":
    print("---The End---\n\n")
    break