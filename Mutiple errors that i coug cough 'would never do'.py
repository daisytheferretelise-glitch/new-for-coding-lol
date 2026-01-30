try:
    num1,num2 =eval(input("Enter 2 numbers,seperated by a comma:" 
    ""))
    result=num1/num2
    print("Result is", result)

except ZeroDivisionError:
    print("Division by zero is error!!")

except SyntaxError:
    print("comma is missing. Enter number sepearted by coma like this 1,2")

except:
    print("wrong input")
else:
    print("No Exceptions")

finally:
    print("This will excute no matter what")