from django.db import models

# Create your models here.

PORT_TYPE=(
    ('MODBUS','MODBUS'),
    ('SERIAL','SERIAL')
    )


class Connection(models.Model):
    name = models.CharField(max_length=100)
    connection_type = models.CharField(max_length=100, choices=PORT_TYPE)
    port_name = models.CharField(max_length=100, help_text="ex : /dev/ttyUSB0")
    baudrate = models.IntegerField(default=9600)
    timeOut = models.IntegerField(default=1, help_text="<1")

    def __str__(self):
        return self.name

