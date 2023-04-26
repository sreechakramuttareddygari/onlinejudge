import zope.interface
import subprocess
from django.shortcuts import render
from .models import Testcases
from .models import Problems

class IExecutor(zope.interface.Interface):
    def execute(self):
        pass

@zope.interface.implementer(IExecutor)
class SimpleExecutorCPP():
    def execute(self,code,problemID):
        codeFile = open("code.cpp",'w+')
        codeFile.write(code)
        codeFile.close()
        command = "g++ code.cpp"
        subprocess.run(command, shell=True)
        tests = Testcases.objects.raw('SELECT * FROM problemviewer_Testcases WHERE ProblemID_id='+str(problemID))
        outputs={}
        for test in tests:
            command = "rm input.txt"
            try:
                subprocess.run(command, shell=True)
            except:
                pass
            input = open("input.txt","w")
            command = "rm output"+str(test.testcaseID)+'.txt'
            try:
                subprocess.run(command,shell=True)
            except:
                pass
            if test.Input is not None:
                input.write(test.Input)
                print(test.Input,type(test.Input))
            input.close()
            command = "./a.out < input.txt > output"+str(test.testcaseID)+'.txt'
            subprocess.run(command,shell=True)
            output = open("output"+str(test.testcaseID)+'.txt','r')
            outputs[test.testcaseID] = output.read()
            output.close()
        return outputs

