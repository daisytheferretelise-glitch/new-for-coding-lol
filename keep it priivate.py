class MyClass:
    __privateVar = 27;
    def __privMeth(self):
        print("I am inside class myclass")
    def hello(self):
        print("private value:",MyClass.__privateVar)
foo= MyClass()
foo.hello()
foo.__privMeth()