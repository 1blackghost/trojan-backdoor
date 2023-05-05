def new_thread():

	from PIL import ImageGrab
	import time


	while True:
		x1, y1 = 0, 0
		x2, y2 = 1920, 1080

		# Capture the specified region
		screenshot = ImageGrab.grab(bbox=(x1, y1, x2, y2))

		# Save the screenshot to a file
		screenshot.save('screenshot.png')

		time.sleep(5)
import threading
t=threading.Thread(target=new_thread())
t.start()
