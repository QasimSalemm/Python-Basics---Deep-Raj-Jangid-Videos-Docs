#check pass fail
# marks=int(input("Enter Marks : "))
# if (marks>32):
#     print("Passed! Your Marks Are : ",marks)
# else :
#     print("Fail! Try Again")
# print("Thank You")

#find greatest number from three numbers
# first_number,second_number,third_number=map(int,input("Enter three numbers by spilt space : ").split())
# if first_number >= second_number and first_number >= third_number:
#     print(first_number," is greatest")
# elif second_number >= first_number and second_number >= third_number:
#     print(second_number," is greatest")
# elif third_number >= first_number and third_number >= second_number:
#     print(third_number," is greatest")
# else:
#     print(first_number,second_number,third_number,"all numbers are equal")

#find greater number in oneline code
# first_number,second_number=map(int,input("Enter Two Numbers Spilt by Space : ").split())
# print( f"{first_number} : 1st number is greater" if first_number > second_number else f"{second_number} : 1st number is greater" if first_number != second_number else f"{first_number} {second_number} : Both numbers are equals ")

#find even and odd 
# number=int(input("Enter Your Integer Number : "))
# print(f"{number} : Even Number" if number%2==0 else f"{number} : Odd Number")

#find area of circle
# import math
# radius=float(input("Enter Radius of Circle : "))
# print(f"Area of Circle : {math.pi*radius**2}" if radius > 0 else  f"Undefined Value : {radius}")

#find area of square
# area_height,area_width=map(float,input("Enter Height and Width with Space : ").split())
# print(f"Area of Square : {area_height * area_width}" if area_height and area_width > 0 else f"Undefind : {area_height} : {area_width}")

#three integers using conditions
# try:
#     first_integer,second_integer,third_integer=map(int,(input(),input(),input()))
#     print(1 if first_integer!=second_integer!=third_integer!=first_integer else 0)
# except ValueError:
#     print("Enter Integer Values")
# except Exception as e:
#     print(f"ERROR! {e}")

#three integers using set
# try:
#     first_integer,second_integer,third_integer=map(int,(input(),input(),input()))
#     print(1 if len({first_integer,second_integer,third_integer})==3 else 0)
# except ValueError:
#     print("Enter Integer Values")
# except Exception as e:
#     print(f"ERROR! {e}")

# Multiple
# try:  
#     M,N=map(int,(input(),input()))
#     print(0 if M%N!=0 else M//N)
# except ValueError:
#     print("Enter Integer Values")
# except Exception as e:
#      print(f"ERROR! {e}")

#Pythagorean Triples
# try:
#     a,b,c=map(int,(input(),input(),input()))
#     print(1 if (a**2)+(b**2)==c**2 else 0)
# except ValueError:
#     print("Enter Integer Values")
# except Exception as e:
#     print("Error! ",e)

#ATM
# try:
#     x_amout,bank_balance=map(float,input().split(" "))
#     if x_amout % 5 == 0:
#         if (x_amout + 0.50) < bank_balance:         
#            bank_balance = bank_balance - (x_amout + 0.50)
#            print(bank_balance)
#         else:
#             print(bank_balance)
#     else :
#         print(bank_balance)
# except ValueError:
#     print("Enter Correct Value")
# except Exception as e:
#     print("Error! ",e)

#padding
# first_number=95
# second_number=2343
# third_number=43232
# print(f"\t%05d\n\t%05d\n+ %05d".expandtabs(tabsize=2)%(first_number,second_number,third_number))
# print("\t-----".expandtabs(tabsize=2))
# print(f"\t{first_number+second_number+third_number}".expandtabs(tabsize=2))

# All Prime numbers
# try:
#     n_number=int(input())
#     initail_number=2
#     while (initail_number <= n_number):
#         print(initail_number)
#         for j in range(2,initail_number):
#             print(j,end=" ")
#         #     print(j,end=" ")
#         #     if initail_number%j==0:
#         #         break
#         # else:
#         #     print(initail_number,end=" ")
#         initail_number=initail_number+1
#         print()
# except ValueError:
#     print("Invalid Value!")
# except Exception as e:
#     print(f"Error! {e}")

#Count Divisors
# try:
#     l,r,k=map(int,input().split(" "))
#     if(l!=0 and r!=0 and k!=0):   
#         count_dividend=0
#         for i in range(l,r+1):
#             if (i%k==0):
#                 count_dividend=count_dividend+1
#         print(count_dividend)
#     else:
#         print("l r k not set 0")
# except ValueError:
#     print("Enter Correct Value!")
# except Exception as e:
#     print("Error! ",e)

#Roy and Profile PictureRoy and Profile Picture
# try:
#     L=int(input())
#     N=(int(input()))

#     while(N>0):
#         W,H=map(int,input().split(" "))
#         if (W<L or H<L):
#             print("UPLOAD ANOTHER")
#         elif (W!=H):
#             print("CROP IT")
#         elif (W==H):
#             print("ACCEPTED")
#         else:
#             ("Something Went Wrong!")
#         N=N-1   
# except ValueError:
#     print("Enter Correct Value!")
# except Exception as e:
#     print("Error! ",e)

print(5^7)