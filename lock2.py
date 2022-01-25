import hid

vid = 0x413d	# Change it for your device
pid = 0x2107	# Change it for your device

with hid.Device(vid, pid) as h:
	print(f'Device manufacturer: {h.manufacturer}')
	print(f'Product: {h.product}')
	print(f'Serial Number: {h.serial}')