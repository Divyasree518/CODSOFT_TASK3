from functools import reduce
def calculator():
    while True:
        print(20*"-","Welcome To the Calculator App",20*"-")
        print(20*"*","Calculator Menu",20*"*")
        print("1.Addition")
        print("2.Subtraction")
        print("3.Multiplication")
        print("4.Division")
        print("5.Square Each number")
        print("6.Filter Even Numbers")
        print("7.Filter Odd Numbers")
        print("8.Sum of all Numbers")
        print("9.Exit")
        choice=input("Enter your choice from 1-9 :")
        if choice=="9":
            print("Exiting.........")
            print("Thank You for using Calculator!!!!")
            break
        nums=list(map(int,input("Enter Numbers Seperated With comma's:").split(",")))  
        match choice:
            case "1":
                result=reduce(lambda a,b:a+b,nums)
                print("Sum =",result)
            case "2":
                result=reduce(lambda a,b:a-b,nums)
                print("Subtraction Result =",result)
            case "3":
                result=reduce(lambda a,b:a*b,nums)
                print("Product Result =",result)
            case "4":
                result=reduce(lambda a,b:a/b,nums)
                print("Division result =",result)
            case "5":
                result=list(map(lambda x:x**2,nums))
                print("Square of Numbers =",result)
            case "6":
                result=list(filter(lambda a:a%2==0,nums))
                print("Even Numbers =",result)
            case "7":
                result=list(filter(lambda a:a%2!=0,nums))
                print("Odd Numbers =",result)
            case "8":
                result=reduce(lambda a,b:a+b,nums)
                print("Sum is =",result)
            case _:
                print("Invalid choice! Try Again")
calculator()            
