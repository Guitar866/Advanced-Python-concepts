from nltk.stem import SnowballStemmer

stemmer = SnowballStemmer("english")

words = ["playing", "played", "plays", "running", "runs"]

for word in words:
    print(word, ":", stemmer.stem(word))