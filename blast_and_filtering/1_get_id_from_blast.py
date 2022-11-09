import os

filenames = [i for i in os.listdir() if i.endswith('blastn_pathogenesis.txt')]
filenames.sort()



for filename in filenames:
    ids = []
    with open(filename, 'r') as inpfile:
        for line in inpfile:
            id_ = line.split()[1]
            if not(id_ in ids):ids.append(id_)
    with open('id_'+filename, 'w') as outputfile:
        for id_ in ids:
            outputfile.write(id_+'\n')
