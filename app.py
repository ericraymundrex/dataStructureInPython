class queue:
        def __init__(self):
                self.Q=[]
        def enqueue(self,data=-1):
                self.Q.append(data)
        def dequeue(self):
                x=self.Q[0]
                self.Q.remove(x)
                return x
        def is_empty(self):
                return len(self.Q)==0
class tree_array:
        def __init__(self):
                self.three=[]
        def create_the_tree(self):
                Q=queue()

                data=int(input("Enter the value of the root node "))
                Q.enqueue(data)
                self.three.append(data)

                while Q.is_empty()==False:
                        x=Q.dequeue()
                        data=int(input(f"Enter the left node of : {x} "))
                        if data != -1:
                                self.three.append(data)
                                Q.enqueue(data)
                        else:
                                self.three.append(None)
                        data=int(input(f"Enter the right node of : {x} "))
                        if data != -1:
                                self.three.append(data)
                                Q.enqueue(data)
                        else:
                                self.three.append(None)
                        #print(Q.Q)
        def print_the_three(self):
                decorator=1
                for data in self.three:
                        if decorator%2 == 0:
                                print("\n")
                        decorator=decorator+1
                        print(str(data)+" ",end="")
        def find_the_ancestor(self,data):
                try:
                        itr=self.three.index(data)
                        while itr>0:
                                print(self.three[itr])
                                itr=itr//2
                except Exception as e:
                        print("There is an exception : "+str(e))
if __name__=="__main__":
        T=tree_array()
        T.create_the_tree()
        T.print_the_three()
        T.find_the_ancestor(30)