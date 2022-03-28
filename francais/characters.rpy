init python:
    def relationship_callback(event, interact=True, **kwargs):
        character = kwargs.get("character")

        if character is None:
            return

        character = getattr(store, character)
        relationship_girls = getattr(store, "relationship_girls")

        if character not in relationship_girls:
            relationship_girls.append(character)
            setattr(store, "relationship_girls", relationship_girls)

# Declare characters used by this game. The color argument colorizes the name of the character.
define character.narrator = Character (None, what_outlines=[ (2, "#000") ])
define character.u = Character("[name]", who_color="#53d769", who_outlines=[ (2, "#000") ], what_outlines=[ (2, "#000") ])
define character.ju = Character("Julia", who_color="#fecb2e", who_outlines=[ (2, "#000") ], what_outlines=[ (2, "#000") ])
define character.car = Character("Voiture", who_color="#147efb", who_outlines=[ (2, "#000") ], what_outlines=[ (2, "#000") ])
define character.ca = Character("Cameron", who_color="#147efb", who_outlines=[ (2, "#000") ], what_outlines=[ (2, "#000") ])
define character.ma = Character("Mason", who_color="#fd9426", who_outlines=[ (2, "#000") ], what_outlines=[ (2, "#000") ])
define character.aut = Character("Autumn", who_color="#fc3158", who_outlines=[ (2, "#000") ], what_outlines=[ (2, "#000") ], callback=relationship_callback, cb_character="autumn")
define character.em = Character("Emily", who_color="#fc3d39", who_outlines=[ (2, "#000") ], what_outlines=[ (2, "#000") ], callback=relationship_callback, cb_character="emily")
define character.an = Character("Mme Anderson", who_color="#fecb2e", who_outlines=[ (2, "#000") ], what_outlines=[ (2, "#000") ])
define character.ch = Character("Chris", who_color="#147efb", who_outlines=[ (2, "#000") ], what_outlines=[ (2, "#000") ])
define character.no = Character("Nora", who_color="#fc3158", who_outlines=[ (2, "#000") ], what_outlines=[ (2, "#000") ], callback=relationship_callback, cb_character="nora")
define character.ry = Character("Ryan", who_color="#5fc9f8", who_outlines=[ (2, "#000") ], what_outlines=[ (2, "#000") ])
define character.ro = Character("Mme Rose", who_color="#fc3d39", who_outlines=[ (2, "#000") ], what_outlines=[ (2, "#000") ], callback=relationship_callback, cb_character="ms_rose")
define character.la = Character("Lauren", who_color="#fd9426", who_outlines=[ (2, "#000") ], what_outlines=[ (2, "#000") ], callback=relationship_callback, cb_character="lauren")
define character.ri = Character("Riley", who_color="#fecb2e", who_outlines=[ (2, "#000") ], what_outlines=[ (2, "#000") ], callback=relationship_callback, cb_character="riley")
define character.el = Character("Elijah", who_color="#147efb", who_outlines=[ (2, "#000") ], what_outlines=[ (2, "#000") ])
define character.imre = Character("Imre", who_color="#fecb2e", who_outlines=[ (2, "#000") ], what_outlines=[ (2, "#000") ])
define character.au = Character("Aubrey", who_color="#fc3158", who_outlines=[ (2, "#000") ], what_outlines=[ (2, "#000") ], callback=relationship_callback, cb_character="aubrey")
define character.sam = Character("Sam", who_color="#fecb2e", who_outlines=[ (2, "#000") ], what_outlines=[ (2, "#000") ])
define character.karen = Character("Karen", who_color="#fc3158", who_outlines=[ (2, "#000") ], what_outlines=[ (2, "#000") ])
define character.jo = Character("Josh", who_color="#147efb", who_outlines=[ (2, "#000") ], what_outlines=[ (2, "#000") ])
define character.courtney = Character("Courtney", who_color="#fc3d39", who_outlines=[ (2, "#000") ], what_outlines=[ (2, "#000") ])
define character.jeremy = Character("Jeremy", who_color="#5fc9f8", who_outlines=[ (2, "#000") ], what_outlines=[ (2, "#000") ])
define character.katy = Character("Katy", who_color="#fd9426", who_outlines=[ (2, "#000") ], what_outlines=[ (2, "#000") ])
define character.sarah = Character("Sarah", who_color="#fecb2e", who_outlines=[ (2, "#000") ], what_outlines=[ (2, "#000") ])
define character.gr = Character("Grayson", who_color="#fd9426", who_outlines=[ (2, "#000") ], what_outlines=[ (2, "#000") ])
define character.cl = Character("Chloé", who_color="#fc3158", who_outlines=[ (2, "#000") ], what_outlines=[ (2, "#000") ], callback=relationship_callback, cb_character="chloe")
define character.tom = Character("Tom", who_color="#147efb", who_outlines=[ (2, "#000") ], what_outlines=[ (2, "#000") ])
define character.tut = Character("Tutoriel", who_color="#53d769", who_outlines=[ (2, "#000") ], what_outlines=[ (2, "#000") ])
define character.lee = Character("Mr Lee", who_color="#5fc9f8", who_outlines=[ (2, "#000") ], what_outlines=[ (2, "#000") ])
define character.ben = Character("Benjamin", who_color="#5fc9f8", who_outlines=[ (2, "#000") ], what_outlines=[ (2, "#000") ])
define character.ehr = Character("Dr Ehrmantraut", who_color="#fecb2e", who_outlines=[ (2, "#000") ], what_outlines=[ (2, "#000") ])
define character.pe = Character("Pénélope", who_color="#fd9426", who_outlines=[ (2, "#000") ], what_outlines=[ (2, "#000") ], callback=relationship_callback, cb_character="penelope")
define character.ev = Character("Evelyn", who_color="#fecb2e", who_outlines=[ (2, "#000") ], what_outlines=[ (2, "#000") ])
define character.aa = Character("Aaron", who_color="#fd9426", who_outlines=[ (2, "#000") ], what_outlines=[ (2, "#000") ])
define character.sec = Character("Agent de sécurité", who_color="#fd9426", who_outlines=[ (2, "#000") ], what_outlines=[ (2, "#000") ])
define character.li = Character("Lindsey", who_color="#fc3158", who_outlines=[ (2, "#000") ], what_outlines=[ (2, "#000") ], callback=relationship_callback, cb_character="lindsey")
define character.unknown = Character("Inconnu", who_color="#147efb", who_outlines=[ (2, "#000") ], what_outlines=[ (2, "#000") ])
define character.uber = Character("Chauffeur Uber", who_color="#5fc9f8", who_outlines=[ (2, "#000") ], what_outlines=[ (2, "#000") ])
define character.clerk = Character("Employé", who_color="#5fc9f8", who_outlines=[ (2, "#000") ], what_outlines=[ (2, "#000") ])
define character.am = Character("Amber", who_color="#fc3158", who_outlines=[ (2, "#000") ], what_outlines=[ (2, "#000") ], callback=relationship_callback, cb_character="amber")
define character.ki = Character("Kim", who_color="#fc3d39", who_outlines=[ (2, "#000") ], what_outlines=[ (2, "#000") ])
define character.ad = Character("Adam", who_color="#fecb2e", who_outlines=[ (2, "#000") ], what_outlines=[ (2, "#000") ])
define character.co = Character("Conseillère d'éducation", who_color="#fecb2e", who_outlines=[ (2, "#000") ], what_outlines=[ (2, "#000") ])

