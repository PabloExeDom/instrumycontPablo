#!/usr/bin/env python3

import visa

rm=visa.ResourceManager()

device=[]
device=rm.list_resources()

my_instrument=rm.open_resource(device[0])
print(my_instrument)

my_instrument.write('*RST')


