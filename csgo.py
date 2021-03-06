import random
from itertools import combinations
class Player:
    def __init__(self, name, surname, age):
        self.name = name
        self.surname = surname
        self.age = age


class Team:
    def __init__(self, name):
        self.team_name = name
        self.team_players = []
        self.team_score = 0

    def add_player(self, player_to_add):
        self.team_players.append(player_to_add)

    def add_players(self, players):
        self.team_players.extend(players)

    def __repr__(self):
        return self.team_name


class Match:
    def __init__(self,team_1, team_2, map):
        self.team1 = team_1
        self.team2 = team_2
        self.map = map
        self.score = {self.team1:0, self.team2:0}

    def add_point(self):
        self.teams = [self.team1,self.team2]
        self.team_choice = random.choice(self.teams)
        self.score[self.team_choice]+=1

    def __str__(self):
        return f"Drużyna {self.team1} zagrała z drużyna {self.team2}, mecz skończył się wynikiem: {self.score} na mapie {self.map}"


class Map:
    def __init__(self, name):
        self.map_name = name

    def __repr__(self):
        return self.map_name

def most_frequently_appearing_map(list_of_maps):
    most_freq = max(list_of_maps, key=list_of_maps.get)
    all_values = list_of_maps.values()
    highest_value = max(all_values)
    return most_freq,highest_value

def main():
    # TeamLiquid
    elige = Player("Jonathan", "Jablonowski", 26)
    naf = Player("Keith", "Markovic", 27)
    stewie2k = Player("Jake", "Yip", 30)
    grim = Player("Michael", "Wince", 26)
    fallen = Player("Gabriel", "Toledo", 26)
    # TeamVirtusPro
    buster = Player("Timur", "Tulepov", 25)
    qikert = Player("Alexey", "Golubev", 29)
    jame = Player("Dzhami", "Ali", 25)
    sanji = Player("Sanjar", "Kuliev", 26)
    yekindar = Player("Mareks", "Galinskis", 32)
    # TeamAstralis
    dupreeh = Player("Peter", "Rothmann", 28)
    xyp9x = Player("Andreas", "Hojsleth", 25)
    gla1ve = Player("Lukas", "Rossander", 29)
    magisk = Player("Emil", "Reif", 30)
    zonic = Player("Danny", "Sorensen", 36)
    # TeamIzakoBoors
    stomp = Player("Daniel", "Plominski", 27)
    byali = Player("Pawel", "Bielinski", 27)
    vegi = Player("Arek", "Nawojski", 29)
    repo = Player("Karol", "Cybulski", 25)
    suonko = Player("Kamil", "Wegrzynkiewicz", 30)

    team_liquid = Team("Team Liquid")
    team_virtus_pro = Team("Team Virtus Pro")
    team_astralis = Team("Team Astralis")
    team_izako_boors = Team("Team Izako Boors")

    team_liquid.add_players([elige, naf, stewie2k, grim, fallen])
    team_virtus_pro.add_players([buster, qikert, jame, sanji, yekindar])
    team_astralis.add_players([dupreeh, xyp9x, gla1ve, magisk, zonic])
    team_izako_boors.add_players([stomp, byali, vegi, repo, suonko])

    teams = [team_liquid,team_virtus_pro,team_astralis,team_izako_boors]

    mirage = Map("Mirage")
    cache = Map("Cache")
    inferno = Map("Inferno")
    de_dust2 = Map("De_dust 2")

    maps = [mirage,cache,inferno,de_dust2]
    team_scores = {team_liquid:0 ,team_virtus_pro:0 ,team_astralis:0 ,team_izako_boors:0}
    frequence_maps = {mirage:0,cache:0,inferno:0,de_dust2:0}
    for team, team_2 in list(combinations(teams, 2)):
        map_chosen = random.choice(maps)
        frequence_maps[map_chosen]+=1
        csgo_match = Match(team,team_2,map_chosen)
        for i in range(30):
            csgo_match.add_point()
            if csgo_match.score[team] == 16:
                team_scores[team] += 3
                print(csgo_match.__str__())
                break
            elif csgo_match.score[team_2] == 16:
                team_scores[team] += 3
                print(str(csgo_match))
                break
            elif (csgo_match.score[team_2] == 15 and csgo_match.score[team] == 15):
                print(str(csgo_match))
                break
    print(team_scores)
    print(most_frequently_appearing_map(frequence_maps))
main()
