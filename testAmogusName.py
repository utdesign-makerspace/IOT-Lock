import usb.core
import time

device=usb.core.find(idVendor=0x413d,idProduct=0x2107)

endpoint=device[0][(0,0)][0]

if device.is_kernel_driver_active(0):
    device.detach_kernel_driver(0)

device.set_configuration()

while True:
    print(endpoint.bEndpointAddress, endpoint.wMaxPacketSize)
    time.sleep(10)