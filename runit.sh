#!/bin/bash
STRING="template.s"

#Excludes .gjf files that already have a .s file and have already run

for j in *.gjf; do

	if [ -f "${j%.*}.s" ];
	then
		echo "${j%.*}"
	else

		#Copies template file and names it the same thing as the .gjf file

		cp /u/af/ao/bpayton/scratch/Templates/template.s ${j%.*}.s
		
	fi
done


#Replaces any instance of 'template' in the copied files with the appropriate string, and runs the .s file (excluding previously run files)

for x in *.s; do

	if [[ -f "${x%.*}.chk" ]];
	then
		echo $x

	elif [[ "$STRING" == "$x" ]];
	then
		echo "Template"

	else 
		sed -i "s/template/${x%.*}/g" $x
		echo $x	
		sbatch -p compute $x

	fi
done
