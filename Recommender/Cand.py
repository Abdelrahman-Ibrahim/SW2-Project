from rest_framework.views import APIView
from rest_framework.response import Response

class Recommend_Candidates(APIView):
        def get(self, request):
            
         url = 'http://127.0.0.1:8002/userman/'   #Get the id of the company when it's logged 
         # params = {'userID': UserId }
         Company_ID = requests.get(url)
         CId = Company_ID.json()

         url = 'http://127.0.0.1:8002/userman/comp/'     #Get list of all candidates that matches with it's interests
         Candidates = requests.get(url)
         List_Candidates = Candidates.json()  

         return Response(List_Candidates)

#     def post(APIView)
#         return Response("HI")
