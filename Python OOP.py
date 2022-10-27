#!/usr/bin/env python
# coding: utf-8

# In[4]:


#WHY USE CLASSES? (for representing complex objects)

#using se1 and se2 objects as lists for position,name,age,level,salary
se1= ["Software Engineer","Max",24,"Junior",5000]

se2= ["Software Engineer","Lisa",28,"Senior",8000]


# In[2]:


#creating classes (a class is used as a blueprint)

class Softwareengineer:
    pass

#instance of class

se1=Softwareengineer()


# In[9]:


#another method to use class is using initialiing method

class Softwareengineer:
    def __init__(self,name,age,level,salary):
        #instance attributes (defined using __init__(self))
        self.name=name
        self.age=age
        self.level=level
        self.salary=salary
        
#instance of class (also called object)

se1=Softwareengineer("Max",24,"Junior",5000)  
print(se1.name,se1.age) #we can access those objects from print like this


# In[10]:


class Softwareengineer:
    
    #class attribute (can be used on the class name itself)
    alias="keyboard magician"
    def __init__(self,name,age,level,salary):
        #instance attributes (only tied to one instance eg: se1, we cannot use it on the whole class)
        self.name=name
        self.age=age
        self.level=level
        self.salary=salary
        
#instance of class

se1=Softwareengineer("Max",24,"Junior",5000)  
print(se1.name,se1.age) #we can access those objects from print like this

#for class attribute
print(se1.alias)
#or
print(Softwareengineer.alias)


# In[12]:


#using functions in classes

se1= ["Software Engineer","Max",24,"Junior",5000]

se2= ["Software Engineer","Lisa",28,"Senior",8000]

#let's say a second object d1
d1=("Designer","philip")

def code(se): #(if our se has to code, we define function called code)
    print(f"{se[1]} is writing code...")
    
code(se1)
code(se2)
code(d1)


# In[16]:



#and we can also define the code function inside the class and it's called "instance method"

se1= ["Software Engineer","Max",24,"Junior",5000]

se2= ["Software Engineer","Lisa",28,"Senior",8000]

#let's say a second object d1
d1=("Designer","philip")

class Softwareengineer:
    
    #class attribute (can be used on the class name itself)
    alias="keyboard magician"
    def __init__(self,name,age,level,salary):
        #instance attributes (only tied to one instance eg: se1, we cannot use it on the whole class)
        self.name=name
        self.age=age
        self.level=level
        self.salary=salary
    #instance method       
    def code(self): #(if our se has to code, we define function called code)
        print(f"{self.name} is writing code...")
#instance of class

se1=Softwareengineer("Max",24,"Junior",5000)  
se2=Softwareengineer("Lisa",28,"Senior",8000) 
print(se1.name,se1.age) #we can access those objects from print like this

se1.code()
se2.code()


# In[20]:


#another instance method

class Softwareengineer:
    
    #class attribute (can be used on the class name itself)
    alias="keyboard magician"
    def __init__(self,name,age,level,salary):
        #instance attributes (only tied to one instance eg: se1, we cannot use it on the whole class)
        self.name=name
        self.age=age
        self.level=level
        self.salary=salary
    #instance method       
    def code(self): #(if our se has to code, we define function called code)
        print(f"{self.name} is writing code...")

    def code_in_language(self,language):
        print(f"{self.name} is writing code in {language}..")
    
#instance of class

se1=Softwareengineer("Max",24,"Junior",5000)  
se2=Softwareengineer("Lisa",28,"Senior",8000) 

se1.code_in_language("python")
se2.code_in_language("c++")   
    


# In[21]:


#another instance method

class Softwareengineer:
    
    #class attribute (can be used on the class name itself)
    alias="keyboard magician"
    def __init__(self,name,age,level,salary):
        #instance attributes (only tied to one instance eg: se1, we cannot use it on the whole class)
        self.name=name
        self.age=age
        self.level=level
        self.salary=salary
    #instance method       
    def code(self): #(if our se has to code, we define function called code)
        print(f"{self.name} is writing code...")

    def code_in_language(self,language):
        print(f"{self.name} is writing code in {language}..")
    def information(self):
        information=f"name={self.name}, age={self.age}, level={self.level}"
        return information
#instance of class

se1=Softwareengineer("Max",24,"Junior",5000)  
se2=Softwareengineer("Lisa",28,"Senior",8000) 

print(se1.information())


# In[31]:


#special methods (in-built)


class Softwareengineer:
    
    #class attribute (can be used on the class name itself)
    alias="keyboard magician"
    def __init__(self,name,age,level,salary):
        #instance attributes (only tied to one instance eg: se1, we cannot use it on the whole class)
        self.name=name
        self.age=age
        self.level=level
        self.salary=salary
    #instance method       
    def code(self): #(if our se has to code, we define function called code)
        print(f"{self.name} is writing code...")

    def code_in_language(self,language):
        print(f"{self.name} is writing code in {language}..")
    def information(self):
        information=f"name={self.name}, age={self.age}, level={self.level}"
        return information
    
    #alternative to information instance method above (dunder method)
    def __str__(self):
        information=f"name={self.name}, age={self.age}, level={self.level}"
        return information
    #eq method which comapres two objects (dunder method)
    def __eq__(self,other):
        return self.name==other.name and self.age==other.age
    @staticmethod  
    def entry_salary(age):
        if age < 25:
            return 5000
        if age < 30:
            return 7000
        return 9000
        
#instance of class

se1=Softwareengineer("Max",24,"Junior",5000)  
se2=Softwareengineer("Lisa",28,"Senior",8000) 
se3=Softwareengineer("Lisa",28,"Senior",8000) 

#__str__ method output
print(se1)

#__eq__ method output
print(se2==se3)

#output for entry_salary function in case there is no self mentioned in the function, function ties to class Softwareengineer will work, 
#but if we use decorator @staticmethod before defining the function, both output print statements below will work
print(se1.entry_salary(24))
print(Softwareengineer.entry_salary(27))


# In[39]:


#Inheritance (child and parent classes)

class Employee:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    #instance method
    def work(self):
        print(f"{self.name} is working...")

#this means these below two classes iinherit all of the atttributes and functions of Employee class above
class Softwareengineers(Employee):
    pass

class Designers(Employee):
    pass


# In[40]:



se=Softwareengineers("Max",25)
print(se.name,se.age)

d=Designers("Philip",24)
print(d.name,d.age)

se.work()
d.work()


# In[ ]:




