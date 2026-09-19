import math as np

def ex1():
    user_input = float(input("Enter circle radius? "))
    radius = user_input
    area = np.pi * radius**2
    print(f"Circle area = {round(area, 0)}")

def ex2():
    user_input = float(input("Enter the temperature in Celsius? "))
    c_degree = user_input
    f_degree = (c_degree * 1.8) + 32
    print(f"{c_degree} (C) = {round(f_degree, 0)} (F)")

def ex3():
    # Check a number is prime or not
    user_input = int(input("Enter a number? "))
    num = user_input
    if(num < 2):
        is_prime = False
    is_prime = True
    for i in range(1, int(np.sqrt(num))):
        if(num % i == 0):
            is_prime = False
            break
    
    if(is_prime):
        print(f"{num} is a prime number")
    else:
        print(f"{num} is NOT a prime number")

def ex4():
    user_input = int(input("Enter a number? "))
    num = user_input
    if(num < 0):
        print("Not a positive interger")
        return
    divisors = [1]
    for i in range(2, int(num/2)+1):
        if(num % i == 0):
            divisors.append(i)
   
    sum = 0
    for i in divisors:
        sum += i
    if sum == num:
        print(f"{num} is a perfect number")
    else:
        print(f"{num} is NOT a perfect number")

def ex5():
    colors = ("red", "green", "magenta", "blue")
    user_input = input("What is your favorite color? ")
    for i in range(0, len(colors)):
        if user_input.lower() == colors[i]:
            print(f"Your color is at index {i+1} in my list")
            return
    print("Sorry, I could not find your color")

def ex6():
    range1 = range(0, 6+1, 1)
    range2 = range(1, 10+1, 3)
    range3 = range(5, 1-1, -1)
    range4 = range(6, -2-1, -2)
    print(f"range1: {list(range1)}")
    print(f"range2: {list(range2)}")
    print(f"range3: {list(range3)}")
    print(f"range4: {list(range4)}")

def ex7():
    user_input = input("Enter a string with a dollar sign($)? ")
    newstring = ""
    b = 0
    for i in range(0, len(user_input)):
        if user_input[i] == '$':
            newstring += user_input[b:i]
            b = i + 1

    newstring += user_input[b:]
    print(f"the new string is {newstring}")

def ex8():
    user_input = list(input("Enter a list of interger? ").split(" "))
    extract_even = []
    for i in user_input:
        if int(i) % 2 == 0:
            extract_even.append(i)
    print(f"The new string is {extract_even}")

def ex9():
    user_input = int(input("Enter a number? "))
    num = user_input
    if num < 1:
        print("Error: can't enter number less than 1")
    factorial_num = 1
    for i in range(2, num+1):
        factorial_num *= i

    print(f"The factorial number is {factorial_num}")

def ex10():
    user_input = int(input("Enter a number? "))
    num = user_input
    if(num < 0):
        print("Not a positive interger")
        return
    divisors = [1]
    for i in range(2, int(num/2)+1):
        if(num % i == 0):
            divisors.append(i)
   
    print(f"divisors of {num} is {divisors}")

def ex11():
    user_input = list(input("Enter a point A[x, y]? ").split(" "))
    A = user_input
    user_input = list(input("Enter a point B[x, y]? ").split(" "))
    B = user_input

    if(len(A) != 2 or len(B) != 2):
        print("You not enter 2 points correctly!")
        return
    AB = [int(B[0]) - int(A[0]), int(B[1]) - int(A[1])]
    ans = np.sqrt(abs(AB[0]**2 + AB[1]**2))
    print(f"The length between 2 points is: {ans}")


def ex12():
    user_input = int(input("Enter m? "))
    m = user_input
    user_input = int(input("Enter n? "))
    n = user_input

    for i in range(0, m):
        for j in range(0,n):
            if(i == 0 or i == m-1):
                print('*', end="")
            elif(j == 0 or j == n-1):
                print('*', end="")
            else:
                print(' ', end="")
        print('')

def main():
    ex1()
    ex2()
    ex3()
    ex4()
    ex6()
    ex7()
    ex8()
    ex9()
    ex10()
    ex11()
    ex12()
main()
