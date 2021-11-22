import math

clk_pos = [[715.0, 866.8911086754465],
[843.1088913245535, 995.0],
[890.0, 1170.0],
[843.1088913245535, 1345.0],
[715.0, 1473.1088913245535],
[540.0, 1520.0],
[365.0, 1473.1088913245535],
[236.89110867544645, 1345.0],
[190.0, 1170.0],
[236.89110867544645, 995.0],
[365.0, 866.8911086754465],
[540.0, 820.0]]

class Coordinates:
	x : float 
	y : float
class Time:
	minute : int
	hour : int

with open('test_results_1637556303.txt') as f:
	lines = f.readlines()
lines = [line.strip() for line in lines]
lines = [line.strip('/n') for line in lines]
lines = [line.strip('(') for line in lines]
lines = [line.strip(')') for line in lines]
number_positions = []
for i in range(12):
	x,y = lines[i].split(',')
	x = float(x)
	y = float(y)
	P = Coordinates()
	P.x = x
	P.y = y
	number_positions.append(P)
hour_hand_angle = float(lines[12])
minute_hand_angle = float(lines[13])
time = Coordinates()
hour,minute = lines[14].split(':')
time.x = int(hour)
time.y = int(minute)

minute_hand_angle_actual = (float(time.y)/60.0)*2.0*math.pi
hour_hand_angle_actual = (float(time.x)/12.0)*2.0*math.pi + minute_hand_angle_actual/12.0


