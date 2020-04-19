import time

while True:
	omar = input("Enter Minutes: ")
	try:
		when_to_stop = abs(int(omar))
	except KeyboardInterrupt:
		break
	except:
		print("Not a number!")

	while when_to_stop > 0:
		m, s = divmod(when_to_stop, 60)
		h, m = divmod(m, 60)
		time_left = str(h).zfill(2) + ":" + str(m).zfill(2) + ":" + str(s).zfill(2)
		print(time_left + "\r", end="")
		time.sleep(1)
		when_to_stop -= 1
	print()
