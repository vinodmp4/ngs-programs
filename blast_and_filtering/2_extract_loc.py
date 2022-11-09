
filenames = [
    ['id_A1_blastn_pathogenesis.txt','gtf/A1.gtf'],
    ['id_A7_blastn_pathogenesis.txt','gtf/A7.gtf'],
    ['id_A10_blastn_pathogenesis.txt','gtf/A10.gtf'],
    ['id_B1_blastn_pathogenesis.txt','gtf/B1.gtf'],
    ['id_B7_blastn_pathogenesis.txt','gtf/B7.gtf'],
    ['id_B10_blastn_pathogenesis.txt','gtf/B10.gtf'],
    ['id_P1_blastn_pathogenesis.txt','gtf/P1.gtf'],
    ['id_P2_blastn_pathogenesis.txt','gtf/P2.gtf']
    ]
locs = []
spec_locs = {}

for index, filename in enumerate(filenames):
    print('Processing',filename[0],'(',index+1,'/',len(filenames),')... ',end="")
    ids = []
    with open(filename[0], 'r') as idfile:
        for line in idfile:
            ids.append(line.rstrip())
    with open(filename[1], 'r') as gtffile:
        for line in gtffile:
            for i in ids:
                if i in line:
                    present = False
                    x = line.split()
                    for y in x:
                        if present:
                            loc = y.replace('"','').replace(';','')
                            if not(loc in locs):
                                locs.append(loc)
                                spec_locs[loc] = i
                        if y == 'ref_gene_name':present = True
                        else:present = False
                            
    print('Done')

print(len(locs),'unique Locations found')
                            
with open('pathogenesis_blast_loc.txt','w') as outfile:
    for loc in locs:
        outfile.write(loc+'\n')

with open('spec_pathogenesis_blast_loc.txt','w') as outfile:
    for loc in spec_locs.keys():
        outfile.write(loc+','+spec_locs[loc]+'\n')
