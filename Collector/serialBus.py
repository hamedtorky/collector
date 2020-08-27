import serial
import logging
FORMAT = ('%(asctime)-15s %(threadName)-15s '
          '%(levelname)-8s %(module)-15s:%(lineno)-8s %(message)s')
logging.basicConfig(format=FORMAT)
log = logging.getLogger()
log.setLevel(logging.DEBUG)


class SERIALBUS(object):
    def __init__(self, buadrate, tty, timeOut):
        self.tty = tty
        self.buadrate = buadrate
        self.client = None
        self.UNIT = timeOut
        self.PktCounter = 0
        self.rxData = []

    def Connect_to_clint(self):
        self.client = serial.Serial(self.tty, self.buadrate, timeout=self.UNIT)

        # if self.client.is_open() is False:
        #     self.client.open()
        

    def read_data(self):
        try:
            self.client.write('1'.encode())
            buff = self.client.read(1000)
            buff = buff.decode('utf-8')
            self.rxData = [buff[i:i+2] for i in range(0, len(buff), 2)]
            self.rx_buffer_validation()
            self.send_to_pipline()
            
            
        except Exception as err:
            print (err)

    def rx_buffer_validation(self):
        for i in range(len(self.rxData)):
            if self.rxData[i] == '1B':
                if self.rxData[i+1] == '3B':
                    if self.rxData[i+2] == '1B':
                        self.PktCounter = self.PktCounter +1
                        print("{}> {}> {}".format(i, self.PktCounter, len(self.rxData)))
                        print(self.rxData)

        
    
    def send_to_pipline(self):
        # print (self.rxData)
        pass

    def close(self):
        self.client.close()