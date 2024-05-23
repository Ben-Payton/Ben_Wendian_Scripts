#!/bin/bash
STRING="template.s"
var="#p Opt=(calcfc,ts,noeigentest) Freq 6-311++g(2d,2p) scrf=(SMD,Solvent=water) m062x"

#Excludes .gjf files that already have a .s file and have already run

for j in *.gjf; do

	if [ -f "${j%.*}.s" ];
	then
		echo "${j%.*}"
	else

		#Removes file definition from my laptop and replaces it appropriately for GeomOpt

		sed -i '1,4d' $j
		sed -i '1s/^/\n\ntemplate OptFreq\n/' $j
		{ echo -n $var; cat $j; } >/tmp/filename.tmp
		mv /tmp/filename.tmp $j
		sed -i '1s/^/%chk=template.chk\n%mem=1GB\n%nproc=16\n/' $j
		sed -i "s/template/${j%.*}/g" $j

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
