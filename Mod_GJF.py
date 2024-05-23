import os
import glob



def copy_file(file):
	with open(file,"r") as file:
		data = file.readlines()
		file.close()
	return data


'''def check_converged(data):
	for i in range(len(data)):
		if "Converged?" in data[i]:
			info = []
			for j in range(5):
				print(data[i+j])
'''

def mod_file(data,file_name):
	chk_file_name = ""
	for i in range(len(file_name)-3):
		chk_file_name = chk_file_name + i
	chk_file_name = chk_file_name + "chk"

	if data[0] != "%chk="+chk_file_name+"\n":
		data[0] = "%chk="+chk_file_name+"\n"

	if data[1] != "%mem=1GB\n":
		data.insert(1,"%mem=1GB\n")

	if data[2] != "%nproc=16\n":
		data.insert(2,"%nproc=16\n")
	


def main():
	
	pattern =  input("What is the pattern for the file you would like to modify?: ")
	directory = os.path.join('.', pattern )	
	matches = glob.glob(directory)
	for i in matches:
		g = copy_file(i)
		for line in g:
					

main()
