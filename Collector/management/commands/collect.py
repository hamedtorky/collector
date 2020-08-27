from logging import getLogger
from django.core.management.base import BaseCommand, CommandError
from Collector.modbus import MODBUS

from Collector.models import Connection as conn



__author__ = 'HamedTorky'
__name__ = 'Collector thread'
logger = getLogger(__name__)

class Command(BaseCommand):
    help = 'Data collector '

    def add_arguments(self, parser):
        parser.add_argument('method', nargs='+', type=str)

    def handle(self, *args, **options):
        try:
            print(options['method'])
            if options['method'][1] == "MODBUS":
                print("ModBus method is running ...")
                if options['method'][2] == "model":
                    bus_info = conn.objects.filter(name=options['method'][3], connection_type="MODBUS").last()
                    if bus_info is not None:
                        modbus = MODBUS(bus_info.baudrate, bus_info.port_name,timeOut=bus_info.timeOut)
                        try:
                            modbus.Connect_to_clint()
                            while True:
                                modbus.read_data()
                                
                        except Exception as err:
                            modbus.close()
                            print (err)
                    else:
                        print("ERROR >>> Not find configration file for {} model".format(options['method'][3]))
                else: 
                    print("ERROR >>> Please select any model")
            elif options['method'][1] == "SERIAL":
                print("Serial method is running ...")
                try:
                    
                    while True:
                        pass        
                        
                except Exception as err:
                    
                    print (err)
            else:
                if options['method'][1] == "":
                    print ('Please select method ["MODBUS","SERIAL"]')
                else:
                    print ("Method '{}' is not valid ... \n Valid method is ['MODBUS','SERIAL']\nClose collector terminal".format(options['method'][1]))
        except Exception as err:
            print (err)