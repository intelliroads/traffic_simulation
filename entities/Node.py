from enum import Enum

from entities.Arc import Arc


class NodeType(Enum):
	sensor = 1
	fork = 2
	finish = 3

class Node(object):
	def __init__(self, nodeId, nodeType):
		self.nodeType = nodeType
		self.nodeId = nodeId
		self.arcs = []

	def addArc(self,arcType, nodeB, cost, distance):
		self.arcs.append(Arc(arcType,self,nodeB, cost, distance))

class TollNode(Node):
    def __init__(self, nodeId, nodeType, servers, service_rate):
        super.__init__(self,nodeId,nodeType)
        self.servers = servers
        self.service_rate = service_rate


class TrafficLightNode(Node):
   def __init__(self, nodeId, nodeType,effective_red_time, saturation_rate):
        super.__init__(self,nodeId,nodeType)
        self.effective_red_time = effective_red_time
        self.saturation_rate = saturation_rate


