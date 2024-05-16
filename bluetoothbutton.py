import evdev
import time

if __name__ == '__main__':

    print("Waiting for device to become ready...")
    dev_path = ""
    while(True):
        devices = [evdev.InputDevice(path) for path in evdev.list_devices()]
        for device in devices:
            if("Shutter" in device.name):
                dev_path = device.path
        if (dev_path == "") :
            sleep(1)
        else : break

	device = evdev.InputDevice(dev_path)
    print("IoT Button is ready.")
    while True:
    	try:
    		print(device)
    		print("OUTPUT:")
    		for event in device.read_loop():
    			if event.type == evdev.ecodes.EV_KEY:
    				if event.value == 1:
    					start = time.time()
    					print(" push:")
    				if event.value == 0:
    					end = time.time()
    					t = end - start
    					print(" release:", t)

    	except KeyboardInterrupt:
        	break

print("\n")