# 6.0
define character.waiter = Character("Serveuse", who_color="#5fc9f8", who_outlines=[ (2, "#000") ], what_outlines=[ (2, "#000") ])
define character.host = Character("Host", who_color="#fecb2e", who_outlines=[ (2, "#000") ], what_outlines=[ (2, "#000") ])
define character.poet1 = Character("Lisa", who_color="#fc3158", who_outlines=[ (2, "#000") ], what_outlines=[ (2, "#000") ])
define character.poet2 = Character("Martin", who_color="#fd9426", who_outlines=[ (2, "#000") ], what_outlines=[ (2, "#000") ])
define character.sa = Character("Samantha", who_color="#fecb2e", who_outlines=[ (2, "#000") ], what_outlines=[ (2, "#000") ], callback=relationship_callback, cb_character="samantha")
define character.guya = Character("Peter", who_color="#5fc9f8", who_outlines=[ (2, "#000") ], what_outlines=[ (2, "#000") ])
define character.guyb = Character("Harry", who_color="#fecb2e", who_outlines=[ (2, "#000") ], what_outlines=[ (2, "#000") ])
define character.finn = Character("Finn", who_color="#5fc9f8", who_outlines=[ (2, "#000") ], what_outlines=[ (2, "#000") ])
define character.guyd = Character("Perry", who_color="#fecb2e", who_outlines=[ (2, "#000") ], what_outlines=[ (2, "#000") ])
define character.se = Character("Sebastian", who_color="#147efb", who_outlines=[ (2, "#000") ], what_outlines=[ (2, "#000") ])
define character.guyc = Character("Marcus", who_color="#fecb2e", who_outlines=[ (2, "#000") ], what_outlines=[ (2, "#000") ])
define character.matt = Character("Matt", who_color="#fecb2e", who_outlines=[ (2, "#000") ], what_outlines=[ (2, "#000") ])

