import serial
import logging


from Collector.models import PXIConfiguration as pxi

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
        self.data = []
        self.fram_info = pxi.objects.filter(name="PXI").last()


    def Connect_to_clint(self):
        self.client = serial.Serial(self.tty, self.buadrate, timeout=(0.01))

        # if self.client.is_open() is False:
        #     self.client.open()

    def write_data(self):
        self.client.write('1'.encode())    

    def read_data(self):
        try:
            
            self.write_data()
            buff = self.client.read(self.fram_info.packet_size+50)
            buff = buff.hex()
            if len(buff) > 0:
                self.rxData = [buff[i:i+2] for i in range(0, len(buff), 2)]
                self.rx_buffer_validation()            
            
        except Exception as err:
            print (err)

    def rx_buffer_validation(self):
        if int(self.rxData[0],16) == self.fram_info.packet_header_1 and int(self.rxData[1],16) == self.fram_info.packet_header_2 and int(self.rxData[2],16) == self.fram_info.packet_header_3:

            paket_size = ((int(self.rxData[9], 16) << 8) + int(self.rxData[10], 16))
            counter = ((int(self.rxData[5], 16) << 28) + (int(self.rxData[6], 16) << 16)+ (int(self.rxData[7], 16) << 8)+ (int(self.rxData[8], 16)))
            origin = (int(self.rxData[3], 16))
            destination = (int(self.rxData[4], 16))

            sum = paket_size + counter + origin + destination
            
            for i in range(paket_size):
                sum = sum + int(self.rxData[i+11], 16)
            _pkt_sum = (int(self.rxData[212], 16) << 8)+int(self.rxData[211], 16)

            if _pkt_sum == sum :
                self.send_to_pipline()
            else:
                print("paket not valid")    



    def send_to_pipline(self):
        print(":D")

    def close(self):
        self.client.close()