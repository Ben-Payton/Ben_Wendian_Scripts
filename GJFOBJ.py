######################################################################################################################################################################################
######################################################################################################################################################################################
# Ben Payton 6/21/23
# This is a python object meant to be used as an atom in gjf file
######################################################################################################################################################################################
######################################################################################################################################################################################


class GAUSSATOM:
	def __init__(self,string):
		self.string = string.split()
		self.TYPE = ""
		self.x_value = ""
		self.y_value = ""
		self.z_value = ""
		self.frozen = " 0"
		self.start_up()

######################################################################################################################################################################################
# Makes the output in the form of a string in one line so it may be inserted in to a gjf file
######################################################################################################################################################################################

	def __str__(self):
		return self.TYPE + "   " + self.frozen + "        " + self.x_value + "   " + self.y_value + "   " + self.z_value

######################################################################################################################################################################################
# Updates the string that is outputed. best to put it at the end of any function that makes a change
######################################################################################################################################################################################
	def update_string(self):
		self.string = []
		self.string.append(self.TYPE)
		self.string.append(self.frozen)
		self.string.append(self.x_value)
		self.string.append(self.y_value)
		self.string.append(self.z_value)

######################################################################################################################################################################################
# A function called at the initialization in order to properly organize structure
# Will work whether there is already a frozen/unfrozen line
######################################################################################################################################################################################

	def start_up(self):
		if len(self.string) == 4:
			self.TYPE = self.string[0]
			self.x_value = self.string[1]
			self.y_value = self.string[2]
			self.z_value = self.string[3]
			self.update_string()
		elif len(self.string) == 5:
			self.TYPE = self.string[0]
			self.frozen = self.string[1]
			self.x_value = self.string[2]
			self.y_value = self.string[3]
			self.z_value = self.string[4]
			self.update_string()

######################################################################################################################################################################################
# if the atom is frozen it will unfreeze it.
# if the atom is unfrozen it will freeze it.
######################################################################################################################################################################################
	
	def flip_freeze(self):
		if self.frozen == "0":
			self.frozen = "-1"
		else:
			self.frozen = " 0"
		self.update_string()

######################################################################################################################################################################################
# Freezes the atom
######################################################################################################################################################################################

	def freeze(self):
		self.frozen = "-1"
		self.update_string()

	def unfreeze(self):
		self.frozen = " 0"
		self.update_string()




######################################################################################################################################################################################
######################################################################################################################################################################################
# Ben Payton 6/21/23
# This is a python object meant to be used to organize and change GJF files for gaussian
######################################################################################################################################################################################
######################################################################################################################################################################################

class GJFFile:
	def __init__(self,name):
		self.Name = name
		self.List_Format = []
		self.chk = "%chk=" + self.Name[0:-4] + ".chk"
		self.mem = "%mem=1GB"
		self.nproc = "%nprocshared=36"
		self.Input_Line = ""
		self.Title = ""
		self.Charge = None
		self.Mult = None
		self.Atom_List = []


		self.file_list()
		self.org_data()

######################################################################################################################################################################################
# opens up a named file and puts it in list format
# Note: must be passed the name of the file without ".gjf" at the end
######################################################################################################################################################################################

	def file_list(self):
		f = open(self.Name,"r")
		for i in f:
			self.List_Format.append(i)
		f.close()

######################################################################################################################################################################################
#Takes the list formatted file and organizes its infromation in to the datastructure parameters
######################################################################################################################################################################################

	def org_data(self):
		space_iter = 0
		atom_iter = 0
		HashCheck = False

		for i in self.List_Format:

			if i == "\n" and self.Input_Line != "":
				space_iter = space_iter + 1
			if i[0] == "#":
				HashCheck = True

			if HashCheck == True and i != "\n":
				self.Input_Line = self.Input_Line + i
			else:
				HashCheck = False


			if space_iter == 1 and i != "\n":
				self.Title = self.Title + i
			if space_iter == 2 and i != "\n":
				if atom_iter == 0:
					self.Charge = int(i[0])
					self.Mult = int(i[2])
					atom_iter = 1
				else:
					self.Atom_List.append(GAUSSATOM(i))
					atom_iter = atom_iter+1

######################################################################################################################################################################################
# if the atom is frozen it will unfreeze it.
# if the atom is unfrozen it will freeze it.
#Does this for all atoms
######################################################################################################################################################################################

	def flip_all_frozen(self):
		for i in self.Atom_List:
			i.flip_freeze()

######################################################################################################################################################################################
# makes sure all atoms are unfrozen
######################################################################################################################################################################################

	def all_unfrozen(self):
		for i in self.Atom_List:
			i.unfreeze()

######################################################################################################################################################################################
# freezes all specified atoms. the first atom starts at 1. list is space delimited.
######################################################################################################################################################################################

	def freeze_some(self,frozen_atoms):
		self.all_unfrozen()
		FAtom = frozen_atoms.split()
		for i in FAtom:
			i = int(i)
			self.Atom_List[int(i)-1].freeze()

