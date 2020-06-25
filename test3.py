# กรุณาเติมส่วนที่ขาดหายไปด้วยภาษา Python เพื่อให้โปรแกรมสามารถทำงานได้ถูกต้อง

class Nose():
   def __init__(self, value):
       self.value = value

   def iMethod(self):
       return 5

class Picasso(Nose):
   def iMethod(self):
       return 5

class Clowns(Picasso):
   def iMethod(self):
       return 7

class Acts (Nose):
   def iMethod(self):
       return 9

print('Hello world')

# ผลลัพธ์

# Hello world
# Nose 5
# Picasso 5
# Clowns 7
# Acts 9
