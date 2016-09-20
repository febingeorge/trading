data = read.csv("trading/fundamentals.csv",header = TRUE,stringsAsFactors = FALSE)
dat2 = data[data$PE > 0,]
dat2$MCap = dat2$MCap / 100000000
meanavgvol = mean(dat2$AvgVol)
data3 = dat2[dat2$AvgVol > meanavgvol,]
write.csv(data3,"finalset.csv")

