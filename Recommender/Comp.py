from rest_framework.views import APIView
from rest_framework.response import Response

# # Class Recommend_Companies    
class Recommend_Companies(APIView):
    def get(self, request):
        return Response("Companies")

# #     def post(APIView)
# #         return Response("HI")
