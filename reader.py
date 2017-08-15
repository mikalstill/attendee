#!/usr/bin/python

import usb.core
import usb.util

# Find our device

def filt(dev):
    # NOTE(mikal): this is written like this because I am sure there will be
    # other devices we want to match later and I am unsure that this vendor /
    # product combination is unique to this device.
    if dev.idVendor == 0xffff and dev.idProduct == 0x0035:
        return True
    return False

for dev in usb.core.find(find_all=True, custom_match=filt):
    print dev
    dev.set_configuration()
