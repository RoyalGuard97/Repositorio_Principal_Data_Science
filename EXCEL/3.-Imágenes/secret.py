import math
from colorama import *
import time
#tamaño
n = 14
init()
for y in range(n+1, -(n-1), -1):
	for x in range(-n, n+1):
		#ecuación
		if ((x**2) + ((5*y/4) - math.sqrt(4*abs(x)))**2) <= n**2:
			time.sleep(0.01)
			print(Fore.RED + "0", end=" ")
		else:
			print(Fore.GREEN + "1", end=" ")
	print("")