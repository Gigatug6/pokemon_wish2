from typePokemons import EnumTypes

class CategoryAttack:
  Physical = 0,
  Special = 1,
  Statut = 2

class SetAttack:
  def __init__(self, name, typeAttack, category, puissance, precision, pp):
    self.name = name
    self.type = typeAttack
    self.category = category
    self.puissance = puissance
    self.precision = precision
    self.pp = pp

attacks = {
  0: SetAttack("Charge", EnumTypes.Normal, CategoryAttack.Physical, 40, 100, 35),
  1: SetAttack("Pistolet à O", EnumTypes.Eau, CategoryAttack.Special, 40, 100, 25),
  2: SetAttack("Flammèche", EnumTypes.Feu, CategoryAttack.Special, 40, 100, 25),
  3: SetAttack("Fouet Lianes", EnumTypes.Plante, CategoryAttack.Special, 40, 100, 25),
}