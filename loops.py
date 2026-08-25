# FOR LOOP 
condition  = True

while condition :
    print("condition is true")

is_fail = True
i = 1

while is_fail and i<=100 :
    print(f"try again {i}" )
    i = i+1
print("i  gave up !")

is_fail = True
i = 1

while is_fail  :
    print(f"try again {i}" )
    i = i+1
    if i >100:
        break

print("i  gave up !")


# even try 
is_fail = True
i = 1
while is_fail :
    if i%2 == 0:
        i=i+1
        continue
    print(f"try again{i}")
    i=i+1
    if i >100:
        break
print("i gave up !")

#Print numbers from 1 to 10
num =1
while num<=10 :
    print(num)
    num = num +1

#2. Print numbers from 10 to 1
i = 10

while i >= 1:
    print(i)
    i = i - 1

#3. Print even numbers from 1 to 20
i = 1
while i <=20:
    if i %2==0:
        print(i) 
    i = i+1

#4. Print odd numbers from 1 to 20
i = 1
while i and i<=20 :
    if i%2!=0:
        print(i)
    i = 1+1

#Skip even numbers using continue
i = 1
while i <=10:
    if i%2==0:
        i = i+1
        continue 
    print(i)
    i = i+1
    

    
#6. Print only numbers divisible by 5
i = 1
while i <=50:
    if i %5!=0:
        i = i+1
        continue


    print(i)
    i = i+1

#Print numbers from 1 to 10, but stop at five
i =1
while i <=10:
    print(i)

    if i==5:
        break
    
    i = i+1

# Print numbers from 1 to 100 but stop when i becomes greater than 20.
i =1
while i <=100:
    print(i)
    if i >=20:
        break
    
    i = i+1

#9. Keep asking until user enters 0
num = int(input(" Enter the numner : "))
while num !=0:
    print("you entered : ", num)
    num = int(input(" Enter the numner : "))
    print(" program ended")

#Keep asking for a password until the user enters the correct password.
password = input("Enter the pasword : ")
while password != "Vinay@007":
    print(" WRONG PASSSWORD ! ")
    password = input("enter the pasword")
print(" wellcome  ")

#The secret number is 7. Keep asking the user to guess until they get it right.
key = 7

key = int( input("enter the key : "))
while key!=7:
    print(" wrong ! ")
    key = int( input("enter the key : "))
print( " correct ")


#Count how many even numbers are between 1 and 100.
i = 1
count = 0
while i <=100:
    if i%2==0:
        count = count+1
    i =i+1
print("total numbers : ",count)

#Count how many odd numbers are between 1 and 100
i =1
count = 0
while i <=100:
    if i%2!=0:
        count = count+1

    i = i+1
print(" total numbers : ")

#Count how many odd numbers are between 1 and 100
i =1
count = 0
while i <=100:
    if i%2!=0:
        count = count+1

    i = i+1
print(" total numbers : ",count)

#Find the sum of numbers from 1 to 100
num = 1
sum = 0
while num <= 100:
    sum = sum+num
    num = num +1
print(" the sum is : ", sum)

#Print odd numbers from 1 to 100. Skip even numbers using continue and stop after 20 using
i = 1
while i <=100:
    if i % 2==0:
        i = i+1
        continue
    print(i)
    i = i+1

    if i==20:
        break
print(" i gave up ! ")


balance = 20000
while  True :
    print("1 check ballance : ")
    print("2 deposit : ")
    print("3 with draw : ")
    print("4 exit ")
    choice = int(input("enter the choice : "))
    if choice ==1 :
        print("balance " , balance )
    elif choice == 2:
        deposit = int(input(" enter the deposit amount : "))
        balance = balance + deposit 
        print("amount deposited & balance is : ", balance )
    elif choice ==3:
         withdraw = int(input(" enter the withdraw amount : "))
         if withdraw<=balance:
             print(" moneywith draw & balance = " , balance)
         else :
              print("insuficient amount ")
    elif choice == 4:
        print("Thank you!")
        break 
    else:
        print("invalid option ")

# FOR LOOPS
#Write a Python program to print numbers from 1 to 10 using a for loop
for i in range(1, 11):
    print(i)

#Print numbers from 10 down to 1
for i in range (1 ,20 , 2):
    print(i)

#Print all even numbers between 1 and 20.
for i in range (1,21):
    if i % 2 == 0:
        print(i)

#Print odd numbers from 1 to 20
for i in range(1,21):
    if i%2 !=0:
        print(i)

#Print multiples of 5 from 5 to 50.
for i in range(5,51,5):
    print(i)

#Print numbers from 1 to 30 that are divisible by 3.
for i in range (1,31,3):
    print(i)    

#Print numbers from 1 to 10 but don't print 5
for i in range (1,11):
    if i == 5:
        continue
    print(i)

#Print numbers from 1 to 10 but stop when you reach 5
for i in range (1,11):
    if i == 5:
        break
    print(i)

#Search for number 7 from 1 to 20 and stop when you find it.
for i in range (1,21):
    if i == 7:
        print("found")
        break
    print(i)

#Print every character in "Sandeep".
name = "sandeep"
for letter in name :
    print(letter) 

#Count the vowels in "python programming".
name  = "python programming"
count = 0
for letter in name :
    if letter in  "aeiou":
        count = count+1
print("vovels = ",count)

#Print every item from this list.
list = ["sandeep","daeshan" , "sudeep ", "yash" ]
for name in list:
    print(name)

#Find the largest number in a list.
numbers = [22,1,3,4,32]
largest = numbers[0]
for num in numbers :
    if num>largest:
        largest= num    
print("largest number in list is  : ",largest ) 


#Find the sum of numbers from 1 to 100.
total = 0
for i in range(1,101):
    total = total+i
print("total : ",total)

#Ask the user for a number and print its multiplication table.
num = int(input("enter the number : "))
for i in range (1,11):
    print(num , "x" ,i ,"=",  num*i)
