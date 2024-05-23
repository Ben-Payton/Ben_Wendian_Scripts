#!/bin/bash
Path_to_template=""

#Excludes .gjf files that already have a .s file and have already run

for j in *.gjf; do

	if [ -f "${j%.*}.s" ];
	then
		echo "${j%.*}"
	else

		cp $Path_to_template ${j%.*}.s
		
	fi
done


# Excludes .inf files that already have a .s file
for j in *.inf; do

	if [ -f "${j%.*}.s" ];
	then
		echo "${j%.*}"
	else

		cp $Path_to_template ${j%.*}.s
		
	fi
done

#Replaces any instance of 'template' in the copied files with the appropriate string, and runs the .s file (excluding previously run files)

for x in *.s; do

	sed -i "s/gjf_filename_here/${x%.*}/g" $x
	echo $x	

done

echo "*.s files made"
