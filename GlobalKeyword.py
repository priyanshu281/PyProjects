x=9

class MyClass:
    #x =9  this will give error
    def set_global_x(self, value):
        global x
        x = value

    def print_global_x(self):
        print(x)

if __name__ == "__main__":
    obj = MyClass()
    #obj.set_global_x(10)
    obj.print_global_x()  # Output will be 10
