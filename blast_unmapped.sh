#!/bin/bash
#BSUB -J "blastn"
#BSUB -o unmapped_blast-v2.sh.log
#BSUB -e unmapped_blast-v2.sh.log
#BSUB -R "span[hosts=1]"
#BSUB -n 5
#BSUB -q Z-LU

echo `date`
source /BioII/lulab_b/containers/singularity/wrappers/bashrc

#/BioII/lulab_b/chenyinghui/software/samtools/samtools-1.9/samtools fasta -f 4 -1 /BioII/lulab_b/chenyinghui/project/PM-CBJYW181178-04/3.map_STAR/unmapped/5--10/5--10.unmapped.read1.fa -2 /BioII/lulab_b/chenyinghui/project/PM-CBJYW181178-04/3.map_STAR/unmapped/5--10/5--10.unmapped.read2.fa  /BioII/lulab_b/chenyinghui/project/PM-CBJYW181178-04/3.map_STAR/unmapped/5--10/5--10Aligned.sortedByCoord.out.bam

#sed -n '1,10000p' /BioII/lulab_b/chenyinghui/project/PM-CBJYW181178-04/3.map_STAR/unmapped/5--10/5--10.unmapped.read1.fa > /BioII/lulab_b/chenyinghui/project/PM-CBJYW181178-04/3.map_STAR/unmapped/5--10/5--10.unmapped.read1.1-5000.fa

blastn -evalue 1e-5 -outfmt "6 qaccver qlen sseqid stitle sgi saccver slen bitscore score evalue qstart qend sstart send gaps" -num_alignments 1 -num_threads 4 -db /BioII/lulab_b/chenyinghui/database/nt/nt -query /BioII/lulab_b/chenyinghui/project/PM-CBJYW181178-04/3.map_STAR/unmapped/5--10/5--10.unmapped.read1.1-5000.fa -out  /BioII/lulab_b/chenyinghui/project/PM-CBJYW181178-04/3.map_STAR/unmapped/5--10/5--10.unmapped.read1.1-5000.blastn.xls

python /BioII/lulab_b/chenyinghui/project/PM-CBJYW181178-04/3.map_STAR/unmapped/5--10/countSpecies.py /BioII/lulab_b/chenyinghui/project/PM-CBJYW181178-04/3.map_STAR/unmapped/5--10/5--10.unmapped.read1.1-5000.blastn.xls
echo `date`
