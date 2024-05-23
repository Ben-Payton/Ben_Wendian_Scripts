#!/bin/bash

echo "What is the name of the folder?"

read New_Folder_Name

cp -r /u/af/ao/bpayton/scratch/Templates/Lammps_Temp_Folder ./$New_Folder_Name

echo "What is the name of this input file?"

read Input_File_Name

mv ./$New_Folder_Name/Template.in ./$New_Folder_Name/$Input_File_Name

sed -i "s?\[File_Name\]?$Input_File_Name?g" ./$New_Folder_Name/LampTemplate.s
