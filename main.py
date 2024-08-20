meme_dict = {
            "LOL": "Sesli güldüm anlamında kullanılınır" ,
              "CRINGE" : "Utanmak tiksinmek anlamında kullanılır" ,
               "AGGRO" : "Sinirlenmek Tartışma başlatmak"
              }

word = input ("Anlamadığınız bir kelimeyi yazınız Lütfen tüm kelimeleri büyük yazınız!")

if word in meme_dict.keys():
    print(meme_dict[word])
else:
    print('Uzgunuz bu kelıme henuz sozlukte yok.')
