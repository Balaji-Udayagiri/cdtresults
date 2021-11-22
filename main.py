from cdt_results_final import ClockDrawingTest
import sys

if __name__ == "__main__":
	filename = sys.argv[1]
	clockDrawingtest = ClockDrawingTest(filename)
	clockDrawingtest.printDetails()
	diff = clockDrawingtest.findHandsDifference()
	diffnum = clockDrawingtest.findNumberPositionDifferences()
	print(diff)
	print(diffnum)
