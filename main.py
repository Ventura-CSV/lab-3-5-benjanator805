def main():
    num1 = int(input('Enter the first number: '))
    num2 = int(input('Enter the second number: '))
    num3 = int(input('Enter the third number: '))
    
    ########################################
    if  num1 == num2 and num3:
        print("duplication = 3")
    elif num1 == num2 or num2 == num3 or num3 == num1:
        print("duplication = 2")
    else: print("duplication = 0")
   
    
    ########################################
    
    duplication = 0
    ########################################
    # Do not delete the return statement
    ########################################
    return duplication


if __name__ == '__main__':
    main()
