#!/usr/bin/env python
import random

# --------------------------------------------------
# Main program start
# --------------------------------------------------
def main():
	tryRandomNumber()
	a = askQuestion("Here is my question? ")
	print("Answer: " + a)
	sampleForLoop()
	sampleIfCondition(8)
	sampleIfCondition(7)
	return 0

# --------------------------------------------------
# Sample for loop
# --------------------------------------------------
def sampleForLoop():
	for i in range (1, 10):
		print("Iteration: " + str(i))

# --------------------------------------------------
# Sample if condition
# --------------------------------------------------
def sampleIfCondition(myValue):
	if (myValue == 7):
		print("Match")
	else:
	  print("No Match")
	  
# --------------------------------------------------
# Get a random number
# --------------------------------------------------
def tryRandomNumber():
	r = random.randint(1, 10)
	print("Next = " + str(r))
	
# --------------------------------------------------
# Ask a question and return the answer
# --------------------------------------------------
def askQuestion(question):
	return raw_input(question)
	
# --------------------------------------------------
# Call the start/main method
# --------------------------------------------------
if __name__ == '__main__':
	main()

