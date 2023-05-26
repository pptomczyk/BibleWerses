import os
import shutil

def zamien_znaki(txt):
    zamiana = {
        'ą': 'a', 'ć': 'c', 'ę': 'e', 'ł': 'l', 'ń': 'n',
        'ó': 'o', 'ś': 's', 'ź': 'z', 'ż': 'z', 'Ą': 'A',
        'Ć': 'C', 'Ę': 'E', 'Ł': 'L', 'Ń': 'N', 'Ó': 'O',
        'Ś': 'S', 'Ź': 'Z', 'Ż': 'Z'
    }
    for znak, zamieniony_znak in zamiana.items():
        txt = txt.replace(znak, zamieniony_znak)
    return txt

def zmien_zawartosc_katalogu(katalog_wejsciowy, katalog_wyjsciowy):
    if not os.path.exists(katalog_wyjsciowy):
        os.makedirs(katalog_wyjsciowy)

    for plik in os.listdir(katalog_wejsciowy):
        sciezka_pliku_wejsciowego = os.path.join(katalog_wejsciowy, plik)
        if os.path.isfile(sciezka_pliku_wejsciowego):
            nazwa_pliku, rozszerzenie = os.path.splitext(plik)
            if rozszerzenie == '.txt':
                sciezka_pliku_wyjsciowego = os.path.join(katalog_wyjsciowy, nazwa_pliku + rozszerzenie)
                with open(sciezka_pliku_wejsciowego, 'r', encoding='windows-1250') as plik_wejsciowy:
                    zawartosc = plik_wejsciowy.read()
                    nowa_zawartosc = zamien_znaki(zawartosc)
                    with open(sciezka_pliku_wyjsciowego, 'w', encoding='utf-8') as plik_wyjsciowy:
                        plik_wyjsciowy.write(nowa_zawartosc)

# Przykładowe użycie
katalog_wejsciowy = 'C:/python/projects/TheBible/biblia_podzielona'
katalog_wyjsciowy = 'C:/python/projects/TheBible/test'

zmien_zawartosc_katalogu(katalog_wejsciowy, katalog_wyjsciowy)
