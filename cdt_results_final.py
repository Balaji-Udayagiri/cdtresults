import math
from ClockDigitPositions import clk_pos

class ClockDrawingTest():
		
	_lines : list
	def __init__(self,filename):
		self.file_name = filename

		self._lines = self._getLines()

		self.position_of_digits = self._getPosition()

		self.minute, self.hour = self._getTimeDisplayed()

		self.minute_hand_angle, self.hour_hand_angle = self._getHandAnglesSet()

		self.minute_hand_angle_actual, self.hour_hand_angle_actual = self._findActualhandAngles()



	def _getLines(self):
		
		with open(self.file_name) as f:
			lines = f.readlines()
		lines = [line.strip() for line in lines]
		lines = [line.strip('/n') for line in lines]
		lines = [line.strip('(') for line in lines]
		lines = [line.strip(')') for line in lines]

		return lines
		

	def printDetails(self):
		print("Displaying detail of file ",self.file_name)
		print("Displaying position of digits :")
		for i in range(len(self.position_of_digits)):
			print("position of ",i+1,"is",self.position_of_digits[i])
		print("Displaying time : ", self.hour,":",self.minute)
		print("Displaying set hand angles :")
		print("			minute hand angle : ",self.minute_hand_angle)
		print("			hour hand angle : ", self.hour_hand_angle )
		print("Displaying actual hand angles :")
		print("			minute hand angle : ",self.minute_hand_angle_actual)
		print("			hour hand angle : ", self.hour_hand_angle_actual)
	def drawClock(self):
		pass
	def findHandsDifference(self, hand = 'both'):
		diff_hour_hand = abs(self.hour_hand_angle - self.hour_hand_angle_actual)
		diff_minute_hand = abs(self.minute_hand_angle - self.minute_hand_angle_actual)
		if(hand == 'both'):
			return diff_minute_hand,diff_hour_hand
		if(hand == 'minute'):
			return diff_minute_hand
		if(hand == 'hour'):
			return diff_hour_hand
		
	def findNumberPositionDifferences(self, digit = 0):
		diff = 0.0
		if digit is not 0:
			diff = math.sqrt((clk_pos[digit-1][0] - self.position_of_digits[digit-1][0])*(clk_pos[digit-1][0] - self.position_of_digits[digit-1][0]) + (clk_pos[digit-1][1] - self.position_of_digits[digit-1][1])*(clk_pos[digit-1][1] - self.position_of_digits[digit-1][1]))
		else:
			for i in range(12):
				diff = diff + math.sqrt((clk_pos[i][0] - self.position_of_digits[i][0])*(clk_pos[i][0] - self.position_of_digits[i][0]) + (clk_pos[i][1] - self.position_of_digits[i][1])*(clk_pos[i][1] - self.position_of_digits[i][1]))
		return diff
	def _getPosition(self):
		list_of_positions = []
		for i in range(12):
			list = []
			x,y = self._lines[i].split(',')
			x = float(x)
			y = float(y)
			list.append(x)
			list.append(y)
			list_of_positions.append(list)
		return list_of_positions

	def _getTimeDisplayed(self):
		hour,minute = self._lines[14].split(':')
		hour = int(hour)
		minute = int(minute)
		return hour,minute

	def _getHandAnglesSet(self):
		hour_hand_angle = float(self._lines[12])
		minute_hand_angle = float(self._lines[13])
		return minute_hand_angle, hour_hand_angle

	def _findActualhandAngles(self):
		minute_hand_angle_actual = (float(self.minute)/60.0)*2.0*math.pi
		hour_hand_angle_actual = (float(self.hour)/12.0)*2.0*math.pi + minute_hand_angle_actual/12.0
		if(minute_hand_angle_actual > math.pi):
			minute_hand_angle_actual = minute_hand_angle_actual - 2*math.pi
		if(hour_hand_angle_actual > math.pi):
			hour_hand_angle_actual = hour_hand_angle_actual - 2*math.pi

		return minute_hand_angle_actual, hour_hand_angle_actual



