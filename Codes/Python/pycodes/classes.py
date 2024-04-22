#class Email:
    #recepient = input("enter recepient name :")
    #subject_line = input("enter the subject line :")

    #def sending(self):
        #print("Email Sent Sucessfully..!")

#Email.sending(1)
#print(Email.recepient)
#print(Email.subject_line)

# class class_name --------> just a blueprint
#   global variables declaration
#     def methodname(parameters) ------>self : passes the global variable to the method declared in the same class
#      method data
#      return

class myname:
    name = "Anu"
    #constructor -----> used to ask input or update class variables in start
    # also can be used for parameter to predefine
    def __init__(self):
        self.name = "Ana"
        myname.name = "Saiii"
    def my_self(self):
        print("My name is " + self.name)
        self.name = "Sai"
        print("My name is " + myname.name)
        print("My name is " + self.name)

m1,m2,m3 = myname(),myname(),myname()
m1.name = "Tana"
m2.name = "Anu"
m3.name = "Sai"

m1.my_self()
m2.my_self()
m3.my_self()