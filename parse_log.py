#!/usr/bin/python
import re,os,sys

inDir=os.path.abspath(sys.argv[1])
outDir=os.path.abspath(sys.argv[2])

outFile = outDir+"/rm_rRNA_stat.xls"

logList = []

OUT= open(outFile,"w")
OUT.write("Sample\tTotal_Reads\trRNA_Reads_Num\trRNA_Reads_Percent(%)\tNon-rRNA_Reads_Num\tNon-rRNA_Reads_Percent(%)\n")
for root, dirs, files in os.walk(inDir):
	for name in files:
		if re.search("stderr.log",name,re.I):
			logList.append(name)

for name in sorted(logList):
	sampleName = re.search("(.*).stderr.log",name).group(1)
	logFile = os.path.join(inDir,name)
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
	OUT.write(sampleName+"\t"+Total_Reads+"\t"+rRNA_Reads_Num+"\t"+rRNA_Reads_Percent+"\t"+Non_rRNA_Reads_Num+"\t"+Non_rRNA_Reads_Percent+"\n")
	LOG.close()
OUT.close()
