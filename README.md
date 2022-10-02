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
   - ex: Magnus+Carlsen from https://www.chess.com/games/search?opening=&openingId=&p1=Magnus+Carlsen&p2=&sort= 
4. Copy extracted player string to [downloadAutomator.py](/downloadAutomator.py) under player section (or use a player already listed).
5. Select the number of pages to query (original value is 50 pages of 25 games).
6. Run [downloadAutomator.py](/downloadAutomator.py).
7. Cut downloaded files (master_games (xx).pgn) from downloads folder to [[PROJECT DIRECTORY]/raw data/[GM NAME]/](/raw%20data/Carlsen/)
   - [GM NAME] should be their last name only as this string is searched for to determine if the GM was playing as white or black in each game.
8. Repeat this step for all GMs being analyzed.
9. Proceed to next step.


# Parse data files to extract specifics of each game.
1. Open [extractResults.py](/extractResults.py) 
2. Add [GM NAME] to the list of gms to parse their data.
3. Run [extractResults.py](/extractResults.py)
4. Proceed to next step.


# Compile individual game data into ELO-based bins and create figures
1. Open [main.py](/main.py)
2. Add [GM NAME], rank, and ELO to the list for all players to analyze.
3. Copy a new lines for each additional GM to analyze.
4. Add new lines to the list of binGM for each new GM, to plotGMBins for each new GM for which you want a plot generated, and a new line to plot2GMbins for each pair of GMs that you want compared side by side.
5. Run [main.py](/main.py).
6. Figures will be saved to the following directory: [[PROJECT DIRECTORY]/figures/](/figures/)
   - Individual plots are saved as [GM RANK]. [GM NAME].png.
   - Comparison plots are saved as [GM1 NAME]-[GM2 NAME].png
   
Colour options for the plots
- ![#E24A33](https://via.placeholder.com/15/E24A33/E24A33.png) `Index 0: #f03c15`
- ![#348ABD](https://via.placeholder.com/15/348ABD/348ABD.png) `Index 1: #c5f015`
- ![#988ED5](https://via.placeholder.com/15/988ED5/988ED5.png) `Index 2: #1589F0`
- ![#777777](https://via.placeholder.com/15/777777/777777.png) `Index 3: #f03c15`
- ![#FBC15E](https://via.placeholder.com/15/FBC15E/FBC15E.png) `Index 4: #c5f015`
- ![#8EBA42](https://via.placeholder.com/15/8EBA42/8EBA42.png) `Index 5: #1589F0`
- ![#FFB5B8](https://via.placeholder.com/15/FFB5B8/FFB5B8.png) `Index 6: #f03c15`
- ![#8b6a78](https://via.placeholder.com/15/8b6a78/8b6a78.png) `Index 7: #c5f015`
- ![#668cc9](https://via.placeholder.com/15/668cc9/668cc9.png) `Index 8: #1589F0`
- ![#8782a6](https://via.placeholder.com/15/8782a6/8782a6.png) `Index 9: #f03c15`
- ![#b99c6a](https://via.placeholder.com/15/b99c6a/b99c6a.png) `Index 10: #c5f015`
- ![#c4bd50](https://via.placeholder.com/15/c4bd50/c4bd50.png) `Index 11: #1589F0`
- ![#c6b77d](https://via.placeholder.com/15/c6b77d/c6b77d.png) `Index 12: #f03c15`
- ![#f07f75](https://via.placeholder.com/15/f07f75/f07f75.png) `Index 13: #c5f015`


# Example plots
## Individual GM Plot
![Carlsen](/figures/1.%20Carlsen.png)
![Niemann](/figures/43.%20Niemann.png)
## GM Comparison Plot
![Carlsen-Niemann](/figures/Carlsen-Niemann.png)


# Reference URLs:
- https://www.chess.com/ratings
- https://www.chess.com/games/search?opening=&openingId=&p1=&p2=&sort=


