<<<<<<< HEAD
#FizzBuzz program in Python; Created on 10/08/2022
import math

def main(): 
    for i in range(1, 101):
        if i % 3 == 0 and i % 5 == 0:
            print("FizzBuzz")
        elif i % 3 == 0: 
            print("Fizz")
        elif i % 5 == 0: 
=======
#FizzBuzz challenge in Python; Created on 10/08/2022
import math

def main(): 
    #iterated through numbers 1-100
    for num in range(1, 101):
        #if the number is divisible by 3 and 5, print FizzBuzz
        if num % 3 == 0 and num % 5 == 0:
            print("FizzBuzz")
        #if the number is divisible by 3, print Fizz
        elif num % 3 == 0: 
            print("Fizz")
        #if the number is divisible by 5, print Buzz
        elif num % 5 == 0: 
>>>>>>> branch3
            print("Buzz")
        #if the number is not divisible by 3 or 5, print the number
        else: 
<<<<<<< HEAD
            print(i)
    
<<<<<<< HEAD
=======
    print(i)
>>>>>>> branch2
=======
            print(i)
    #print the string of numbers
    print(i)
>>>>>>> branch3
main()
