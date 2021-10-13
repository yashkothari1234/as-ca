from flask import Flask, jsonify, request
from demographic_filtering import output
from content_filtering import get_recommendations
from storage import all_articles, liked_articles, not_liked_articles


app = Flask(__name__)

@app.route("/get-article")
def get_article():
    article_data = {
        "title": all_articles[0][14],
        "text" : all_articles[0][15],
        "eventType" : all_articles[0][4],
        "lang" : all_articles[0][16]
       
    }
    return jsonify({
        "data": article_data,
        "status": "success"
    })

@app.route("/liked-article", methods=["POST"])
def liked_article():
    articles = all_articles[0]
    liked_articles.append(movie)
    all_articles.pop(0)
    return jsonify({
        "status": "success"
    }), 201

@app.route("/unliked-movie", methods=["POST"])
def unliked_article():
    articles = all_articles[0]
    not_liked_articles.append(articles)
    all_articles.pop(0)
    return jsonify({
        "status": "success"
    }), 201

@app.route("/popular-articles")
def popular_articles():
    article_data = []
    for article in output:
        _d = {
          "eventType" : article[0],
          "title": article[1],
          "text":article[2],
          "lang": article[3],
        }
        movie_data.append(_d)
    return jsonify({
        "data": article_data,
        "status": "success"
    }), 200

@app.route("/recommended-articles")
def recommended_articles():
    all_recommended = []
    for liked_article in liked_articles:
        output = get_recommendations(liked_articles[19])
        for data in output:
            all_recommended.append(data)
    import itertools
    all_recommended.sort()
    all_recommended = list(all_recommended for all_recommended,_ in itertools.groupby(all_recommended))
    article_data = []
    for recommended in all_recommended:
        _d = {
          "eventType" : article[0],
          "title": article[1],
          "text":article[2],
          "lang": article[3],
        }
        article_data.append(_d)


    return jsonify({
        "data": article_data,
        "status": "success"
    }), 200

if __name__ == "__main__":
  app.run()