## What is Encapsulation?
# Encapsulation mai hum data ko hide krty hai and uskop access krny ky liyai hum method ko use krty hai.
# Method ko use krty hai kyunki hum chahaty hai ky humari data ko koi bhi access na kar sake.
# Getter and Setter methods o use krty hai .
class Person:
    def __init__(self,name,age):
        self.name=name ## public attributes
        self.__age=age ## private attributes 
    
    def get_age(self):
        return self.__age
    
    def set_age(self,new_age):
        if new_age>0:
            self.__age=new_age
        else:
            print("Age must be positive!")
#object            
person = Person("Samia", 30)
# access attributes public
print(person.name)
#access attributes private
## note: private attributes kabhi bhi  outside access nhi hoga hum isko access method ky through krty h.
# get value ko read krta h
print(person.get_age())
#set update krta h value ko and chnge bhi
person.set_age(25)
print(person.get_age())