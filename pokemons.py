from typePokemons import EnumTypes
from attacks import attacks, SetAttack

class SetPokemon:
  def __init__(self, name:str, hp:int, attack:int, defense:int, specAttack:int, specDefense:int, speed:int, types:list[EnumTypes], xp:int, ptsXp:int, maxXP:int, attacksPokemon:list[SetAttack]):
    self.name = name #nom
    self.hp = hp #iv pv
    self.attack = attack #iv attack
    self.defense = defense #iv defense
    self.specAttack = specAttack #iv spé attaque
    self.specDefense = specDefense #iv spé defense
    self.speed = speed  #iv speed
    self.types = types #type list[EnumTypes]
    self.xp = xp  #xp actuell du pokemon
    self.life = 10 #cacluler les pv en fonction des iv / lvl, pv du actuel pokemon
    #self.capXp = capXp #cap xp pour cacluler les niveau //1029.495
    self.ptsXp = ptsXp #xp donner 
    self.maxXp = maxXP  #xp lvl 100
    self.attacks = attacksPokemon #attaque list[setAttack]

    """
    calculer xp pour le lvl suivant : N = (N^3) * 5
    calculer le lvl : Niveau (N) = Racine carrée (XP / 5)
    """

pokemons = {
  1: SetPokemon("Bulbizarre", 3, 3, 3, 4, 4, 3, 1, 65, 1059860, [EnumTypes.Plante, EnumTypes.Poison], [attacks[0], attacks[3]]),
  4: SetPokemon("Salamèche", 3, 4, 3, 4, 3, 4, 1, 65, 1059860, [EnumTypes.Feu], [attacks[0], attacks[2
  ]]),
  7: SetPokemon("Carapuce", 3, 3, 4, 3, 4, 3, 1, 65, 1059860, [EnumTypes.Feu], [attacks[0], attacks[1]]),
}

