import os

text = "python " + os.path.dirname(os.path.abspath(__file__)) + "\main.py %*"

file = open("mat.bat","w") 
file.write(text)
 
file.close() 