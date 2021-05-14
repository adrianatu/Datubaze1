import  adreses
from os import system
sakums = """ Sveicināti!
------------------------------
Lūdzu ,izvēlēties darbību:
1 - pievienot jaunu adrese
2 - atrast adresi
3 - rediģēt adresi
4 - adreses dzēšana
-----------------------------
"""

def adreses_piev():
  personask = input("Lūdzu, ievadiet personas kodu:")
  adrese = input("Lūdzu,ievadiet adresi:")
  
  print(f"Pievienota adrese: {personask} {adrese}")

  adreses.piev_adreses(personask, adrese)




def adreses_red():
  iepr_personask = input("Ievadi personas kodu kuru nepieciešams rediģēt:")
  iepr_adrese = adreses.atrod_adresi(iepr_personask)

  if iepr_adrese:
    jaunais_personask = input(f"Ievadi personas kodu(atstāj tukšu ,ja nevēlies mainīt{iepr_personask})").strip()
    jauna_adrese = input(f"Ievadi kontakta numuru (atstāj tukšu, janevēlies mainīt{iepr_adrese})").strip()
    if not jauna_adrese:
      jauna_adrese = iepr_adrese
    if not jaunais_personask:
      adreses.mainit_adresi
      (iepr_personask, jauna_adrese)
    else:
      adreses.mainit_adresi(iepr_personask, jauna_adrese, jaunais_personask)

  else:
    print(f"Izskatās, ka {iepr_personask} neeksistē")




def adreses_atrasana():
  personask = input("Ievadi personas kodu, kuru meklē:")
  adrese = adreses.atrod_adresi(personask)


  if adreses:
    print(f"{personask} adrese ir {adrese}")
  else:
    sakrit = adreses.adreses_mekl(personask)
    if sakrit:
      for k in sakrit:
        print(f"{k} numurs ir {sakrit[k]}")
    else:
      print(f"Izskatās, ka {personask} nav sarakstā")






def adreses_dzesana():
  personask = input("Ievadi personas kodu, kuru vēlies dzēst: ")
  adrese = adreses.atrod_adresi

  
  if adrese:
    print(f'{personask} tika izdzēsts.')
    adreses.dzest_adresi(personask)
  else:
    print(f'Izskatās,ka adrese {personask}neeksistē')



def galvena_izv():
  print (sakums)
  izvele = input("Tava izvēlēta darbība:").strip()
 


  if izvele == "1":
    adreses_piev()
  elif izvele == "2":
    adreses_atrasana()
  elif izvele == "3":
    adreses_red()
  elif izvele == "4":
    adreses_dzesana()
  else:
    print("Neeksistējoša darbība. Lūdzu mēģiniet vēlre2iz")



while True:
  system("")
  galvena_izv()
  input("Nospied Enter, lai turpinātu:")