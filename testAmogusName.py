import usb.core

device=usb.core.find(idVendor=0x413d,idProduct=0x2107)

device.set_configuration()

endpoint=device[0][(0,0)][0]

if device.is_kernel_driver_active():
    device.detach_kernel_driver()

while True:
    print(endpoint.bEndpointAddress, endpoint.wMaxPacketSize)