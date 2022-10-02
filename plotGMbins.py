import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib as mpl
import seaborn as sns

sns.set()
plt.style.use('ggplot')

FONT_SIZE_SUPTITLE = 21
FONT_SIZE_AXIS = 12
FONT_SIZE_TITLE = 18



def plotGMbins(df_bins,gm_info,elo_pack,DO_SAVE):
    playername,playerrank,playerelo,colour_index=gm_info
    elo_min, elo_max, elo_step, elo_stagger = elo_pack
    #stagger doubled for single bins only
    elo_stagger*=2

    full_colours, dulled_colours, faded_colours = buildColours()
    fig, axes = plt.subplots(figsize=(16,9), facecolor='#ffffff', ncols=4, sharey=True)

    fig.suptitle(f'#{playerrank}. {playername} ({playerelo}) Historical Performance Based on Relative ELO Ranking',fontsize=FONT_SIZE_SUPTITLE)
    fig.tight_layout()

    #SUBPLOT
    axes[0].barh(df_bins['White ELO Adv'],df_bins['White Win %']+df_bins['White Tie %']+df_bins['White Loss %'],edgecolor=None,color=faded_colours[colour_index], align='center',height=(elo_stagger/2)-1)
    axes[0].barh(df_bins['White ELO Adv'],df_bins['White Win %']+df_bins['White Tie %'],edgecolor=None,color=dulled_colours[colour_index], align='center',height=(elo_stagger/2)-1)
    axes[0].barh(df_bins['White ELO Adv'],df_bins['White Win %'],edgecolor=None,color=full_colours[colour_index],align='center', height=(elo_stagger/2)-1)
    axes[0].plot((0,0),(elo_min,elo_max), linewidth=1,color='w')
    axes[0].plot((25,25),(elo_min,elo_max), linewidth=1,color='w')
    axes[0].plot((50,50),(elo_min,elo_max), linewidth=1,color='w')
    axes[0].plot((75,75),(elo_min,elo_max), linewidth=1,color='w')
    axes[0].plot((100,100),(elo_min,elo_max), linewidth=1,color='w')
    axes[0].set_xlim(left=0,right=100)
    axes[0].set_xticks([0,25,50,75,100])
    axes[0].set_xlabel('Outcome Rate (%)')
    axes[0].invert_xaxis()
    axes[0].set_ylabel('ELO Advantage')
    axes[0].set_ylim(bottom=elo_min,top=elo_max)

    #SUBPLOT
    axes[1].barh(df_bins['White ELO Adv'],df_bins['White Wins']+df_bins['White Ties']+df_bins['White Losses'],edgecolor=None,color=faded_colours[colour_index], align='center',height=(elo_stagger/2)-1,label=f'{playername} Losses ({df_bins["White Losses"].sum():.0f}W/{df_bins["Black Losses"].sum():.0f}B)')
    axes[1].barh(df_bins['White ELO Adv'],df_bins['White Wins']+df_bins['White Ties'],edgecolor=None,color=dulled_colours[colour_index], align='center',height=(elo_stagger/2)-1,label=f'{playername} Ties ({df_bins["White Ties"].sum():.0f}W/{df_bins["Black Ties"].sum():.0f}B)')
    axes[1].barh(df_bins['White ELO Adv'],df_bins['White Wins'],edgecolor=None,color=full_colours[colour_index],align='center', height=(elo_stagger/2)-1,label=f'{playername} Wins ({df_bins["White Wins"].sum():.0f}W/{df_bins["Black Wins"].sum():.0f}B)')
    
    axes[1].set_title('Playing with White Pieces',fontsize=FONT_SIZE_TITLE,horizontalalignment='right')
    axes[1].set_xticks([0,20,40,60,80])
    axes[1].set_xlim(left=0,right=100)
    axes[1].set_xlabel('Games Played')
    axes[1].invert_xaxis()

    handles, labels = axes[1].get_legend_handles_labels()
    order = [2,1,0]

    plt.legend(handles=[handles[idx] for idx in order],labels=[labels[idx] for idx in order],loc='lower right',bbox_to_anchor=(0, -0.2),fancybox=False, shadow=False, ncol=3)# ,

    #SUBPLOT
    axes[2].plot((0,0),(elo_min,elo_max), linewidth=1,color='#888888',zorder=1)
    axes[2].plot((20,20),(elo_min,elo_max), linewidth=1,color='#888888',zorder=1)
    axes[2].plot((40,40),(elo_min,elo_max), linewidth=1,color='#888888',zorder=1)
    axes[2].plot((60,60),(elo_min,elo_max), linewidth=1,color='#888888',zorder=1)
    axes[2].plot((80,80),(elo_min,elo_max), linewidth=1,color='#888888',zorder=1)
    axes[2].plot((100,100),(elo_min,elo_max), linewidth=1,color='#888888',zorder=1)
    axes[2].plot((0,100),(500,500), linewidth=1,color='#888888',zorder=1)
    axes[2].plot((0,100),(400,400), linewidth=1,color='#888888',zorder=1)
    axes[2].plot((0,100),(300,300), linewidth=1,color='#888888',zorder=1)
    axes[2].plot((0,100),(200,200), linewidth=1,color='#888888',zorder=1)
    axes[2].plot((0,100),(100,100), linewidth=1,color='#888888',zorder=1)
    axes[2].plot((0,100),(0,0), linewidth=1,color='#888888',zorder=1)
    axes[2].plot((0,100),(-100,-100), linewidth=1,color='#888888',zorder=1)
    axes[2].plot((0,100),(-200,-200), linewidth=1,color='#888888',zorder=1)
    axes[2].plot((0,100),(-300,-300), linewidth=1,color='#888888',zorder=1)
    axes[2].plot((0,100),(-400,-400), linewidth=1,color='#888888',zorder=1)
    axes[2].plot((0,100),(-500,-500), linewidth=1,color='#888888',zorder=1)

    axes[2].barh(df_bins['White ELO Adv'],df_bins['Black Wins']+df_bins['Black Ties']+df_bins['Black Losses'],edgecolor=None,color=faded_colours[colour_index],align='center', height=(elo_stagger/2)-1)
    axes[2].barh(df_bins['White ELO Adv'],df_bins['Black Wins']+df_bins['Black Ties'],edgecolor=None,color=dulled_colours[colour_index],align='center', height=(elo_stagger/2)-1)
    axes[2].barh(df_bins['White ELO Adv'],df_bins['Black Wins'],edgecolor=None,color=full_colours[colour_index],align='center', height=(elo_stagger/2)-1)

    axes[2].set_title('Playing with Black Pieces',fontsize=FONT_SIZE_TITLE,horizontalalignment= 'left')
    axes[2].set_xticks([0,20,40,60,80])
    axes[2].set_xlim(left=0,right=100)
    axes[2].set_xlabel('Games Played')

    #SUBPLOT
    axes[3].plot((0,100),(500,500), linewidth=1,color='#888888',zorder=1)
    axes[3].plot((0,100),(400,400), linewidth=1,color='#888888',zorder=1)
    axes[3].plot((0,100),(300,300), linewidth=1,color='#888888',zorder=1)
    axes[3].plot((0,100),(200,200), linewidth=1,color='#888888',zorder=1)
    axes[3].plot((0,100),(100,100), linewidth=1,color='#888888',zorder=1)
    axes[3].plot((0,100),(0,0), linewidth=1,color='#888888',zorder=1)
    axes[3].plot((0,100),(-100,-100), linewidth=1,color='#888888',zorder=1)
    axes[3].plot((0,100),(-200,-200), linewidth=1,color='#888888',zorder=1)
    axes[3].plot((0,100),(-300,-300), linewidth=1,color='#888888',zorder=1)
    axes[3].plot((0,100),(-400,-400), linewidth=1,color='#888888',zorder=1)
    axes[3].plot((0,100),(-500,-500), linewidth=1,color='#888888',zorder=1)
    axes[3].barh(df_bins['White ELO Adv'],df_bins['Black Win %']+df_bins['Black Tie %']+df_bins['Black Loss %'],edgecolor=None,color=faded_colours[colour_index], align='center',height=(elo_stagger/2)-1)
    axes[3].barh(df_bins['White ELO Adv'],df_bins['Black Win %']+df_bins['Black Tie %'],edgecolor=None,color=dulled_colours[colour_index], align='center',height=(elo_stagger/2)-1)
    axes[3].barh(df_bins['White ELO Adv'],df_bins['Black Win %'],edgecolor=None,color=full_colours[colour_index],align='center', height=(elo_stagger/2)-1)
    axes[3].plot((0,0),(elo_min,elo_max), linewidth=1,color='#888888')
    axes[3].plot((25,25),(elo_min,elo_max), linewidth=1,color='#888888')
    axes[3].plot((50,50),(elo_min,elo_max), linewidth=1,color='#888888')
    axes[3].plot((75,75),(elo_min,elo_max), linewidth=1,color='#888888')
    axes[3].plot((100,100),(elo_min,elo_max), linewidth=1,color='#888888')
    
    axes[3].set_xticks([0,25,50,75,100])
    axes[3].set_xlabel('Outcome Rate (%)')
    axes[3].set_xlim(left=0,right=100)

    plt.subplots_adjust(wspace=0,top=0.875,bottom=0.15,left=0.1,right=0.95)
    if DO_SAVE:
        plt.savefig(f'figures/{playerrank}. {playername}.png')

