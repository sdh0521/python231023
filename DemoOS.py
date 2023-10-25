# DemoOS.py

from os.path import *
from os import *
import glob

print("전체경로: ", abspath("python.exe"))
print("전체경로: ", basename("c:\\work\\demo.txt"))

strPython="c:\\python310\\python.exe"
if exists(strPython):
    print("크기: {0}".format(getsize(strPython)))
else:
    print("없음")