from rest_framework.views import APIView
from rest_framework.response import Response


# Class Recommend_Quizzes
class Recommend_Quizzes(APIView):
    def get(self, request):
        return Response("Quizzes")

#     def post(APIView)
#         return Response("HI")