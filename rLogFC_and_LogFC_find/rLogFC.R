library("DESeq2")
directory <- "/home/dcb/Documents/htseq/VERSUS/"
setwd(directory)

S1 = "B7"
S2 = "B10"
TYPE = "mid-late"

outputPrefix <- paste(S1,'v',S2,"_DESeq2_",sep="")
sampleFiles<- c(paste(S1,".counts",sep=""), paste(S2,".counts",sep=""))
sampleNames <- c(paste(S1,TYPE,sep="_"), paste(S2,TYPE,sep="_"))
sampleCondition <- c(paste("S1",TYPE,sep="_"), paste("S2",TYPE,sep="_"))
sampleTable <- data.frame(sampleName = sampleNames, fileName = sampleFiles, condition = sampleCondition)
treatments <- c(paste("S1",TYPE,sep="_"), paste("S2",TYPE,sep="_"))

ddsHTSeq <- DESeqDataSetFromHTSeqCount(sampleTable = sampleTable, directory = directory, design = ~ condition)
rld <- rlogTransformation( ddsHTSeq )
res <- data.frame(assay(rld), avgLogExpr = ( assay(rld)[,1] + assay(rld)[,2] ) / 2, rLogFC = assay(rld)[,2] - assay(rld)[,1] )
write.table(res, paste(outputPrefix,"result.txt",sep=""))

#filtered <- rbind(subset(res, rLogFC>=1.00), subset(res, rLogFC<=-1.00))
#filtered <- filtered[order(filtered$rLogFC),]
#write.table(filtered, paste(outputPrefix,"result_filtered.txt",sep=""))
