#!/usr/bin/python
import re,os,sys

inDir_rRNA=os.path.abspath(sys.argv[1])
inDir_STAR=os.path.abspath(sys.argv[2])
outDir=os.path.abspath(sys.argv[3])

outFile = outDir+"/rm_rRNA_stat.xls"

logList_rRNA = []
logList_STAR = []
sample_info_dict = {}

for root, dirs, files in os.walk(inDir_rRNA):
	for name in files:
		if re.search("stderr.log",name,re.I):
			sampleName = re.search("(.*).stderr.log",name).group(1)
			logFile = os.path.join(root,name)
			LOG=open(logFile,"r")
			for line in LOG:
				line=line.strip()
				if re.search("reads processed: ",line):
					Total_Reads = re.search("reads processed: (\d+)",line).group(1)
				if re.search("reads with at least one reported alignment: ",line):
					rRNA_Reads_Num = re.search("reads with at least one reported alignment: (\d+) \(([0-9\.%]+)\)",line).group(1)
					rRNA_Reads_Percent = re.search("reads with at least one reported alignment: (\d+) \(([0-9\.%]+)\)",line).group(2)
				if re.search("reads that failed to align: ",line):
					Non_rRNA_Reads_Num = re.search("reads that failed to align: (\d+) \(([0-9\.%]+)\)",line).group(1)
					Non_rRNA_Reads_Percent = re.search("reads that failed to align: (\d+) \(([0-9\.%]+)\)",line).group(2)
			info = sampleName+"\t"+Total_Reads+"\t"+rRNA_Reads_Num+"\t"+rRNA_Reads_Percent+"\t"+Non_rRNA_Reads_Num+"\t"+Non_rRNA_Reads_Percent+"\t"
			sample_info_dict[sampleName]=info
			LOG.close()

for root, dirs, files in os.walk(inDir_STAR):
	for name in files:
		if re.search("Log.final.out",name,re.I):
			sampleName = re.search("(.*)Log.final.out",name).group(1)
			logFile = os.path.join(root,name)
			LOG=open(logFile,"r")
			for line in LOG:
				line=line.strip()
				if re.search("Number of input reads",line):
					reads_for_mapping = re.split("\t",line)[1]
				if re.search("Uniquely mapped reads number",line):
					Uniquely_mapped_reads_number = re.split("\t",line)[1]
				if re.search("Uniquely mapped reads %",line):
					Uniquely_mapped_reads_percent = re.split("\t",line)[1]
				if re.search("Number of reads mapped to multiple loci",line):
					multiple_mapping_reads_num = re.split("\t",line)[1]
				if re.search("% of reads mapped to multiple loci",line):
					multiple_mapping_reads_percent = re.split("\t",line)[1]
			info = reads_for_mapping+"\t"+Uniquely_mapped_reads_number+"\t"+Uniquely_mapped_reads_percent+"\t"+multiple_mapping_reads_num+"\t"+multiple_mapping_reads_percent+"\n"
			if sample_info_dict.has_key(sampleName):
				sample_info_dict[sampleName] = sample_info_dict[sampleName] + info
			else:
				print("ERROR: there is a sample named "+sampleName+" is not found in rm_rRNA step.")
			LOG.close()

OUT= open(outFile,"w")
OUT.write("Sample\tTotal_Reads\trRNA_Reads_Num\trRNA_Reads_Percent(%)\tNon-rRNA_Reads_Num\tNon-rRNA_Reads_Percent(%)\tTotal_Reads_for_Mapping\tUniquely_Mapped_Reads\tUniquely_Mapped_Reads_Percentage\tNumber of reads mapped to multiple loci\tPercentage of reads mapped to multiple loci\n")
for sample in sorted(sample_info_dict.keys()):
	OUT.write(sample_info_dict[sample])
OUT.close()		
