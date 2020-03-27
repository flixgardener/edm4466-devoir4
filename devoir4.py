# coding: utf-8
import csv, spacy
from collections import Counter
martino = "martino.csv"

f = open(martino, encoding="utf-8")
# Comme lorsque nous faisions l'exercice en classe avec les commentaires de CRTC, mon ordi affiche tout le temps
    # le même message d'erreur lors de la lecture du fichier: "UnicodeDecodeError: 'charmap' codec
    # can't decode byte 0x9d in position 911: character maps to <undefined>"" La solution, je l'ai trouvée
    # en ligne! Il faut tout simplement ajouter "encoding="utf-8"" après l'ouverture du fichier
chroniques = csv.reader(f)
next(chroniques)

tal = spacy.load("fr_core_news_md")
tal.Defaults.stop_words.add("il")
tal.Defaults.stop_words.add("t")
tal.Defaults.stop_words.add("y")

bigrams = []
toutesChroniques = []

for chronique in chroniques:
    doc = tal(chronique[3])
    tokens = [token.text for token in doc]
    # print(tokens)
    # print(len(tokens))
    lemmes = [token.lemma_ for token in doc]
    # print(lemmes)
    # print(len(lemmes))
    mots = [token.lemma_ for token in doc if token.is_stop == False and token.is_punct == False]
    
    # print (mots)
    # print (len(mots))

    for x, y in enumerate(mots[:-1]):
         bigrams.append("{} {}".format("mot1", "mot2"))
         if "islam" in bigrams or "musulm" in bigrams:
             print(bigrams)
             bigram.append(bigrams)

            
    # print(bigrams)

freq = Counter(bigrams)
print(freq.most_common(50))

# À noter: je crois que mon script fonctionne, mais mon ordi n'est pas assez puissant pour faire des tests
# à outrance (on parle de quelques heures à chaque test). S'il y a une ou des erreurs, c'est très possible! 
# J'ai fait mon possible avec mon ordi fossile.
    