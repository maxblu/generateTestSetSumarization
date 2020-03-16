import streamlit as st
import nltk
import json

with open("Examples.txt", encoding='utf-8') as fd:
    example_news =fd.read().split('****')

index = st.selectbox('Examples', range(len(example_news)))

text = example_news[index]

sentences =  nltk.tokenize.sent_tokenize(text,language='spanish')

order = []

for i,j in zip(range(len(sentences)),sentences):
    str(i)+" : " +j
    # number = st.sidebar.number_input(value=0,label='Sentence# '+str(i) ,min_value=-1,max_value=len(example_news))
    number = st.sidebar.checkbox("Sentence# "+str(i))
    # if number == -1 :
        # continue
    if not number:
        continue
    # order.append((number,j))
    order.append((i,j))


# st.write(len(sentences))
# st.write(len(order))
order.sort(key= lambda order : order[0] )


if st.button("Save"):
    with open("summary"+str(index)+".json" ,'w',encoding='utf-8') as fd:
        json.dump(order,fd)

# with open("summary "+str(index)+".json",'r',encoding='utf-8') as fd:
#     order = json.load(fd)

# order

