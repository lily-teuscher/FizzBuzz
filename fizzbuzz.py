#FizzBuzz program in Python; Created on 10/08/2022
import math

def main(): 
    for num in range(1, 101):
        if num % 3 == 0 and num % 5 == 0:
            print("FizzBuzz")
        elif num % 3 == 0: 
            print("Fizz")
        elif num % 5 == 0: 
            print("Buzz")
        else: 
            print(num)
    
    print(num)

main()
