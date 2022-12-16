from main import df
import pandas as pd
# st="asia i kasia"
#
# if "asia" in st:
#     print("yes")

text_full = df['text_full']

df.dropna(inplace=True)
lista_keywords = ['powierzchni m', 'samo przewinienie', 'dawkach dziennych', 'godzinach nadliczbowych', 'jaki sposób', 'których mowa', 'której mowa', 'którym mowa', 'rozwiązaniu umowy', 'miesiącu lipcu', 'wymiarze dni', 'kształcie litery', 'hotelu pracownikom', 'spadku przypadnie', 'wartości spadku', 'aktu notarialnego', 'samodzielnej pracy', 'jest oddelegowaniem', 'formie oddelegowania', 'odbywaniu dyżurów', 'charakterze świadka', 'innym oddziale', 'wykreślenie wpisu', 'tygodniu pracująca', 'co dalej', 'trakcie pracy', 'miejscu wskazanym', 'sądzie wniosek', 'podmiocie zewnętrznym', 'wypowiedzeniu umowy', 'trakcie postępowania', 'wypowiedzenie umowy', 'niepodjęciu leczenia', 'ramach której', 'ustalonych dniachgodzinach', 'zaistniałej sytuacji', 'innych miejscach', 'podwójnej dawce', 'można wystąpić', 'planie urlopowym', 'późniejszym czasie', 'obydwu lokalizacjach', 'udzielenie urlopu', 'zakładzie pracy', 'do stycznia', 'zakresie pośrednictwa', 'świetle przepisów', 'opinii prawnej', 'sądzie co', 'jej istnieniu', 'jaką informację', 'niedziele co', 'określonym terminie', 'ramach zgłoszenia', 'ust umowy', 'nabyciu spadku', 'hurtowniach spożywczych', 'wiadomości czy', 'tygodniu czy', 'terminie czy', 'polsce czy', 'operacji czy', 'przypadku gdy', 'przypadku złożenia', 'dniu grudnia', 'przypadku zajścia', 'szpitalu zakaźnym', 'szpitalu covidowym', 'pracę bądź', 'pracę informując', 'sprawie standardów', 'aptece przypadającego', 'ciążę czy', 'pracę czy', 'czy', 'przypadku', 'ciążę', 'dniu', 'szpitalu', 'pracę', 'sprawie', 'aptece', 'okresie', 'latach', 'umowę', 'będzie', 'oparciu', 'umowie', 'izolacji', 'ustawy', 'możliwe', 'ciąży', 'całości', 'zachowek', 'ustawie', 'domu', 'rejestracji', 'pomoc', 'jak', 'roku', 'interwencję', 'systemie', 'opiniach', 'prace', 'gotowości', 'szkodzie', 'firmie', 'pozwie', 'wchodzi', 'współpracę', 'kilometrówce', 'sobotę', 'przeszłości', 'sygn', 'prokuraturze', 'poniedziałki', 'współpracy', 'szkoleniu']

# print(df.iloc[df['text_full']=='%powierzchni m%'])


for i in range(len(lista_keywords)):
    contain_values = df[df['text_full'].str.contains(lista_keywords[i])]
    print(contain_values.index)
