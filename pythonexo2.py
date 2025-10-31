def analyse_lexicale(texte):
    for c in [",", ".", "!", "?", ":", ";"]:
        texte = texte.replace(c, " ")


    mots = texte.lower().split()

    frequences = {}
    for mot in mots:
        if mot in frequences:
            frequences[mot] += 1
        else:
            frequences[mot] = 1
    mots_uniques = set(mots)
    longueurs = [len(m) for m in mots]
    longueur_moyenne = sum(longueurs) / len(longueurs)
    max_freq = max(frequences.values())
    min_freq = min(frequences.values())
    mots_plus = [mot for mot, f in frequences.items() if f == max_freq]
    mots_moins = [mot for mot, f in frequences.items() if f == min_freq]
    palindromes = []
    for mot in mots_uniques:
        if len(mot) > 1 and mot == mot[::-1]:
            palindromes.append(mot)

    print("=== ANALYSE LEXICALE ===")
    print("Nombre total de mots :", len(mots))
    print("Nombre de mots uniques :", len(mots_uniques))
    print("Longueur moyenne des mots :", round(longueur_moyenne, 2))
    print("Mots les plus utilisés :", mots_plus)
    print("Mots les moins utilisés :", mots_moins)
    print("Palindromes détectés :", palindromes)
    print("\nFréquence des mots :", frequences)


#analyse grammaticale


def analyse_grammaticale(texte):
    separateurs = [".", "!", "?"]
    phrases = []
    phrase = ""

    for c in texte:
        phrase += c
        if c in separateurs:
            phrases.append(phrase.strip())
            phrase = ""
    if phrase.strip():
        phrases.append(phrase.strip())

    nb_phrases = len(phrases)

    longueurs_phrases = [len(p.split()) for p in phrases]
    longueur_moyenne = sum(longueurs_phrases) / nb_phrases


    ponctuation = {".": 0, "!": 0, "?": 0, ",": 0, ";": 0, ":" : 0}
    for c in texte:
        if c in ponctuation:
            ponctuation[c] += 1
    stats_mots = {"noms_propres": 0, "adverbes": 0, "adjectifs": 0, "autres": 0}
    mots = texte.replace(".", "").replace(",", "").split()
    for mot in mots:
        if mot[0].isupper():
            stats_mots["noms_propres"] += 1
        elif mot.endswith("ment"):
            stats_mots["adverbes"] += 1
        elif mot.endswith("e"):
            stats_mots["adjectifs"] += 1
        else:
            stats_mots["autres"] += 1

    mots_uniques = set([m.strip(".,!?").lower() for m in mots])

    print("=== ANALYSE GRAMMATICALE ===")
    print(f"Nombre de phrases : {nb_phrases}")
    print(f"Longueur moyenne des phrases (en mots) : {round(longueur_moyenne, 2)}")
    print(f"Types de ponctuation utilisés : {ponctuation}")
    print(f"Statistiques par type de mot : {stats_mots}")
    print(f"Mots uniques trouvés : {len(mots_uniques)}")
    print("\nListe des phrases :")
    for i, p in enumerate(phrases, 1):
        print(f"  {i}) {p}")

#rapport

def rapports(texte):

    for c in [",", ";", ":", "(", ")", "\"", "'"]:
        texte = texte.replace(c, "")


    separateurs = [".", "!", "?"]
    phrases = []
    phrase = ""

    for c in texte:
        phrase += c
        if c in separateurs:
            phrases.append(phrase.strip())
            phrase = ""
    if phrase.strip():
        phrases.append(phrase.strip())


    mots = []
    for p in phrases:
        mots += p.lower().replace(".", "").replace("!", "").replace("?", "").split()


    freqs = {}
    for mot in mots:
        freqs[mot] = freqs.get(mot, 0) + 1


    mots_uniques = set(mots)


    top_10 = sorted(freqs.items(), key=lambda x: x[1], reverse=True)[:10]


    longueurs = [len(p.split()) for p in phrases]
    max_len = max(longueurs) if longueurs else 0
    phrases_longues = [p for p in phrases if len(p.split()) == max_len]


    diversite = (len(mots_uniques) / len(mots)) * 100


    patterns = {}
    for i in range(len(mots) - 1):
        paire = mots[i] + " " + mots[i + 1]
        patterns[paire] = patterns.get(paire, 0) + 1
    patterns_repetitifs = [p for p, f in patterns.items() if f > 1]

    print("=== RAPPORTS D'ANALYSE ===")
    print(f"Top 10 des mots : {top_10}")
    print(f"Phrases les plus longues ({max_len} mots) :")
    for p in phrases_longues:
        print("  -", p)
    print(f"Diversité du vocabulaire : {diversite:.2f}%")
    print("Patterns répétitifs (groupes de 2 mots) :", patterns_repetitifs)



texte = input("Entrez un texte  : ")
analyse_lexicale(texte)
analyse_grammaticale(texte)
rapports(texte)


