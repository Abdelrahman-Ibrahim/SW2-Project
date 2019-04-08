import sys
import os
import pandas

class Recommend_Quizzes(object):
    Quiz_Title = ""
    Quiz_Type = ""
    Quiz_Score = ""
    User_skills= []
    List_of_Quizzes = []
    Recommended_Quizzes = []

    def __init__(self, Title ,Type, Score ,Skills , recom):
        self.Quiz_Title = Title
        self.Quiz_Type = Type
        self.Quiz_Score = Score
        self.User_skills = Skills
        self.Recommended_Quizzes = recom

        for i in range(10):
            self.List_of_Quizzes.append(Recommend_Quizzes(i))

    def recommend(self):
        obj = Recommend_Quizzes(object)
        for x in range(0,len(self.List_of_Quizzes)):
            if  obj.Quiz_Type == obj.User_skills:
                self.Recommended_Quizzes.append(obj.Quiz_Type)




