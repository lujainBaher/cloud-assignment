file_path = "C:/Users/Elsafwa/Downloads/archive/random_paragraphs.txt"  

with open(file_path, 'r') as file:
    content = file.readlines()
    
for line in content[:5]:  
    print(line)

print(type(content))

import nltk
from nltk.corpus import stopwords

nltk.download('stopwords')
nltk.download('punkt')
",".join(stopwords.words('english'))

stop_words=set(stopwords.words('english'))

filtered_sentences = []
for sentence in content:
    words = sentence.lower().split()
    filtered_words = [word for word in words if word not in stop_words]
    filtered_sentence = " ".join(filtered_words)
    filtered_sentences.append(filtered_sentence)

for line in filtered_sentences[:15]:  
    print(line)

from collections import Counter


text = ' '.join(filtered_sentences)
words = text.split()

word_frequency = Counter(words)

for word, frequency in word_frequency.items():
    print(f"Word: {word}, Frequency: {frequency}")