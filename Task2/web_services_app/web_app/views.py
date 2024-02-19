import json

from django.core.paginator import Paginator
from rest_framework import response, status, views

from resources.mongodb import client, mongo

from .serializers import PostListSerializer

db = client.blog
collection = db.posts


class PostListView(views.APIView):

    def get(self, request):

        posts = mongo.select(collection)

        serializer = PostListSerializer(posts, many=True)

        page_size = request.query_params.get('page_size', 20)
        page_num = request.query_params.get('page_num', 1)

        paginator = Paginator(posts, page_size)
        total_items = paginator.count
        total_pages = paginator.num_pages

        if serializer:
            if int(page_num) <= paginator.num_pages:
                serializer = PostListSerializer(
                    paginator.page(page_num), many=True).data
            else:
                serializer = dict(message="no results")

            return response.Response(
                dict(
                    posts=serializer,
                    total_pages=total_pages,
                    total_items=total_items
                )
            )

        return response.Response(
            {"Detail:": "No Database Found."},
            status=status.HTTP_404_NOT_FOUND
        )


class NewPostView(views.APIView):
    def post(self, request):
        data: dict = json.loads(request.body)

        if not data:
            return response.Response(status=status.HTTP_400_BAD_REQUEST)

        if len(data) > 1:
            docs = mongo.insert(collection, data, True)
            if docs:
                # seriliazer = PostListSerializer(docs, many=True)

                return response.Response(status=status.HTTP_201_CREATED)

        doc = mongo.insert(collection, data)

        if doc:
            return response.Response(status=status.HTTP_201_CREATED)

        return response.Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class DeletePostView(views.APIView):

    def delete(self, request):

        post_id = request.query_params.get('post_id', None)

        print(post_id)

        if post_id:

            obj = mongo.delete(collection, post_id)
            if obj:
                return response.Response(status=status.HTTP_204_NO_CONTENT)
            return response.Response(
                {"Detail:": "Post not found."},
                status=status.HTTP_404_NOT_FOUND
            )

        return response.Response(status=status.HTTP_400_BAD_REQUEST)
