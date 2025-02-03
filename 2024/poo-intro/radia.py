import math
from pointOperationsObj import Point2d

PI = math.pi#global variable

class CentesimalAzimut():
    def __init__(self,centesimalAzimut:float):#constructor
        self.centesimalAzimut: float = None#class variable	
        self.setCentesimalAzimut(centesimalAzimut)#setter de la propiedad centesimalAzimut
    def setCentesimalAzimut(self,value:float):
        """
        Setter de centesimalAzimut. Establece el valor correcto de la propiedad
        """
        if value > 800:
            raise Exception("Angulo mayor de 800")
        if float(value) < 0:
            self.centesimalAzimut = value+400
        else:
            if float(value) > 400:
                self.centesimalAzimut = value-400
            else:
                self.centesimalAzimut = value
    #getters
    def getAsSexagesimal(self):
        return (self.centesimalAzimut*180)/200
    
    def getAsRadians(self):
        return (self.centesimalAzimut*PI)/200
        
    def getAsCentesimal(self):
        return self.centesimalAzimut

class Observation2d(CentesimalAzimut):
    def __init__(self,centesimalAzimut:float,distance:float):
        CentesimalAzimut.__init__(self, centesimalAzimut)
        self._checkPositiveDistance(distance)
        self.distance2d:float = float(distance)
        
    def _checkPositiveDistance(self,value:float):
        if float(value) <= 0:
            mess="Distance must be bigger than 0"
            raise Exception(mess)
        
    def getDistance(self):
        return self.distance2d
    
    def getDistanceWithOffset(self,offset:float = 0):
        return self.distance2d+float(offset)

class Radia2d():    
    def __init__(self,base:Point2d,obs:Observation2d):
        self.base: Point2d = base
        self.obs: Observation2d = obs
        self.radiatedPt2d:Point2d=None
        self.setRadiatedPt2d()
    
    def setRadiatedPt2d(self):
        x=self.base.x + self.obs.distance2d*math.sin(self.obs.getAsRadians())
        y=self.base.y + self.obs.distance2d*math.cos(self.obs.getAsRadians())
        self.radiatedPt2d=Point2d(x,y)
        
    def getAsPoint2d(self):
        return self.radiatedPt2d
    def getAsList(self):
        return self.radiatedPt2d.getXYAsList()
    def getAsDict(self):
        return self.radiatedPt2d.getAsDict()
    def printPoint(self):
        self.radiatedPt2d.printAsList()

#demostración de uso
if __name__=="__main__":
 
    #Comprobación de Observation2d
    obs = Observation2d(centesimalAzimut=500, distance=200)
    print("Angulo en centesimal: {0}".format(obs.getAsCentesimal()))
    print("Distancia: {0}".format(obs.getDistance()))
    print("Distancia con -0.025 de offset: {0}".format(obs.getDistanceWithOffset(offset=-0.025)))
    
    #Radiación de un punto
    ptBase=Point2d(100,100) 
    rd=Radia2d(base=ptBase, obs=obs)
    print("Radiación primer punto:")
    rd.printPoint()
    
    ptBase2=Point2d(800,800)
    obs2=Observation2d(centesimalAzimut=300, distance=450)
    rd2=Radia2d(base=ptBase2, obs=obs2)
    print("Radiación segundo punto:")
    rd2.printPoint()