# 7.0
define character.cal = Character("Caleb", who_color="#83d81c", who_outlines=[ (2, "#000") ], what_outlines=[ (2, "#000") ]) # Ape pledge
define character.coop = Character("Cooper", who_color="#11af68", who_outlines=[ (2, "#000") ], what_outlines=[ (2, "#000") ]) # Ape pledge
define character.kai = Character("Kai", who_color="#1caedb", who_outlines=[ (2, "#000") ], what_outlines=[ (2, "#000") ]) # Ape pledge
define character.wes = Character("Wesley", who_color="#db6f1c", who_outlines=[ (2, "#000") ], what_outlines=[ (2, "#000") ]) # Ape
define character.par = Character("Parker", who_color="#a815f2", who_outlines=[ (2, "#000") ], what_outlines=[ (2, "#000") ]) # Ape
define character.rg1 = Character("Angelica", who_color="#db6f1c", who_outlines=[ (2, "#000") ], what_outlines=[ (2, "#000") ])
define character.rg2 = Character("Elisa", who_color="#a815f2", who_outlines=[ (2, "#000") ], what_outlines=[ (2, "#000") ])
define character.nerd = Character("Nerd", who_color="#147efb", who_outlines=[ (2, "#000") ], what_outlines=[ (2, "#000") ])
define character.xav = Character("Xavier", who_color="#147efb", who_outlines=[ (2, "#000") ], what_outlines=[ (2, "#000") ])
define character.jax = Character("Jaxon", who_color="#fecb2e", who_outlines=[ (2, "#000") ], what_outlines=[ (2, "#000") ])
define character.teach = Character("Professeur", who_color="#147efb", who_outlines=[ (2, "#000") ], what_outlines=[ (2, "#000") ])
define character.class1 = Character("La classe", who_color="#fecb2e", who_outlines=[ (2, "#000") ], what_outlines=[ (2, "#000") ])

# 8.0
define character.de = Character("Doyenne", who_color="#fc3d39", who_outlines=[ (2, "#000") ], what_outlines=[ (2, "#000") ])
define character.je = Character("Joe", who_color="#53d769", who_outlines=[ (2, "#000") ], what_outlines=[ (2, "#000") ])
define character.ann = Character("Annonce vocale", who_color="#fd9426", who_outlines=[ (2, "#000") ], what_outlines=[ (2, "#000") ])
define character.empl = Character("Guichetier", who_color="#5fc9f8", who_outlines=[ (2, "#000") ], what_outlines=[ (2, "#000") ])

