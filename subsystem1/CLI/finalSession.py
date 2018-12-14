from finalPCAP import PCAP
from finalMessageType import messageType
from finalFilter import filter
import subprocess
import xml.etree.ElementTree as ET

class Session:

    #New session object as defined within the srs and sdd
    def __init__(self, name, description):
        self.SessionName = name
        self.description = description
        self.filterList = list()
        self.messageTypeList  = list()

    #Binds the given PDML to the session object
    #placeholder until we figure out how this works lol
    def addPDML(self,pdmlObject):
        self.sessionPDML = pdmlObject

    #add a messageType object to the session
    def addMessageType(self,messageType):
        self.messageTypeList.append(messageType)

    #add a filter object to the session
    def addFilter(self, filter):
        self.filterList.append(filter)

testPcap = PCAP("testPcap", "no file")
testPcap.convertToPdml()

testFilter = filter("ipx only", "ipx")

testMessageType = messageType("nameIsTest","name=test")

#testPcap.convertToPdml()
#print testPcap

testSession = Session("test","A session used to showcase CLI functionality")
pdml = testPcap.convertToPdml()
testSession.addPDML(pdml)
testSession.addFilter(testFilter)
testSession.addMessageType(testMessageType)

#print testSession.sessionPDML
print testSession.description
print testSession.filterList
print testSession.SessionName
print testSession.messageTypeList



#print testSession