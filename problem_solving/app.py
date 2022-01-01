def factorial(num):
    #n!=(n)*(n-1)
    if num==0:
        return 1
    print(id(num))
    return num*factorial(num-1)
if __name__=="__main__":
    print(factorial(5))