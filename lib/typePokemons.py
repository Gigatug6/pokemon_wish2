class EnumTypes:
  Acier = 0
  Combat = 1
  Dragon = 2
  Eau = 3
  Electrik = 4
  Fee = 5
  Feu = 6
  Glace = 7
  Insect = 8
  Normal = 9
  Plante = 10
  Poison = 11
  Psy = 12
  Roche = 13
  Sol = 14
  Spectre = 15
  Tenebre = 16
  Vol = 17

class SetType:
  def __init__(self, name:str, defense:list[int], attack:list[int]):
    self.name = name
    self.defense = defense
    self.attack = attack


listTypes:dict[int, SetType] = {
  EnumTypes.Acier: SetType('Acier', [1/2, 2, 1/2, 1, 1, 1/2, 2, 1/2, 1/2, 1/2, 1/2, 0, 1/2, 1/2, 2, 1, 1, 1/2], [1/2, 1, 1, 1/2, 1/2, 2, 1/2, 2, 1, 1, 1, 1, 1, 2, 1, 1, 1, 1]),
  EnumTypes.Combat: SetType('Combat', [1, 1, 1, 1, 1, 2, 1, 1, 1/2, 1, 1, 1, 2, 1/2, 1, 1, 1/2, 2], [2, 1, 1, 1, 1, 1/2, 1, 2, 1/2, 2, 1, 1/2, 1/2, 2, 1, 0, 2, 1/2]),
  EnumTypes.Dragon: SetType('Dragon', [1, 1, 2, 1/2, 1/2, 2, 1/2, 2, 1, 1, 1/2, 1, 1, 1, 1, 1, 1, 1], [1/2, 1, 2, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1])
}
