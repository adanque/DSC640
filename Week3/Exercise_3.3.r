#Author: Alan Danque
#Date:   20200921
#Class:  DSC 640
#Exercise 3.2

#install.packages("rpivotTable")
#install.packages("readxl")
#install.packages("tidyverse")
#install.packages("reshape2")
#library(reshape2)
#library(rpivotTable)
#install.packages("data.table")                     # Install data.tablepackage
#install.packages("plotly")
#library(plotly)
#library(treemap)

# create list of packages we need 
packages <- c("ggplot2", "dplyr", "gapminder", "readxl", "tidyverse", "reshape2", "data.table", "plotly", "treemap")
print(packages)
# Install packages 
lapply(packages, install.packages, character.only = TRUE)

# Load packages
lapply(packages, library, character.only = TRUE)
# In case you are unfamiliar with lapply() - it has been used to apply the install.packages() and library() functions over a list of package names. More information here: https://www.r-bloggers.com/using-apply-sapply-lapply-in-r/



# Read csv input
pggdata <- read.csv("./datasets/unemployement-rate-1948-2010.csv")
print(is.data.frame(pggdata))
print(ncol(pggdata))
print(nrow(pggdata))
print(pggdata)


Years <- distinct(pggdata, Year)
pggdatafiltered50 <- pggdata[pggdata$Year %like% "195", ]
pggdatafiltered60 <- pggdata[pggdata$Year %like% "196", ]
pggdatafiltered70 <- pggdata[pggdata$Year %like% "197", ]
pggdatafiltered80 <- pggdata[pggdata$Year %like% "198", ]
pggdatafiltered90 <- pggdata[pggdata$Year %like% "199", ]
pggdatafiltered20 <- pggdata[pggdata$Year %like% "200", ]



expdf <- read.table("./datasets/expenditures.txt", sep = '\t',header = TRUE) #, fileEncoding = "UTF-16LE")
print(is.data.frame(expdf))
print(ncol(expdf))
print(nrow(expdf))



# treemap
# Aggregate Sum by Year
expdfagg <- aggregate(pggdata$Value, by=list(Year=pggdata$Year), FUN=sum)
print(expdfagg)
group <- expdfagg$Year # c("group-1","group-2","group-3")
value <- expdfagg$x #c(13,5,22)
data <- data.frame(group,value)
treemap(data,
        index="group",
        vSize="value",
        type="index",
        title="Unemployment Rates between 1984 to 2010",
        fontsize.title = 14
)
dev.copy(png,"./plots/Unemployment Rates between 1984 to 2010 Tree Map R.png")
dev.off()

# Area Chart
xValue <- expdfagg$Year # c("group-1","group-2","group-3")
yValue <- expdfagg$x #c(13,5,22)
data <- data.frame(group,value)

ggplot(data, aes(x=xValue, y=yValue)) +
  geom_area( fill="#69b3a2", alpha=0.4) +
  geom_line(color="#69b3a2", size=2) +
  geom_point(size=3, color="#69b3a2") +
  theme_ipsum() +
  labs(x = "Years", y = "Amount") +
  ggtitle("Total Expenditures by Year")
dev.copy(png,"./plots/Total Expenditures by Year Area Chart R.png")
dev.off()

# Stacked Area Chart

Vals <- round(pggdata$Value, 0)
dataout <- data.frame(Year=pggdata$Year, Period=pggdata$Period, Vals=round(pggdata$Value, 0))
plot = ggplot(dataout, aes(x=Year, y=Vals, fill=Period))
plot + geom_area(colour="black", size=.2, alpha=.8) +
     theme_bw() +
     ggtitle("Unemployment Rate by Month by Year") 
dev.copy(png,"./plots/Unemployment Rate by Month by Year Stacked Area Chart R.png")
dev.off()


