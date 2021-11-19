import usb.core
import time

device=usb.core.find(idVendor=0x413d,idProduct=0x2107)

if device is None:
    raise ValueError('Device not found')

endpoint=device[0][(0,0)][0]

if device.is_kernel_driver_active(0):
    device.detach_kernel_driver(0)

device.set_configuration()

data = None
RxData = None
while True:
    try:
        data = device.read(endpoint.bEndpointAddress,
                           endpoint.wMaxPacketSize).tobytes()
        RxData = ''.join([chr(x) for x in data])
    except usb.core.USBError as e:
        data = None
        if e.args == ('Operation timed out',):
            continue
    print(RxData)
    #time.sleep(1)