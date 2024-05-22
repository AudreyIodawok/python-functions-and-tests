
import pytest
import pandas as pd

# --------------------------------------------------------------------------------------------------
# Testabilité
# --------------------------------------------------------------------------------------------------

# Avez-vous déjà découvert que votre prétraitement était défectueux après des semaines d'expériences 
# sur le jeu de données prétraité ? Non ? Vous avez de la chance. J'ai en fait dû répéter une série 
# d'expériences à cause d'annotations incorrectes, ce qui aurait pu être évité si j'avais testé 
# juste quelques fonctions de base.

# Les scripts importants doivent être testés. Même si le script n'est qu'un assistant, 
# j'essaie maintenant de tester au moins les fonctions cruciales, les plus basiques. Revenons sur 
# les étapes que nous avons suivies depuis le début.

# Je n'aime même pas penser à tester cela, c'est très redondant et nous avons contourné l'effet 
# secondaire. Cela teste également un tas de fonctionnalités différentes : le calcul de la longueur 
# du nom et l'agrégation du résultat pour l'élément maximal. En plus, ça échoue, vous l'aviez vu venir ?

#  NB : Dans le test test_find_max_name_length, les paramètres df et result sont déjà définis 
# dans le décorateur @pytest.mark.parametrize. Ce décorateur crée des cas de test 
# paramétrés en utilisant différentes valeurs pour df et result à partir de la liste 
# spécifiée. Donc, lorsque le test est exécuté, pytest exécutera automatiquement le 
# test pour chaque combinaison de valeurs spécifiée dans la liste.

# def find_max_name_length(df: pd.DataFrame) -> int:
    # df["name_len"] = df["name"].str.len()  # effet secondaire
    # return max(df["name_len"])

# --------------------------------------------------------------------------------------------------
# Test fonction find_max_name_length (fonction n°4)
#---------------------------------------------------------------------------------------------------

# from source.fonctions import find_max_name_length

# --------------------------------------------------------------------------------------------------
# 1ère syntaxe :
# --------------------------------------------------------------------------------------------------

# @pytest.mark.parametrize("df, result", [
#     (pd.DataFrame({"name": []}), 0),  # oops, cela échoue !
#     (pd.DataFrame({"name": ["bert"]}), 4),
#     (pd.DataFrame({"name": ["bert", "roberta"]}), 7),
# ])

# def test_find_max_name_length(df: pd.DataFrame, result: int):
#     assert find_max_name_length(df) == result

# --------------------------------------------------------------------------------------------------
# 2ème syntaxe :
# --------------------------------------------------------------------------------------------------

# Définition du DataFrame
# df_data = [
#     (pd.DataFrame({"name": []}), 0),  # Cela peut échouer
#     (pd.DataFrame({"name": ["bert"]}), 4),
#     (pd.DataFrame({"name": ["bert", "roberta"]}), 7),
# ]
# print(df_data)

# #Utilisation de pytest.mark.parametrize avec le DataFrame défini
# @pytest.mark.parametrize("df, result", df_data)
# def test_find_max_name_length(df: pd.DataFrame, result: int):
#     assert find_max_name_length(df) == result

# def create_name_len_col(series: pd.Series) -> pd.Series:
#     return series.str.len()

# Dans ce cas, on a une erreur "AttributeError: Can only use .str accessor with 
# string values!"
# Dans ce test, on utilise des DataFrames vides ou avec des valeurs uniques pour tester 
# la fonction find_max_name_length. Cependant, cette fonction essaie d'appliquer 
# l'accessoire .str sur la colonne name, ce qui provoque l'erreur lorsque la colonne 
# est vide.

# --------------------------------------------------------------------------------------------------
# Test fonction find_max_name_length_bis (fonction n°5)
# --------------------------------------------------------------------------------------------------

# Pour éviter cette erreur, on peut vérifier si la colonne contient des valeurs 
# de type chaîne avant d'appliquer l'accessoire .str. Voici comment le faire :

from source.fonctions import find_max_name_length_bis

@pytest.mark.parametrize("df, result", [
    (pd.DataFrame({"name": []}), 0),  
    (pd.DataFrame({"name": ["bert"]}), 4),
    (pd.DataFrame({"name": ["bert", "roberta"]}), 7),
])

def test_find_max_name_length(df: pd.DataFrame, result: int):
    assert find_max_name_length_bis(df) == result

# Cette fonction ne renvoie pas d'erreur lorsque le df est vide ou que la colonne "name"
# ne contient pas de valeur.



# --------------------------------------------------------------------------------------------------
# SANS UTILISER @PYTEST.MARK.PARAMETRIZE()
# --------------------------------------------------------------------------------------------------

# from source.fonctions import find_max_name_length, find_max_name_length_series

# # Test pour la fonction find_max_name_length
# def test_find_max_name_length():
#     # Créer un DataFrame pour tester
#     df = pd.DataFrame({"name": ["bert", "roberta", "charles"]})
#     assert find_max_name_length(df) == 7  # La longueur maximale est 7

# # Test pour la fonction find_max_name_length_series
# def test_find_max_name_length_series():
#     # Créer un DataFrame pour tester
#     df = pd.DataFrame({"name": ["bert", "roberta", "charles"]})
#     assert find_max_name_length_series(df) == 7  # La longueur maximale est 7