def plot2GMbins(df_bins1,df_bins2,gm1_info,gm2_info,elo_pack,DO_SAVE):
    playername1,playerrank1,playerelo1,colour_index1=gm1_info
    playername2,playerrank2,playerelo2,colour_index2=gm2_info
    elo_min, elo_max, elo_step, elo_stagger = elo_pack

    full_colours, dulled_colours, faded_colours = buildColours()
    fig, axes = plt.subplots(figsize=(16,9), facecolor='#ffffff', ncols=4, sharey=True)

    fig.suptitle(f'{playername1} and {playername2} Historical Performance Based on Relative ELO Ranking',fontsize=FONT_SIZE_SUPTITLE)
    fig.tight_layout()

    #SUBPLOT
    axes[0].barh(df_bins1['White ELO Adv']-(elo_stagger/2-1)/2,df_bins1['White Win %']+df_bins1['White Tie %']+df_bins1['White Loss %'],edgecolor=None,color=faded_colours[colour_index1], align='center',height=(elo_stagger/2)-1)
    axes[0].barh(df_bins1['White ELO Adv']-(elo_stagger/2-1)/2,df_bins1['White Win %']+df_bins1['White Tie %'],edgecolor=None,color=dulled_colours[colour_index1], align='center',height=(elo_stagger/2)-1)
    axes[0].barh(df_bins1['White ELO Adv']-(elo_stagger/2-1)/2,df_bins1['White Win %'],edgecolor=None,color=full_colours[colour_index1],align='center', height=(elo_stagger/2)-1)
    axes[0].barh(df_bins2['White ELO Adv']+(elo_stagger/2-1)/2,df_bins2['White Win %']+df_bins2['White Tie %']+df_bins2['White Loss %'],edgecolor=None,color=faded_colours[colour_index2], align='center',height=(elo_stagger/2)-1)
    axes[0].barh(df_bins2['White ELO Adv']+(elo_stagger/2-1)/2,df_bins2['White Win %']+df_bins2['White Tie %'],edgecolor=None,color=dulled_colours[colour_index2], align='center',height=(elo_stagger/2)-1)
    axes[0].barh(df_bins2['White ELO Adv']+(elo_stagger/2-1)/2,df_bins2['White Win %'],edgecolor=None,color=full_colours[colour_index2],align='center', height=(elo_stagger/2)-1)
    axes[0].plot((0,0),(elo_min,elo_max), linewidth=1,color='w')
    axes[0].plot((25,25),(elo_min,elo_max), linewidth=1,color='w')
    axes[0].plot((50,50),(elo_min,elo_max), linewidth=1,color='w')
    axes[0].plot((75,75),(elo_min,elo_max), linewidth=1,color='w')
    axes[0].plot((100,100),(elo_min,elo_max), linewidth=1,color='w')
    axes[0].set_xlim(left=0,right=100)
    axes[0].set_xticks([0,25,50,75,100])
    axes[0].set_xlabel('Outcome Rate (%)')
    axes[0].invert_xaxis()
    axes[0].set_ylabel('ELO Advantage')
    axes[0].set_ylim(bottom=elo_min,top=elo_max)

    #SUBPLOT
    axes[1].barh(df_bins1['White ELO Adv']-(elo_stagger/2-1)/2,df_bins1['White Wins']+df_bins1['White Ties']+df_bins1['White Losses'],edgecolor=None,color=faded_colours[colour_index1], align='center',height=(elo_stagger/2)-1,label=f'{playername1} Losses ({df_bins1["White Losses"].sum():.0f}W/{df_bins1["Black Losses"].sum():.0f}B)')
    axes[1].barh(df_bins1['White ELO Adv']-(elo_stagger/2-1)/2,df_bins1['White Wins']+df_bins1['White Ties'],edgecolor=None,color=dulled_colours[colour_index1], align='center',height=(elo_stagger/2)-1,label=f'{playername1} Ties ({df_bins1["White Ties"].sum():.0f}W/{df_bins1["Black Ties"].sum():.0f}B)')
    axes[1].barh(df_bins1['White ELO Adv']-(elo_stagger/2-1)/2,df_bins1['White Wins'],edgecolor=None,color=full_colours[colour_index1],align='center', height=(elo_stagger/2)-1,label=f'{playername1} Wins ({df_bins1["White Wins"].sum():.0f}W/{df_bins1["Black Wins"].sum():.0f}B)')
    axes[1].barh(df_bins2['White ELO Adv']+(elo_stagger/2-1)/2,df_bins2['White Wins']+df_bins2['White Ties']+df_bins2['White Losses'],edgecolor=None,color=faded_colours[colour_index2], align='center',height=(elo_stagger/2)-1,label=f'{playername2} Losses ({df_bins2["White Losses"].sum():.0f}W/{df_bins2["Black Losses"].sum():.0f}B)')
    axes[1].barh(df_bins2['White ELO Adv']+(elo_stagger/2-1)/2,df_bins2['White Wins']+df_bins2['White Ties'],edgecolor=None,color=dulled_colours[colour_index2], align='center',height=(elo_stagger/2)-1,label=f'{playername2} Ties ({df_bins2["White Ties"].sum():.0f}W/{df_bins2["Black Ties"].sum():.0f}B)')
    axes[1].barh(df_bins2['White ELO Adv']+(elo_stagger/2-1)/2,df_bins2['White Wins'],edgecolor=None,color=full_colours[colour_index2],align='center', height=(elo_stagger/2)-1,label=f'{playername2} Wins ({df_bins2["White Wins"].sum():.0f}W/{df_bins2["Black Wins"].sum():.0f}B)')
   
    axes[1].set_title('Playing with White Pieces',fontsize=FONT_SIZE_TITLE,horizontalalignment='right')
    axes[1].set_xticks([0,20,40,60,80])
    axes[1].set_xlim(left=0,right=100)
    axes[1].set_xlabel('Games Played')
    axes[1].invert_xaxis()

    handles, labels = axes[1].get_legend_handles_labels()
    order = [2,5,1,4,0,3]

    plt.legend(handles=[handles[idx] for idx in order],labels=[labels[idx] for idx in order],loc='lower right',bbox_to_anchor=(0, -0.2),fancybox=False, shadow=False, ncol=3)# ,

    #SUBPLOT
    axes[2].plot((0,0),(elo_min,elo_max), linewidth=1,color='#888888',zorder=1)
    axes[2].plot((20,20),(elo_min,elo_max), linewidth=1,color='#888888',zorder=1)
    axes[2].plot((40,40),(elo_min,elo_max), linewidth=1,color='#888888',zorder=1)
    axes[2].plot((60,60),(elo_min,elo_max), linewidth=1,color='#888888',zorder=1)
    axes[2].plot((80,80),(elo_min,elo_max), linewidth=1,color='#888888',zorder=1)
    axes[2].plot((100,100),(elo_min,elo_max), linewidth=1,color='#888888',zorder=1)
    axes[2].plot((0,100),(500,500), linewidth=1,color='#888888',zorder=1)
    axes[2].plot((0,100),(400,400), linewidth=1,color='#888888',zorder=1)
    axes[2].plot((0,100),(300,300), linewidth=1,color='#888888',zorder=1)
    axes[2].plot((0,100),(200,200), linewidth=1,color='#888888',zorder=1)
    axes[2].plot((0,100),(100,100), linewidth=1,color='#888888',zorder=1)
    axes[2].plot((0,100),(0,0), linewidth=1,color='#888888',zorder=1)
    axes[2].plot((0,100),(-100,-100), linewidth=1,color='#888888',zorder=1)
    axes[2].plot((0,100),(-200,-200), linewidth=1,color='#888888',zorder=1)
    axes[2].plot((0,100),(-300,-300), linewidth=1,color='#888888',zorder=1)
    axes[2].plot((0,100),(-400,-400), linewidth=1,color='#888888',zorder=1)
    axes[2].plot((0,100),(-500,-500), linewidth=1,color='#888888',zorder=1)

    axes[2].barh(df_bins1['White ELO Adv']-(elo_stagger/2-1)/2,df_bins1['Black Wins']+df_bins1['Black Ties']+df_bins1['Black Losses'],edgecolor=None,color=faded_colours[colour_index1],align='center', height=(elo_stagger/2)-1)
    axes[2].barh(df_bins1['White ELO Adv']-(elo_stagger/2-1)/2,df_bins1['Black Wins']+df_bins1['Black Ties'],edgecolor=None,color=dulled_colours[colour_index1],align='center', height=(elo_stagger/2)-1)
    axes[2].barh(df_bins1['White ELO Adv']-(elo_stagger/2-1)/2,df_bins1['Black Wins'],edgecolor=None,color=full_colours[colour_index1],align='center', height=(elo_stagger/2)-1)
    axes[2].barh(df_bins2['White ELO Adv']+(elo_stagger/2-1)/2,df_bins2['Black Wins']+df_bins2['Black Ties']+df_bins2['Black Losses'],edgecolor=None,color=faded_colours[colour_index2],align='center', height=(elo_stagger/2)-1)
    axes[2].barh(df_bins2['White ELO Adv']+(elo_stagger/2-1)/2,df_bins2['Black Wins']+df_bins2['Black Ties'],edgecolor=None,color=dulled_colours[colour_index2],align='center', height=(elo_stagger/2)-1)
    axes[2].barh(df_bins2['White ELO Adv']+(elo_stagger/2-1)/2,df_bins2['Black Wins'],edgecolor=None,color=full_colours[colour_index2],align='center', height=(elo_stagger/2)-1)

    axes[2].set_title('Playing with Black Pieces',fontsize=FONT_SIZE_TITLE,horizontalalignment= 'left')
    axes[2].set_xticks([0,20,40,60,80])
    axes[2].set_xlim(left=0,right=100)
    axes[2].set_xlabel('Games Played')

    #SUBPLOT
    axes[3].plot((0,100),(500,500), linewidth=1,color='#888888',zorder=1)
    axes[3].plot((0,100),(400,400), linewidth=1,color='#888888',zorder=1)
    axes[3].plot((0,100),(300,300), linewidth=1,color='#888888',zorder=1)
    axes[3].plot((0,100),(200,200), linewidth=1,color='#888888',zorder=1)
    axes[3].plot((0,100),(100,100), linewidth=1,color='#888888',zorder=1)
    axes[3].plot((0,100),(0,0), linewidth=1,color='#888888',zorder=1)
    axes[3].plot((0,100),(-100,-100), linewidth=1,color='#888888',zorder=1)
    axes[3].plot((0,100),(-200,-200), linewidth=1,color='#888888',zorder=1)
    axes[3].plot((0,100),(-300,-300), linewidth=1,color='#888888',zorder=1)
    axes[3].plot((0,100),(-400,-400), linewidth=1,color='#888888',zorder=1)
    axes[3].plot((0,100),(-500,-500), linewidth=1,color='#888888',zorder=1)
    axes[3].barh(df_bins1['White ELO Adv']-(elo_stagger/2-1)/2,df_bins1['Black Win %']+df_bins1['Black Tie %']+df_bins1['Black Loss %'],edgecolor=None,color=faded_colours[colour_index1], align='center',height=(elo_stagger/2)-1)
    axes[3].barh(df_bins1['White ELO Adv']-(elo_stagger/2-1)/2,df_bins1['Black Win %']+df_bins1['Black Tie %'],edgecolor=None,color=dulled_colours[colour_index1], align='center',height=(elo_stagger/2)-1)
    axes[3].barh(df_bins1['White ELO Adv']-(elo_stagger/2-1)/2,df_bins1['Black Win %'],edgecolor=None,color=full_colours[colour_index1],align='center', height=(elo_stagger/2)-1)
    axes[3].barh(df_bins2['White ELO Adv']+(elo_stagger/2-1)/2,df_bins2['Black Win %']+df_bins2['Black Tie %']+df_bins2['Black Loss %'],edgecolor=None,color=faded_colours[colour_index2], align='center',height=(elo_stagger/2)-1)
    axes[3].barh(df_bins2['White ELO Adv']+(elo_stagger/2-1)/2,df_bins2['Black Win %']+df_bins2['Black Tie %'],edgecolor=None,color=dulled_colours[colour_index2], align='center',height=(elo_stagger/2)-1)
    axes[3].barh(df_bins2['White ELO Adv']+(elo_stagger/2-1)/2,df_bins2['Black Win %'],edgecolor=None,color=full_colours[colour_index2],align='center', height=(elo_stagger/2)-1)
    axes[3].plot((0,0),(elo_min,elo_max), linewidth=1,color='#888888')
    axes[3].plot((25,25),(elo_min,elo_max), linewidth=1,color='#888888')
    axes[3].plot((50,50),(elo_min,elo_max), linewidth=1,color='#888888')
    axes[3].plot((75,75),(elo_min,elo_max), linewidth=1,color='#888888')
    axes[3].plot((100,100),(elo_min,elo_max), linewidth=1,color='#888888')
    axes[3].set_xticks([0,25,50,75,100])
    axes[3].set_xlabel('Outcome Rate (%)')
    axes[3].set_xlim(left=0,right=100)

    plt.subplots_adjust(wspace=0,top=0.875,bottom=0.15,left=0.1,right=0.95)
    if DO_SAVE:
        plt.savefig(f'figures/{playername1}-{playername2}.png')

