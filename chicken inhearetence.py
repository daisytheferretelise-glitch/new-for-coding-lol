class Hen(object):
    def __init__(self,name, idnumber):
        self.name=name
        self.idnumber=idnumber
    def display(self):
        print(self.name)
        print(self.idnumber)

class chick(Hen):
    def  __init__(self,name,idnumber,salary,post):
          self.salary=salary
          self.post=post

          Hen.__init__(self,name,idnumber)
a=chick("Marlo",588883334,30510431244,"baby")
a.display()