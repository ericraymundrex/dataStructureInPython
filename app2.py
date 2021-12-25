from email.errors import NonPrintableDefect


if __name__=="__main__":
    x=int(input("Enter the value of x "))
    y=int(input("Enter the value of y "))
    try:
        z=x/y
    except Exception as e:
        print("The exception occured "+str(e))
        z=None
    print(z)