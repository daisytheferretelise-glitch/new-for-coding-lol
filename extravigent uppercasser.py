class IOString():

    def get_String(self):
        self.strl =input("Input string: ")
      
    def print_String(self):
        print("Result is...:", self.strl.upper())

str1= IOString()
str1.get_String()
str1.print_String()