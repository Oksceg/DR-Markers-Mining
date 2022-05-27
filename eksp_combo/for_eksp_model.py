import re

d = {}
with open('C:/Users/Ксюша/Downloads/cval_prob1eksp.txt', 'r', encoding="utf-8") as inp:
    for i in inp.readlines():
        try:
            key,val = i.strip().split(':')
            d[key] = float(val)
        except:
            pass

top160 = []
for k in list(d.keys())[:160]:
    top160.append(k)
top_set = list(set(top160))

t = []
with open("C:/ФИКЛ/Курсовая Извлечение Коннекторов/news_data.txt", 'r', encoding="utf-8") as f:
    for line in f:
        cleaned_snt = re.sub(r'[^\w\s\.]','', line)
        cleaned_snt = cleaned_snt.replace(' - ', ' ')
        noenters_snt = cleaned_snt.replace('\n', ' ')
        whole_snt = noenters_snt.replace('  ', ' ')
        t.append(whole_snt.lower())

t_ = [snt for snt in t if snt != " "]

text_with_uc = []
for sent in t_:
    for cnct in top_set:
        if cnct in sent:
            sent = sent.replace(cnct, cnct.replace(" ", "_"))
    text_with_uc.append(sent)

with open("for_model_eksp.txt", "w", encoding = 'utf-8') as f:
    for line in text_with_uc:
        f.write(line)
        f.write('\n')
