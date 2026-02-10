class Enemy:
    
    def __init__(self, hp, weapon):
        self.hp = int(hp)
        self.weapon = weapon

    @property
    def hp(self):
        return self._hp

    @hp.setter
    def hp(self, hp):
        self._hp = int(hp)

    @property
    def weapon(self):
        return self._weapon
    
    @weapon.setter
    def weapon(self, weapon):
        self._weapon = weapon

    def take_damage(self, damage):
        self.hp -= damage

    def heal(self, heal):
        self.hp += heal