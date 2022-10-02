from binGM import binGM
from plotGMbins import plotGMbins, plot2GMbins

#### extractResults.py should be run before executing this code #######################

################### DATA OPTIONS ######################################################

#format: [GM NAME], [RANK], [Elo], [Colour Index (max 6)]
gms_info=[['Carlsen', 1, 2856, 0],
['Niemann', 43, 2699, 1],
['Anand', 10, 2756, 10],
['Aronian', 11, 2755, 11],
['Caruana', 8, 2763, 8],
['Ding', 2, 2811, 2],
['Dominguez Perez', 13, 2747, 13],
['Firouzja', 4, 2785, 4],
['Giri', 7, 2764, 7],
['Karjakin', 15, 2747, 1],
['Mamedyarov', 14, 2747, 0],
['Nakamura', 6, 2768, 6],
['Nepomniachtchi', 3, 2793, 3],
['Rapport', 12, 2754, 12],
['So', 5, 2771, 5],
['Vachier-Lagrave', 9, 2757, 9]]

SAVE_SINGLES=True
SAVE_COMP=True

################### PARSE BIN OPTIONS ##############################################

elo_stagger=20
elo_step=20
elo_min=-600
elo_max=600
elo_pack=[elo_min, elo_max, elo_step, elo_stagger]

################### PROCESS RESULTS FILES ##########################################
#call individual analyses with the following:
#df_gm=binGM(gms[0],elo_pack)

df_gms=list()
for this_gm_index, this_gm_info in enumerate(gms_info):
    #compute results
    df_gms.append(binGM(gms_info[this_gm_index],elo_pack))
    #plot results
    plotGMbins(df_gms[this_gm_index].bins,this_gm_info,elo_pack,SAVE_SINGLES)


#create comparison plots of results. Written such that it could be modified to iterate all combinations later.
gm1_index=0
gm2_index=1
plot2GMbins(df_gms[gm1_index].bins,df_gms[gm2_index].bins,gms_info[gm1_index],gms_info[gm2_index],elo_pack,SAVE_COMP)

