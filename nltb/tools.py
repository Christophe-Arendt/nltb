#-------------------------------------------------------
#   Natural Language Processing TOOLS
#-------------------------------------------------------

from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
import string
import unidecode
from nltk.stem import WordNetLemmatizer
from sklearn.feature_extraction.text import CountVectorizer
from nltk.stem.porter import PorterStemmer
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
import nltk
from nltk.corpus import wordnet

#-------------------------------------------------------

try:
  nltk.data.find('punkt')
  nltk.data.find('stopwords')
  nltk.data.find('averaged_perceptron_tagger')
  nltk.data.find('wordnet')
except LookupError:
  nltk.download('punkt', quiet=True)
  nltk.download('stopwords', quiet=True)
  nltk.download('averaged_perceptron_tagger', quiet=True)
  nltk.download('wordnet', quiet=True)

#-------------------------------------------------------


def get_wordnet_pos(word):
    tag = nltk.pos_tag([word])[0][1][0].upper()
    tag_dict = {"J": wordnet.ADJ,
                "N": wordnet.NOUN,
                "V": wordnet.VERB,
                "R": wordnet.ADV}
    return tag_dict.get(tag, wordnet.NOUN)


def text_cleaning(text, regroup='POS-Lemmatizing', language='english', output='token'):
    """
    Natural Language Processing Text Cleaning Function,
    Choose language, and regrouping technique

    # Arguments
    text : string text
    regroup : Different techniques to stem or lemmatize
      options > [Lemmatizing, POS-Lemmatizing, Stemming]
    language : Language for stop-words
      options : ['en', etc.]
    output : Type of output
      options [text, token]
    """
    # Lower case
    text = text.lower()
    # Remove digits
    text = text.translate(str.maketrans('', '', string.digits))
    # Remove punctuation
    text = text.translate(str.maketrans('', '', string.punctuation))
    # Remove accents
    text = unidecode.unidecode(text)

    # Remove Stopwords
    stop_words = stopwords.words(language)
    word_tokens = word_tokenize(text)
    token = [word for word in word_tokens if not word in stop_words]

    # Stemming or Lemmatizing
    if regroup == 'Lemmatizing':
        lemmatizer = WordNetLemmatizer()
        token = [lemmatizer.lemmatize(w) for w in token]
    if regroup == 'POS-Lemmatizing':
        lemmatizer = WordNetLemmatizer()
        token = [lemmatizer.lemmatize(w, get_wordnet_pos(w)) for w in token]
    if regroup == 'Stemming':
        stemmer = PorterStemmer()
        token = [stemmer.stem(w) for w in text]

    # type of output
    if output == 'text':
        return "".join(text)
    else:
        return token


if __name__ == '__main__':
  text = '999 Football is my passion. I love to play with footballs!! Who else loves football?,  matching, matcher the match. the butcher butches the butchery'
  clean = text_cleaning(text, regroup='POS-Lemmatizing',
                language='english', output='text')
  print('##### Example Text dirty #####')
  print(text)
  print('##### Example Text cleaned #####')
  print(clean)

