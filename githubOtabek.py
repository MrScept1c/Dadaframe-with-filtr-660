# -*- coding: utf-8 -*-
"""Untitled0.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/15sSygglyW8lxG45T5Mnx7yiWm5hYu-Px
"""



import pandas as pd
baza={
    "FISH": [ "Aliyev Ali", "Murodjonov Khasanboy", "Karimov", "Abdusalomov", "Ergashev", "Obidjonov", "Asqarova", "Egamberdiyev", "Abdullayeva", "Jobs"],
    "Yoshi": ["11", "18", "18", "20", "20", "19", "30", "35", "25", "50"],
    "Jinsi": ["erkak", "erkak", "erkak", "erkak", "erkak", "erkak", "ayol", "erkak", "ayol", "erkak"],
    "Maktabi": ["2-maktab","3-maktab","4-maktab","5-maktab","6-maktab","7-maktab","8-maktab","9-maktab","10-maktab","1-maktab" ],
    "Manzili": ["Farg'ona shahar","Farg'ona shahar","Oltiariq tumani","Andijon shahar","Farg'ona shahar","Farg'ona shahar","Farg'ona shahar","Farg'ona shahar","Toshkent","San Fransisco"],
    "Tel raqami": ["99 302 22 12","93 242 62 72","99 232 11 167","92 789 23 12","93 302 55 22","99 999 22 12","99 345 67 12","99 323 78 12","93 323 45 12","1 111 11 11",]
}
filtr=db[db['Jinsi']=="erkak"]
filtr=db[db['Yoshi']<"20"]
filtr=db[db['Manzili']=="Farg'ona shahar"]
print(filtr)

filtr=db[(db['Jinsi']=="erkak") & (db['Yoshi']<"20") & (db['Manzili']=="Farg'ona shahar")]
print(filtr)