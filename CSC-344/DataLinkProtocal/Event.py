# Author: Clayton S. Ferner
# Date: 9/12/2023
# Description: This program implements Events.
class Event:
    # Event Types
    frame_arrival = 801
    network_layer_ready = 802
    acknowlegement = 803
    chksumError = 804
    timeout = 805
    connectionLost = 806

    def __init__(self, type = frame_arrival):
        '''
        This is the constructor.
        :param type:
        '''
    def getType(self):
        '''
        Get the Event's type
        :return: type:
        '''
    def setType(self, type):
        '''
        Sets the type
        :param type:
        :return: None
        '''
    def __str__(self):
        '''
        Returns a string representation of the event.
        :return:
        '''
