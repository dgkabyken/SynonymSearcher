import pandas as pd
import numpy as np
import re
import psycopg2
from configparser import ConfigParser
from pymystem3 import Mystem
from django.utils.safestring import mark_safe


conn = psycopg2.connect(host='35.228.159.171', database='postgres', user='postgres', password='zerde9mkr')
cur = conn.cursor()



def read_file(filename):
    with open('{path}/{filename}'.format(path='media/media/', filename=filename), 'r') as inp:
        text = inp.read()
    return text


def get_syn(word):
    cur.execute("SELECT id FROM origin where word = '{}';".format(word))
    if cur.rowcount == 0:
        return []
    id_ = cur.fetchone()[0]
    cur.execute("SELECT syn FROM synonym_update where id = '{}';".format(id_))
    rows = cur.fetchall()
    synonyms = [syn[0] for syn in rows]
    return synonyms


class color:
   PURPLE = '\033[95m'
   CYAN = '\033[96m'
   DARKCYAN = '\033[36m'
   BLUE = '\033[94m'
   GREEN = '\033[92m'
   YELLOW = '\033[93m'
   RED = '\033[91m'
   BOLD = '\033[1m'
   UNDERLINE = '\033[4m'
   END = '\033[0m'


def get_syn_pos(word, text):
    list_text = [word for word in text.split(' ')]

    synonyms = get_syn(word)
    synonyms.append(word)
    t = ''
    for syn in synonyms:
        t += syn + ' '
    tmp = ''.join(Mystem().lemmatize(t)).strip('\n')[:-1]
    synonyms = [i for i in tmp.split(' ')]

    lemmas = Mystem().lemmatize(text)
    inf_text = ''.join(lemmas).strip('\n')
    clean_inf_text = [re.sub(r'[.,!"@#$%]', '', word) for word in inf_text.split(' ')]
    result = ''

    for i, word in enumerate(clean_inf_text):
        if word in synonyms:
            result += '<mark>' + list_text[i] + '</mark>' + ' '
        else:
            result += list_text[i] + ' '
    return mark_safe(result)