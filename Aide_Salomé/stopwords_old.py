#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 14 16:18:39 2022

@author: salomeouaknine
"""
import requests
from bs4 import BeautifulSoup
import pickle
import pandas as pd
import numpy as np
import re #regular expression
from re import search
#import string 
import nltk
from nltk.tokenize import word_tokenize
from nltk.probability import FreqDist
from nltk.stem import SnowballStemmer



link = '.'
document = '/JORFARTI000045294276.xml'

#1. Recuperer le document
def link_to_transcript(link):
    page = open(link)
    soup = BeautifulSoup(page, "lxml")
    text = [p.text for p in soup.find_all('p')] 
    #code = soup.find_all(text = "code")
    return text

texte = link_to_transcript(link + document)

def combine_text(list_of_text):
    '''Takes a list of text and combines them into one large chunk of text.'''
    combined_text = ' '.join(list_of_text)
    return combined_text

data_combined = combine_text(texte) #concaténation de tout le texte

pd.set_option('max_colwidth',150)


#2. Nettoyer les donnees
def clean_text_round1(text):
    #text = text.lower()
    #text = re.sub('\[.*?\]', '', text) #enlever les données dans les [] dans le texte
    #text = re.sub('[%s]' % re.escape(string.punctuation), '', text) #enlever toutes les ponctuations 
    #text = re.sub('\w*\d\w*', '', text) #enlever tous les noms possédant des chiffres à l'intérieur
    #text = re.sub('[‘’“”…]', '', text)
    return text

#data_combined_clean = clean_text_round1(data_combined)
stop_words = set(nltk.corpus.stopwords.words('french'))


#3. Tokeniser

def tokenizer (text) : 
    sentence_tokens = word_tokenize(text)
    return(sentence_tokens)

sentence_tokens = tokenizer(data_combined)
sentence_tokens = [word for word in sentence_tokens if not word.lower() in stop_words]


fdist = FreqDist()
for word in sentence_tokens :
    fdist[word.lower()]+=1

quote_ngrams = list(nltk.ngrams(sentence_tokens, 6)) #(mots, groupes)


#print(quote_ngrams)


#4. Chercher les mots permettant de remplacer 
##4.1 essayer la stemmatisation 
pst=SnowballStemmer('french')
stem_words = []
for w in sentence_tokens:
    x = pst.stem(w)
    stem_words.append(x)

##Tester l'action du texte
def action_du_texte (stem) : 
    if (pst.stem('remplace')) in stem: 
        print('remplacement')
    if (pst.stem('modification')) in stem: 
        print('modification')
    if (pst.stem('abroge')) in stem: 
        print('abrogation')
    if (pst.stem('supprime')) in stem: 
       print('suppression')
    if (pst.stem('ajoute')) in stem: 
        print('ajout') 
    if (pst.stem('création')) in stem: 
        print('création')


#5. Chercher les codes cités 

def join_tuple (tuple_list) : 
    string_list = []
    for x in tuple_list :
        y = ' '.join(x)
        string_list.append(y)
    return string_list

### Preparer les references des codes dans le texte de loi 
def code_present_texte_loi (ngram) :
    code_dans_ngram = [] 
    for tupleobj in ngram : 
        if tupleobj.count('code') > 0 : 
            if (tupleobj[2] == 'code') and (tupleobj[1] != 'présent'):
                code_dans_ngram.append(tupleobj[3])
        
    return code_dans_ngram

def article_et_code_dans_meme_tuple (ngram) :
    article_et_code_dans_ngram = [] 
    for tupleobj in ngram : 
        if tupleobj.count('code') > 0 : 
            if (tupleobj[2] == 'code') and (tupleobj[1] != 'présent'):
                article_et_code_dans_ngram.append(tupleobj)
        
    return article_et_code_dans_ngram


code = code_present_texte_loi(quote_ngrams)
#code_str = join_tuple(code)

article_et_code_tuple = article_et_code_dans_meme_tuple(quote_ngrams)


### Rajouter les codes, leurs liens legifrance et leur version stemmée 
file_codes = 'les_codes_juridiques.csv'
df_codes = pd.read_csv(file_codes, sep=';')
df_codes_tokenise = []
df_codes_string = []

def tokenisation_nom_codes (df_codes): 
    df_codes_tokenise = []
    for index in df_codes.index : 
        x = df_codes.loc[index]['nom_du_code']
        x = re.sub(r'[^\w\s]',' ',x) #enlever la ponctuation, surtout les apostrophes 
        x = re.sub(r'Code', '', x) #enelever le mot code permet d'avoir l'essentiel
        x = tokenizer(x)
        y = [word for word in x if not word.lower() in stop_words]
        df_codes_tokenise.append(y)
    return(df_codes_tokenise)
  
df_codes_tokenise = tokenisation_nom_codes(df_codes)
df_codes_string  = join_tuple(df_codes_tokenise)
df_codes['code_stemme'] = df_codes_string

### Trouver le(s) code(s) utilisé(s) dans le texte 

def code_utilise (liste_codes_dans_texte_loi, df_codes) :
    codes_utilises_dans_le_texte = []
    for y in liste_codes_dans_texte_loi : 
       for x in df_codes["code_stemme"] : 
           if search(y, x):
               codes_utilises_dans_le_texte.append(x)
    return(codes_utilises_dans_le_texte)

codes_utilises_dans_le_texte = code_utilise(code, df_codes)



#6. Ouvrir le code 

def ouvrir_le_code (df_codes) :
    #for x in codes_utilises_dans_le_texte : #remplacer ligne dessous "consommation" par x
    loc_code_cite = df_codes.loc[df_codes['code_stemme'] == "consommation"]
    url_liste = loc_code_cite['lien'].tolist()
    url = url_liste[0]
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'lxml')
    title = soup.findAll('head')
        #    soup = BeautifulSoup(html_file, 'lxml')
    print(title)

      

ouvrir_le_code (df_codes) 

#7. Recuperer l'article

 
