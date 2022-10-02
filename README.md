# Chess-GM-ELO-Bin-Analysis
 Tools to acquire, create, and display historical performance of chess GMs.

This project the following phases:
1. Acquire data from the Chess.com game database.
2. Parse data files to extract specifics of each game.
3. Compile individual game data into ELO-based bins and create figures.

# Acquire data from the Chess.com game database. 
Requires: selenium and chromium driver (or can be done manually)
1. Navigate to https://www.chess.com/games/search?opening=&openingId=&p1=&p2=&sort=
2. Enter name of GM for Player 1 and click Search.
3. Examine URL to extract chess.com name of player.
-ex: Magnus+Carlsen from https://www.chess.com/games/search?opening=&openingId=&p1=Magnus+Carlsen&p2=&sort= 
4. Copy extracted player string to downloadAutomator.py under player section (or use a player already listed).
5. Select the number of pages to query (original value is 50 pages of 25 games).
6. Run downloadAutomator.py.
7. Cut downloaded files (master_games (xx).pgn) from downloads folder to [PROJECT DIRECTORY]/raw data/[GM NAME]/
-[GM NAME] should be their last name only as this string is searched for to determine if the GM was playing as white or black in each game.
8. Repeat this step for all GMs being analyzed.
9. Proceed to next step.


# Parse data files to extract specifics of each game.
1. Open extractResults.py 
2. Add [GM NAME] to the list of gms to parse their data.
3. Run extractResults.py
4. Proceed to next step.

# Compile individual game data into ELO-based bins and create figures
1. Open main.py
2. Add [GM NAME], rank, and ELO to the list for all players to analyze.
3. Copy a new lines for each additional GM to analyze.
4. Add new lines to the list of binGM for each new GM, to plotGMBins for each new GM for which you want a plot generated, and a new line to plot2GMbins for each pair of GMs that you want compared side by side.
5. Run main.py.
6. Figures will be saved to the following directory: [PROJECT DIRECTORY]/figures/
*Individual plots are saved as [GM NAME].png.
*Comparison plots are saved as [GM1 NAME]-[GM2 NAME].png


# Reference URLs:
https://www.chess.com/ratings
https://www.chess.com/games/search?opening=&openingId=&p1=&p2=&sort=


