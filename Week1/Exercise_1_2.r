#Author: Alan Danque
#Date:   20200903
#Class:  DSC 640
#Exercise 1.2

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



#data <- read.csv("./datasets/obama-approval-ratings.xls")
oadata <- read_excel("./datasets/obama-approval-ratings.xls")
print(oadata)

print(is.data.frame(oadata))
print(ncol(oadata))
print(nrow(oadata))


# BAR CHART
# make the base plot and save it in the object "plot_base"
plot_base <- ggplot(data = oadata, mapping = aes(x = reorder(Issue, Approve), y = Approve))
# display the plot object
#plot_base

# save a better-formatted version of the base plot in "plot_base_clean"
plot_base_clean <- plot_base + 
  # apply basic black and white theme - this theme removes the background colour by default
  theme_bw() + 
  # remove gridlines. panel.grid.major is for vertical lines, panel.grid.minor is for horizontal lines
  theme(panel.grid.major = element_blank(), panel.grid.minor = element_blank(),
        # remove borders
        panel.border = element_blank(),
        # removing borders also removes x and y axes. Add them back
        axis.line = element_line())
  

# display the plot object
p <- plot_base_clean + theme(axis.text.x = element_text(angle = 90))

p + geom_bar(stat = "identity", fill = "blue") +
  ggtitle("Obama Approval Rating by Issue") +
  theme(plot.title = element_text(hjust = 0.5))  + 
  coord_flip()
ggsave("./plots/barchart_obama_approval_ratings_R.png")


# STACKED BAR CHART
DF1 <- melt(oadata, id.var="Issue")
ggplot(DF1, aes(x =Issue, y = value, fill = variable)) + 
  geom_bar(stat = "identity")+ theme(axis.text.x = element_text(angle = 90)) + 
  theme(plot.title = element_text(hjust = 0.5, size = 11, face = "plain")) +
  ggtitle("Obama Ratings by Issue")+
  geom_col() +
  geom_text(aes( label = value, group =variable), color = "white", position = position_stack(vjust = 0.5, reverse = FALSE)) +
  labs(x = "Issue", y = "Rating")
ggsave("./plots/Stacked_barchart_obama_approval_ratings_R.png")



# PIE CHART
oa.data <- subset(oadata, Issue=='Economy')
oa.data <- melt(oa.data, id.vars = "Issue")
oaout.data <- oa.data %>%
  arrange(desc(Issue)) %>%
  mutate(lab.ypos = cumsum(value) - 0.5*value)

mycols <- c("#0073C2FF", "#EFC000FF", "#868686FF")
ggplot(oaout.data, aes(x = "", y = value , fill = variable )) +
  geom_bar(width = 1, stat = "identity", color = "white") +
  coord_polar("y", start = 0)+
  geom_text(aes(y = lab.ypos , label = value*.01), color = "white")+
  scale_fill_manual(values = mycols) +
  theme(plot.title = element_text(hjust = 0.5, size = 11, face = "plain")) +  
  labs(x = NULL, y = "Rating")+ 
  ggtitle("Obama Approval Ratings on Economics")
ggsave("./plots/Pie_chart_obama_approval_ratings_On_Economics_R.png")



# DONUT CHART
mycols <- c("#0073C2FF", "#EFC000FF", "#868686FF")
ggplot(oaout.data, aes(x = 2, y = value , fill = variable )) +
  geom_bar(width = 1, stat = "identity", color = "white") +
  coord_polar("y", start = 0)+
  geom_text(aes(y = lab.ypos , label = value*.01), color = "white")+
  scale_fill_manual(values = mycols) +
  theme_void()+
  xlim(0.5, 2.5)+
  #theme(plot.title = element_text(hjust = 0.5, size = 11, face = "plain")) +  
  labs(x = NULL, y = "Rating")+ 
  ggtitle("Obama Approval Ratings on Economics")
ggsave("./plots/Donut_chart_obama_approval_ratings_On_Economics_R.png")

