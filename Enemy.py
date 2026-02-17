class Enemy:
    
    def __init__(self, name, hp, die, prize):
        self.name = name
        self.hp = int(hp)
        self.die = die
        self.prize = int(prize)

    @property
    def hp(self):
        return self._hp

    @hp.setter
    def hp(self, hp):
        self._hp = int(hp)

    @property
    def die(self):
        return self._die
    
    @die.setter
    def die(self, die):
        self._die = die

    @property
    def prize(self):
        return self._prize

    @prize.setter
    def prize(self, prize):
        self._prize = int(prize)

    def take_damage(self, damage):
        self.hp -= damage

    def heal(self, heal):
        self.hp += heal