import textwrap

patternfile = "input.txt"
malefile = "male_trinity_longest_only.fasta.transdecoder.pep"
femalefile = "female_trinity_longest_only.fasta.transdecoder.pep"

patterns = []

with open(patternfile, 'r') as inpfile:
    for line in inpfile:
        line = line.rstrip()
        patterns.append(line)


def matchpattern(text,patterns):
    for patt in patterns:
        if patt.lower() in text.lower():return True
    return False

def writeoutput(filen, text_title, text_seq):
    filen.write(text_title)
    txt = textwrap.wrap(text_seq,60)
    for t in txt:
        filen.write(t+'\n')
    

with open('fem_trinity.fasta','w') as outfile:
    with open(femalefile, 'r') as inpfile:
        this_title = ''
        this_seq = ''
        for line in inpfile:
            if line.startswith('>'):
                if matchpattern(this_seq, patterns):writeoutput(outfile,this_title,this_seq)
                this_seq = ''
                this_title = line
            else:this_seq += line.rstrip()

with open('male_trinity.fasta','w') as outfile:
    with open(malefile, 'r') as inpfile:
        this_title = ''
        this_seq = ''
        for line in inpfile:
            if line.startswith('>'):
                if matchpattern(this_seq, patterns):writeoutput(outfile,this_title,this_seq)
                this_seq = ''
                this_title = line
            else:this_seq += line.rstrip()

