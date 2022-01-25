import hid

vid = 0x413d	# Change it for your device
pid = 0x2107	# Change it for your device

while True:
    print(hid.Device(vid, pid).read(9))