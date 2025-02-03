import typing
'''
Created on 16 feb. 2023

@author: Gaspar Mora Navarro
Dep. Ing. Cartografica, Geodesia y Fotogrametri­a

---
Explanation of why classes and objects (OOP) are interesting
---
Classes are ways to organize data, like lists, but they can also do things
through methods.
With a list you can store three coordinates [x,y,z], but with a class
you can store that information and do things with it.
Point3D, for example:
    - Converts coordinates to numbers in case they come in list form
    - Checks that there are no negative coordinates
    - Returns the coordinates in list form
    - Prints the coordinates
    
Each 3d point can do the above mentioned by creating it this way:
    Point3d(10,20,30)
A list is created similarly, 
    [10,20,30] 
    but it does nothing.
    
Concepts you need to know to use OOP:
    - How to create a class
    - How to create the constructor
    - How to create public and private methods
    - How to create public and private class variables
    - How to access class variables
    - Difference between class and local variables
    - How to inherit from another class
    - What is a parent class and a child class
    - How to initialize the parent class
    - How to override a method from a parent class in a child class
    
In this simple program you have a working example of all the above mentioned.
I encourage you to investigate it, and ask me what you don't understand.
This knowledge will be very useful in the future.
'''

class Point2d():
    """
    Class variables, accessible from all methods with self.variable
    
    Class variables can also be made private by putting an 
    _ in front of the name. E.g.: _sum. This will indicate that the variable _sum
    is not of interest outside this class. These variables are known
    as private variables.
    """

    def __init__(self,x:float, y:float, n:int=-1):
        """
        All class methods receive a first argument called self.
        This argument is mandatory, but it is automatic. We don't have to pass it.
        
        The __init__ method is called the constructor. It is passed the necessary values
        to initialize the class variables. E.g.: pt1=Point2d(10,20,1)
        
        String values are also accepted E.g.: pt1=Point2d('10','20',1)
        """
        self.point_number: int = None
        self.x: float = None
        self.y: float = None
        #initialization of class variables
        self.point_number=n
        #check for negative values
        self._checkValue(x)
        self._checkValue(y)
        #if all goes well these variables are initialized
        self.x=float(x)
        self.y=float(y)

    def _checkValue(self,value:float):
        """
        Checks that the value is not less than zero. If that happens, it generates an error
        and terminates the program.
        An underscore is put in the name to indicate that it is not useful
        outside this class. These are known as private methods.
        """
        if float(value) < 0:
            mess="Coordinate values must be bigger than 0. Point number: {n}".format(n=self.point_number)
            raise Exception(mess)
        
    def getXYAsList(self) -> list:
        return [self.x,self.y]
    def getXYNAsList(self) -> list:
        l=self.getXYAsList()
        l.append(self.point_number)
        return l
    def getAsDict(self) -> dict:
        return {'x':self.x, 'y':self.y, 'point_number': self.point_number}
    def printAsList(self):
        print(self.getXYNAsList())

class Point3d(Point2d):
    """
    This class is known as a child class. Its parent class is Point2d.
    It has inherited all the properties and methods of the parent class, and adds more things.
    """
    def __init__(self,x:float,y:float,z:float=0,n:int=-1):
        """
        Constructor 
        String values are also accepted E.g.: pt1=Point2d('10','20','30',1)
        """
        self.z:float=None
        Point2d.__init__(self,x, y, n)
        self._checkValue(z)
        self.z=float(z)
    def getXYZAsList(self) -> list:
        return [self.x,self.y,self.z]
    def getXYZNAsList(self) -> list:
        l=self.getXYZAsList()
        l.append(self.point_number)
        return l
        
    def printAsList(self):
        """
        This method is also in the parent class. By having a method with the same
        name in the child class (this class) we are overriding
        the method of the parent class. 
        This means that if I run printAsList() on a 2d point, the result will be
        the implementation of printAsList in Point2d, and if I run printAsList on
        a 3d point the result will be
        the implementation of printAsList in Point3d
        """
        print(self.getXYZNAsList())
        
    def getAsDict(self) -> dict:
        """
        Also in the parent class (overrides)
        """
        return {'x':self.x, 'y':self.y, 'z': self.z, 'point_number': self.point_number}

class PointOperations():
    #class variable
    
    def __init__(self,l:typing.List[Point3d]):
        #constructor
        self.l:typing.List[Point3d]=l
    def sumXYZ(self)-> Point3d:
        #method
        sumX=0
        sumY=0
        sumZ=0
        for i in range(len(self.l)):
            sumX=sumX+self.l[i].x
            sumY=sumY+self.l[i].y
            sumZ=sumZ+self.l[i].z
        return Point3d(sumX,sumY,sumZ) 
    
    def geocenterXY(self) -> Point3d:
        #method
        sum:Point3d=self.sumXYZ()
        n=len(self.l)
        return Point3d(sum.x/n,sum.y/n,sum.z/n)
        
if __name__=="__main__":

    print("2d Point")
    p=Point2d(10,10,1000)
    print(p.getXYAsList())
    print(p.getXYNAsList())
    p.printAsList()
    
    print("3d Point")
    p=Point3d('20','20','20',2000)
    print(p.getXYZAsList())
    print(p.getXYZNAsList())
    p.printAsList()
    
    l=[Point3d(10,10,10),Point3d(20,20,20), Point3d(30,30,30)]
    po=PointOperations(l)
    pt1:Point3d=po.sumXYZ()
    print("Sum")
    pt1.printAsList()
    pt2:Point3d=po.geocenterXY()
    print("Geocenter")
    pt2.printAsList()
    print("Finished")