import sys

filename = sys.argv[1]
limit = int(sys.argv[2])

fileindex = 1
seqindex = 0

outputfile = open(str(fileindex)+'_'+filename,'w')

with open(filename, 'r') as inpfile:
    for line in inpfile:
        if line.startswith('>'):seqindex = seqindex + 1
        if seqindex>limit:
            seqindex = 1;fileindex = fileindex + 1
            outputfile.close()
            outputfile = open(str(fileindex)+'_'+filename,'w')
        outputfile.write(line)
    
outputfile.close()