######################################################################################################################################################################################
# changes the given input line to a new one
# input is a string
######################################################################################################################################################################################

	def Change_input_line(self,new_input_line):
		self.Input_Line = new_input_line

######################################################################################################################################################################################
# changes the given multiplicity to a new one
# input is an int
######################################################################################################################################################################################

	def Change_Mult(self,new_Mult):
		self.Mult = new_Mult

######################################################################################################################################################################################
# changes the given charge to a new one
# input is an int
######################################################################################################################################################################################

	def Change_Charge(self,new_Charge):
		self.Charge = new_Charge

######################################################################################################################################################################################
# prints the current input data above the atoms
######################################################################################################################################################################################

	def print_Current(self):
		print(self.chk)
		print(self.mem)
		print(self.nproc)
		print(self.Input_Line)
		print(self.Charge, self.Mult)

######################################################################################################################################################################################
# Makes a new GJF file after changes have been made
# Will overwrite a file if it is given the same name
######################################################################################################################################################################################

	def Make_New_File(self,name):
		self.print_Current()
		name = name
		f = open(name,"w")
		L = ["%chk="+name[0:-4]+".chk\n","%mem=1GB\n","%nprocshared=36\n","\n",self.input_line + "\n",self.Title + "\n", str(self.Charge) + " " + str(self.Mult) + "\n"]
		f.writelines(L)
		f.close()

		f = open(name,"a")
		for i in self.Atom_List:
			f.write(i.__str__() + "\n")
		f.write("\n")





######################################################################################################################################################################################
######################################################################################################################################################################################
# Benjamin Payton
# Object for Gaussian Log Files
# 6/22/23
# Notes
# 	Stationary points are a good search option
# 	GradGradGradGradGradGradGradGradGradGradGradGradGradGradGradGradGradGrad is a good search line
# 	
######################################################################################################################################################################################
######################################################################################################################################################################################

class GaussLog:

	def __init__(self, name):
		self.name = name
		self.list_format = []
		self.Thermo_List = []
		self.SCF_Converged = False
		self.Geometry_Converged = False
		self.Freq_Converged = False
		self.ZPC = None
		self.TC_Energy = None
		self.TC_Enthalpy = None
		self.TC_GFE = None
		self.EE_and_ZPC = None
		self.EE_and_TCEG = None
		self.EE_and_TCET = None
		self.EE_and_GFE = None
		self.LastGeometry = None
		self.input_line = ""
		self.Error = "There was no error found"

		self.file_list()
		self.org_data()

######################################################################################################################################################################################
# Reads the file to a list for easy manipulation
######################################################################################################################################################################################

	def file_list(self):
		f = open(self.name,"r")
		for i in f:
			self.list_format.append(i)
		f.close()


######################################################################################################################################################################################
# extracts the Termo properties
######################################################################################################################################################################################

	def Therm_Properties(self):
		for i in self.Thermo_List:
			
			if " Zero-point correction=" in i:
				temp = i.split()
				self.ZPC = float(temp[-2])

			if " Thermal correction to Energy=" in i:
				temp = i.split()
				self.TC_Energy = float(temp[-1])

			if " Thermal correction to Enthalpy=" in i:
				temp = i.split()
				self.TC_Enthalpy = float(temp[-1])

			if " Thermal correction to Gibbs Free Energy=" in i:
				temp = i.split()
				self.TC_GFE = float(temp[-1])

			if " Sum of electronic and zero-point Energies=" in i:
				temp = i.split()
				self.EE_and_ZPC = float(temp[-1])

			if " Sum of electronic and thermal Energies=" in i:
				temp = i.split()
				self.EE_and_TCEG = float(temp[-1])

			if " Sum of electronic and thermal Enthalpies=" in i:
				temp = i.split()
				self.EE_and_TCET = float(temp[-1])

			if " Sum of electronic and thermal Free Energies=" in i:
				temp = i.split()
				self.EE_and_GFE = float(temp[-1])

######################################################################################################################################################################################
# Organizes Data upon saving of log file
######################################################################################################################################################################################

	def org_data(self):
#		print("1")

		Recording_Thermo = False

		for i in self.list_format:

			if i == "    -- Stationary point found.\n" and self.Geometry_Converged:
				self.Freq_Converged = True
#				print("2")

			if i == "    -- Stationary point found.\n" and not self.Geometry_Converged:
				self.Geometry_Converged = True
#				print("3")

			if i == " - Thermochemistry -\n":
				Recording_Thermo = True
#				print("4")

			if Recording_Thermo:
				if i == " GradGradGradGradGradGradGradGradGradGradGradGradGradGradGradGradGradGrad\n":
					Recording_Thermo = False
				self.Thermo_List.append(i)
#				print("5")

		self.Therm_Properties()


