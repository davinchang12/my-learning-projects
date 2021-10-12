import json
import string
import re
import random
import math
import pandas as pd

from Sastrawi.Stemmer.StemmerFactory import StemmerFactory

class ChatBot:
    def __init__(self):
        self.stemmer = StemmerFactory().create_stemmer()

        # Cleaning data
        self.df_main = self.process()
        self.input_slangword = []
        self.output_slangword = []

        f = open('data/notNormalized/slangword.txt')
        slangword = f.read()
        f.close()
        slangword = slangword.split('\n')

        for i in range(len(slangword)):
            x , y = slangword[i].split(':')
            self.input_slangword.append(x)
            self.output_slangword.append(y)

    def clean(self, text):
        """
        Return clean data
        """
        text = " ".join([c for c in text if c not in string.punctuation])
        text = text.lower()
        text = re.sub('\W+',' ', text)
        text = re.sub(r'[0-9]', '', text)
        text = re.sub(r'([a-z])\1+', r'\1', text) 
        text = re.findall("[\w']+", text)
        text = [self.stemmer.stem(t) for t in text]   
        text = list(set([t for t in text]))
        text = ' '.join(text)

        return text

    def clean_query(self, text):
        """
        Return clean query
        """
        text = "".join([c for c in text if c not in string.punctuation])
        text = text.lower()
        text = re.sub('\W+',' ', text)
        text = re.sub(r'[0-9]', '', text)
        text = re.sub(r'([a-z])\1+', r'\1', text)  
        text = re.findall("[\w']+", text)

        for i in range(len(text)):
            for j in range(len(self.input_slangword)):
                if(text[i] == self.input_slangword[j]):
                    text[i] = self.output_slangword[j]

        text = [self.stemmer.stem(t) for t in text]
        text = ' '.join(text)

        return text

    def process(self):
        """
        Return combined cleaned data and cleaned query
        """
        file = ['agent.json', 'dialog.json', 'motivasi.json', 'user.json', 'None.json']
        query_raw = []
        responsean_raw = []

        for nama_file in file:
            nama_file = 'data/corpus/corpus/' + nama_file 
            f = open(nama_file, 'r')
            data_total = json.load(f)
            for data in data_total:
                query_raw.append(data['utterances'])
                responsean_raw.append(data['answers'])
            f.close()

        df = {'query':query_raw, 'responsean':responsean_raw}
        df = pd.DataFrame(data=df)

        df['cleaned_query'] = df['query'].apply(self.clean)

        return df

    def bow(self, data, vocab):
        """
        Return bag-of-words of each data
        """
        bow = { i : 0 for i in vocab}
        for v in vocab:
            for t in data.split():
                if t == v:
                    bow[v] += 1
        return bow
        
    def make_vocab(self, data):
        """
        Return vocabulary of the data
        """
        output = list(set([y for x in data for y in x.split()]))
        return output

    def tf(self, text, bows):
        """
        Return TF calculation
        """
        text = text.split()
        tf = {}
        text_len = len(text)
        
        for k, v in bows.items():
            if(text_len != 0):
                tf[k] =  v / float(text_len)
            else :
                tf[k] = 0

        return tf

    def idf(self, vocab, df):
        """
        Return IDF calculation
        """
        idf = { word : 0 for word in vocab }
        len_data = len(df)
        for text in df:
            for t in text.split():
                idf[t] += 1
        
        for k, v in idf.items():
            idf[k] = math.log10(len_data / float(v))
        
        return idf

    def tfidf(self, tf, idf):
        """
        Return TF-IDF calcualtion
        """
        tfidf = {}
        for k, v in tf.items():
            tfidf[k] = v * idf[k]
        
        return tfidf

    def cosine_similarity(self, df):
        """
        Return cosine similarity
        """
        query_index = df.shape[0]
        cosine = []
        query_value = []
        sum_query_value = 0
        for _, v in df.iloc[query_index-1].items():
            query_value.append(v)
            sum_query_value += float(v**2)

        i = 1
        for data in df:
            if i != query_index:
                upper =  0
                lower = 0

                sum_v1 = 0
                i_in = 0
                for _, v in data.items():
                    upper += float(v * query_value[i_in])
                    i_in += 1
                    sum_v1 += float(v**2)
                    
                lower = (sum_v1)**0.5 * (sum_query_value)**0.5
                try:
                    cosine.append(float(upper / lower))
                except ZeroDivisionError:
                    cosine.append(0)
            else:
                cosine.append(0)
            i += 1
        
        # Check if user question is exists on data
        return cosine.index(max(cosine)) if(len(set(cosine)) != 1) else 65

    def response(self, query):
        """
        Return predicted answer
        """
        df = self.df_main.copy()
        query = self.clean_query(query)
        query = {'query':'', 'response':'', 'cleaned_query':query}
        df = df.append(query, ignore_index=True)
        vocab = self.make_vocab(df['cleaned_query'])

        df['p_bow'] = df['cleaned_query'].apply(lambda x : self.bow(x, vocab))  
        temp = []
        for i in range(df.shape[0]):
            temp.append(self.tf(df['cleaned_query'][i], df['p_bow'][i]))
        df['p_tf'] = temp
        p_idf = self.idf(vocab, df['cleaned_query'])
        df['p_tfidf'] = df['p_tf'].apply(lambda x : self.tfidf(x, p_idf))
        idx_cosine = self.cosine_similarity(df['p_tfidf'])

        return random.choice(df['responsean'].iloc[idx_cosine])