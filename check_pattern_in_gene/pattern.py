import sys, re

filename = sys.argv[1]
pattern = sys.argv[2]

#R_LR

def checkpattern(text, pattern):
    pattern = pattern.replace('_','.')
    reg = re.compile(pattern)
    x = reg.search(text)
    if x:return True
    return False

sequence = {}
seqorder = []

thisseqname = ">Unknown Sequence\n"
with open(filename, 'r') as inpfile:
    for line in inpfile:
        if line.startswith('>'):
            thisseqname = line
            sequence[thisseqname] = []
            seqorder.append(line)
        else:
            if len(sequence.keys())==0:
                sequence[thisseqname] = []
                seqorder.append(thisseqname)
            sequence[thisseqname].append(line)

with open(pattern+'+'+filename,'w') as outfile:
    for seq in seqorder:
        fullseq = ''.join([i.rstrip() for i in sequence[seq]])
        if checkpattern(fullseq,pattern):
            outfile.write(seq)
            for i in sequence[seq]:
                outfile.write(i)
