from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import parser_classes, api_view
from rest_framework import parsers
import json
from articles.models import User, Article
from articles.serializers import ArticleSerializer

@parser_classes([parsers.FileUploadParser])
@api_view(["POST"])
def fileUpload(request):
    file_obj = request.data
    articlesJson = json.loads(file_obj["file"].open().read())
    articles = []
    for article in articlesJson:
        user = User.objects.get_or_create(id=int(article["userId"]))[0]
        art = Article(title=article["title"], body=article["body"], user=user)
        articles.append(art)
    res = Article.objects.bulk_create(articles)
    return Response({"data": {"message": "Done! data inserted"}}, status=status.HTTP_200_OK)

@api_view(["GET"])
def getArticles(request):
    articles = Article.objects.all()
    data = []
    for article in articles:
        data.append(ArticleSerializer(article).data)

    return Response({"data": data}, status=status.HTTP_200_OK)
