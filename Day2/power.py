import re

def createGameDict():
    file = open('input.txt', 'r')
    Lines = file.readlines()

    games_list = []

    for game in Lines:
        id = game[5:game.index(':')]
        indiv_games = game[8:].split(';')
        temp_games_list = []
        for indiv in indiv_games:
            temp_games_dict = {}
            blue_total = sum(map(int, re.findall(r"(\d+)(?=\s*blue)",indiv)))
            red_total = sum(map(int, re.findall(r"(\d+)(?=\s*red)",indiv)))
            green_total = sum(map(int, re.findall(r"(\d+)(?=\s*green)",indiv)))
            temp_games_dict = {
                "Blues": blue_total,
                "Reds": red_total,
                "Greens": green_total
            }
            temp_games_list.append(temp_games_dict)
        red = 0
        green = 0
        blue = 0
        for temp in temp_games_list:
            if int(temp['Reds']) > int(red) and int(temp['Reds']) != 0:
                red = int(temp['Reds'])
            if int(temp['Blues']) > int(blue) and int(temp['Blues']) != 0:
                blue = int(temp['Blues'])
            if int(temp['Greens']) > int(green) and int(temp['Greens']) != 0:
                green = int(temp['Greens'])
        games_dict = {
            "ID": id,
            "Blues": blue,
            "Reds": red,
            "Greens": green
        }
        games_list.append(games_dict)

    return games_list

def output_sum(games_list):
    sum = 0

    for item in games_list:
        trip = item["Blues"]*item["Greens"]*item["Reds"]
        sum = sum + trip
    print("The Sum Is " + str(sum))
    
         



if __name__ == "__main__":
  games_list = createGameDict()
  output_sum(games_list)