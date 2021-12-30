
def febi(n):  
    if n==1:
        return 1
    if n==0:
        return 0

    return febi(n-1)+febi(n-2)
    
if __name__=="__main__":
    print(febi(6))