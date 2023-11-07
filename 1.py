# count = int(input("enter a number(-1 t0 quit)"))
# while count != -1: 
#         print(count)
# #         count -= 1
# #         if count == 5:
# #                 break
#         count = int(input("enter a number(-1 t0 quit)"))
           
# else:
#                print("in else block")
# print("out from loop")

### OOP ###


# class Imstructor:
#                def __init__(self,name1,adress):
#                      self.name1 = name1
#                      self.adress = adress
#                      self.follower = 0
                     



# instructor1 = Imstructor("bial",'\nabdchg\n') #name id address coputer store etc.
# print(instructor1.name1,instructor1.adress,instructor1.follower)

# instructor1.name = "payal"
# instructor1.address ="delhi"
# print(instructor1.name,instructor1.address)

# instructor2 = Imstructor() #name id address coputer store etc.
# instructor2.name = "bilal"
# instructor2.address ="delhi"
# print(instructor2.name,instructor2.address)


# class instructor:
#                follower = 0
#                def __init__(self,name,address):
#                        self.name=name
#                        self.address = address
#                 #        self.follower = 0
#                def display(self,subjec_name):
#                        print(f"hi i am {self.name} and i teach {subjec_name}")
#                def update_follower(self,follower_name):
#                        self.follower += 1
                       
                       
 
# instructor1 = instructor("bilal",'karachi')
# print(instructor1.name,instructor1.address,"\n",instructor1.follower)

# instructor1.display("python")
# instructor1.update_follower("paypal")
# print(instructor1.follower)

# instructor2= instructor("nabeel",'karachi')
# print(instructor2.name,instructor2.address)
# instructor2.update_follower("bilal")
# print(instructor2.follower)


# class Instructor:
#                 # follr = 0
               
#                 def __init__(self, name, address):
#                        self.name = name
#                        self.address = address
#                        self.follr = 0
#                 def display(self,subject_name):
#                         print(f"i am {self.name} and i am tech in {subject_name} and addres name {self.address}")

#                 def update_foolow(self,followe_name):
#                         self.follr += 1
                        
                        

# insructor_1 = Instructor('billa',"hhdgfdgf")
# print(insructor_1.name,insructor_1.address)
# insructor_1.display("english")
# insructor_1.update_foolow("bilal")
# print(insructor_1.follr)


# class Human:
#                def __init__(self,num_heart):
#                        self.num_eye = 2
#                        self.num_arm = 2
#                        self.num_heart = num_heart
#                def eat(self):
#                        print("i can eat")
#                def work(self):
#                        print("i can work")
# class Male(Human):
#         def __init__(self,name,heart):
#                 super().__init__(heart)
#                 self.name = name
                
#         def flirt(self):
#                 print("I can Flirt")
#         def work(self):
#                super().work()
#                print("I can Code")
#         def eat(self):
#                 super().eat()
#                 print("i can biryani")
#         def display(self):
#                 print(f"Hi, I am {self.name} and I have {self.num_heart} heart")
# male_1 = Male("bilal",1)

# male_1.flirt()
# male_1.eat()
# male_1.work()
# print(f"number of eye is : {male_1.num_eye}")
# print(f"number of eye is : {male_1.num_arm}")
# print(f"number of hear is : {male_1.num_heart}")
# male_1.display()



# class Human:
#                def __init__(self):
#                        self.name_eye = 2
#                        self.name_nose = 1
#                def eat(self):
#                        print("i can eat")
#                def work(self):
#                        print("I can work")
# class Male:
#         def __init__(self,name):
#                 self.name = name
#         def flirt(self):
#                 print("I can Flirt")    
#         def work(self):
#                 # super().work()
#                 print("I can code")
               
# class Boy(Male,Human):
#         def sleep(self):
#                 print("I can Sleep")
#         def work(self):
#                 # super().work()
#                 print("i can test")


# boy_1 = Boy("bilal")
# print(boy_1.)
# boy_1.work()
# Boy.mro()
# print(Boy.mro())
# boy_1.work()
# Male.work(boy_1)
# Human.eat(boy_1)


class Human:
               def __init__(self,num_heart):
                       print("human class")
                       self.name_eye = 2
                       self.name_arm = 2          
                       self.num_heart = num_heart         
               def eat(self):
                       print("i can eat")
               def work(self):
                       print("I can work")
class Male(Human):
               def __init__(self,name):
                       print("init male class")
                       self.name = name
               def sleep(self):
                       print("i can sleep")

class Boy(Male):
               def work(self):
                #        Human.work(self)
                       super().work()
                       print("I can code")

class Programmer:
        def work(self):
                print("I can write programmer")
obj = Boy(1)
# obj.work()
# prog_1= Programmer()
# prog_1.work()
print(obj.name_eye)
print(Boy.mro())