from rest_framework.views import APIView
from rest_framework.response import Response
# from bs4 import BeautifulSoup
import json
import requests

#admin panel in django
# Class Recommend_Quizzes
class Recommend_Quizzes(APIView):
        def get(self, request ,UserId):
            url = 'http://127.0.0.1:8002/userman/' + str(UserId)
            skills_Req = requests.get(url)
            skill_type = skills_Req.json()
            # userId = request.query_params.get("UserId")
            # ?key=vaue
            url2 = 'http://127.0.0.1:8003/list/' + skill_type['skill_type']
            List_Req = requests.get(url2)            # List_Req = requests.get(url2, params={"UserId": UserId})
            quizzes = List_Req.json()
              
            return Response(quizzes)



 
#     def post(APIView)
#         return Response("HI") 
