mystockuniverse = read.csv("historicalpe.csv")
stocdata = read.csv("trading/stockdata.csv")
date1 = as.Date(stocdata$Date)
stocdata$Date = as.Date(stocdata$Date)

stocdatanew = stocdata[as.numeric(format(stocdata$Date,"%Y")) > 2011,]
stocdatanew$Year = as.numeric(format(stocdatanew$Date,"%Y"))
stocdatanew$X <- NULL
anew = ddply(stocdatanew,.(Year),numcolwise(mean))
bnew <- as.data.frame(t(anew))
bnew <- bnew[-1,]
colnames(bnew) <- c("P2012","P2013","P2014","P2015","P2016")
bnew$stockname <- rownames(bnew)
bnew$stockname = substr(bnew$stockname,1,nchar(bnew$stockname)-3)
mergedset <- merge(mystockuniverse,bnew,by = "stockname")
mergedset$PE2012 = as.numeric(mergedset$P2012) / as.numeric(as.character(mergedset$X2012))
mergedset$PE2013 = as.numeric(mergedset$P2013) / as.numeric(as.character(mergedset$X2013))
mergedset$PE2014 = as.numeric(mergedset$P2014) / as.numeric(as.character(mergedset$X2014))
mergedset$PE2015 = as.numeric(mergedset$P2015) / as.numeric(as.character(mergedset$X2015))
mergedset$PE2016 = as.numeric(mergedset$P2016) / as.numeric(as.character(mergedset$X2016))
mergedsetfinal = mergedset[,c(1,7:16)]
totalprincipal = 300000

stocklist2012 = mergedsetfinal[mergedsetfinal$PE2012 > 15 & mergedsetfinal$PE2012 < 25,]
stocklist2012 <- stocklist2012[,c("stockname","P2012","PE2012")]
stocklist2012 <- na.omit(stocklist2012)
eachstockamount <- totalprincipal/length(stocklist2012$stockname)
stocklist2012$numofshares <- rep(eachstockamount,length(stocklist2012$stockname))/stocklist2012$P2012
stocklist2012$numofshares <- round(stocklist2012$numofshares)
stocklist2012final <- stocklist2012[,c("stockname","numofshares")]
write.csv(stocklist2012final,"stocklist2012.csv",row.names = FALSE)

stocklist2013 = mergedsetfinal[mergedsetfinal$PE2013 > 15 & mergedsetfinal$PE2013 < 25,]
stocklist2013 <- stocklist2013[,c("stockname","P2013","PE2013")]
stocklist2013 <- na.omit(stocklist2013)
eachstockamount <- totalprincipal/length(stocklist2013$stockname)
stocklist2013$numofshares <- rep(eachstockamount,length(stocklist2013$stockname))/stocklist2013$P2013
stocklist2013$numofshares <- round(stocklist2013$numofshares)
stocklist2013 <- stocklist2013[,c("stockname","numofshares")]
write.csv(stocklist2013,"stocklist2013.csv",row.names = FALSE)

stocklist2014 = mergedsetfinal[mergedsetfinal$PE2014 > 15 & mergedsetfinal$PE2014 < 25,]
stocklist2014 <- stocklist2014[,c("stockname","P2014","PE2014")]
stocklist2014 <- na.omit(stocklist2014)
eachstockamount <- totalprincipal/length(stocklist2014$stockname)
stocklist2014$numofshares <- round(rep(eachstockamount,length(stocklist2014$stockname))/stocklist2014$P2014)
stocklist2014 <- stocklist2014[,c("stockname","numofshares")]
write.csv(stocklist2014,"stocklist2014.csv",row.names = FALSE)

stocklist2015 = mergedsetfinal[mergedsetfinal$PE2015 > 15 & mergedsetfinal$PE2015 < 25,]
stocklist2015 <- stocklist2015[,c("stockname","P2015","PE2015")]
stocklist2015 <- na.omit(stocklist2015)
eachstockamount <- totalprincipal/length(stocklist2015$stockname)
stocklist2015$numofshares <- round(rep(eachstockamount,length(stocklist2015$stockname))/stocklist2015$P2015)
stocklist2015 <- stocklist2015[,c("stockname","numofshares")]
write.csv(stocklist2015,"stocklist2015.csv",row.names = FALSE)

stocklist2016 = mergedsetfinal[mergedsetfinal$PE2016 > 15 & mergedsetfinal$PE2016 < 25,]
stocklist2016 <- stocklist2016[,c("stockname","P2016","PE2016")]
stocklist2016 <- na.omit(stocklist2016)
eachstockamount <- totalprincipal/length(stocklist2016$stockname)
stocklist2016$numofshares <- round(rep(eachstockamount,length(stocklist2016$stockname))/stocklist2016$P2016)
stocklist2016 <- stocklist2016[,c("stockname","numofshares")]
write.csv(stocklist2016,"stocklist2016.csv",row.names = FALSE)
