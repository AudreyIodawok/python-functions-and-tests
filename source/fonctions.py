import pandas as pd

# ------------------------------------------------------------------------------------------------------
# # A. IMPACT DES FONCTIONS SUR LES OBJETS MUTABLES ET IMMUABLES
# ------------------------------------------------------------------------------------------------------

# ------------------------------------------------------------------------------------------------------
# # A1. Fonction pour modifier un dataframe 
# ------------------------------------------------------------------------------------------------------

# ******************************************************************************************************
# **1. FONCTION MODIFY_DF**
# ******************************************************************************************************

def modify_df(in_df : pd.DataFrame) -> pd.DataFrame:
    in_df["name_cap"] = in_df["name"].str.title()
    return in_df

if __name__ == "__main__":
    df = pd.DataFrame({"name" : ["mike", "tim"]})
    df = modify_df(df)

# print(df)
# ******************************************************************************************************

# Les DataFrames de Pandas sont des objets dont les valeurs sont modifiables. 
# Chaque fois que vous modifiez un objet mutable, cela affecte exactement la même 
# instance que celle que vous avez créée à l'origine, et son emplacement physique 
# en mémoire reste inchangé. En revanche, lorsque vous modifiez un objet immuable 
# (par exemple, une chaîne de caractères), Python crée un tout nouvel objet à un 
# nouvel emplacement mémoire et échange la référence pour le nouveau.

# C'est le point crucial : en Python, les objets sont passés à la fonction par affectation. 
# Regardez le résultat : la valeur de df a été affectée à la variable in_df lorsqu'elle 
# a été passée à la fonction en tant qu'argument. Tant l'original df que in_df à 
# l'intérieur de la fonction pointent vers le même emplacement mémoire (valeur numérique 
# entre parenthèses), même s'ils portent des noms de variables différents. Pendant la 
# modification de ses attributs, l'emplacement de l'objet mutable reste inchangé. Ainsi, 
# tous les autres contextes peuvent également voir les modifications — ils accèdent 
# au même emplacement mémoire.

# En réalité, puisque nous avons modifié l'instance originale, il est redondant de retourner 
# le DataFrame et de l'affecter à la variable. Ce code a exactement le même effet :

# ------------------------------------------------------------------------------------------------------
# # A2. Fonction pour modifier un dataframe 2 
# ------------------------------------------------------------------------------------------------------

# ******************************************************************************************************
# **2. FONCTION MODIFY_DF_2**
# ******************************************************************************************************
def modify_df_2(in_df : pd. DataFrame) -> None:
    in_df["name_cap"] = in_df["name"].str.title()

if __name__ == "__main__":
    df = pd.DataFrame({"name" : ["bert", "albert"]})
    df = modify_df_2(df)

# print(df2)
# ******************************************************************************************************

# La fonction modify_df retourne un nouveau DataFrame avec la colonne ajoutée, tandis que la 
# fonction modify_df_2 modifie directement le DataFrame passé en argument sans retourner quoi 
# que ce soit.

# ------------------------------------------------------------------------------------------------------
# A3. Fonction pour modifier une chaine de caractères 
# ------------------------------------------------------------------------------------------------------

# En revanche, si l'objet est immuable, il changera d'emplacement mémoire tout au long de 
# la modification, comme dans l'exemple ci-dessous. Étant donné que la 1ère chaîne ne 
# peut pas être modifiée (les chaînes sont immuables), la 2ème chaîne est créée par-dessus 
# l'ancienne, mais en tant que nouvel objet, réclamant un nouvel emplacement en mémoire. 
# La chaîne retournée n'est pas la même chaîne, alors que le DataFrame retourné était exactement 
# le même DataFrame.

# ******************************************************************************************************
# **3. FONCTION MODIFY_STRING**
# ******************************************************************************************************
def modify_string(string : str) -> str:
    string = string.title()
    return string

if __name__ == "__main__":
    string = "bert albert"
    string = modify_string(string)

# print(string)
# ******************************************************************************************************

# Le point essentiel est que la mutation des DataFrames à l'intérieur des fonctions a un effet 
# global. Si vous ne gardez pas cela à l'esprit, vous pourriez :
# 1. Modifier ou supprimer accidentellement une partie de vos données, en pensant que l'action se 
# déroule uniquement à l'intérieur de la portée de la fonction, ce qui n'est pas le cas,
# 2. Perdre le contrôle sur ce qui est ajouté à votre DataFrame et quand il est ajouté, par exemple 
# lors d'appels de fonctions imbriquées.

# ------------------------------------------------------------------------------------------------------
# B. EFFETS SECONDAIRES :
# ------------------------------------------------------------------------------------------------------

