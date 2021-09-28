import numpy as np 
import sys

#define a function tht returns a value 
def expo(x):
	return np.expo(x) #returns the np e^x function

#define a subroutine that does not return a value
def show_expo(n):

	for i in range(n): #i = [0, n-1]
		print(expo(float(i)))

#define main function
def main():
	n = 10 #provide a default value for n

	#check if there is a command line argument provided 
	if(len(sys.argv)>1):
		n = int(sys.argv[1]) #if an argument was provided, use 

	show_expn(n) #call the show_exp subroutine 

	#run the main function 
	if __name__ == "__main__":
		main()