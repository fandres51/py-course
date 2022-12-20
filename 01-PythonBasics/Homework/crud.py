from classes import Anime
from classes import Character
import functions as func
import file_conections as file_func

animes_dic = file_func.read_anime_file() # Loads data from file
animes = animes_dic['animes']
menu_options = {
    '1': func.search_menu,
    '2': func.list_animes,
    '3': func.upload_anime_menu
}

anime_options = {
    '1': func.show_anime_data,
    '2': func.update_anime,
    '3': func.delete_anime,
    '4': func.show_characters_menu
}

anime_char_options = {
    '1': func.list_characters,
    '2': func.create_character,
    '3': func.search_char_menu
}

char_options = {
    '1': func.list_char_data,
    '2': func.update_char,
    '3': func.delete_char
}

option = func.main_menu() # Load main menu
print('')
choosed_anime = menu_options[option](animes)
print('')

if(choosed_anime):
    ani_option = func.show_anime_menu(choosed_anime)
    opc_char = anime_options[ani_option](animes, choosed_anime)
    if(opc_char):
        selected_char = anime_char_options[opc_char](animes, choosed_anime)
        if(selected_char):
            char_option = func.show_char_speci_menu(selected_char)
            char_options[char_option](animes, choosed_anime, selected_char)
