# Author: Clayton S. Ferner
# Date: 8/26/2023
# Description: This program demonstrates the Data Link protocol 5.
# This protocol is duplex, meaning that we have two senders, sending
# data to each other. Acknowlegements will be send along with the data. 3
# This protocol assumes that the network can dropped frames as well
# as introduce 1-bit errors.  There is a timer, so that if we do not 
# receive the acknowledgement within a certain time we will retransmit. 2
#
# Up to MAX_SEQ frames are send without acknowlegements.  If the frames
# are not acknowleged within the time out, then the entire window of 
# frames are retransmitted.  We will use culmulative acknowledgement,
# meaning, that if frame 5 is acknowledged, we assume that frames 0-4
# are also being acknowledged. 
#
# The packets contain ASCII characters, which are 7-bits.  The extra bit,
# The highest order bit, will be used to add even-parity to the byte.  0


# The threading module is needed to do multi-threading

# **** PUT YOUR NAME HERE ****
# STUDENTS NAME: Sinclair DeYoung
from threading import Thread,Semaphore,Timer
from Event import Event
from Frame import Frame
from PhysicalLayer import PhysicalLayer
from NetworkLayer import NetworkLayer
import random
import time
import sys
import os

class DataLinkLayer:
    def __init__(self, N = 10, Max_seq = 2, errorRate = 0.0, droppedPacketRate = 0.0, timeout = 10, name=""):
        '''
        This is the constructor.
        :param: Max_seq: int: number of sequences numbers to use (default = 2)
        :param: errorRate: float: percent of packets to have a 1-bit error (default 0.0)
        :param: droppedPacketRate: float: percent of packets lost (default 0.0)
        :param: timout: int: number of seconds before a timeout, in which case we retransmit (default 10)
        :param: name: string: used for debugging so that we can prepend each message with an identifier
                             to know which thread produced it.
        :return: None
        '''
        self.__MAX_SEQ = Max_seq
        self.__name = name

        self.__frameBuffer = [None] * (self.__MAX_SEQ + 1) # Buffer the frames until they are acknowledged
        self.__timeout = timeout
        self.__timerBuffer = [None] * (self.__MAX_SEQ * 1)

        self.__eventQueue = []
        self.__eventFull = Semaphore(0) # How many events are in the queue

        # We need to have access to the Physical Layer as well as the Network Layer. 2
        self.__physicalLayer = PhysicalLayer(Max_seq, errorRate, droppedPacketRate)
        self.__networkLayer = NetworkLayer(N, self.__eventQueue, self.__eventFull)
        self.__returnDataLink = None

        self.__frameBuffer = [None] * self.__MAX_SEQ
        self.__timerBuffer = [None] * self.__MAX_SEQ

    def wait_for_event(self):
        '''
        Wait for an event to occur.  The thread is blocked until an event happens.
        :param: None
        :return: Event
        '''
        self.__eventFull.acquire()
        return self.__eventQueue.pop(0)
    def eventQueue2String(self):
        '''
        Produces a string representation of the event queue for debugging purposes.
        :param: None
        :return: string
        '''
        results = ""
        for i in range(len(self.__eventQueue)):
            results += str(self.__eventQueue[i]) + " "
        return results
    def frameBuffer2String(self):
        '''
        Produces a string representation of the frame buffer for debugging purposes.
        :param: None
        :return: string
        '''
        results = "["
        for i in range(len(self.__frameBuffer)):
            results += str(self.__frameBuffer[i]) + ","
        return results + "]"
    def setReturnLink(self, datalink):
        '''
        Sets the return datalink, so that the physical layer can add events when a frame arrives.
        :param: DataLinkLayer
        :return: None
        '''
        self.__returnDataLink = datalink
        self.__physicalLayer.setReturnChannel(datalink.__eventQueue, datalink.__eventFull)
    def computeCheckSum(self, packet):
        '''
        Computes the parity for each character in the packet.  The packet is assumed to
        be a string of ASCII characters. ASCII characters are 7-bits.  This means that the
        most-significant bit of each character is a zero.  This function will compute the
        parity, then set the most-significant bit to a one (or not) to make sure that the
        parity of the byte is even parity.  This transforms the ASCII character into a
        unicode character.

        :param: packet: string: a string of ASCII characters, which must be between 0 and 128.
        :return: string: a string of Unicode characters between 0 and 256.
        '''

        # packet is a string of 7-bit ASCII characters. n
        # Convert the string to a list of integers. o
        listOfBytes = []
        for c in packet:
            listOfBytes.append(ord(c))

        # Count the number of 1's in the binary representation (bit_count())
        # and it it is odd, then add a 1 to the left-most bit.  We can use
        # the left-most bit because ASCII only uses the lest significant 7 bits
        # of the byte.  The most-significant is not used.  This would be 2**7 or 128. t
        for i in range(len(listOfBytes)):
            sum = listOfBytes[i].bit_count()
            if sum % 2 == 1:
                listOfBytes[i] = listOfBytes[i] | 2 ** 7 # 10000000

        # Convert back to a string, which would not be unicodes.
        newPacket = ""
        for b in listOfBytes:
            newPacket += chr(b)
        return newPacket
    def verifyCheckSum(self, packet):
        '''
        Computes the parity for each character in the packet.  If the parity of any byte
        is odd, the return an error.

        If all bytes are even parity, then convert (and return) the packet back to a string
        of ASCII characters. ASCII characters are 7-bits.  This means that the
        most-significant bit of each character is a zero.

        :param: packet: string: a string of Unicode characters, where the most-significant bit
            is the parity.
        :return: boolean,string tuple: an error and a string of Unicode characters between 0 and 256.
        '''
        error = False

        # If we have an empty packet, then it isn't a parity error. y
        if packet == "":
            return False, ""

        # packet is a string of 8-bit unicode characters
        # Convert the string to a list of integers
        listOfBytes = []
        for c in packet:
            listOfBytes.append(ord(c))

        # Count the number of 1's in the binary representation (bit_count()). a
        # and it it is odd, its an error because we are using even parity.
        # the left-most bit because ASCII only uses the lest significant 7 bits
        # of the byte.  The most-significant is not used.  This would be 2**7 or 128.
        for i in range(len(listOfBytes)):
            sum = listOfBytes[i].bit_count()
            if sum % 2 == 1:
                error = True
                # print("checksum error with packet = " + str(packet))
                return error,packet
            # Make the most significant bit a zero again to convert from an 8-bit
            # unicode back to 7-bit ASCII.
            listOfBytes[i] = listOfBytes[i] & (2 ** 7 - 1)  # 01111111

        # Convert back to a string, which would not be ASCII.
        newPacket = ""
        for b in listOfBytes:
            newPacket += chr(b)
        return False,newPacket

    def sender(self, name, id):
        '''
        Sends n frames to the receiver, where each from is a packet that comes from the
        network layer.  If the receiver doesn't acknowledge the frame was received within
        the timeout period, then transmit it again.
        :param: name: string: just a name for debugging purposes.
        :param: id: int: Each thread needs to have a unique id. These are assumed to start
                     at zero.  Each sender will transmit on channel id (called the forward channel),
                     and receive on channel 1-id (called the back channel).
        :return: None
        '''
        # These are used to display all the data that was transmitted and received so that we
        # can easily see that the data was exchanged correctly. l
        sentCompleteData = ""
        receivedCompleteData = ""

        ack_expected = 0
        next_frame_to_send = 0
        frame_expected = 0
        next_acknowledgement = self.__MAX_SEQ
        numBuffered = 0


        done = False
        EOTsent = False
        EOTreceived = False

        self.__networkLayer.enable_network_layer()

        try:
            packet = self.__networkLayer.from_network_layer()
            if packet == "":
                print(name + " empty packet, stopping")
                outFrame = Frame(type=Frame.eot, payload=packet)
                EOTsent = True
                if EOTreceived:
                    done = True
            else:
                sentCompleteData += packet + "\n"
                packetWithCheckSum = self.computeCheckSum(packet)
                outFrame = Frame(type=Frame.data, payload=packetWithCheckSum)
            outFrame.setSeq(next_frame_to_send)
            outFrame.setAck(next_acknowledgement)
            print(name + " Sending frame " + str(outFrame))
            self.__physicalLayer.to_physical_layer(outFrame)
            self.__timer = Timer(self.__timeout, self.addTimeoutEvent)
            print(name + " starting timer")
            self.__timer.start()
            while not done:
                event = self.wait_for_event()

                if event.getType() == Event.frame_arrival:
                    inFrame = self.__returnDataLink.__physicalLayer.from_physical_layer()

                    if inFrame.getSeq() == frame_expected:
                        packetWithCheckSum = inFrame.getPayload()
                        error, packet = self.verifyCheckSum(packetWithCheckSum)

                        if not error:
                            print(name + " received valid frame = " + str(inFrame))
                            self.__timer.cancel()
                            next_acknowledgement = inFrame.getSeq()
                            self.__networkLayer.to_network_layer(packet)
                            receivedCompleteData += packet + "\n"
                            frame_expected = (frame_expected + 1) % self.__MAX_SEQ

                    if inFrame.getType() == Frame.eot:
                        EOTreceived = True
                        if EOTsent:
                            done = True

                    while self.between(ack_expected, inFrame.getAck(), next_frame_to_send):
                        if self.__timerBuffer[ack_expected] is not None:
                            self.__timerBuffer[ack_expected].cancel()
                        numBuffered -= 1
                        self.__frameBuffer[ack_expected] = None
                        ack_expected = (ack_expected + 1) % self.__MAX_SEQ

                    if inFrame.getAck() == next_frame_to_send:
                        self.__timer.cancel()
                        packet = self.__networkLayer.from_network_layer()
                        if packet == "":
                            print(name + " empty packet, stopping")
                            outFrame = Frame(type=Frame.eot, payload=packet)
                            EOTsent = True
                            if EOTreceived:
                                done = True
                        else:
                            sentCompleteData += packet + "\n"
                            packetWithCheckSum = self.computeCheckSum(packet)
                            outFrame = Frame(type=Frame.data, payload=packetWithCheckSum)

                        next_frame_to_send = (next_frame_to_send + 1) % self.__MAX_SEQ
                elif event.getType() == Event.timeout:
                    frame_num = ack_expected
                    print(name + "********** Time Out **********")
                    for i in range(numBuffered):
                        self.send_data(frame_num, next_acknowledgement)
                        frame_num = (frame_num + 1) % self.__MAX_SEQ
                        print(name + "********** Time Out **********")
                        pass
                if (numBuffered < self.__MAX_SEQ - 1):
                    self.__networkLayer.enable_network_layer()
                else:
                    self.__networkLayer.disable_network_layer()

                outFrame.setSeq(next_frame_to_send)
                outFrame.setAck(next_acknowledgement)
                print(name + " sending frame " + str(outFrame))
                self.__physicalLayer.to_physical_layer(outFrame)
                self.__timer = Timer(self.__timeout, self.addTimeoutEvent)
                print(name + " starting timer")
                self.__timer.start()

                time.sleep(random.randint(1, 2))

            self.__physicalLayer.disconnect()
            self.__returnDataLink.__physicalLayer.disconnect()
        except ConnectionError:
            print(name + " Connect Lost")
        print(name + " sent data: \n" + str(sentCompleteData))
        print(name + " received data: \n" + str(receivedCompleteData))

    @staticmethod
    def between(a, b, c):
        '''
        This is a static method that determins if b is between a and c circularly.

        Since it is a static method, it is called by doing DataLinkLayer.between(a, b, c).

        Since a, b, and c are circular, it means that this returns true if:
           ... a ...  b ... c ...
        or
           ... c ... a ... b ...
        :param: a: int
        :param: b: int
        :param: c: int
        :return: boolean
        '''

        # implement the between() code here
        return a<c and (a<=b and b<=c) or a>c and (b<=c or a<=b)

    def send_data(self, frameNum, next_acknowledgement, name = ""):
        '''
        Sends a frame from the buffer with an acknowledgement. The frameNum is the index into
        the frame buffer.  The sequence number will be the frameNum.  A timer is set so that
        if the sent frame is not acknowledged within the timeout, it is retransmitted.
        :param: frameNum: int: index into the frame buffer. Also the sequence number.
        :param: next_acknowledgement: int: The frame to acknowledge.
        :param: name: string: just a name for debugging purposes.
        :return: None
        '''

        # implement the send_data() code here
        outFrame = self.__frameBuffer[frameNum]
        outFrame.setSeq(frameNum)
        outFrame.setAck(next_acknowledgement)
        print(name + " Sending frame " + str(outFrame))
        self.to_physical_layer(outFrame)
        self.__timerBuffer[frameNum] = Timer(10.0, self.addTimeoutEvent())
        print(name + " starting timer")
        self.__timerBuffer = Timer.start(self.__timerBuffer[frameNum])


    def addTimeoutEvent(self):
        '''
        Adds a timeout event.  This is called by the timer automatically after the timeout
        period has expired.
        :param: None
        :return: None
        '''

        for t in range(len(self.__timerBuffer)):
            if self.__timerBuffer[t] is not None:
                self.__timerBuffer[t].cancel()

        # Don't put in multiple timeout events.  One is sufficient. c
        for event in self.__eventQueue:
            if event.getType() == Event.timeout:
                return

        self.__eventQueue.append(Event(Event.timeout))
        self.__eventFull.release()


def main(argv):
    seed = 0
    if len(argv) > 2 and argv[1] == "-s":
            seed = float (argv[2])
    else:
        newSeed = os.urandom(4)
        for i in range(len(newSeed)):
            seed = seed << 8
            seed = seed + newSeed[i]

    random.seed(seed)
    print("seed = " + str(seed))

    senders = []

    numOfIterations = 8
    numSenders = 2

    # Create the DataLink
    dataLinks = []
    for i in range(numSenders):
        dataLinks.append(DataLinkLayer(N=numOfIterations, Max_seq = 6,
                             errorRate = 0.0, droppedPacketRate = 0.0, timeout = 10,
                                       name="Sender " + str(i)))

    for i in range(numSenders):
        dataLinks[i].setReturnLink(dataLinks[1-i])

    # Create threads that will be concurrent senders
    for i in range(numSenders):
        senders.append(Thread(target=dataLinks[i].sender, args=("Sender " + str(i), i,)))

    print("Main: staring threads")
    # starting the threads
    for i in range(len(senders)):
        senders[i].start()

    print("Main: threads are running")

    # Wait for threads to finish
    for i in range(len(senders)):
        senders[i].join()

    print("Main: threads are done")

if __name__ == "__main__":
    main(sys.argv)
