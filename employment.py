class Employee:
    def __init__(self):
        print("Employee created")
    def __del__(self):
        print("Destroucter called")
def Creator_obj():
    print("Making Obiect")
    obj=Employee()
    print("function ended")
    return obj
print("calling Create_obj() function...")
obj=Creator_obj()
print("program ended..")