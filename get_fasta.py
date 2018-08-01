#! /usr/bin/env python
#! -*- coding:utf-8 -*- \#
from Bio import SeqIO
import re
import sys
infile = sys.argv[1]
outfile1 = sys.argv[2]
outfile = sys.argv[3]
with open (outfile1,'w') as out1,open (outfile,'w') as out:
    for record in SeqIO.parse(infile,'fasta'):
        pid = re.match(r'.*\|(.*)\|.*',record.id).group(1)
        out1.write("%s\n" %pid)
        description = re.sub(r'(.*\|.*\|\w*)',pid,record.description)
        record.id = description
        record.description = ""
        SeqIO.write(record,out,'fasta')

