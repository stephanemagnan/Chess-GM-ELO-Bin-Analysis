import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib as mpl
import seaborn as sns
from binGM import binGM
from plotGMbins import plotGMbins, plot2GMbins

#### extractResults.py should be run before executing this code #######################

################### DATA OPTIONS ######################################################
name_p1='Carlsen'
rank_p1=1
elo_p1=2856
name_p2='Niemann'
rank_p2=43
elo_p2=2699
name_p3='Anand'
rank_p3=10
elo_p3=2756
name_p4='Aronian'
rank_p4=11
elo_p4=2755
name_p5='Caruana'
rank_p5=8
elo_p5=2763
name_p6='Ding'
rank_p6=2
elo_p6=2811
name_p7='Firouzja'
rank_p7=4
elo_p7=2785
name_p8='Giri'
rank_p8=7
elo_p8=2764
name_p9='Karjakin'
rank_p9=15
elo_p9=2747
name_p10='Mamedyarov'
rank_p10=14
elo_p10=2747
name_p11='Nakamura'
rank_p11=6
elo_p11=2768
name_p12='Nepomniachtchi'
rank_p12=3
elo_p12=2793
name_p13='Perez'
rank_p13=13
elo_p13=2747
name_p14='Rapport'
rank_p14=2754
elo_p14=12
name_p15='So'
rank_p15=5
elo_p15=2771
name_p16='Vachier-Lagrave'
rank_p16=9
elo_p16=2757


colourind_p1=0
colourind_p2=1
colourind_p3=2
colourind_p4=3
colourind_p5=4
colourind_p6=5
colourind_p7=6
colourind_p8=0
colourind_p9=1
colourind_p10=2
colourind_p11=3
colourind_p12=4
colourind_p13=5
colourind_p14=6
colourind_p15=0
colourind_p16=1

SAVE_SINGLES=True
SAVE_COMP=True

################### PARSE BIN OPTIONS ##############################################

elo_stagger=20
elo_step=20
elo_min=-400
elo_max=400

################### PROCESS RESULTS FILES ##########################################
df_p1=binGM(name_p1,elo_min,elo_max,elo_step)
df_p2=binGM(name_p2,elo_min,elo_max,elo_step)
df_p3=binGM(name_p3,elo_min,elo_max,elo_step)
df_p4=binGM(name_p4,elo_min,elo_max,elo_step)
df_p5=binGM(name_p5,elo_min,elo_max,elo_step)
df_p6=binGM(name_p6,elo_min,elo_max,elo_step)
df_p7=binGM(name_p7,elo_min,elo_max,elo_step)
df_p8=binGM(name_p8,elo_min,elo_max,elo_step)
df_p9=binGM(name_p9,elo_min,elo_max,elo_step)
df_p10=binGM(name_p10,elo_min,elo_max,elo_step)
df_p11=binGM(name_p11,elo_min,elo_max,elo_step)
df_p12=binGM(name_p12,elo_min,elo_max,elo_step)
df_p13=binGM(name_p13,elo_min,elo_max,elo_step)
df_p14=binGM(name_p14,elo_min,elo_max,elo_step)
df_p15=binGM(name_p15,elo_min,elo_max,elo_step)
df_p16=binGM(name_p16,elo_min,elo_max,elo_step)


#create plots of results
plotGMbins(df_p1.bins,name_p1,rank_p1,elo_p1,elo_min,elo_max,elo_stagger*2,colourind_p1,SAVE_SINGLES)
plotGMbins(df_p2.bins,name_p2,rank_p2,elo_p2,elo_min,elo_max,elo_stagger*2,colourind_p2,SAVE_SINGLES)
plotGMbins(df_p3.bins,name_p3,rank_p3,elo_p3,elo_min,elo_max,elo_stagger*2,colourind_p3,SAVE_SINGLES)
plotGMbins(df_p4.bins,name_p4,rank_p4,elo_p4,elo_min,elo_max,elo_stagger*2,colourind_p4,SAVE_SINGLES)
plotGMbins(df_p5.bins,name_p5,rank_p5,elo_p5,elo_min,elo_max,elo_stagger*2,colourind_p5,SAVE_SINGLES)
plotGMbins(df_p6.bins,name_p6,rank_p6,elo_p6,elo_min,elo_max,elo_stagger*2,colourind_p6,SAVE_SINGLES)
plotGMbins(df_p7.bins,name_p7,rank_p7,elo_p7,elo_min,elo_max,elo_stagger*2,colourind_p7,SAVE_SINGLES)
plotGMbins(df_p8.bins,name_p8,rank_p8,elo_p8,elo_min,elo_max,elo_stagger*2,colourind_p8,SAVE_SINGLES)
plotGMbins(df_p9.bins,name_p9,rank_p9,elo_p9,elo_min,elo_max,elo_stagger*2,colourind_p9,SAVE_SINGLES)
plotGMbins(df_p10.bins,name_p10,rank_p10,elo_p10,elo_min,elo_max,elo_stagger*2,colourind_p10,SAVE_SINGLES)
plotGMbins(df_p11.bins,name_p11,rank_p11,elo_p11,elo_min,elo_max,elo_stagger*2,colourind_p11,SAVE_SINGLES)
plotGMbins(df_p12.bins,name_p10,rank_p12,elo_p12,elo_min,elo_max,elo_stagger*2,colourind_p12,SAVE_SINGLES)
plotGMbins(df_p13.bins,name_p11,rank_p13,elo_p13,elo_min,elo_max,elo_stagger*2,colourind_p13,SAVE_SINGLES)
plotGMbins(df_p14.bins,name_p10,rank_p14,elo_p14,elo_min,elo_max,elo_stagger*2,colourind_p14,SAVE_SINGLES)
plotGMbins(df_p15.bins,name_p11,rank_p15,elo_p15,elo_min,elo_max,elo_stagger*2,colourind_p15,SAVE_SINGLES)
plotGMbins(df_p16.bins,name_p10,rank_p16,elo_p16,elo_min,elo_max,elo_stagger*2,colourind_p16,SAVE_SINGLES)

plot2GMbins(df_p1.bins,df_p2.bins,name_p1,name_p2,elo_min,elo_max,elo_stagger,colourind_p1,colourind_p2,SAVE_COMP)


print(df_p8.bins)