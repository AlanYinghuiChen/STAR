#!/mnt/fvg01vol8/software/biosoft/python/bin/python
#-*- coding:UTF-8 -*-

import sys,collections,os,re

def countSpecies(xlspath):
	speciesdict = collections.OrderedDict()
	read_index_list = []
	hit_reads = 0
	with open(xlspath,"r") as xlsF:
		for line in xlsF:
			linelist = line.split("\t")
			read_index = linelist[0]
			if read_index in read_index_list:
				continue
			else:
				read_index_list.append(read_index)
				hit_reads = hit_reads + 1
			list4 = linelist[3].split(",")
			species_name = list4[0]
			if speciesdict.has_key(species_name):
				speciesdict[species_name] = speciesdict[species_name]+1
			elif not  speciesdict.has_key(species_name):
				speciesdict[species_name] = 1

	with open(xlspath+"stat.xls","w") as xlsFstat:
		xlsFstat.write("Reference\tPercentage\thit reads/total reads\n")
		for item in speciesdict:
			persent = round(float(speciesdict[item])/hit_reads,4)
			persent = str(persent*100)
			xlsFstat.write("%s\t%s\t%s/%s\n" % (item,persent,str(speciesdict[item]),str(hit_reads)))

			
xlspath = sys.argv[1]
countSpecies(xlspath)
