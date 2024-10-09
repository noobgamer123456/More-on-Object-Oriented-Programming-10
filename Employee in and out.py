class Employee:
    
    def __init__(self):
        print('Employee Created')
        
        
    def __del__(self):
        print("Destructor called")
        

def Create_obj():
    print('Making Object ....')
    obj = Employee()
    print('function end ....')
    return obj

obj = Create_obj()
print('Program End....')