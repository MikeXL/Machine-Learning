mport pandas as pd

import sys
print sys.version


import nltk

help(nltk.download)
nltk.download('all-corpora')

from nltk.corpus import state_union

state_union.words()
len(state_union.words())

sentences = state_union.sents()
print sentences

state_union_text = nltk.Text(state_union.words())
print state_union_text.count("war")
state_union_text.concordance("economy")
state_union_text.similar("economy")
state_union_text.common_contexts(["economy", "jobs"])

from nltk.probability import FreqDist

fdist = FreqDist(state_union_text)
result = fdist.most_common(15)
result


from nltk.corpus import stopwords
stopwords.words("english")


filtered = [w for w in state_union.words() if not w in stopwords.words("english")]
len(filtered)


fdist_filtered = FreqDist(filtered)
fdist_filtered.most_common(20)


fdist_filtered.freq("good")/fdist_filtered.freq("bad")
fdist_filtered.freq("bad")/fdist_filtered.freq("evil")


fdist_filtered.plot(30)

