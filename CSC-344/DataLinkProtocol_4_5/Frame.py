# Author: Clayton S. Ferner
# Date: 9/12/2023
# Description: This program demonstrates the Data Link protocol 3.
import sys

class Frame:
    # Frame Type
    data = 777 # Just sending a normal frame of data
    ack = 778  # Acknowledgement frame
    nak = 779  # Non-acknowledgement frame
    eot = 780  # Marks the end of transmission

    # This is not a Frame Type
    flagByte = 126 # In binary is 01111110

    def __init__(self, type = data, seq = None, ack = None, payload = None):
        '''
        This is the constructor.
        :param type: Frame type
        :param seq: int: sequence number of this frame
        :param ack: int: ackowledgement of a frame received
                         that is sent back using this frame
        :param payload: any type: Contents (i.e. packet)
        '''
    def getType(self):
        '''
        Gets the frame type
        :return: Frame type
        '''
    def getSeq(self):
        '''
        Gets the sequence number
        :return: int: sequence number
        '''
    def getAck(self):
        '''
        Gets the acknowledgment number
        :return: int: acknowledgement number
        '''
    def getPayload(self):
        '''
        Gets the payload
        :return: any type: returns the packet
        '''
    def setType(self, type):
        '''
        Sets the type of the frame
        :param type: int: type
        :return: None
        '''
    def setSeq(self, seq):
        '''
        Sets the sequence number of the frame
        :param seq: int: sequence number
        :return: None
        '''
    def setAck(self, ack):
        '''
        Sets the acknowledgement number of the frame
        :param ack: int: acknowledgement number
        :return: None
        '''
    def setPayload(self, payload):
        '''
        Sets the payload of the fram
        :param payload: anytype: packet
        :return: None
        '''
    def __str__(self):
        '''
        Returns a string representation of the frame so that it can be printed.
        :return: string:
        '''
    def prettyType(self):
        '''
        Returns a string representation of the type.
        :return: string:
        '''
