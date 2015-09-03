import nltk,re,os
from nltk.corpus import wordnet as wn
#Lossy text compression using a thesaurus

print "File size originally: " , float(os.path.getsize('Sample.txt')) / 1048576, "MB"
with open('Sample.txt','r') as f, open('Output.txt', 'w+') as O:
    for line in f:
        for word in line.split():
            punctuation = []
            l = []
            if "." in word:
                word = word.replace(".","")
                punctuation.append(".")
            elif "," in word:
                word = word.replace(",","")
                punctuation.append(",")
            
            l.append(word)
            word = str(word).decode('utf-8')

            for ss in wn.synsets(word):
                for sim in ss.similar_tos():
                    sim = re.sub("Synset\('","", str(sim))
                    m = re.sub(".\w.\d\d'\)","", str(sim))
                    l.append(m)
            if len(punctuation) != 0:
                O.write(str(min(l, key=len) + punctuation[0]) + " ")
            else:
                O.write(str(min(l, key=len)) + " ")
print "File size after lossy compression: " , float(os.path.getsize('Output.txt')) / 1048576, "MB"