# ******************************************************************************************************
# **4. FONCTION FIND_MAX_NAME_LENGTH**
# ******************************************************************************************************
def find_max_name_length(df: pd.DataFrame) -> int:
    df["name_len"] = df["name"].str.len() # effet secondaire
    return max(df["name_len"])

if __name__ == "__main__":
    df = pd.DataFrame({"name" : ["bert", "albert"]})
    max_name_length = find_max_name_length(df)  # Renommer la variable
    print(max_name_length)
    print(df)
# ******************************************************************************************************

# La fonction find_max_name_length modifie le DataFrame original en ajoutant 
# une nouvelle colonne "name_len" qui contient la longueur de chaque nom dans 
# la colonne "name". Cette modification est effectuée par l'instruction 
# df["name_len"] = df["name"].str.len().
# Cela se produit parce que les objets DataFrame de pandas sont mutables, 
# ce qui signifie qu'ils peuvent être modifiés en place sans avoir besoin 
# de les réassigner à une nouvelle variable. Lorsque vous modifiez df à 
# l'intérieur de la fonction find_max_name_length, vous modifiez directement 
# le DataFrame passé en argument.

# En revanche, la fonction retournera une erreur (cf test) si la colonne name 
# est vide. Pour l'éviter, on devra modifier la fonction comme suit :

# ******************************************************************************************************
# **5. FONCTION FIND_MAX_NAME_LENGTH_BIS**
# ******************************************************************************************************
def find_max_name_length_bis(df: pd.DataFrame) -> int:
    if not df.empty and df["name"].dtype == "object":
        df["name_len"] = df["name"].str.len() # Effet secondaire
        return max(df["name_len"])
    else:
        return 0  
    # Retourner 0 si le DataFrame est vide ou si la colonne name ne 
    # contient pas de valeurs de type chaîne de caractères
# ******************************************************************************************************

# ------------------------------------------------------------------------------------------------------
# C. A FAIRE : REDUIRE LES MODIFICATIONS
# ------------------------------------------------------------------------------------------------------

# ------------------------------------------------------------------------------------------------------
# C1. Créer des variables temporaires :
# ------------------------------------------------------------------------------------------------------
# Pour éliminer l'effet secondaire, dans le code ci-dessous, nous avons créé une 
# nouvelle variable temporaire au lieu de modifier le DataFrame original. La notation 
# lengths: pd.Series indique le type de données de la variable.

# ******************************************************************************************************
# **6. FONCTION FIND_MAX_NAME_LENGTH_SERIES_TER**
# ******************************************************************************************************
def find_max_name_length_series_ter(df: pd.DataFrame) -> int:
    lengths: pd.Series = df["name"].str.len()
    return max(lengths)

if __name__ == "__main__":
    df4 = pd.DataFrame({"name" : ["bert", "albert"]})
    max_name_length_series: pd.Series = find_max_name_length_series_ter(df4)
    print(max_name_length_series)
    print(type(max_name_length_series)) # class int
# ******************************************************************************************************

# Ce choix de conception de fonction est meilleur car il encapsule l'état intermédiaire au 
# lieu de produire un effet secondaire.

# Un autre point à noter : veuillez être attentif aux différences entre la copie profonde 
# et la copie superficielle des éléments du DataFrame. Dans l'exemple ci-dessus, nous avons 
# modifié chaque élément de la série originale df["name"], donc l'ancien DataFrame et la 
# nouvelle variable n'ont aucun élément partagé. Cependant, si vous affectez directement 
# l'une des colonnes d'origine à une nouvelle variable, les éléments sous-jacents conservent 
# les mêmes références en mémoire. Voyez les exemples :

# ------------------------------------------------------------------------------------------------------
# C2. Copies profondes et copies superficielles
# ------------------------------------------------------------------------------------------------------
df = pd.DataFrame({"name": ["bert", "albert"]})

series1 = df["name"]     # copie superficielle
series1[0] = "roberta"   # <-- cela change le dataframe original
#print(series1[0])
print(df)

# ******************************************************************************************************
df1 = pd.DataFrame({"name": ["bert", "albert"]})

series2 = df["name"].copy(deep=True) # copie profonde
series2[0] = "roberta"   # <-- ceci ne change pas le dataframe original
print(df1)

# ******************************************************************************************************
df2 = pd.DataFrame({"name": ["bert", "albert"]})

series3 = df2["name"].str.title()  # ne constitue pas une copie
series3[0] = "roberta"   # <-- ceci ne change pas le dataframe original
print(df2)
print(series3)
print(series3[0])

