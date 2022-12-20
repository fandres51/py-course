import file_conections as file_func

# Main menu

def main_menu():
    print('\nHello master, and welcome to the anime encyclopedia!\n')
    print('What do you want to do today?\n')
    print('1) Look for an anime')
    print('2) List all animes')
    print('3) Upload a new anime\n')
    option = input('Type the selected number here: ')
    return option

def search_menu(anime_list):
    option = input('Type the name of the anime you are looking for: ')
    anime = search_anime(anime_list, option)[0]
    return anime

def list_animes(anime_list):
    for anime in anime_list:
        print(anime['name'])
    return 0

def upload_anime_menu(anime_list):
    print('Type the data of the new anime in the following form:\n')
    name = input('Name: ')
    genre = input('Genre: ')
    season = input('Season: ')
    num_ep = int(input('Number of episodes: '))
    on_air = bool(input('On air: '))
    anime_dic = {
        'name':name,
        'genre':genre,
        'season':season,
        'num_episodes':num_ep,
        'on_air':on_air,
        'characters': []
    }
    anime_list.append(anime_dic)
    upload_anime_list(anime_list)
    return 0

#Anime menu

def show_anime_menu(anime):
    print('This is the main menu for ' + anime['name'])
    print('What do you want to do?\n')
    print('1) Anime info')
    print('2) Edit anime info')
    print('3) Delete anime')
    print('4) Characters menu')
    option = input('\nType the selected number here: ')
    return option

def show_anime_data(animes, anime):
    print('')
    print('Name: ' + anime['name'])
    print('Genre: ' + anime['genre'])
    print('Season: ' + anime['season'])
    print('Number of Episodes: ' + str(anime['num_episodes']))
    print('Currently on air: ' + ('Yes' if anime['on_air'] else 'No'))
    print('')
    return 0

def delete_anime(anime_list, anime):
    new_list = []
    for ani in anime_list:
        if(ani['name'] != anime['name']):    
            new_list.append(ani)
    upload_anime_list(new_list)
    return 0

def update_anime(anime_list, anime):

    print('\nType the new data of the anime in the following form:\n')
    name = input('Name: ')
    genre = input('Genre: ')
    season = input('Season: ')
    num_ep = int(input('Number of episodes: '))
    on_air = bool(input('On air: '))
    new_anime = {
        'name':name,
        'genre':genre,
        'season':season,
        'num_episodes':num_ep,
        'on_air':on_air
    }

    new_list = []
    for ani in anime_list:
        if(ani['name'] == anime['name']):    
            new_list.append(new_anime)
        else:
            new_list.append(ani)
    upload_anime_list(new_list)
    return 0

# Characters

def show_characters_menu(anime_list, anime):
    print('\nThis is the menu for the characters of ' + anime['name'])
    print('What do you want to do?\n')
    print('1) List all characters')
    print('2) Create new character')
    print('3) Look for a character')
    # print('4) Return')
    option = input('\nType the selected number here: ')
    return option

def list_characters(anime_list, anime):
    print('')
    for char in anime['characters']:
        print(char['name'])
    print('')
    return 0

def create_character(animes, anime):
    print('Type the data of the new character in the following form:\n')
    name = input('Name: ')
    genre = input('Genre: ')
    age = int(input('Age: '))
    is_p = True if (input('Is the main protagonist?: ')) == 'True' else False
    character_dic = {
        'name':name,
        'genre':genre,
        'age':age,
        'is_protagonist':is_p,
        'anime': anime['name']
    }
    list = add_character(character_dic, anime['name'], animes)
    upload_anime_list(list)
    return 0

def search_char_menu(animes, anime):
    opc_char = input('\nWrite the name of the character you are looking for: ')
    char = search_anime(anime['characters'], opc_char)[0]
    return char

# Character Specific functions

def show_char_speci_menu(character):
    print('\nThis is the menu for ' + character['name'])
    print('What do you want to do?\n')
    print('1) List info')
    print('2) Update info')
    print('3) Delete character')
    # print('4) Return')
    option = input('\nType the selected number here: ')
    return option

def list_char_data(anim_list, anime, character):
    print('')
    print('Name: ' + character['name'])
    print('Genre: ' + character['genre'])
    print('Age: ' + str(character['age']))
    print('Is the main protagonist?: ' + ('Yes' if character['is_protagonist'] else 'No'))
    print('')
    return 0

def delete_char(anim_list, anime, character):
    for ani in anim_list:
        if(ani['name'] == anime['name']):
            ani = delete_char_in_anime(ani, character)
            break
    upload_anime_list(anim_list)

def update_char(anim_list, anime, character):
    print('\nType the new data for the character in the following form:\n')
    name = input('Name: ')
    genre = input('Genre: ')
    age = int(input('Age: '))
    is_protagonist = True if (input('Is the main protagonist?: ')) == 'True' else False
    new_character = {
        'name':name,
        'genre':genre,
        'age': age,
        'is_protagonist': is_protagonist,
        'anime': anime['name']
    }
    new_list = []
    for ani in anim_list:
        if(ani['name'] == anime['name']):
            new_list.append(update_char_in_anime(ani, new_character, character))
        else:
            new_list.append(ani)
    upload_anime_list(new_list)
    # print(anim_list)
# Other functions

def search_anime(anime_list, search_word=''):
    searched = []
    for anime in anime_list:
        if search_word.upper() in anime['name'].upper():
            searched.append(anime)
    return searched

def upload_anime_list(anime_list):
    anime_dic = {
        'animes':anime_list
    }
    file_func.write_anime_file(anime_dic)

def add_character(character, anime_name, animes):
    for ani in animes:
        if(ani['name'] == anime_name):
            ani['characters'].append(character)
            break
    return animes
    
def delete_char_in_anime(anime, char):
    new_list = []
    for ch in anime['characters']:
        if(ch['name'] != char['name']):
            new_list.append(ch)
    anime['characters'] = new_list
    return anime

def update_char_in_anime(anime, new_char, old_char):
    new_list = []
    for char in anime['characters']:
        if(old_char['name'] == char['name']):
            new_list.append(new_char)
        else:
            new_list.append(char)
    anime['characters'] = new_list
    return anime


