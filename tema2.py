import string
text="""Peste 100 de mii de microîntreprinderi
            nu știu cum vor fi taxate în viitor."""
jumatate = len(text) // 2#am injumatatit fraza
text_1 = (text[0:jumatate])#am declarat prima parte a frazei
text_1 = text_1.upper()#am facut majuscule
text_1 = text_1.replace(" ","")#fara spatii
text_2 = (text[jumatate:])#de la jumatatea frazei la final
text_2 = text_2[::-1]#am inversat ordinea caracterelor
text_2 = text_2[0] + text_2[1].upper() + text_2[2:]#prima litera transformata in majuscula
text_2 = text_2.translate(str.maketrans("","",string.punctuation))#eliminarea semnelor de punctuatie
text_mare = text_2 + text_1#lipirea celor 2 siruri(prima jumatate si cea de a doua)
print(text_mare)