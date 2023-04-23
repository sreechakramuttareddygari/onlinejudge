import zope.interface
import subprocess
from django.shortcuts import render
from .models import Testcases

class IExecutor(zope.interface.Interface):
    def execute(self):
        pass

@zope.interface.implementer(IExecutor)
class SimpleExecutorCPP():
    def execute(self,code,problemID):
        codeFile = open("code.cpp",'w+')
        codeFile.write(code)
        codeFile.close()
        command = "c++ code.cpp"
        subprocess.run(command, shell=True)
        tests = Testcases.objects.raw('SELECT testcaseID,Input FROM problemviewer_Testcases WHERE ProblemID=' + str(problemID))
        outputs={}
        for test in tests:
            input = open("input.txt","w")
            if test.Input is not None:
                input.write(test.Input)
            command = "./a.out < input.txt > output"+str(test.testcaseID)+'.txt'
            subprocess.run(command,shell=True)
            output = open("output"+str(test.testcaseID)+'.txt','r')
            outputs[test.testcaseID] = output.read()
        return outputs

