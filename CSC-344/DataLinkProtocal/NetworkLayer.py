# Author: Clayton S. Ferner
# Date: 9/12/2023
# Description: This program implements the NetworkLayer.
import random
from Event import *

class NetworkLayer:
    def __init__(self, n = 10, eventQueue = None, eventFull = None):
        '''
        This is the constructor.
        :param n: int: The number of values to produce.
        :param eventQueue: Used to insert network_ready events
        :param eventFull: Semaphores used to indicate that an event is ready.
        '''
    def enable_network_layer(self):
        '''
        Enables the network layer to start producing values.
        :return: None
        '''
    def disable_network_layer(self):
        '''
        Disables the network so that it pauses producing values.
        :return: None
        '''
    def from_network_layer(self):
        '''

        :return: packet: string A string length NetworkLayer.packetSize of
        random ASCII characters.
        '''
    def to_network_layer(self, packet):
        '''
        This sends a packet to the network layer.
        :param packet: string A string length NetworkLayer.packetSize of
        random ASCII characters.
        :return: None
        '''
