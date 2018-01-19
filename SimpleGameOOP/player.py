class Player(object):

    def __init__(self, name):
        self.name = name
        self._lives = 3
        self._level = 1
        self._score = 0

    def _get_lives(self):
        return self._lives

    def _set_lives(self, lives):
        if lives >= 0:
            self._lives = lives
        else:
            print("Lives cannot be negative")
            self._lives = 0

    def _get_level(self):
        return self._level

    def _set_level(self, level):
        if level >= 1:
            self._level = level
            self._score = 1000*(level-1)
        else:
            print("Level cannot be lower than ")
            self._level = 1
            self._score = 0

# ------- decorator - other style of making getters and setters
    @property
    def score(self):
        return self._score

    @score.setter
    def score(self, score):
        self._score = score

    lives = property(_get_lives, _set_lives)
    level = property(_get_level, _set_level)

    def __str__(self):
        return "Name: {0.name}, lives: {0.lives}, level: {0.level}, score {0.score}".format(self)
