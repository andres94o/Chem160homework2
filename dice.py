from random import choices 
ntrials = 10000 #the number of trials that will be done;
player1wins = 0 #this sets player1 with initally zero wins; this keeps count of player1's wins
for i in range(ntrials): #this will go through all the trials
    player1 = choices(range(1, 7), k=2) #player 1 will roll 2 dice, and get a number between 1 and 6
    if player1[0] == player1[1]: #if the first rolled number equals the second rolled number (both by player1), player 1 gets a point
        player1wins = player1wins + 1 #adds one point to player 1
        continue
    player2 = choices(range(1, 7), k=3) #player2 will roll 3 dice, and get a number between 1 and 6
    player2.sort(reverse=True) #this will sort the 3 rolled dice in order from greatest to least
    if player1[0] + player1[1] >= player2[0] + player2[1]: #this will compare player1's rolls with player2's 2 highest rolls
        player1wins += 1 #if player1's rolls are greater than player2's 2 highest rolls, player one gets a point
print("Ratio of player1 wins =", player1wins/ntrials) #this prints the ratio of how many times player1 wins

probability = player1wins/ntrials * 100 # multiplies p(layer1wins/ntrials) by 100
print("Player 1's winning probability is", probability, "percent.") #this prints out the percentage