# 9.0
define character.unkfem = Character("Voix féminine", who_color="#fc3158", who_outlines=[ (2, "#000") ], what_outlines=[ (2, "#000") ])

# 10.0
define character.jen = Character("Jenny", who_color="#fc3158", who_outlines=[ (2, "#000") ], what_outlines=[ (2, "#000") ], callback=relationship_callback, cb_character="jenny")
define character.mrr = Character("Mr Rose", who_color="#0055ff", who_outlines=[ (2, "#000") ], what_outlines=[ (2, "#000") ])
define character.be = Character("Ben", who_color="#0055ff", who_outlines=[ (2, "#000") ], what_outlines=[ (2, "#000") ])
define character.jer = Character("Jerry", who_color="#0055ff", who_outlines=[ (2, "#000") ], what_outlines=[ (2, "#000") ])
define character.dg1 = Character("Rachel", who_color="#fc3158", who_outlines=[ (2, "#000") ], what_outlines=[ (2, "#000") ])
define character.dg2 = Character("Eleanor", who_color="#fc3158", who_outlines=[ (2, "#000") ], what_outlines=[ (2, "#000") ])
define character.dg3 = Character("Karen", who_color="#fc3158", who_outlines=[ (2, "#000") ], what_outlines=[ (2, "#000") ])
define character.dg4 = Character("Rebecca", who_color="#fc3158", who_outlines=[ (2, "#000") ], what_outlines=[ (2, "#000") ])

# 11.0
define character.art = Character("Directeur artistique", who_color="#0055ff", who_outlines=[ (2, "#000") ], what_outlines=[ (2, "#000") ])
define character.air = Character("Hôtesse de l'aéroport", who_color="#fecb2e", who_outlines=[ (2, "#000") ], what_outlines=[ (2, "#000") ])
define character.ran = Character("Éleveur", who_color="#fecb2e", who_outlines=[ (2, "#000") ], what_outlines=[ (2, "#000") ])
define character.hor = Character("Cheval", who_color="#a815f2", who_outlines=[ (2, "#000") ], what_outlines=[ (2, "#000") ])
define character.dun = Character("Duncan", who_color="#0055ff", who_outlines=[ (2, "#000") ], what_outlines=[ (2, "#000") ])
define character.bartender = Character("Barman", who_color="#5fc9f8", who_outlines=[ (2, "#000") ], what_outlines=[ (2, "#000") ])
define character.foxy = Character("Foxy", who_color="#fd9426", who_outlines=[ (2, "#000") ], what_outlines=[ (2, "#000") ])
define character.ericka = Character("Ericka", who_color="#fecb2e", who_outlines=[ (2, "#000") ], what_outlines=[ (2, "#000") ])
define character.jane = Character("Jane", who_color="#fc3d39", who_outlines=[ (2, "#000") ], what_outlines=[ (2, "#000") ])
define character.candy = Character("Candy", who_color="#fc3158", who_outlines=[ (2, "#000") ], what_outlines=[ (2, "#000") ])
define character.mana = Character("Gérant du magasin", who_color="#5fc9f8", who_outlines=[ (2, "#000") ], what_outlines=[ (2, "#000") ])
define character.driver = Character("Conducteur", who_color="#5fc9f8", who_outlines=[ (2, "#000") ], what_outlines=[ (2, "#000") ])
define character.sus = Character("Susan", who_color="#fd9426", who_outlines=[ (2, "#000") ], what_outlines=[ (2, "#000") ])
define character.jud = Character("Examinatrice", who_color="#db6f1c", who_outlines=[ (2, "#000") ], what_outlines=[ (2, "#000") ])
define character.charli = Character("Charli", who_color="#0055ff", who_outlines=[ (2, "#000") ], what_outlines=[ (2, "#000") ])
define character.csa = Character("concessionnaire auto", who_color="#0055ff", who_outlines=[ (2, "#000") ], what_outlines=[ (2, "#000") ])
define character.dennis = Character("Dennis", who_color="#0055ff", who_outlines=[ (2, "#000") ], what_outlines=[ (2, "#000") ])
define character.bank = Character("Conseillère bancaire", who_color="#fc3158", who_outlines=[ (2, "#000") ], what_outlines=[ (2, "#000") ])

