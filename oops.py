# -*- coding: utf-8 -*-
"""
Created on Sat Dec  8 23:03:24 2018

@author: harshal
"""

class mainLNMM:
    eyes = "brown"
    age = 22
    def thisMethod(self):
        return 'hey this method works'
    
class className:
    def createName(self,name):
        self.name = name
    def displayName(self):
        return self.name
    def saying(self):
        print("hello %s" % self.name)
        
class parentClass:
    var1 = "i am var1"
    var2 = "i am var2"
    
class childClass(parentClass):
    var2 = "i am not var2"
    
class mom:
    var1="i am mom"
    
class dad:
    var2="hey there son"
    
class childNew(mom,dad):
    var3="i am a new variable"
    
class swine:
    def apples(self):
        print("am swine")
        
class new:
    def __init__(self):
        print("this is a cnstructor")
        print("it prints out")
    
    
exampleObject = mainLNMM()
exampleObject.thisMethod()

first = className()
second = className()
first.createName('bucky')
second.createName('tony')

pob = parentClass()
cob = childClass()

childObj = childNew()

fob=open('c:/gits/python/moduleMaking/a.txt','w')
fob.write('hey brown cow')
fob.close()
fob=open('c:/gits/python/moduleMaking/a.txt','r')
fob.read()

#% read line by line
fob=open('c:/gits/python/moduleMaking/a.txt','r')
fob.readlines()

# write line by line
fob=open('c:/gits/python/moduleMaking/a.txt','w')