def buildColours():
    #create three tones of default style colours
    stock_colours = plt.rcParams["axes.prop_cycle"].by_key()["color"]
    #add extra colours betwen the 7 bases
    interp_colors=list()
    prev_colour=stock_colours[-1]
    for this_colour_index, this_colour in enumerate(stock_colours):
        this_red=int(this_colour[1:3],16)
        this_green=int(this_colour[3:5],16)
        this_blue=int(this_colour[5:7],16)

        prev_red=int(prev_colour[1:3],16)
        prev_green=int(prev_colour[3:5],16)
        prev_blue=int(prev_colour[5:7],16)

        mid_red=int((this_red+prev_red)/2)
        mid_green=int((this_green+prev_green)/2)
        mid_blue=int((this_blue+prev_blue)/2)
        
        interp_colors.append(f'#{mid_red:02x}{mid_green:02x}{mid_blue:02x}')

        prev_colour=this_colour
    
    #to interweave colours use this:
    # full_colours=[sub[item] for item in range(len(stock_colours)) for sub in [interp_colors,stock_colours]]
    #for more contrast between consecutive indices:
    full_colours = stock_colours
    full_colours.extend(interp_colors[1:7])
    full_colours.append(interp_colors[0])

    # print(full_colours)

    faded_colours = list()
    dulled_colours = list()
    for this_colour in full_colours:
        this_red=int(this_colour[1:3],16)
        this_green=int(this_colour[3:5],16)
        this_blue=int(this_colour[5:7],16)

        faded_red=int((this_red+255)/2)
        faded_green=int((this_green+255)/2)
        faded_blue=int((this_blue+255)/2)

        dulled_red=int((this_red+faded_red)/2)
        dulled_green=int((this_green+faded_green)/2)
        dulled_blue=int((this_blue+faded_blue)/2)

        faded_colours.append(f'#{faded_red:02x}{faded_green:02x}{faded_blue:02x}')
        dulled_colours.append(f'#{dulled_red:02x}{dulled_green:02x}{dulled_blue:02x}')
    # print(full_colours, dulled_colours, faded_colours)
    return full_colours, dulled_colours, faded_colours