# 12.0
define character.robber = Character("Robber", who_color="#0055ff", who_outlines=[ (2, "#000") ], what_outlines=[ (2, "#000") ])
define character.fwait = Character("Serveuse française", who_color="#0055ff", who_outlines=[ (2, "#000") ], what_outlines=[ (2, "#000") ])
define character.na = Character("Naomi", who_color="#fc3158", who_outlines=[ (2, "#000") ], what_outlines=[ (2, "#000") ])
define character.pg = Character("Photographe", who_color="#fd9426", who_outlines=[ (2, "#000") ], what_outlines=[ (2, "#000") ])
define character.lmass = Character("Masseuse", who_color="#fc3158", who_outlines=[ (2, "#000") ], what_outlines=[ (2, "#000") ])
define character.mmass = Character("Masseur", who_color="#147efb", who_outlines=[ (2, "#000") ], what_outlines=[ (2, "#000") ])
define character.clady = Character("Femme folle", who_color="#ff8afb", who_outlines=[ (2, "#000") ], what_outlines=[ (2, "#000") ])
define character.escman = Character("Manager", who_color="#5fc9f8", who_outlines=[ (2, "#000") ], what_outlines=[ (2, "#000") ])
define character.bishop = Character("Évêque", who_color="#800080", who_outlines=[ (2, "#000") ], what_outlines=[ (2, "#000") ])
define character.nurse = Character("Infirmière", who_color="#dbfffe", who_outlines=[ (2, "#000") ], what_outlines=[ (2, "#000") ])
define character.barber = Character("Coiffeur", who_color="#fecb2e", who_outlines=[ (2, "#000") ], what_outlines=[ (2, "#000") ])
define character.greeter = Character("Greeter", who_color="#0055ff", who_outlines=[ (2, "#000") ], what_outlines=[ (2, "#000") ])
define character.tattoo = Character("Tatoueur", who_color="#ff1694", who_outlines=[ (2, "#000") ], what_outlines=[ (2, "#000") ])

# 13.0
define character.ary = Character("Aryssa", who_color="#fd9426", who_outlines=[ (2, "#000") ], what_outlines=[ (2, "#000") ])
define character.ash = Character("Ashton", who_color="#fd9426", who_outlines=[ (2, "#000") ], what_outlines=[ (2, "#000") ])
define character.barh = Character("Hôte", who_color="#147efb", who_outlines=[ (2, "#000") ], what_outlines=[ (2, "#000") ])
define character.clipps = Character("Clipps", who_color="#cccccc", who_outlines=[ (2, "#000") ], what_outlines=[ (2, "#000") ])
define character.emmy = Character("Emmy", who_color="#fc3158", who_outlines=[ (2, "#000") ], what_outlines=[ (2, "#000") ])
define character.gary = Character("Gary", who_color="#0055ff", who_outlines=[ (2, "#000") ], what_outlines=[ (2, "#000") ])
define character.gitw = Character("Inconnu", who_color="#0055ff", who_outlines=[ (2, "#000") ], what_outlines=[ (2, "#000") ])
define character.kourt = Character("Kourtney", who_color="#ff8afb", who_outlines=[ (2, "#000") ], what_outlines=[ (2, "#000") ])
define character.luuk = Character("Luuk", who_color="#ff1694", who_outlines=[ (2, "#000") ], what_outlines=[ (2, "#000") ])
define character.polly = Character("Polly", who_color="#8b0000", who_outlines=[ (2, "#000") ], what_outlines=[ (2, "#000") ])
define character.random_guy = Character("Barman", who_color="#5fc9f8", who_outlines=[ (2, "#000") ], what_outlines=[ (2, "#000") ])

