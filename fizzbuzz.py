#FizzBuzz program in Python; Created on 10/08/2022
import math

def main(): 
    for i in range(1, 101):
        if i % 3 == 0 and i % 5 == 0:
            print("FizzBuzz")
        elif i % 3 == 0: 
            print("Fizz")
        elif i % 5 == 0: 
            print("Buzz")
        else: 
            print(i)
    
<<<<<<< HEAD
=======
    print(i)
>>>>>>> branch2
main()
