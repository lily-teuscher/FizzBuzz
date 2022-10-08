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
            print("Buzz")
        #if the number is not divisible by 3 or 5, print the number
        else: 
            print(num)
    #print the string of numbers
    print(num)
main()
