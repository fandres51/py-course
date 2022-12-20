import ast

def write_anime_file(dictionary):
    try:
        path = './animes.txt'
        open_file = open(path, 'w')
        open_file.write(str(dictionary))
        open_file.close()
    except Exception as e:
        print(f'\nNo se pudo escribir en el archivo\n\nDetalles del error:\n{e}')    

def read_anime_file():
    try:
        path = './animes.txt'
        open_file = open(path) #File
        str_dictionary = open_file.readline()
        # print(str_dictionary)
        anime_dictionary = ast.literal_eval(str_dictionary)
        open_file.close()
        return anime_dictionary
    except Exception as e:
        print(f'\nNo se pudo leer el archivo\n\nDetalles del error:\n{e}')  


# file_ops.write_anime_file({
#     'animes': [
#         {
#             'name':'One Piece',
#             'genre':'Fighting Shounen',
#             'season':'1999-Today',
#             'num_episodes':1076,
#             'on_air':True
#         },
#         {
#             'name':'Dragon Ball',
#             'genre':'Fighting Shounen',
#             'season':'1981-1995',
#             'num_episodes':405,
#             'on_air':False

#         },
#         {
#             'name':'Naruto',
#             'genre':'Fighting Shounen',
#             'season':'2003-2017',
#             'num_episodes':721,
#             'on_air':False
#         }
#     ]
# })