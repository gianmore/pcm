#!/bin/bash

filename="../rifdata/PRJEB38481/ERR4605243/ERR4605243.fastq.gz"
#zcat $filename > tmp.asdf
transeq -sequence tmp.asdf -outseq testaa.fastq -frame 6 -clean
