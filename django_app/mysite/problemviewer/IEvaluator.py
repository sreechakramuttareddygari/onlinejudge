from django.shortcuts import render
from django.http import HttpResponse
from .models import Testcases
import zope.interface
# Create your views here.

class IEvaluator(zope.interface.Interface):
    def evaluate(self):
        pass

@zope.interface.implementer(IEvaluator)
class BitwiseEvaluator:
    def evaluate(self,outputs):
        ret = True
        for output in outputs:
            result = Testcases.objects.raw('SELECT testcaseID,Output FROM problemviewer_Testcases WHERE testcaseID='+str(output))[0]
            print(result.Output,type(result.Output))
            print(outputs[output],type(outputs[output]))
            ret = ret and (result.Output==outputs[output])
        return ret


