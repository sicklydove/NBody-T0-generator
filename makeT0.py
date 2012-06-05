from simulation import *
from probabilityDistribution import *
from particleDistribution import *
from particleAgent import *

if  __name__  ==  '__main__':

  sim=Simulation('./0.xml')
  sim.initOutput()

  distrib=ParticleDistribution(15000, True, 100, 2)
  distribMass=ProbabilityDistribution('fixed', 0.030)
  distribxPos=ProbabilityDistribution('linear', 0, 3)
  distribxVels=ProbabilityDistribution('linear', -0.0,0.0)
  distribyVels=ProbabilityDistribution('fixed', -0.0)
  distribzVels=ProbabilityDistribution('gaussian', 0, -3.2)

  distrib.setMasses(distribMass)
  distrib.setPositions(distribxPos)
  distrib.setVelocities(distribxVels)
  sim.writeAgents(distrib.getParticleAgents())

  sim.closeOutput()
