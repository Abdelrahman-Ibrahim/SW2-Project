from rest_framework.views import APIView
from rest_framework.response import Response
# from bs4 import BeautifulSoup
import requests


# Class Recommend_Quizzes
class Recommend_Quizzes(APIView):
        def get(self, request , UserId): 
            url = 'http://127.0.0.1:8002/userman/'  
            # params = {'userID': UserId }
            skills_Req = requests.get(url , params = {'userID': UserId })
            skill_type = skills_Req.json()
            
            url2 = 'http://127.0.0.1:8003/list/' 
            # params2 = {'skill_type': skill_type}
            List_Req = requests.get(url2 , data = {'skill_type': skill_type})
            quizzes = List_Req.json()
              
            return Response(quizzes)
 
#     def post(APIView)
#         return Response("HI") 
