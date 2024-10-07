import string

def create_hashtag(sentence):
    cleaned_sentence = sentence.translate(str.maketrans('', '', string.punctuation)).split()

    capitalized_words = [word.capitalize() for word in cleaned_sentence]

    hashtag = "#" + "".join(capitalized_words)

    if len(hashtag) > 140:
        hashtag = hashtag[:140]

    return hashtag
