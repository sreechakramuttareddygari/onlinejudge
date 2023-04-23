from django.db import models
# ■ User:
#   UserID: CharField, Primarykey
#             ■ Problems:
#   ProblemID : Int, Primarykey
#   Statement : CharField
#   Difficulty    : CharField
#             ■ Testcases:
#                           testcaseID: Int, Primarykey
#                           ProblemID: Int, Foriegnkey
#                           Input         : CharField
#                           Output      : CharField
#             ■ Solutions:
#    SolutionID               : CharField, Primarykey
#    ProblemID              : Int, Foreignkey
#    UserID                    : Int, Foreighkey
#    Submitted_at           : Timestamp
#    Failed_test_case    : Int, Foreignkey
#    succededTestcases: Int
#    (count)
#    Time_taken             : Time
#    Verdict                     : boolean
#

# Create your models here.
class User(models.Model):
    UserID = models.CharField(max_length=200,primary_key = True)

class Problems(models.Model):
    ProblemID= models.IntegerField(primary_key = True)
    ProblemName = models.CharField(max_length=200)
    Statement = models.CharField(max_length=1000)
    Difficuly = models.CharField(max_length=30)

class Testcases(models.Model):
    testcaseID = models.IntegerField(primary_key = True)
    ProblemID  = models.ForeignKey(Problems, on_delete=models.CASCADE)
    Input     = models.TextField(null=True)
    Output    = models.TextField(None)

class Solutions(models.Model):
    SolutionID = models.CharField(max_length=200,primary_key = True)
    ProblemID = models.ForeignKey(Problems,on_delete = models.SET_NULL,null=True)
    UserID = models.ForeignKey(User, on_delete=models.CASCADE,null=True)
    Submitted_at = models.DateTimeField(auto_now=False,auto_now_add=False,null=True)
    Failed_test_case = models.ForeignKey(Testcases,on_delete = models.SET_NULL,null=True)
    succededTestcases = models.IntegerField
    Time_taken = models.TimeField(auto_now=False, auto_now_add=False)
    Verdict = models.BooleanField(default=False)
