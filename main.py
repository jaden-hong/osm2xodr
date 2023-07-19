from math import floor, pi
import numpy as np
from OSMParser.testing import TestEntity, _test_nodes, testSimpleRoad, test_3WayTCrossing2
from OSMParser.osmParsing import parseAll,rNode, OSMWay,JunctionRoad, OSMWayEndcap, createOSMJunctionRoadLine, createOSMWayNodeList2XODRRoadLine
from OSMParser.xodrWriting import startBasicXODRFile,fillNormalRoads,fillJunctionRoads

osmPfad = r'C:\Users\jhong324\Documents\RESEARCH\osm\westernNeighbourhood2.osm'
#topographieKartenPfad = ''
xodrPfad = r'C:\Users\jhong324\Documents\RESEARCH\xodr\westernNeighbourhood2.1.xodr'

#parseAll(osmPfad, bildpfad=topographieKartenPfad, minimumHeight = 163.0, maximumHeight= 192.0, curveRadius=12)
parseAll(osmPfad, minimumHeight = 163.0, maximumHeight= 192.0, curveRadius=12)

startBasicXODRFile(xodrPfad)
fillNormalRoads(xodrPfad)
fillJunctionRoads(xodrPfad)

