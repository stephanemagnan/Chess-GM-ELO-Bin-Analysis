import numpy as np
import pandas as pd

class binGM:
    def __init__(self, playername,elo_min,elo_max,elo_step ):
        bins=np.arange(elo_min,elo_max+1,elo_step)

        df_games=pd.read_csv(f'extracted/{playername}.txt', sep='\t', header=0, dtype={'White': 'string','White ELO': 'int','Black': 'string','Black ELO': 'int','Result': 'string','Date': 'string'})
        #split into different data frames for easier handling

        #only use games that have a listed ELO
        df_games=df_games[df_games['White ELO']!=0]

        white_inds=df_games['White'].str.startswith(f'{playername}')
        black_inds=df_games['Black'].str.startswith(f'{playername}')

        #add ELO vs opponent
        df_games.insert(loc=6,column='White ELO Adv',value=(df_games.loc[:,('White ELO')]-df_games.loc[:,('Black ELO')]))

        # #add outcome column for result parsing
        df_games.insert(loc=7,column='White Outcome',value='')

        #parse outcome column and change to Win/Tie/Loss
        df_games.loc[df_games['Result']=='1/2-1/2','White Outcome']='Tie'
        df_games.loc[(df_games['Result']=='1-0') & (white_inds),'White Outcome']='Win'
        df_games.loc[(df_games['Result']=='0-1') & (white_inds),'White Outcome']='Loss'
        df_games.loc[(df_games['Result']=='1-0') & (black_inds),'White Outcome']='Loss'
        df_games.loc[(df_games['Result']=='0-1') & (black_inds),'White Outcome']='Win'

        
        # Create the pandas DataFrame with column name is provided explicitly
        df_bins = pd.DataFrame(np.zeros((bins.shape[0],15)), columns=['White ELO Adv','White Wins','White Ties','White Losses','White Count','White Win %','White Tie %','White Loss %','Black Wins','Black Ties','Black Losses','Black Count','Black Win %','Black Tie %','Black Loss %'])
        df_bins['White ELO Adv']=bins.transpose()

        #Tabulate bin counts
        for this_index,this_elo in df_bins.iterrows():
            df_bins.loc[this_index,'White Wins']=df_games[(df_games['White Outcome']=='Win') & (white_inds) & (df_games['White ELO Adv']>=this_elo['White ELO Adv']-elo_step/2) & (df_games['White ELO Adv']<this_elo['White ELO Adv']+elo_step/2)].shape[0]
            df_bins.loc[this_index,'White Ties']=df_games[(df_games['White Outcome']=='Tie') & (white_inds) & (df_games['White ELO Adv']>=this_elo['White ELO Adv']-elo_step/2) & (df_games['White ELO Adv']<this_elo['White ELO Adv']+elo_step/2) ].shape[0]
            df_bins.loc[this_index,'White Losses']=df_games[(df_games['White Outcome']=='Loss') & (white_inds) & (df_games['White ELO Adv']>=this_elo['White ELO Adv']-elo_step/2) & (df_games['White ELO Adv']<this_elo['White ELO Adv']+elo_step/2) ].shape[0]
            df_bins.loc[this_index,'Black Wins']=df_games[(df_games['White Outcome']=='Loss') & (black_inds) & (-df_games['White ELO Adv']>=this_elo['White ELO Adv']-elo_step/2) & (-df_games['White ELO Adv']<this_elo['White ELO Adv']+elo_step/2) ].shape[0]
            df_bins.loc[this_index,'Black Ties']=df_games[(df_games['White Outcome']=='Tie') & (black_inds) & (-df_games['White ELO Adv']>=this_elo['White ELO Adv']-elo_step/2) & (-df_games['White ELO Adv']<this_elo['White ELO Adv']+elo_step/2) ].shape[0]
            df_bins.loc[this_index,'Black Losses']=df_games[(df_games['White Outcome']=='Win') & (black_inds) & (-df_games['White ELO Adv']>=this_elo['White ELO Adv']-elo_step/2) & (-df_games['White ELO Adv']<this_elo['White ELO Adv']+elo_step/2) ].shape[0]

        #Add count columnt
        df_bins['White Count']=df_bins['White Wins']+df_bins['White Ties']+df_bins['White Losses']
        df_bins['Black Count']=df_bins['Black Wins']+df_bins['Black Ties']+df_bins['Black Losses']

        #Compute % performance columns
        df_bins.loc[df_bins['White Count']>0,'White Win %']=df_bins.loc[df_bins['White Count']>0]['White Wins']/df_bins.loc[df_bins['White Count']>0]['White Count']*100
        df_bins.loc[df_bins['White Count']>0,'White Tie %']=df_bins.loc[df_bins['White Count']>0]['White Ties']/df_bins.loc[df_bins['White Count']>0]['White Count']*100
        df_bins.loc[df_bins['White Count']>0,'White Loss %']=df_bins.loc[df_bins['White Count']>0]['White Losses']/df_bins.loc[df_bins['White Count']>0]['White Count']*100
        df_bins.loc[df_bins['Black Count']>0,'Black Win %']=df_bins.loc[df_bins['Black Count']>0]['Black Wins']/df_bins.loc[df_bins['Black Count']>0]['Black Count']*100
        df_bins.loc[df_bins['Black Count']>0,'Black Tie %']=df_bins.loc[df_bins['Black Count']>0]['Black Ties']/df_bins.loc[df_bins['Black Count']>0]['Black Count']*100
        df_bins.loc[df_bins['Black Count']>0,'Black Loss %']=df_bins.loc[df_bins['Black Count']>0]['Black Losses']/df_bins.loc[df_bins['Black Count']>0]['Black Count']*100

        self.bins=df_bins
        
        # print(df_games)
        # print(self.bins)