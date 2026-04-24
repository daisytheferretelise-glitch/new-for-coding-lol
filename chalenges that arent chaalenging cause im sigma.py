class a:
    def __init__(self,a):
        self.a=a
        def __it__(self,other):
            if (self.a>other.a):
                return "Ob1 is less than Obi2"
            else:
                return "Obi1 is more than Obi2"
            
        def __eq__(self,other):
            if(self.a==other.a)