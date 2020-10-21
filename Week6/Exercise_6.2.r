#Author: Alan Danque
#Date:   20201003
#Class:  DSC 640
#Exercise 6.2
#R histograms, box plots, bullet charts, and an additional charts of your choice

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

birthrate <- read.csv("./datasets/birth-rate.csv")
print(is.data.frame(birthrate))
print(ncol(birthrate))
print(nrow(birthrate))

crime <- read.csv("./datasets/crimeratesbystate-formatted.csv")
print(is.data.frame(crime))
print(ncol(crime))
print(nrow(crime))

education <- read.csv("./datasets/education.csv")
print(is.data.frame(education))
print(ncol(education))
print(nrow(education))

# Histograms
hist(crime$motor_vehicle_theft,
     main="Motor Vehicle Thefts Counts by Amount",
     xlab="Motor Vehicle Thefts Amounts",
     ylab="Counts",
     col="darkmagenta",
     freq=TRUE)
dev.copy(png,"./plots/Histogram R.png")
dev.off()


# Box plots
library(ggplot2)
options(warn=-1)
crimedf <- subset(crime, select = -c(state))
meltData <- melt(crimedf)
p <- ggplot(meltData, aes(factor(variable), value)) 
p + geom_boxplot() + facet_wrap(~variable, scale="free")+ 
        theme(axis.text.x=element_text(angle=0, hjust=0, vjust= 0.1)) +
        theme(axis.text.y=element_text(hjust=0, vjust= 0.1)) +
        ggtitle("US Crime Statistics") +
        xlab("Statistic") + 
        ylab("Instance Counts")
dev.copy(png,"./plots/Box Plot R.png")
dev.off()


# Bullet charts
eddf <- education[,c("state","math")]
eddf <- eddf[!(eddf$state=='United States'),]
eddf$mean <- 400
eddf$target <- 800

p <- ggplot(eddf, aes(math, state) )
p <- ggplot(eddf, aes(state, math) )
p <- p + geom_col(fill="grey", width=0.5)
p <- p + geom_col(aes(state, mean), width=0.2)
p <- p + geom_point(aes(state, target), colour="red")
p <- p + geom_errorbar(aes(y = target,x = state, ymin = target,ymax
                           = target), width = .45)
p <- p + coord_flip()+ 
        theme(axis.text.x=element_text(angle=0, hjust=0, vjust= 0.1)) +
        theme(axis.text.y=element_text(hjust=0, vjust= 0.1)) +
        ggtitle("PSAT Math Scores By State") +
        xlab("Math Scores") + 
        ylab("States")
dev.copy(png,"./plots/Bullet Chart R.png")
dev.off()
p

# An additional charts of your choice













