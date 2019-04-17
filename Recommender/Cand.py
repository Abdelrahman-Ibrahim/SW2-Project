from rest_framework.views import APIView
from rest_framework.response import Response

class Recommend_Candidates(APIView):
        def get(self, request):
            return Response("Candidates")

#     def post(APIView)
#         return Response("HI")
