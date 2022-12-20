class Anime:
    name = '',
    genre = '',
    season = '',
    on_air = False,
    num_episodes = 0

    def __init__(self, name, genre, season, num_episodes, on_air=True) -> None:
        self.name = name
        self.genre = genre
        self.season = season
        self.num_episodes = num_episodes
        self.on_air = on_air

    def __str__(self) -> str:
        on_air_msg = 'that is currently on air.' if self.on_air else 'currently is not on air any more.'
        message = self.name + ' is an anime from ' + \
            self.season + ' with ' + \
            str(self.num_episodes) + ' episodes from ' + \
            self.genre + ' genre ' + on_air_msg
        return message

class Character:
    name = '',
    genre = '',
    age = 0,
    is_protagonist = True,
    __anime = ''

    def __init__(self,  name,  genre,  age = -1,  is_protagonist = False) -> None:
        self.name = name
        self.genre = genre
        self.age = age
        self.is_protagonist = is_protagonist

    def __str__(self) -> str:
        protagonist = ' is the protagonist of ' if self.is_protagonist else ' is a character from '
        message = self.name + protagonist + 'the anime ' + self.__anime + '.'
        return message
