import numpy as np
from os import listdir
import os
from os.path import isfile, join

#### downloadAutomator.py should be run before executing this code #######################
# Raw data for GMs is from the Chess.com game database. Each file is one page of results (25). 
# See downloadAutomator.py for more info
## example: Carlsen (50 pages): https://www.chess.com/games/search?opening=&openingId=&p1=Magnus+Carlsen&p2=&sort=


################### OPTIONS ########################
gms={'Anand','Aronian','Carlsen','Caruana','Ding','Dominguez Perez','Firouzja','Giri','Karjakin','Mamedyarov','Nakamura','Nepomniachtchi','Niemann','Rapport','So','Vachier-Lagrave'}

####################################################

#current working directory
directory = os.getcwd()

for gm in gms:
    #list raw data files
    filedirs = [join(directory,'raw data',gm,filename) for filename in listdir(join(directory,'raw data',gm))]

    #prepare output file
    with open(f'extracted/{gm}.txt', 'w') as outfile:
        #add header to output file
        outfile.write('White\tWhite ELO\tBlack\tBlack ELO\tResult\tDate')
        #parse results file
        for resultsfile in filedirs:
            # print(resultsfile)

            with open(resultsfile, 'r') as this_resultfile:

                last_line='none'
                this_white=''
                this_whiteELO='0'
                this_black=''
                this_blackELO='0'
                this_date=''
                this_result=''

                for line in this_resultfile:
                    this_line=line.strip()

                    if this_line.startswith('[White "'):
                        this_white=this_line.replace('[White "','').split('"')[0]
                    elif this_line.startswith('[WhiteElo "'):
                        this_whiteELO=this_line.replace('[WhiteElo "','').split('"')[0]
                        if this_whiteELO=='?':
                            this_whiteELO='0'
                    elif this_line.startswith('[Black "'):
                        this_black=this_line.replace('[Black "','').split('"')[0]
                    elif this_line.startswith('[BlackElo "'):
                        this_blackELO=this_line.replace('[BlackElo "','').split('"')[0]
                        if this_blackELO=='?':
                            this_blackELO='0'
                    elif this_line.startswith('[Result "'):
                        this_result=this_line.replace('[Result "','').split('"')[0]
                    elif this_line.startswith('[EventDate "') or this_line.startswith('[Date "'):
                        this_date=this_line.replace('[EventDate "','').replace('[Date "','').split('"')[0]
                    else:
                        pass

                    # each result ends with two blank lines (must avoid case where >2 lines)
                    if last_line=='' and this_line=='':
                        if this_white!='':
                            outfile.write(f'\n{this_white}\t{this_whiteELO}\t{this_black}\t{this_blackELO}\t{this_result}\t{this_date}')
                        # reset fields
                        this_white=''
                        this_whiteELO='0'
                        this_black=''
                        this_blackELO='0'
                        this_date=''
                        this_result=''

                    last_line = this_line

                #last result in file does not have dual cr/lf as seperator
                if this_white!='': 
                    outfile.write(f'\n{this_white}\t{this_whiteELO}\t{this_black}\t{this_blackELO}\t{this_result}\t{this_date}')

