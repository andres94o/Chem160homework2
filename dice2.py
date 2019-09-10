from random import choices
ntrials = 10000 # this is the number of trials (dice) that will be rolled
player1wins = 0 #this will keep count of player1's wins
for i in range(ntrials): #this will go through all the trials, one by one
    player1 = choices(range(1, 7), k=2) #this line sets how many dice (k=2) player1 will roll, and the range of values that will be chosen are 1 to 6
    if player1[0] == player1[1]: #if player1's first rolls equals the second roll, enter the for loop
        player1wins += 1 #this adds a point to the variable player1 if the if loop checks out
        continue
    player2 = choices(range(1, 7), k=3) #this sets how many dice player2 will roll (3) and the range of values that can be chosen
    player2.sort(reverse=True) #this sets the dice rolled by player 2 in order from greatest to least
    if player1[0] + player1[1] >= player2[0] + player2[1]: #this compares player1's rolls with player2's two highest rolls
        player1wins += 1 #if player1's rolls are greater than player2, player1 gets a point
        continue
    if (player2[0] and player2[1] == 2) or (player2[0] and player2[2] == 2) or (player2[1] and player2[2] == 2): #this checks to see if player2 rolls 2 # 2's
        player1wins += 1 #if player 2 does roll 2 # 2's, this line gives player1 a point
print("Ratio of player1wins =", player1wins/ntrials)

probability = player1wins/ntrials * 100
print("Player 1's winning probability is", probability, "percent. The percentage of winning for player 1 increases with this new rule added, that states player 1 wins if player 2 rolls two # 2's.")

#completed using original version of homework
