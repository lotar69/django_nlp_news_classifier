import re
from app_nlp_news_classifier.forms import ArticleForm
from django.shortcuts import render
from joblib import load
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer

tfidf_vectorizer = load(
    r"C:\Users\lotar\Desktop\projets\00.django_projects\django_nlp_news_classifier\src\saved_models\tfidf_vectorizer"
    r".joblib")

multinomial_nb_classifier = load(
    r"C:\Users\lotar\Desktop\projets\00.django_projects\django_nlp_news_classifier\src\saved_models"
    r"\multinomial_nb_classifier.joblib")


# Create your views here.
def index(request):
    article = ArticleForm()

    if request.method == "POST":
        if article.is_valid():
            article.save()

    return render(request, "index.html", {"form": article})


def result(request):
    article = request.GET.get("article", "")
    ps = PorterStemmer()
    new_corpus = []
    review = re.sub("[^a-zA-Z]", " ", article)
    review = review.lower()
    review = review.split()
    review = [ps.stem(word) for word in review if word not in stopwords.words("english")]
    review = " ".join(review)
    new_corpus.append(review)
    article_vectorized = tfidf_vectorizer.transform(new_corpus)
    article_pred = multinomial_nb_classifier.predict(article_vectorized)

    if article_pred == [0]:
        article_pred = "Cet article est une Fake News."
    else:
        article_pred = "Cet article est authentifié."

    return render(request, "result.html", {'article_analyzed': article_pred})
