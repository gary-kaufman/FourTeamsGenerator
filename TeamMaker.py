import random
import math

#get number of players
def get_num_of_players():
    num_of_players = input("\nHow many players are there?   ")
    num_of_players = int(num_of_players)
    return (num_of_players)

#create random number list length of number of players
def get_random_list(num_of_players):
    my_list = list(range(1,(num_of_players+1)))
    random.shuffle(my_list)
    return(my_list)

#get number of teams
def get_number_of_teams():
    number_of_teams = input("\nHow many teams are there?    ")
    return(number_of_teams)

#form and display teams
def create_teams(random_list, number_of_teams):
    players_per_team = math.floor((len(random_list)/int(number_of_teams)))
    player_remainder = (len(random_list)%int(number_of_teams))
    player_list = random_list
    print(number_of_teams)
    print("\nFor {} players the teams will be... \n".format(len(random_list)))

    for team in range(int(number_of_teams)):
        team_list = []
        for x in range(players_per_team):
            team_list.insert(0,player_list.pop())
        if player_remainder > 0:
            team_list.insert(0,player_list.pop())
            player_remainder -= 1
        print("Team = {}".format(team_list))
        
###  MAIN METHOD
while True:
    teams = create_teams(get_random_list(get_num_of_players()),get_number_of_teams())