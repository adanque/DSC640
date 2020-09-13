#Author: Alan Danque
#Date:   20200913
#Class:  DSC 640
#Exercise 2.2

#install.packages("rpivotTable")
#install.packages("readxl")
#install.packages("tidyverse")
#install.packages("reshape2")
#library(reshape2)
#library(rpivotTable)

# create list of packages we need 
packages <- c("ggplot2", "dplyr", "gapminder", "readxl", "tidyverse", "reshape2")
print(packages)
# Install packages 
lapply(packages, install.packages, character.only = TRUE)

# Load packages
lapply(packages, library, character.only = TRUE)
# In case you are unfamiliar with lapply() - it has been used to apply the install.packages() and library() functions over a list of package names. More information here: https://www.r-bloggers.com/using-apply-sapply-lapply-in-r/

# Read csv input
pggdata <- read.csv("./datasets/ppg2008.csv")

# Sort the dataframe on Games Played
pggdata_sorted <- pggdata[with (pggdata, order(G)),]

# Add unique ID
pggdata_sorted$ID <- 1:nrow(pggdata_sorted) 

print(is.data.frame(pggdata_sorted))
print(ncol(pggdata_sorted))
print(nrow(pggdata_sorted))

IDvector <- as.vector(pggdata_sorted$ID)
Gvector <- as.vector(pggdata_sorted$G)

print(IDvector)
print(Gvector)

print(typeof(IDvector))
print(typeof(Gvector))
dev.off()

# Line Chart
plot(IDvector,Gvector, type="l", col="blue", lwd=5, xlab="Player ID", ylab="Games Played", main="Number of Games Played by Player ID")
dev.copy(png,"./plots/Line Chart Number of Games Played by Player ID R.png")
dev.off()

# Step Chart
plot(IDvector,Gvector, type="s", col="grey", lwd=5, xlab="Player ID", ylab="Games Played", main="Number of Games Played by Player ID")
dev.copy(png,"./plots/Step Chart Number of Games Played by Player ID R.png")
dev.off()



