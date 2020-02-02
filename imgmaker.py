import math
with open("img.ppm", 'w') as img:
	img.write('P3\n')
	img.write('500 500\n')
	img.write('255\n')
	for x in range(500):
		for y in range(500):
			clr = [(x + y) % 255, abs((x - y) % 255), (x / (y + 1)) % 255]
			img.write(str(clr[0]) + ' ' + str(clr[1]) + ' ' + str(clr[2]) + ' ')
