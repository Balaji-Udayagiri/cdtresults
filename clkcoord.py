'''import math
x = 540
y = 1170
r = 350

x1 = x + r*math.cos(math.radians(30))
y1 = y - r*math.sin(math.radians(30))
list1 = []
list1.append(x1)
list1.append(y1)
print(list1)'''

class Temp :
	#val : int
	def __init__(self):
		self.val = self._valfun()

	def _valfun(self):
		return 5

temp = Temp()
print(temp.val)
