class Warrior:

    RANKS = ['Pushover', 'Novice', 'Fighter', 'Warrior', 'Veteran', 'Sage', 'Elite', 'Conqueror', 'Champion', 'Master',
             'Greatest']
    max_experience = 10000

    def __init__(self):
        self._exp = 100
        self.achievements = []

    @property
    def experience(self):
        return self._exp

    @property
    def level(self):
        return int(self._exp/100)

    @property
    def rank(self):
        return self.RANKS[self.level // 10]

    def battle(self, enemy):
        diff = enemy - self.level
        if self.level > 100 or self.level < 1:
            return 'Invalid level'
        else:
            if enemy == self.level:
                self.add_experience(experience=10)
                return 'A good fight'
            elif self.level - enemy == 1:
                self.add_experience(experience=5)
                return 'A good fight'
            elif self.level - enemy >= 2:
                return 'Easy fight'
            elif enemy - self.level >= 5 and enemy // 10 != self.level // 10:
                return 'You\'ve been defeated'
            else:
                self.add_experience(experience=(20 * diff * diff))
                return 'An intense fight'

    def training(self, arr):
        name, count_experience, min_level_train = arr
        if self.level >= min_level_train:
            self.achievements.append(name)
            self.add_experience(experience=count_experience)
            return name
        else:
            return "Not strong enough"

    def add_experience(self, experience):
        current_exp = self.experience + experience
        if current_exp > self.max_experience:
            current_exp = self.max_experience

        self._exp = current_exp


if __name__ == '__main__':
    bruce_lee = Warrior()
    print(bruce_lee.level)
    print(bruce_lee.experience)
    print(bruce_lee.rank)
    print(bruce_lee.achievements)
    print(bruce_lee.training(["Defeated Chuck Norris", 9000, 1]))
    print(bruce_lee.experience)
    print(bruce_lee.level)
    print(bruce_lee.rank)
    bruce_lee.battle(90)
    print(bruce_lee.experience)
    print(bruce_lee.achievements)