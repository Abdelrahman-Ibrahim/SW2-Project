from rest_framework.views import APIView
from rest_framework.response import Response
import json

# # Class Recommend_Companies to candidates

class Recommend_Companies(APIView):
    C_obj= Companies()
    def get(self, request):

         url = 'http://127.0.0.1:8002/userman/'   #Get the id of the user when he logins 
         # params = {'userID': UserId }
         candidate_ID = requests.get(url)
         CId = candidate_ID.json()

        url = 'http://127.0.0.1:8002/userman/comp/'     #Get list of all companies that matches with his skills
        Companies = requests.get(url)
        List_Companies = Companies.json()  #Convert JSON array to Python list

         return Response(List_Companies)

# #     def post(APIView)
# #         return Response("HI")
