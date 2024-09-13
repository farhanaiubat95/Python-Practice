#Private(like) attributes & methods
#conceptual implementation
#its are meant to be used only within the class and are not accessible from outside the class
#for private, use __a(double underscore before variable)
class Account:
    def __init__(self,acc_no,acc_pass):
        self.acc_no=acc_no
        self.__acc_pass=acc_pass #private attribute
    def reset_pass(self):
        print("Account Password : ",self.__acc_pass)
    def __private_name(self): #private method
        print("Private number")
    def reset_p(self):
        self.__private_name()
        

acc1=Account("123","cqijhj")
print("Account No : ",acc1.acc_no)
acc1.reset_pass()
acc1.reset_p()
