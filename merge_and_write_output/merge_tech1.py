proc = 'pathogenesis'
locfile = proc+'_blast_loc.txt'


locs = {}

with open(locfile,'r') as lfile:
    for line in lfile:
        locs[line.rstrip()] = []

filenames = [
    'filtered/'+proc+'/logFC_'+proc+'_A1vA7.txt',
    'filtered/'+proc+'/logFC_'+proc+'_A1vA10.txt',
    'filtered/'+proc+'/logFC_'+proc+'_A1vB1.txt',
    'filtered/'+proc+'/logFC_'+proc+'_A1vP1.txt',
    'filtered/'+proc+'/logFC_'+proc+'_A7vB7.txt',
    'filtered/'+proc+'/logFC_'+proc+'_A10vB10.txt',
    'filtered/'+proc+'/logFC_'+proc+'_B1vB7.txt',
    'filtered/'+proc+'/logFC_'+proc+'_B1vB10.txt',
    'filtered/'+proc+'/logFC_'+proc+'_B1vP2.txt',
    'filtered/'+proc+'/logFC_'+proc+'_P1vP2.txt'
    ]

for filename in filenames:
    with open(filename,'r') as inpfile:
        for line in inpfile:
            data = line.rstrip().split(sep=",")
            locs[data[0]].append(data[-1])


f = open('logFC_TECH1_'+proc+'_merged.csv','w')
f.write('Location,A1vA7,A1vA10,A1vB1,A1vP1,A7vB7,A10vB10,B1vB7,B1vB10,B1vP2,P1vP2\n')
for i in locs.keys():
    f.write(i+','+','.join(locs[i])+'\n')
f.close()
