from rest_framework import serializers
from .models import Problems

class ProblemSerializer(serializers.ModelSerializer):

    class Meta:
        model = Problems 
        fields = ('pk','ProblemID','ProblemName','Statement','Difficuly')