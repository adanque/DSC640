#Author: Alan Danque
#Date:   20201003
#Class:  DSC 640
#Exercise 4.2
#Scatterplots, bubble charts and density plot charts 

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
crdata <- read.csv("./datasets/crimerates-by-state-2005.csv")
print(is.data.frame(crdata))
print(ncol(crdata))
print(nrow(crdata))
# Remove the United States from the dataframe so to contain only states.
crdata <- crdata[-c(1),]


#Scatterplot
ggplot(crdata, aes(x=state, y=motor_vehicle_theft)) + 
  theme(axis.text.x = element_text(angle = 90,hjust=0.95,vjust=0.2)) +
  theme(
    plot.title = element_text(color="blue", size=14, face="bold"),
    axis.title.x = element_text(color="blue", size=14, face="bold"),
    axis.title.y = element_text(color="blue", size=14, face="bold")
  ) +
  theme(plot.title = element_text(hjust = 0.5)) +
  ggtitle("Mortor Vehicle Theft Rate \n by State") +
  xlab("State") + 
  ylab("Mortor Vehicle Theft Rate") +
  geom_point()
dev.copy(png,"./plots/Motor Vehicle Theft Rate Scatter Plot R.png")
dev.off()

#Bubble chart
ggplot(crdata, aes(x=state, y=motor_vehicle_theft, size = motor_vehicle_theft)) +
  theme(axis.text.x = element_text(angle = 90,hjust=0.95,vjust=0.2)) +
  theme(
    plot.title = element_text(color="blue", size=14, face="bold"),
    axis.title.x = element_text(color="blue", size=14, face="bold"),
    axis.title.y = element_text(color="blue", size=14, face="bold")
  ) +
  theme(plot.title = element_text(hjust = 0.5)) +
  ggtitle("Mortor Vehicle Theft Rate \n by State") +
  xlab("State") + 
  ylab("Mortor Vehicle Theft Rate") +
  geom_point(alpha=0.7)
dev.copy(png,"./plots/Motor Vehicle Theft Rate Bubble Chart R.png")
dev.off()

#Density plot charts 
p <- ggplot(crdata, aes(x=motor_vehicle_theft)) + 
  theme(axis.text.x = element_text(angle = 90,hjust=0.95,vjust=0.2)) +
  theme(
    plot.title = element_text(color="blue", size=14, face="bold"),
    axis.title.x = element_text(color="blue", size=14, face="bold"),
    axis.title.y = element_text(color="blue", size=14, face="bold")
  ) +
  theme(plot.title = element_text(hjust = 0.5)) +
  ggtitle("Mortor Vehicle Theft Rate \n Density Plot") +
  xlab("Mortor Vehicle Theft Rate") + 
  ylab("Density") +
  geom_density() 
p
# Add mean line
#p+ geom_vline(aes(xintercept=mean(motor_vehicle_theft)),
#              color="blue", linetype="dashed", size=1)
dev.copy(png,"./plots/Motor Vehicle Theft Rate Density Plot R.png")
dev.off()


