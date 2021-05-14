from replit import db

def piev_adreses(personask, adrese):
  if personask in db:
    print("Personas kods jau eksistē")
  else: 
   db[personask] = adrese
   print(f"{personask} adrese ir {adrese}")


def atrod_adresi(personask):
 adrese = db.get(personask)
 return adrese


def adreses_mekl(meklet):
   sakrit_elementi = db.prefix(meklet)
   return {k: db[k] for k in sakrit_elementi}



def mainit_adresi(iepr_personask, jauna_adrese):
  db[iepr_personask] = jauna_adrese


def maint_adresi(iepr_personask, jauna_adrese, jaunais_personask):
  db[jaunais_personask] = jauna_adrese
  del db[iepr_personask]


def dzest_adresi(personask):
  del db[personask]