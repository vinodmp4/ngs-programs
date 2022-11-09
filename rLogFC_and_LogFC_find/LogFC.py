import math

def logfc(x, y):
    if ((x == 0)or(y == 0)):return 0 # case infinity
    return math.log((y/x),2)

countsfilenames = [
    "../counts/A1.counts", # 0
    "../counts/P1.counts", # 1
    "../counts/A7.counts", # 2
    "../counts/A10.counts",# 3
    "../counts/B1.counts", # 4
    "../counts/P2.counts", # 5
    "../counts/B7.counts", # 6
    "../counts/B10.counts" # 7
    ]

combinations = {
    "logFC_A1vA7.txt":(0,2),
    "logFC_A1vA10.txt":(0,3),
    "logFC_A1vB1.txt":(0,4),
    "logFC_A1vP1.txt":(0,1), # TECH 2
    "logFC_A7vB7.txt":(2,6),
    "logFC_A10vB10.txt":(3,7),
    "logFC_B1vB7.txt":(4,6),
    "logFC_B1vB10.txt":(4,7),
    "logFC_B1vP2.txt":(4,5), # TECH 2
    "logFC_P1vP2.txt":(1,5),
    "logFC_P1vA7.txt":(1,2), # TECH 2
    "logFC_A7vA10.txt":(2,3),# TECH 2
    "logFC_P2vB7.txt":(5,6), # TECH 2
    "logFC_B7vB10.txt":(6,7) # TECH 2
    }

for outputfilename in combinations.keys():
    this_data = {}
    with open(outputfilename, 'w') as outfile:
        xfilename = countsfilenames[combinations[outputfilename][0]]
        yfilename = countsfilenames[combinations[outputfilename][1]]
        with open(xfilename, 'r') as xfile:
            for line in xfile:
                data = line.rstrip().split()
                if not(data[0] in this_data.keys()):this_data[data[0]] = []
                this_data[data[0]].append(int(data[1]))
        with open(yfilename, 'r') as yfile:
            for line in yfile:
                data = line.rstrip().split()
                if not(data[0] in this_data.keys()):this_data[data[0]] = []
                this_data[data[0]].append(int(data[1]))
        for data in this_data.keys():
            if len(this_data[data])==2:
                outfile.write(data+','+str(logfc(this_data[data][0],this_data[data][1]))+'\n')

