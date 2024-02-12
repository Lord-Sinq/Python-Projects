# Author: Clayton S. Ferner
# Date: 9/12/2023
# Description: This program implements the physical layer.
import copy
# The threading module is needed to do multi-threading
from threading import *
from Event import Event
import random

class PhysicalLayer:
    def __init__(self, Max_seq = 2, errorRate = 0.0, droppedPacketRate = 0.0, utopian = False):
        '''
        This is the constructor.
        :param Max_seq: int: number of sequences numbers to use (default = 2)
        :param errorRate: float: percent of packets to have a 1-bit error (default 0.0)
        :param droppedPacketRate: float: percent of packets lost (default 0.0)
        :param utopian: boolean: using to have a pristine channel where sender and receiver
        :return: None
        '''
    def setReturnChannel(self, returnEventsQueue, returnEventsSemas):
        '''
        Sets the return event queue and the return event queue semaphores.
        This is so that the physical channel can indicate a frame arrival.
        :param returnEventsQueue:
        :param returnEventsSemas:
        :return: None
        '''
    def isConnected(self):
        '''
        Checks if the channel is still connected
        :return: boolan
        '''
    def disconnect(self):
        '''
        Disconnects the channel
        :return: None
        '''
    def to_physical_layer(self, frame):
        '''
        This transmits a frame.
        :param frame:
        :return: None
        :raises: ConnectError: if the connection is lost.
        '''
    def from_physical_layer(self):
        '''
        This receives a frame.
        :return: Frame
        :raises: ConnectError: if the connection is lost.
        '''
    def channel2String(self):
        '''
        Returns a string of the stuff in the channel for debugging purposes.
        :return: string
        '''

