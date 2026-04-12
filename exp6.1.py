class stu:
    def __init__(self):
        self.rno=[]
        self.nm=[]
    def add(self):
        a=int(input('Enter roll no :'))
        self.rno.append(a)
        n=input('Enter name :')
        self.nm.append(n)
    def disp(self):
        if self.rno:
            print('Roll no  Name')
            for i in range(len(self.rno)):
                print(f"{self.rno[i]:6}  {self.nm[i]:20}")                
            return
        else:
            return None
class mse(stu):
    def __init__(self):
        super().__init__()
        self.p=[]
    def per(self):
        if self.rno:
            print(self.rno,self.nm,self.p)
            per=float(input('Enter percentage :'))
            self.p.append(per)
            return self
        else:
            return None
    def marks(self):
        if self.rno:
            print('Roll no  Name Percentage\n')
            for i in range(len(self.rno)):
                if i>=len(self.p):
                    break
                print(f"{self.rno[i]:8} {self.nm[i]:20} {self.p[i]:8.2f}")
            return
        else:
            return None
            
s=mse()
while True:
    print('\n1.Student info add\n2.Student info display\n3.Marks Entery \n4 Marklist \n5.Exit')
    c=int(input('Enter choice :'))
    if c==1:
        s.add()
    elif c==2:
        m=s.disp()
        if m is None:
            print('No student present ')
    elif c==3:
         m=s.per()
         if m is None:
             print('No student present ')
    elif c==4:
        m=s.marks()
        if m is None:
             print('No student present ')
    elif c==5:
        break
    else:
        print('Enter choice within 1 to 5 :')
        
        
    
    


