from django import forms
import nltk
from nltk.tokenize import word_tokenize
from nltk.tag import pos_tag
from django.db import models
import spacy

nltk.download('averaged_perceptron_tagger')
nlp = spacy.load("en_core_web_sm")

class Metin(forms.Form):
    icerik = forms.CharField(widget=forms.Textarea,label=False)
    icerik.widget = forms.Textarea(attrs={'placeholder': 'Metin'})
    secenek = (('secimyapiniz','Seçim Yapınız...'),('fiiller', 'Fiiller'),('isimler', 'İsimler'),)
    secenekliste = forms.ChoiceField(choices=secenek,label=False)

    def tur_getir(self):
        return str(self.data['secenekliste'])

    def fiiller_getir(self):
        words = word_tokenize(str(self.data['icerik']))
        tagged_words = pos_tag(words)
        verbs = [word for word, tag in tagged_words if tag.startswith('VB')]
        return verbs

    def isimler_getir(self):
        doc = nlp(str(self.data['icerik']))
        names=[entity.text for entity in doc.ents if entity.label_ == "PERSON"]
        return names
