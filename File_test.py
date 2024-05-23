import os
import glob



def copy_file(file):
	with open(file,"r") as file:
		data = file.readlines()
		file.close()
	return data


def check_converged(data):
	for i in range(len(data)):
		if "Converged?" in data[i]:
			info = []
			for j in range(5):
				print(data[i+j])



def main():
	directory = os.path.join('.','*.log')	
	matches = glob.glob(directory)
	for i in matches:
		temp = copy_file(i)
		print(i)
		check_converged(temp)

main()
