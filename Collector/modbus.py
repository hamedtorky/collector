from pymodbus.client.sync import ModbusSerialClient as ModbusClient
import logging
FORMAT = ('%(asctime)-15s %(threadName)-15s '
          '%(levelname)-8s %(module)-15s:%(lineno)-8s %(message)s')
logging.basicConfig(format=FORMAT)
log = logging.getLogger()
log.setLevel(logging.DEBUG)


class MODBUS(object):
    def __init__(self, buadrate, tty, timeOut):
        self.tty = tty
        self.buadrate = buadrate
        self.client = None
        self.UNIT = timeOut


    def Connect_to_clint(self):
        self.client = ModbusClient(method='rtu', port=self.tty, timeout=1, baudrate=self.buadrate)
        self.client.connect()


    def read_data(self):
        rr = self.client.read_coils(1, 1, unit=self.UNIT)
        print (rr)

    def close(self):
        self.client.close()