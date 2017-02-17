"""
Represent a Checker object
"""
class Checker:
    
    def __init__(self, team='X', id=0, is_active=True):
        self.team = team
        self.id = id
        self.is_active = is_active

    def __repr__(self):
        return str(self)

    def __str__(self):
        return str(self.team) + " | " + str(self.id)
