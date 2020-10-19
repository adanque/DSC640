#Author: Alan Danque
#Date:   20201003
#Class:  DSC 640
#Exercise 5.2
#R Heat maps, Spatial charts and Contour chart

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
nba <- read.csv("./datasets/ppg2008.csv")
print(is.data.frame(nba))
print(ncol(nba))
print(nrow(nba))

costcodata <- read.csv("./datasets/costcos-geocoded.csv")
print(is.data.frame(costcodata))
print(ncol(costcodata))
print(nrow(costcodata))


# Heat maps
nba$Name <- with(nba, reorder(Name, PTS))

library(ggplot2)
library(plyr)
library(dplyr)
library(reshape2)
library(scales)

nba.m <- melt(nba)
nba.m <- ddply(nba.m, .(variable), transform, rescale = rescale(value))
base_size <- 9
(p <- ggplot(nba.m, aes(variable, Name)) + geom_tile(aes(fill = rescale), colour = "white") + scale_fill_gradient(low = "white", high = "steelblue"))
p + theme_grey(base_size = base_size) + labs(x = "", y = "") + scale_x_discrete(expand = c(0, 0)) +
        scale_y_discrete(expand = c(0, 0)) + 
        theme(axis.text.x=element_text(angle=90, hjust=0, vjust= 0.1)) +
        theme(axis.text.y=element_text(hjust=0, vjust= 0.1)) +
        ggtitle("2008 Basketball Player Statistics") +
        xlab("Statistic") + 
        ylab("Basketball Player")
dev.copy(png,"./plots/Heatmap Plot R.png")
dev.off()



# Spatial charts
library(leaflet)
library(htmlwidgets)
costcodata$faddr <- paste(costcodata$Address, costcodata$City, costcodata$State, costcodata$Zip.Code )
print(costcodata$faddr)
m <- leaflet()
m <- addTiles(m)
m <- addMarkers(m, lng=costcodata$Longitude, lat=costcodata$Latitude, popup=costcodata$faddr)
m
saveWidget(m, file="C://Users/aland/DSC640/Week5/plots/Spatial Map R.html")


# Contour chart
library(ggplot2)
library(akima)
library(dplyr)

interpdf <-interp2xyz(interp(x=nba$FGA, y=nba$PTS, z=nba$FGP, duplicate="mean"), data.frame=TRUE)
print(interpdf)
interpdf %>%
        filter(!is.na(z)) %>%
        tbl_df() %>%
        ggplot(aes(x = x, y = y, z = z, fill = z)) + 
        geom_tile() + 
        geom_contour(color = "white", alpha = 0.05) + 
        scale_fill_distiller(palette="Blues", na.value="white") + 
        theme_bw() +
        xlab("PTS") +
        ylab("FGA") +
        ggtitle("Basketball FGP Based on FGA and PTS Contour Plot") +
        guides(fill=guide_legend(title="FGP"))
dev.copy(png,"./plots/Contour Plot R.png")
dev.off()
