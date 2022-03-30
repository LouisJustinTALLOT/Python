#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 14 16:18:39 2022

@author: salomeouaknine, LouisJustinTALLOT
"""
from typing import List, Tuple
import requests
from bs4 import BeautifulSoup

import pickle

import pandas as pd
import numpy as np

import re  # regular expression
from re import search

import nltk
from nltk.tokenize import word_tokenize
from nltk.probability import FreqDist
from nltk.stem import SnowballStemmer


# 1. Recuperer le document
def link_to_transcript(link: str) -> List[str]:
    with open(link, encoding="utf8") as page:
        soup = BeautifulSoup(page, "lxml")
        text = [p.text for p in soup.find_all('p')]
        #code = soup.find_all(text = "code")
    return text


def combine_text(list_of_text: List[str]) -> str:
    '''Takes a list of text and combines them into one large chunk of text.'''
    return ' '.join(list_of_text)


# 2. Nettoyer les données
def clean_text_round1(text: str) -> str:
    #text = text.lower()
    # text = re.sub('\[.*?\]', '', text) # enlever les données dans les [] dans le texte
    # text = re.sub('[%s]' % re.escape(string.punctuation), '', text) # enlever toutes les ponctuations
    # text = re.sub('\w*\d\w*', '', text) # enlever tous les noms possédant des chiffres à l'intérieur
    #text = re.sub('[‘’“”…]', '', text)
    return text


# 3. Tokeniser
def my_tokenizer(text: str) -> List[str]:
    sentence_tokens = word_tokenize(text)
    return sentence_tokens


# Tester l'action du texte
def action_du_texte(stem):
    if pst.stem('remplace') in stem:
        print('remplacement')
    if pst.stem('modification') in stem:
        print('modification')
    if pst.stem('abroge') in stem:
        print('abrogation')
    if pst.stem('supprime') in stem:
        print('suppression')
    if pst.stem('ajoute') in stem:
        print('ajout')
    if pst.stem('création') in stem:
        print('création')


# 5. Chercher les codes cités
def join_tuple(tuple_list: List[Tuple]) -> List[str]:
    string_list = []
    for one_tuple in tuple_list:
        string_list.append(' '.join(one_tuple))
    return string_list


# Préparer les références des codes dans le texte de loi
def code_present_texte_loi(ngram: List[Tuple]) -> List[str]:
    # print("\n".join(lists(str(_) for _ in ngram)))
    code_dans_ngram = []
    for tupleobj in ngram:
        if tupleobj.count('code') > 0:
            if (tupleobj[2] == 'code') and (tupleobj[1] != 'présent'):
                # Aprint(tupleobj)
                code_dans_ngram.append(tupleobj[3])

    return code_dans_ngram


def article_et_code_dans_meme_tuple(ngram):
    article_et_code_dans_ngram = []
    for tupleobj in ngram:
        if tupleobj.count('code') > 0:
            if (tupleobj[2] == 'code') and (tupleobj[1] != 'présent'):
                article_et_code_dans_ngram.append(tupleobj)

    return article_et_code_dans_ngram


def tokenisation_nom_codes(df_codes: pd.DataFrame) -> List:
    df_codes_tokenise = []
    for index in df_codes.index:
        nom_du_code = df_codes.loc[index]['nom_du_code']
        # enlever la ponctuation, surtout les apostrophes
        nom_du_code = re.sub(r'[^\w\s]', ' ', nom_du_code)
        # enelever le mot code permet d'avoir l'essentiel
        nom_du_code = re.sub(r"\b(Code|de|du|des|de la|de l\')\b", '', nom_du_code)
        nom_du_code_tokenise = my_tokenizer(nom_du_code)
        y = [word for word in nom_du_code_tokenise if not word.lower() in stop_words]
        df_codes_tokenise.append(y)
    return df_codes_tokenise


# Trouver le(s) code(s) utilisé(s) dans le texte
def code_utilise(liste_codes_dans_texte_loi, df_codes):
    codes_utilises_dans_le_texte = []
    for nom_code in liste_codes_dans_texte_loi:
        for code_texte in df_codes["code_stemme"]:
            if search(nom_code, code_texte):
                codes_utilises_dans_le_texte.append(code_texte)
    return codes_utilises_dans_le_texte


# 6. Ouvrir le code
def ouvrir_le_code(df_codes: pd.DataFrame):
    # for x in codes_utilises_dans_le_texte : #remplacer ligne dessous "consommation" par x
    loc_code_cite = df_codes.loc[df_codes['code_stemme'] == "consommation"]
    url_liste = loc_code_cite['lien'].tolist()
    url = url_liste[0]
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'lxml')
    title = soup.findAll('head')
    # soup = BeautifulSoup(html_file, 'lxml')
    print(title)


if __name__ == "__main__":
    pd.set_option('max_colwidth', 150)
    
    link = '.'
    document = '/JORFARTI000045294276.xml'
    texte = link_to_transcript(link + document)

    data_combined = combine_text(texte)  # concaténation de tout le texte

    # data_combined_clean = clean_text_round1(data_combined)
    stop_words = set(nltk.corpus.stopwords.words('french'))

    sentence_tokens = my_tokenizer(data_combined)
    sentence_tokens = [word for word in sentence_tokens if not word.lower() in stop_words]

    fdist = FreqDist()
    for word in sentence_tokens:
        fdist[word.lower()] += 1

    quote_ngrams = list(nltk.ngrams(sentence_tokens, 6))  # (mots, groupes)
    # print(quote_ngrams)

    # 4. Chercher les mots permettant de remplacer
    # 4.1 essayer la stemmatisation
    pst = SnowballStemmer('french')
    stem_words = []
    for w in sentence_tokens:
        stem_words.append(pst.stem(w))

    code = code_present_texte_loi(quote_ngrams)
    # print(code)
    # code_str = join_tuple(code)

    article_et_code_tuple = article_et_code_dans_meme_tuple(quote_ngrams)

    # Rajouter les codes, leurs liens legifrance et leur version stemmée
    file_codes = 'les_codes_juridiques.csv'
    df_codes = pd.read_csv(file_codes, sep=';')
    # df_codes_tokenise = []
    # df_codes_string = []

    df_codes_tokenise = tokenisation_nom_codes(df_codes)
    df_codes_string = join_tuple(df_codes_tokenise)
    df_codes['code_stemme'] = df_codes_string

    codes_utilises_dans_le_texte = code_utilise(code, df_codes)

    ouvrir_le_code(df_codes)
