#!/usr/bin/python
# ladfx version 0.2.5

import os
import time
import shutil
import bz2
import re
from os import listdir
from os.path import isfile, join, getatime
from datetime import datetime, timedelta

# Fonction nécéssaire pour la récursivité utilisée pour atteindre les sub-folers de l'arborescence
def fladfx(path):
    # Boucle de génération de la listes des fichiers
    for file in os.listdir(path):
        # Définition variable f : file. 
        # f : concaténation chemin absolue et nom de fichiers (join : concatenation)
        f = os.path.join(path, file)
        # Condition de génération de la liste des fichiers 
        if os.path.isdir(f):
            fladfx(f)
        if os.path.isfile(f):
            # -----------------------------------------------
            # Exclusion du traitement : ex > zip, iso, ...
            # re : Regular Expression - search : recherche dans toute la chaine
            # re.search(pattern, str) - je ne trouve pas de solution pour recherche 
            # de plusieurs patterns dans la même ligne
            exc1 = re.search(".*\.zip$", f)
            exc2 = re.search(".*\.iso$", f)
            # if (cond1 AND/OR COND2) AND/OR (cond3 AND/OR cond4):
            if (exc1) or (exc2):
                continue
                # Si besoin affichage détection fichiers ZIP ou ISO.
                # Décommenter la ligne ci-dessous :
                # print("FICHIER ZIP ou ISO")
            # ------------------------------------------------
            # Affichage des fichiers cible en chemin absolu depuis racine
            print(f)
            # Déf variable : time_up_to_deadline : durée jusqu'à la date limite
            # La date lim étant la date en deça ou au dessus de laquelle l'action est effectuée.
            time_up_to_deadline = 4
            # Date actuelle au format datetime : 
            # ex : 2021-05-10 12:32:11.503663
            dat_now = datetime.now()
            # Affichage de la date date locale actuelle format datetime
            print("Date actuelle :  ", dat_now)
            # Déf variable : date lim cible en deça ou au dessus de laquelle l'action est effectuée. 
            # timedelta : intervalle de temps soustrait à la date actuelle.
            # class datetime.timedelta(days=0, seconds=0, microseconds=0, 
            # milliseconds=0, minutes=0, hours=0, weeks=0)
            dat_lim_j = dat_now - timedelta(days = time_up_to_deadline)
            # Affichage de la date limite cible 
            print("Date lim. cible :", dat_lim_j)
            # Conversion date limite en seconde = format "epoch"
            dat_lim_j_in_sec = dat_lim_j.timestamp()
            # Si besoin affichage date limite en seconde = format "epoch"
            # décommenter ligne ci-dessous :            
            print("Date limite epoch :  ", dat_lim_j_in_sec)  
            # Définition de la variable de date de dernière consultation format epoch
            access_time = getatime(f)
            # Si besoin d'afficher dernière date d'accès en sec depuis "epoch"
            # décommenter la ligne => print [...] access_time, ci-dessous
            print("Der. consult. epoch :", access_time)
            # Définition de la variable date de dernière consultation 
            # en temps local au format ctime 
            # ex : Thu Apr 29 15:26:26 2021
            local_time = time.ctime(access_time)
            # Affichage de la date locale de dernière consultation en format ctime 
            # ex : Thu Apr 29 15:26:26 2021
            print("Der. consult. :", local_time)
            # -------------------------------------------------
            # Conditions déclenchant les actions :
            # Cond 1 : si date de der. consult. dépasse (antérieur) à date limite 
            if access_time < dat_lim_j_in_sec: # Renvoi True ou False 
                print("Der. consult. du fichier antérieur à date limite :", 
                access_time < dat_lim_j_in_sec) # Renvoi True ou False
                print(">>>>> A archiver ! <<<<<" + '\n') 
                # ----------------------------------------------
                # Archivage & compression : module shutil
                # base_dir=os.path.basename(f) : permet d'archiver / compresser que le fichier seul (sans l'arbo)
                shutil.make_archive(base_dir=os.path.basename(f), root_dir=path + '/', format='zip', base_name=f)  
                # ----------------------------------------------
                # Suppression du fichier original (non archivé / compréssé)              
                os.remove(f)
            # -------------------------------------------------
            # Cond 2 : autrement si date de der. consult. pas antérieur à la date lim 
            elif access_time > dat_lim_j_in_sec:                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 
                print("Der. consult. du fichier antérieur à date limite :", 
                access_time < dat_lim_j_in_sec) # Renvoi True ou False
                print(">>>>> Ne pas archiver ! <<<<<" + '\n') 

path = '/home/guillerbe/Documents/DossFichiers'
fladfx(path)