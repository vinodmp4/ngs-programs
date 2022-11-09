import sys

fastafile = sys.argv[1]
idfile = sys.argv[2]

outputfile = open('filtered_'+fastafile,'w')


ids = []

with open(idfile, 'r') as id_file:
    for line in id_file:
        if not(line.startswith('#')):ids.append(line.rstrip())

enable_write = False

with open(fastafile, 'r') as fasta_file:
    for line in fasta_file:
        if line.startswith('>'):
            this_id = line.replace('>','').split()[0]
            if (this_id in ids):enable_write = True
            else:enable_write = False
        if enable_write:
            outputfile.write(line)
        
outputfile.close()
