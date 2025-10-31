import string

def compter_mots(texte):
    return len(texte.split())

def frequences_mots(texte):
    freq = {}
    for mot in texte.split():
        mot = mot.strip(string.punctuation).lower()
        freq[mot] = freq.get(mot, 0) + 1
    return freq

def stats_mots(texte):
    mots = [m.strip(string.punctuation) for m in texte.split() if m]
    longueurs = [len(m) for m in mots]
    moyenne = sum(longueurs) / len(longueurs) if longueurs else 0
    freq = frequences_mots(texte)
    max_occ = max(freq.values())
    plus_frequents = [mot for mot, occ in freq.items() if occ == max_occ]
    return plus_frequents, max_occ, moyenne

def trouver_palindromes(texte):
    mots = [m.strip(string.punctuation).lower() for m in texte.split()]
    return [m for m in mots if len(m) > 1 and m == m[::-1]]

def compter_phrases(texte):
    return len([p for p in texte.split('.') if p.strip()])

def longueur_phrases(texte):
    return [len(p.split()) for p in texte.split('.') if p.strip()]

def ponctuation_trouvee(texte):
    return {c for c in texte if c in string.punctuation}

def mots_distincts(texte):
    return {m.strip(string.punctuation).lower() for m in texte.split()}

def top_dix(texte):
    freq = frequences_mots(texte)
    return sorted(freq.items(), key=lambda x: x[1], reverse=True)[:10]

def phrase_la_plus_longue(texte):
    phrases = [p.strip() for p in texte.split('.') if p.strip()]
    return max(phrases, key=lambda x: len(x.split())) if phrases else ""

def diversite_vocabulaire(texte):
    mots = [m.strip(string.punctuation).lower() for m in texte.split()]
    return (len(set(mots)) / len(mots)) * 100 if mots else 0

def patterns_repetitifs(texte, longueur=2):
    mots = [m.strip(string.punctuation).lower() for m in texte.split()]
    patterns = {}
    for i in range(len(mots) - longueur + 1):
        p = " ".join(mots[i:i + longueur])
        patterns[p] = patterns.get(p, 0) + 1
    repetes = {k: v for k, v in patterns.items() if v > 1}
    return dict(sorted(repetes.items(), key=lambda x: x[1], reverse=True))

with open("data.txt", "r", encoding="utf-8") as f:
    contenu = f.read()
    print(f"Nombre total de mots : {compter_mots(contenu)}")
    print("Fréquence des mots :", frequences_mots(contenu))
    plus_frequents, nb_occ, moyenne = stats_mots(contenu)
    print(f"Mots les plus utilisés : {plus_frequents} ({nb_occ} fois)")
    print(f"Longueur moyenne des mots : {moyenne:.2f}")
    print("Palindromes :", trouver_palindromes(contenu))
    print("Nombre de phrases :", compter_phrases(contenu))
    print("Longueurs des phrases :", longueur_phrases(contenu))
    print("Ponctuation utilisée :", ponctuation_trouvee(contenu))
    print("Mots uniques :", mots_distincts(contenu))
    print("Top 10 des mots :", top_dix(contenu))
    print("Phrase la plus longue :", phrase_la_plus_longue(contenu))
    print(f"Diversité du vocabulaire : {diversite_vocabulaire(contenu):.2f}%")
    print("Patterns répétitifs :", patterns_repetitifs(contenu))
