

class Avtomobil:
    def __init__(self, marka: str,vypusk: int):
        self.marka = marka
        self.vypusk = vypusk

class SportivnyAvtomobil(Avtomobil):
    def __init__(self, marka: str, vypusk: int, maxSkorost: int):
        super().__init__(marka, vypusk)
        self.maxSkorost = maxSkorost

mashina = SportivnyAvtomobil("Mers", 2022, 340)

print(f"Марка: {mashina.marka}")
print(f"Год выпуска: {mashina.vypusk}")
print(f"Максимальная скорость: {mashina.maxSkorost} км/ч")