# 14.0
define character.ngam = Character("Joueur nocturne", who_color="#ff1694", who_outlines=[ (2, "#000") ], what_outlines=[ (2, "#000") ])
define character.emerald = Character("Emerald", who_color="#046307", who_outlines=[ (2, "#000") ], what_outlines=[ (2, "#000") ])
define character.madame = Character("Madame", who_color="#800080", who_outlines=[ (2, "#000") ], what_outlines=[ (2, "#000") ])
define character.satin = Character("Satine", who_color="#ecd9c9", who_outlines=[ (2, "#000") ], what_outlines=[ (2, "#000") ])
define character.wtrain = Character("Dresseur de loups", who_color="#ff1694", who_outlines=[ (2, "#000") ], what_outlines=[ (2, "#000") ])
define character.rub = Character("Rubee", who_color="#8b0000", who_outlines=[ (2, "#000") ], what_outlines=[ (2, "#000") ])
define character.trainer = Character("Entraîneur", who_color="#147efb", who_outlines=[ (2, "#000") ], what_outlines=[ (2, "#000") ])
define character.lady = Character("Dame", who_color="#ff8afb", who_outlines=[ (2, "#000") ], what_outlines=[ (2, "#000") ])
define character.gentleman = Character("Gentilhomme", who_color="#147efb", who_outlines=[ (2, "#000") ], what_outlines=[ (2, "#000") ])
define character.elm = Character("Mère d'Elijah", who_color="#fc3158", who_outlines=[ (2, "#000") ], what_outlines=[ (2, "#000") ])
define character.bird = Character("Oiseau", who_color="#5fc9f8", who_outlines=[ (2, "#000") ], what_outlines=[ (2, "#000") ])

# 15.0
define character.males = Character("Étudiant", who_color="#5fc9f8", who_outlines=[ (2, "#000") ], what_outlines=[ (2, "#000") ])
define character.fems = Character("Étudiante", who_color="#fc3158", who_outlines=[ (2, "#000") ], what_outlines=[ (2, "#000") ])
define character.oscars_owner = Character("Maître d'Oscar", who_color="#5fc9f8", who_outlines=[ (2, "#000") ], what_outlines=[ (2, "#000") ])
define character.male_buyer = Character("Acheteur", who_color="#5fc9f8", who_outlines=[ (2, "#000") ], what_outlines=[ (2, "#000") ])
define character.female_buyer = Character("Acheteuse", who_color="#a3a3a3", who_outlines=[ (2, "#000") ], what_outlines=[ (2, "#000") ])
define character.cashier = Character("Cashier", who_color="#5fc9f8", who_outlines=[ (2, "#000") ], what_outlines=[ (2, "#000") ])
define character.mactor = Character("Acteur", who_color="#fecb2e", who_outlines=[ (2, "#000") ], what_outlines=[ (2, "#000") ])
define character.factor = Character("Actrice", who_color="#a815f2", who_outlines=[ (2, "#000") ], what_outlines=[ (2, "#000") ])
define character.admin = Character("Administrateur de réservation", who_color="#fecb2e", who_outlines=[ (2, "#000") ], what_outlines=[ (2, "#000") ])
define character.aumom = Character("Maman d'Aubrey", who_color="#a815f2", who_outlines=[ (2, "#000") ], what_outlines=[ (2, "#000") ])
define character.audad = Character("Papa d'Aubrey", who_color="#fc3158", who_outlines=[ (2, "#000") ], what_outlines=[ (2, "#000") ])
define character.rick = Character("Oncle Rick", who_color="#fecb2e", who_outlines=[ (2, "#000") ], what_outlines=[ (2, "#000") ])
define character.wedoff = Character("Wedding Officiant", who_color="#5fc9f8", who_outlines=[ (2, "#000") ], what_outlines=[ (2, "#000") ])
