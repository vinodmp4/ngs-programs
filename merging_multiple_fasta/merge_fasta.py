import os

filenames = [i for i in os.listdir() if (i.endswith('fasta'))]

mergedfile = open('pathogenesis.fasta','w')


for filename in filenames:
    index = 0
    seqid = filename.split('.')[0]
    with open(filename, 'r') as inputfile:
        name = seqid.replace(' ','')
        for line in inputfile:
            if line.startswith('>'):
                index = index + 1
                if index>1:mergedfile.write(">"+name+"_"+str(index)+"\n")
                else:mergedfile.write(">"+name+"\n")
            else:
                mergedfile.write(line)
        mergedfile.write("\n")

mergedfile.close()
