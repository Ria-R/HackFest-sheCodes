# -*- coding: utf-8 -*-
"""resume_parse.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/16XnIOoTIO8wMxFsjQR3_NRe17ddqX3bl
"""

!pip install pyresparser
!pip install spacy==2.3.5
!pip install https://github.com/explosion/spacy-models/releases/download/en_core_web_sm-2.3.1/en_core_web_sm-2.3.1.tar.gz

import nltk
nltk.download('stopwords')
from pyresparser import ResumeParser
data = ResumeParser('insert_pdf.pdf').get_extracted_data()
print(data)