# Créer une copie profonde va allouer un nouvel emplacement mémoire, alors il est important de 
# le garder en tête si le script doit rester efficace en terme de mémoire.
# En effet, créer une copie profonde allouera effectivement une nouvelle mémoire pour 
# chaque objet et son contenu, offrant ainsi une indépendance par rapport aux données 
# d'origine. Cependant, il est essentiel de réfléchir à la nécessité d'optimiser 
# l'utilisation de la mémoire de votre script, car la copie profonde peut consommer 
# plus de mémoire, surtout pour de grands ensembles de données.

# ------------------------------------------------------------------------------------------------------
# D. A FAIRE : GROUPER LES OPERATIONS SIMILAIRES
# ------------------------------------------------------------------------------------------------------

# Il est possible que, pour une raison quelconque, vous souhaitiez stocker le résultat 
# de ce calcul de longueur. Cependant, il n'est toujours pas judicieux de l'ajouter au 
# DataFrame à l'intérieur de la fonction en raison de la violation de l'effet secondaire 
# ainsi que de l'accumulation de plusieurs responsabilités à l'intérieur d'une seule fonction.

# Nous devons nous assurer que les instructions à l'intérieur de notre fonction sont toutes 
# au même niveau d'abstraction.
# Mélanger les niveaux d'abstraction au sein d'une fonction est toujours confus. Les lecteurs 
# peuvent ne pas être en mesure de dire si une expression particulière est un concept essentiel 
# ou un détail.

# Il est préférable de séparer les préoccupations et de rendre la fonction plus modulaire 
# en évitant les effets secondaires. Vous pouvez simplement retourner le résultat du calcul et 
# ensuite, si nécessaire, ajouter cette colonne au DataFrame à l'extérieur de la fonction. 
# Cela rend le code plus clair, plus facile à comprendre et plus facile à maintenir.

# ------------------------------------------------------------------------------------------------------
# D1. Solution 1
# ------------------------------------------------------------------------------------------------------

# ******************************************************************************************************
# **7. FONCTION CALCULATE_NAME_LENGTHS**
# ******************************************************************************************************
def calculate_name_lengths(df: pd.DataFrame) -> pd.Series:
    return df["name"].str.len()

# Création d'un DataFrame
df = pd.DataFrame({"name": ["bert", "albert"]})

# Calcul des longueurs des noms
name_lengths = calculate_name_lengths(df) # ou si le df a pls colonnes : calculate_name_lengths(df["name"])

# Ajout de la colonne de longueurs au DataFrame
df["name_lengths"] = name_lengths

# Affichage du DataFrame avec la nouvelle colonne ajoutée
print(df)
# ******************************************************************************************************
# Dans cet exemple, la fonction calculate_name_lengths se concentre uniquement sur le calcul 
# des longueurs des noms et renvoie une série de ces longueurs. En dehors de la fonction, cette 
# série est ensuite ajoutée au DataFrame. Cela rend le code plus modulaire et plus facile à 
# comprendre, tout en évitant les effets secondaires indésirables.

# ------------------------------------------------------------------------------------------------------
# D2. Solution 2
# ------------------------------------------------------------------------------------------------------
# Pourquoi ne pas préparer vos données à l'avance ? Séparons la préparation des données
# de la computation réelle dans des fonctions distinctes :

# ******************************************************************************************************
# **8 et 8 bis. FONCTIONS CREATE_NAME_LEN_COL ET FIND_MAX_ELEMENT**
# ******************************************************************************************************
from typing import Collection

def create_name_len_col(series: pd.Series) -> pd.Series: # entrée : objet du type pd.Series, sortie : idem
    return series.str.len() # retourne la longueur de la chaine de caractère de chaque élément de la série

def find_max_element(collection: Collection) -> int: # entrée : collection d'éléments de type entier
    return max(collection) if len(collection) else 0 # renvoie l'élément max si existe, sinon 0

df = pd.DataFrame({"name": ["bert", "albert"]})
df["name_len"] = create_name_len_col(df.name) # création de la colonne "name_len"
max_name_len = find_max_element(df.name_len) # trouve le max de caractères parmi les éléments de la colonne "name_len"
print(max_name_len)
# ******************************************************************************************************

# La fonction create_name_len_col semble modifier le DataFrame original en ajoutant une nouvelle colonne name_len. 
# Cependant, la modification du DataFrame original n'est pas directement liée à la fonction create_name_len_col. 
# Cette fonction prend simplement une série en entrée, calcule la longueur des chaînes de caractères dans cette 
# série et renvoie une nouvelle série contenant ces longueurs.

# C'est l'assignation df["name_len"] = create_name_len_col(df.name) qui modifie réellement le DataFrame en 
# ajoutant une nouvelle colonne name_len basée sur les valeurs renvoyées par create_name_len_col.

