filenames = [
    ['all_pathogenesis_blastn.txt','spec_pathogenesis_blast_loc.txt','pathogenesis_corresponding_ids.txt']
    ]

for filename in filenames:
    r_ids = []
    r_specs = {}
    with open(filename[1], 'r') as inpfile:
        for line in inpfile:
            l_id = line.rstrip().split(sep=',')[0]
            r_id = line.rstrip().split(sep=',')[1]
            if not(r_id in r_ids):
                r_ids.append(r_id)
                r_specs[r_id] = [l_id]
    r_id_vals = {}
    for i in r_ids:
        r_id_vals[i]=['',0]
    with open(filename[0], 'r') as inpfile:
        for line in inpfile:
            for r_id in r_ids:
                if r_id in line:
                    if float(line.split()[2])>r_id_vals[r_id][1]:
                        r_id_vals[r_id] = [line.split()[0],float(line.split()[2])]
    with open(filename[2],'w') as outfile:
        for r_id in r_ids:
            outfile.write(r_id+','+r_specs[r_id][0]+','+r_id_vals[r_id][0]+','+str(r_id_vals[r_id][1])+'\n')
