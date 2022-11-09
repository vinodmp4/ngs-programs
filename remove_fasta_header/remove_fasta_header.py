import sys

filename = sys.argv[1]

outputfilename = 'processed_'+filename

with open(outputfilename, 'w') as outfile:
    with open(filename, 'r') as inpfile:
        for line in inpfile:
            if line.startswith('>'):outfile.write('\n')
            else:outfile.write(line)
