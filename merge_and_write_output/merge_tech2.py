proc = 'pathogenesis'
locfile = proc+'_blast_loc.txt'


locs = {}

with open(locfile,'r') as lfile:
    for line in lfile:
        locs[line.rstrip()] = []

filenames = [
    'filtered/'+proc+'/logFC_'+proc+'_A1vP1.txt',
    'filtered/'+proc+'/logFC_'+proc+'_P1vA7.txt',
    'filtered/'+proc+'/logFC_'+proc+'_A7vA10.txt',
    'filtered/'+proc+'/logFC_'+proc+'_B1vP2.txt',
    'filtered/'+proc+'/logFC_'+proc+'_P2vB7.txt',
    'filtered/'+proc+'/logFC_'+proc+'_B7vB10.txt'
    ]

for filename in filenames:
    with open(filename,'r') as inpfile:
        for line in inpfile:
            data = line.rstrip().split(sep=",")
            locs[data[0]].append(data[-1])


f = open('logFC_TECH2_'+proc+'_merged.csv','w')
f.write('Location,A1vP1,P1vA7,A7vA10,B1vP2,P2vB7,B7vB10\n')
for i in locs.keys():
    f.write(i+','+','.join(locs[i])+'\n')
f.close()
