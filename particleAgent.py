class ParticleAgent:
  def __init__(self, mass, isDark, particleGroup, (xPos, yPos, zPos), (xVel, yVel, zVel)):
    self.xPos=xPos
    self.yPos=yPos
    self.zPos=zPos
    self.xVel=xVel
    self.yVel=yVel
    self.zVel=zVel
    self.mass=mass
    self.isDark=isDark
    self.particleGroup=particleGroup

  #Return XML for writing to t0 files
  def getAgentXML(self):
    outStr='<xagent>'
    outStr+=makeXML("name", "Particle")
    outStr+=makeXML("mass", self.mass)
    outStr+=makeXML("isDark", self.isDark)
    outStr+=makeXML("x", self.xPos)
    outStr+=makeXML("y", self.yPos)
    outStr+=makeXML("z", self.zPos)
    outStr+=makeXML("xVel", self.xVel)
    outStr+=makeXML("yVel", self.yVel)
    outStr+=makeXML("zVel", self.zVel)
    outStr+=makeXML("particleGroup", self.particleGroup)
    outStr+='</xagent>\r\n'
    return outStr

  def setMass(self, mass):
    self.mass=mass

  def setIsDark(self, isDark):
    self.isDark=isDark

  def setParticleGroup(self, offset):
    self.particleGroup=offset
  
  def setPositions(self, x,y,z):
    self.xPos=x
    self.yPos=y
    self.zPos=z

  def setVels(self, x,y,z):
    self.xVel=x
    self.yVel=y
    self.zVel=z


def makeXML(tag, value):
  return "<"+tag+">"+str(value)+"</"+tag+">"
