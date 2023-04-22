import zope.interface
import subprocess
from django.shortcuts import render

class IExecutor(zope.interface.Interface):
    def execute(self):
        pass

@zope.interface.implementer(IExecutor)
class SimpleExecutorCPP():
    def execute(self,code):
        codeFile = open("code.cpp",'w+')
        codeFile.write(code)
        codeFile.close()
        command = "c++ code.cpp"
        subprocess.run(command, shell=True)
        command = "./a.out"
        subprocess.run(command,shell=True)