# ------------------------------------------------------------------------------------------------------
# D3. solution 3
# ------------------------------------------------------------------------------------------------------

# On peut également utiliser les fonctions suivantes :

# ******************************************************************************************************
# **9. FONCTIONS FIND_NAME_LENGTH_SERIES (ET FIND_MAX ELEMENT - cf fonct. 8 bis)**
# ******************************************************************************************************
def find_name_length_series(df: pd.DataFrame) -> pd.Series:
    lengths: pd.Series = df["name"].str.len()
    return lengths

#def find_max_element(collection: Collection) -> int:
    #return max(collection) if len(collection) else 0

# Création du DataFrame
df = pd.DataFrame({"name": ["bert", "albert"]})

# Utilisation de la fonction pour obtenir les longueurs des noms
name_lengths = find_name_length_series(df)

# Trouver la longueur maximale
max_name_len = find_max_element(name_lengths)

# Affichage de la longueur maximale
print(max_name_len)
# ******************************************************************************************************

# ------------------------------------------------------------------------------------------------------
# D4. Solution 4 : Avec pd.concat 
# ------------------------------------------------------------------------------------------------------

# Organisons le code en suivant les étapes proposées :

# 1. Utiliser la fonction concat et l'extraire dans une fonction séparée appelée prepare_data, qui 
# regrouperait toutes les étapes de préparation des données en un seul endroit.
# 2. Utiliser la méthode apply pour travailler sur des textes individuels au lieu de séries de textes.
# 3. Prendre en compte l'utilisation de copies superficielles ou profondes selon la nécessité de modifier 
# ou non les données d'origine.

# Voici un exemple de code restructuré :

# ******************************************************************************************************
# **10 et 10 bis. FONCTION COMPUTE_LENGTH ET PREPARE_DATA**
# ******************************************************************************************************
from typing import Optional

def compute_length(word: Optional[str]) -> int:
    return len(word) if word else 0

def prepare_data(df: pd.DataFrame) -> pd.DataFrame:
    return pd.concat([
        df.copy(deep=True),  # copie profonde
        df.name.apply(compute_length).rename("name_len"),
    ], axis=1)

# Création du DataFrame
df = pd.DataFrame({"name": ["bert", "albert"]})

df_prepared = prepare_data(df)

print(df_prepared)
# ******************************************************************************************************

# ------------------------------------------------------------------------------------------------------
# E. REUTILISABILITE 
# ------------------------------------------------------------------------------------------------------

# La manière dont nous avons divisé le code le rend vraiment facile à reprendre plus tard, 
# de prendre toute la fonction et de la réutiliser dans un autre script. 

# Il y a encore une chose que nous pouvons faire pour augmenter le niveau de réutilisabilité : 
# passer les noms des colonnes en tant que paramètres aux fonctions. Le refactoring devient 
# un peu exagéré, mais cela en vaut parfois la peine pour le bien de la flexibilité ou de 
# la réutilisabilité.

# ******************************************************************************************************
# **11. FONCTION CREATE_NAME_LEN_COL_BIS**
# ******************************************************************************************************
def create_name_len_col_bis(df: pd.DataFrame, orig_col: str, target_col: str) -> pd.Series:
    return df[orig_col].str.len().rename(target_col)

name_label, name_len_label = "name", "name_len"
pd.concat([
    df,
    create_name_len_col_bis(df, name_label, name_len_label)
], axis=1)

# Création du DataFrame
df = pd.DataFrame({"name": ["bert", "albert"]})

df_prepared = create_name_len_col_bis(df, "name", "name_len")

print(df_prepared) # le résultat incluera uniquement la colonne "target", soit "name_len"
# ******************************************************************************************************

# # Pour conserver la colonne "name" originale :

# ******************************************************************************************************
# **12. FONCTION CREATE_NAME_LEN_COL_TER**
# ******************************************************************************************************
def create_name_len_col_ter(df: pd.DataFrame, orig_col: str, target_col: str) -> pd.DataFrame:
    # Créer un nouveau DataFrame avec les deux colonnes
    new_df = df[[orig_col]].copy()  # Inclure la colonne originale
    new_df[target_col] = df[orig_col].str.len()  # Ajouter la colonne de longueur des noms
    return new_df

# Création du DataFrame
df = pd.DataFrame({"name": ["bert", "albert"]})
print(df)

# Utilisation des noms de colonnes pour la fonction
name_label, name_len_label = "name", "name_len"
df_prepared_bis = create_name_len_col_ter(df, name_label, name_len_label)

print(df_prepared_bis)
# ******************************************************************************************************








