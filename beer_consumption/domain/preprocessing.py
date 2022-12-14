import pandas as pd 
import numpy as pd

def analyse_brasserie(data):
    # Quelle brasserie produit les bières les plus fortes en % ABV 
    print(data.groupby(by = ["brewery_name"]).max("beer_abv")[["beer_abv"]].sort_values(by=['beer_abv'], ascending=False)) 
    # Si vous deviez choisir 3 bières à recommander en utilisant uniquement ces données, laquelle choisiriez-vous
    data.groupby(by = ["beer_name"]).mean("review_overall")[["review_overall"]].sort_values(by=['review_overall'], ascending=False).head(15)
    # Lesquels des facteurs (arôme, Tate, apparence, palais) sont les plus importants pour déterminer la qualité globale d'une bière