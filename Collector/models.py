from django.db import models

# Create your models here.

PORT_TYPE=(
    ('MODBUS','MODBUS'),
    ('SERIAL','SERIAL')
    )

FRAM_INFO_TYPE =(
    ('PXI','PXI'),
    ('SSI','SSI')
    ) 


class Connection(models.Model):
    name = models.CharField(max_length=100)
    connection_type = models.CharField(max_length=100, choices=PORT_TYPE)
    port_name = models.CharField(max_length=100, help_text="ex : /dev/ttyUSB0")
    baudrate = models.IntegerField(default=9600)
    timeOut = models.IntegerField(default=1, help_text="<1")

    def __str__(self):
        return self.name


class PXIConfiguration(models.Model):
    name = models.CharField(max_length=100, choices=FRAM_INFO_TYPE)
    packet_size = models.IntegerField(default=200)
    packet_header_1 = models.IntegerField(default=27)
    packet_header_2 = models.IntegerField(default=59)
    packet_header_3 = models.IntegerField(default=27)

    CRC_size = models.IntegerField(default=2)
    
    def __str__(self):
        return "{}  ***Note  : Active last model ".format(self.name)
