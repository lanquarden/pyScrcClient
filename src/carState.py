'''
Created on Apr 5, 2012

@author: lanquarden
'''
import msgParser

class CarState(object):
    '''
    Class that hold all the car state variables
    '''


    def __init__(self):
        '''Constructor'''
        self.parser = msgParser.MsgParser()
        self.sensors = None
        self.angle = None
        self.curLapTime = None
        self.damage = None
        self.distFromStart = None
        self.distRaced = None
        self.focus = None
        self.fuel = None
        self.gear = None
        self.lastLapTime = None
        self.opponents = None
        self.racePos = None
        self.rpm = None
        self.speedX = None
        self.speedY = None
        self.speedZ = None
        self.track = None
        self.trackPos = None
        self.wheelSpinVel = None
        self.z = None
    
    def setFromMsg(self, str_sensors):
        self.sensors = self.parser.parse(str_sensors)
        
        self.setAngleD()
        self.setCurLapTimeD()
        self.setDamageD()
        self.setDistFromStartD()
        self.setDistRacedD()
        self.setFocusD()
        self.setFuelD()
        self.setGearD()
        self.setLastLapTimeD()
        self.setOpponentsD()
        self.setRacePosD()
        self.setRpmD()
        self.setSpeedXD()
        self.setSpeedYD()
        self.setSpeedZD()
        self.setTrackD()
        self.setTrackPosD()
        self.setWheelSpinVelD()
        self.setZD()
    
    def toMsg(self):
        self.sensors = {}
        
        self.sensors['angle'] = [self.angle]
        self.sensors['curLapTime'] = [self.curLapTime]
        self.sensors['damage'] = [self.damage]
        self.sensors['distFromStart'] = [self.distFromStart]
        self.sensors['distRaced'] = [self.distRaced]
        self.sensors['focus'] = self.focus
        self.sensors['fuel'] = [self.fuel]
        self.sensors['gear'] = [self.gear]
        self.sensors['lastLapTime'] = [self.lastLapTime]
        self.sensors['opponents'] = self.opponents
        self.sensors['racePos'] = [self.racePos]
        self.sensors['rpm'] = [self.rpm]
        self.sensors['speedX'] = [self.speedX]
        self.sensors['speedY'] = [self.speedY]
        self.sensors['speedZ'] = [self.speedZ]
        self.sensors['track'] = self.track
        self.sensors['trackPos'] = [self.trackPos]
        self.sensors['wheelSpinVel'] = self.wheelSpinVel
        self.sensors['z'] = [self.z]
        
        return self.parser.stringify(self.sensors)
    
    def getFloatD(self, name):
        try:
            val = self.sensors[name]
        except KeyError:
            val = None
        
        if val != None:
            val = float(val[0])
        
        return val
    
    def getFloatListD(self, name):
        try:
            val = self.sensors[name]
        except KeyError:
            val = None
        
        if val != None:
            l = []
            for v in val:
                l.append(float(v))
            val = l
        
        return val
    
    def getIntD(self, name):
        try:
            val = self.sensors[name]
        except KeyError:
            val = None
        
        if val != None:
            val = int(val[0])
        
        return val
    
    def setAngle(self, angle):
        self.angle = angle
    
    def setAngleD(self):        
        self.angle = self.getFloatD('angle')
        
    def getAngle(self):
        return self.angle
    
    def setCurLapTime(self, curLapTime):
        self.curLapTime = curLapTime
    
    def setCurLapTimeD(self):
        self.curLapTime = self.getFloatD('curLapTime')
    
    def getCurLapTime(self):
        return self.curLapTime
    
    def setDamage(self, damage):
        self.damage = damage
    
    def setDamageD(self):
        self.damage = self.getFloatD('damage')
        
    def getDamage(self):
        return self.damage
    
    def setDistFromStart(self, distFromStart):
        self.distFromStart = distFromStart
    
    def setDistFromStartD(self):
        self.distFromStart = self.getFloatD('distFromStart')
    
    def getDistFromStart(self):
        return self.distFromStart
    
    def setDistRaced(self, distRaced):
        self.distRaced = distRaced
    
    def setDistRacedD(self):
        self.distRaced = self.getFloatD('distRaced')
    
    def getDistRaced(self):
        return self.distRaced
    
    def setFocus(self, focus):
        self.focus = focus
    
    def setFocusD(self):
        self.focus = self.getFloatListD('focus')
    
    def setFuel(self, fuel):
        self.fuel = fuel
    
    def setFuelD(self):
        self.fuel = self.getFloatD('fuel')
    
    def getFuel(self):
        return self.fuel
    
    def setGear(self, gear):
        self.gear = gear
    
    def setGearD(self):
        self.gear = self.getIntD('gear')
    
    def getGear(self):
        return self.gear
    
    def setLastLapTime(self, lastLapTime):
        self.lastLapTime = lastLapTime
    
    def setLastLapTimeD(self):
        self.lastLapTime = self.getFloatD('lastLapTime')
    
    def setOpponents(self, opponents):
        self.opponents = opponents
        
    def setOpponentsD(self):
        self.opponents = self.getFloatListD('opponents')
    
    def getOpponents(self):
        return self.opponents
    
    def setRacePos(self, racePos):
        self.racePos = racePos
    
    def setRacePosD(self):
        self.racePos = self.getIntD('racePos')
    
    def getRacePos(self):
        return self.racePos
    
    def setRpm(self, rpm):
        self.rpm = rpm
    
    def setRpmD(self):
        self.rpm = self.getFloatD('rpm')
    
    def getRpm(self):
        return self.rpm
    
    def setSpeedX(self, speedX):
        self.speedX = speedX
    
    def setSpeedXD(self):
        self.speedX = self.getFloatD('speedX')
    
    def getSpeedX(self):
        return self.speedX
    
    def setSpeedY(self, speedY):
        self.speedY = speedY
    
    def setSpeedYD(self):
        self.speedY = self.getFloatD('speedY')
    
    def getSpeedY(self):
        return self.speedY
    
    def setSpeedZ(self, speedZ):
        self.speedZ = speedZ
    
    def setSpeedZD(self):
        self.speedZ = self.getFloatD('speedZ')
    
    def getSpeedZ(self):
        return self.speedZ
    
    def setTrack(self, track):
        self.track = track
    
    def setTrackD(self):
        self.track = self.getFloatListD('track')
    
    def getTrack(self):
        return self.track
    
    def setTrackPos(self, trackPos):
        self.trackPos = trackPos
    
    def setTrackPosD(self):
        self.trackPos = self.getFloatD('trackPos')
    
    def getTrackPos(self):
        return self.trackPos
    
    def setWheelSpinVel(self, wheelSpinVel):
        self.wheelSpinVel = wheelSpinVel
    
    def setWheelSpinVelD(self):
        self.wheelSpinVel = self.getFloatListD('wheelSpinVel')
    
    def getWheelSpinVel(self):
        return self.wheelSpinVel
    
    def setZ(self, z):
        self.z = z
    
    def setZD(self):
        self.z = self.getFloatD('z')
    
    def getZ(self):
        return self.z
    
    