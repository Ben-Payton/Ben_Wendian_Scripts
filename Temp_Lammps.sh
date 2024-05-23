#!/bin/bash

echo -e "What kind of Lammps Job are you running? type the corresponding number and press enter. \n 1: general \n 2: rerun \n 3: random packing"

read option

genpath="/u/af/ao/bpayton/scratch/Templates/Lammps_Temp_Folder"

echo "What is the name of the job"
read Job_Name

NEW_JOB_FOLDER="./$Job_Name"

DEF_DO(){
	cp -r $tpath $NEW_JOB_FOLDER
	sed -i "s?\[Job_Name\]?$Job_Name?g" ./$NEW_JOB_FOLDER/LampTemplate.s
	mv $NEW_JOB_FOLDER/Template.in "$NEW_JOB_FOLDER/${Job_Name}.in"

}


if [[ $option == 1 ]]; then
	tpath="$genpath/General"
	DEF_DO
fi

if [[ $option == 2 ]]; then
        tpath="$genpath/Rerun"
	DEF_DO
fi

if [[ $option == 3 ]]; then
        tpath="$genpath/Rand_Pack"
	DEF_DO
fi

