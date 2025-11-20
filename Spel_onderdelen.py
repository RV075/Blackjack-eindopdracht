class Kaart(): #hoofdletters (!)
    def __init__ (self, score, symbool, naam):
        self.score = score
        self.symbool = symbool
        self.naam = naam
    def __str__(self):
        return f"{self.symbool} {self.naam} {self.score}"

class Deler():
    def __init__ (self):
        self.hand = []
    
    def bereken_score(self):
        totaal_score = 0
        for kaart in self.hand:
            totaal_score = totaal_score + kaart.score # +=
        return totaal_score

# wat voor Deler moet, moet ook voor Speler

class Speler():
    def __init__ (self):
        self.hand = []
    
    def bereken_score(self):
        totaal_score = 0
        for kaart in self.hand:
            totaal_score  = totaal_score +  kaart.score # +=
        return totaal_score