class Vault:
    def __init__(self, galleons=0, sickels=0, knuts=0):
        self.galleons = galleons
        self.sickles = sickels
        self.knuts = knuts

    def __str__(self):
        return f"{self.galleons} galleons, {self.sickles} sickles, {self.knuts} knuts."
    
    def __add__(self, other):
        galleons = self.galleons + other.galleons
        sickles = self.sickles + other.sickles
        knuts = self.knuts + other.knuts
        return Vault(galleons, sickles, knuts)

potter = Vault(100, 25, 50)
print(potter)

ron = Vault(35, 15, 100)
print(ron)

## Overload operator
total = potter + ron
print(total)