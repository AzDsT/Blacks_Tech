#!/usr/bin/env python
# coding: utf-8

# In[10]:


get_ipython().system('pip install spacy')
import spacy


# In[16]:


import spacy  
get_ipython().system('python -m spacy download xx_ent_wiki_sm   ')
from spacy import displacy  


# In[27]:


def extract_entities(text,lang_code):
    nlp = spacy.load(lang_code)
    doc = nlp(text)
    entities = []
    for ent in doc.ents:
        entities.append({'text':ent.text, 'type':ent.label_ , 'start_pos':ent.start_char, 'end_pos':ent.end_char})
        return entities
text = "Das ukrainische Regierung hat keine Hoffnung, in den Trümmern des von einer Rakete zerstörten Hochhauses noch Überlebende zu finden. Präsident Selenskij hofft auf weitere Hilfszusagen vom Weltwirtschaftsforum in Davos und von einem Treffen in Ramstein."
lang_code = "xx_ent_wiki_sm"
entities = extract_entities(text,lang_code)
print(entities)


# In[ ]:




