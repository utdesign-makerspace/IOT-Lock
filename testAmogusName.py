import usb.core
import time

device=usb.core.find(idVendor=0x413d,idProduct=0x2107)

if device is None:
    raise ValueError('Device not found')

#endpoint=device[0][(0,0)][0]

#if device.is_kernel_driver_active(0):
#    device.detach_kernel_driver(0)

device.set_configuration()

cfg = dev.get_active_configuration()
intf = cfg[(0,0)]

ep = usb.util.find_descriptor(
    intf,
    # match the first OUT endpoint
    custom_match = \
    lambda e: \
        usb.util.endpoint_direction(e.bEndpointAddress) == \
        usb.util.ENDPOINT_OUT)

assert ep is not None

# write the data
ep.write('test')

# data = None
# while True:
#     try:
#         data = device.read(endpoint.bEndpointAddress,
#                            endpoint.wMaxPacketSize)
#     except usb.core.USBError as e:
#         data = None
#         if e.args == ('Operation timed out',):
#             continue
#     print(data)
#     time.sleep(1)