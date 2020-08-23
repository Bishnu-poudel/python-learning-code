'''print("hello world")
d1 ={"bishnu":"pizza" ,"golul":"burger", "sushila":{"b":"chuchau","d":"chauchau"},"aama":"[daal,bhat, tarkali]"}
print(d1["bishnu"])
print(d1["sushila"])
print(d1)
print(d1["aama"])


d1 = {"ram":"100","sam":"200","hari":"300","gopal":"400","krishna":"500"}
print("enter your dictonary vlues")
value=input()
print(d1[value])
s= set()
#l =[ 1, 2, 3, 4]
#s_set_from_list =set(l)
#print(s_set_from_list)
#print(type(s_set_from_list))
s.add(1)
s.add(2)
 s.add({3,4,5})
print(s,s1)
# Faulty Calculator
a = float(input("Enter value of a : "))
b = float(input("Enter value of b : "))
print("1.Addition")
print("2.Sutraction")
print("3.Multiplication")
print("4.Division")
choice = int(input("Enter your choice(1,2,3 or 4) : "))
if choice == 1:
    if a == 56 and b == 9:
        print("Answer = 77")
    else:
        result = a+b
        print("Answer =", result)
elif choice == 2:
    if a == 45 and b == 10:
        print("Answer = 50")
    else:
        result = a-b
        print("Answer =", result)
elif choice == 3:
    if a == 45 and b == 3:
        print("Answer = 555")
    else:
        result = a*b
        print("Answer =", result)
elif choice == 4:
    if a == 56 and b == 6:
        print("Answer = 4")
    else:
        result = a/b
        print("Answer =", result)
else:
    print("INVALID INPUT!!!!")'''
a = float(input("enter the number a ="))
b = float(input("enter the number b ="))
print("1.addition")
print("2.subraction")
print("3.multiplication")
print("4.division")
operation = int(input("choose the number 1, 2, 3 or 4  "))
if operation == 1:
 if a==56 and b==9 :
  print("the answer is 77")
 else:
  result = a+b
  print("the answer is " ,result)
elif operation == 2:
  if a ==45 and b == 10:
   print("the answer is 87")
  else:
   result = a - b
   print("the answer is ", result)
elif operation == 3:
  if a == 50 and b == 5:
   print("the answer is 97")
  else:
   result = a * b
   print("the answer is ", result)
elif operation == 4:
  if a == 100 and b == 10:
   print("the answer is 107")
  else:
   result = a / b
   print("the answer is ", result)
else:
 print('invalid input')




