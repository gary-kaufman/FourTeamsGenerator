import random
import math
#get number of players
def get_num_of_players():
    num_of_players = input("How many players are there?  ")
    num_of_players = int(num_of_players)
    return (num_of_players)

#create random number list length of number of players
def get_random_list(num_of_players):
    my_list = list(range(1,(num_of_players+1)))
    random.shuffle(my_list)
    return(my_list)


#divide number of players by 4 and create teams

def create_teams(random_list):
    players_per_team = math.floor((len(random_list)/4))
    player_remainder = (len(random_list)%4)
    player_list = random_list
    print("\nFor {} players the teams will be... \n".format(len(random_list)))
#form and display teams


    team_one = []
    for x in range(players_per_team):
        team_one.insert(0,player_list.pop())
    if player_remainder > 0:
        team_one.insert(0,player_list.pop())
        player_remainder -= 1
    print("Team one will be, " + str(team_one) + "\n")

    team_two = []
    for x in range(players_per_team):
        team_two.insert(0,player_list.pop())
    if player_remainder > 0:
        team_two.insert(0,player_list.pop())
        player_remainder -= 1
    print("Team two will be, " + str(team_two) + "\n")

    team_three = []
    for x in range(players_per_team):
        team_three.insert(0,player_list.pop())
    if player_remainder > 0:
        team_three.insert(0,player_list.pop())
        player_remainder -= 1
    print("Team three will be, " + str(team_three) + "\n")

    team_four = []
    for x in range(players_per_team):
        team_four.insert(0,player_list.pop())
    if player_remainder > 0:
        team_four.insert(0,player_list.pop())
        player_remainder -= 1
    print("Team four will be, " + str(team_four) + "\n")

###  MAIN METHOD
while True:
    teams = create_teams(get_random_list(get_num_of_players()))