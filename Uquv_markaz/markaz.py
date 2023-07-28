# import json
#
# class File:
#     def __init__(self, filename):
#         self.filename = filename
#
#     def read(self):
#         with open(self.filename) as file:
#             try:
#                 l = json.load(file)
#             except:
#                 l = []
#             return l
#
#     def write(self, lists: list):
#         with open(self.filename, 'w') as file:
#             json.dump(lists, file, indent=4)
#
#
# class Student:
#     def __init__(self, name = None, username=None, password = None, phone_num = None, my_kurs = []):
#         self.name = name
#         self.username = username
#         self.password = password
#         self.phone_num = phone_num
#         self.my_kurs = my_kurs
#
#     def check_login(self):
#         obj = File('student.json').read()
#         for i in obj:
#             if i['username'] == self.username:
#                 print("Bunday nomli username band!")
#                 return True
#         else:
#             return
#
#     def check_username(self):
#         obj = File('student.json').read()
#         for i in obj:
#             if i['username'] == self.username and i['password'] == self.password:
#                 return True
#         else:
#             return False
#
#     def regestratsiya(self):
#         obj = File('student.json')
#         load = obj.read()
#         load.append(self.__dict__)
#         obj.write(load)
#
#     def addkurs(self, id = None):
#         obj = File('kurs.json').read()
#         new = []
#         for i in obj:
#             if i['id'] == id:
#                 new.append({
#                     "id": i['id'],
#                     "name": i['name'],
#                     "price": i['price'],
#                     "davomiylik": i['davomiylik']
#                 })
#         obj1 = File('student.json').read()
#         for i in obj1:
#             if i['username'] == self.username:
#                 i['my_kurs'].append(*new)
#         File('student.json').write(obj1)
#
#
# class Kurs:
#     def __init__(self, id = None, name = None, price = None, davomiylik = None, sigim = None ):
#         self.id = id
#         self.name = name
#         self.price = price
#         self.davomiylik = davomiylik
#         self.sigim = sigim
#
#     def infokurs(self):
#         obj = File('kurs.json').read()
#         for i in obj:
#             print("ID raqam:", i['id'], "  ", "Kurs nomi:", i['name'], "  ", "Kurs narxi:", i['price'], "  ", "Kurs davomiyligi:", i['davomiylik'], "  ", "Gurux sig'imi:", i['sigim'])
#
#     def saqla(self):
#         file = File('kurs.json')
#         load = file.read()
#         load.append(self.__dict__)
#         File('kurs.json').write(load)
#
#         newm = []
#         for i in load:
#             if i['id'] == self.id:
#                 newm.append({
#                     'id': i['id'],
#                     'name': i['name'],
#                     'price': i['price'],
#                     'davomiylik': i['davomiylik'],
#                     'sigim': i['sigim']
#                 })
#         file2 = File('mentor.json').read()
#
#         for i in file2:
#             if i['username'] == musername:
#                 i['add_my_kurs_m'].append(*newm)
#                 print("Kurs qushildi!")
#         File('mentor.json').write(file2)
#
#
# class Mentor:
#     def __init__(self, usernamem=None, passwordm=None, uziqushgan=None):
#         if uziqushgan is None:
#             uziqushgan = []
#         self.usernamem = usernamem
#         self.passwordm = passwordm
#         self.uziqushgan = uziqushgan
#
#
#     def check_login_mentor(self):
#         obj = File('mentor.json')
#         for i in obj.read():
#             if i['username'] == self.usernamem and i['password'] == self.passwordm:
#                 return True
#         else:
#             return False
#
#     def xsobot(self):
#         obj = File('mentor.json').read()
#         for i in obj:
#             if i['username'] == self.usernamem:
#                 for j in i['add_my_kurs_m']:
#                     print("ID raqam:", j['id'], "  ", "Kurs nomi:", j['name'], "  ", "Kurs narxi:", j['price'], "  ",
#                           "Kurs davomiyligi:", j['davomiylik'], "  ", "Gurux sig'imi:", j['sigim'])
#
#
#     def delatekurs(self, id1):
#         obj = File('kurs.json').read()
#         for i in range(len(obj)):
#             if obj[i]['id'] == id1:
#                 obj.pop(i)
#         File('kurs.json').write(obj)
#         print("Amalyot bajarildi!")
#
#
#
#
# print("_________________PDP_________________")
# print("Kim sifatida kirmoqchisiz!")
# while True:
#     text = '''
#     1) Mentor
#     2) Student
#     >>>>  '''
#     tanla = input(text)
#     if tanla == '1':
#         musername = input("Usernameingizni kiriting: ")
#         mkod = int(input("Passwordni kiriting: "))
#         chek = Mentor(usernamem=musername, passwordm=mkod)
#         chek.check_login_mentor()
#         while True:
#             if chek.check_login_mentor():
#                 text_mentor = '''
#                 1) Kurs qushish
#                 2) Kurs o'chirish
#                 3) O'zi qushgan kurslarni kurish
#                 0) Exit
#                 >>>  '''
#                 tala_mentor = input(text_mentor)
#                 if tala_mentor == '1':
#                     id = int(input("Kurs ID raqamini kiriting: "))
#                     name = input("Kurs nomini kiriting: ")
#                     price = int(input("Kurs narxini kiriting: "))
#                     davomiylik = int(input("Kurs davomiyligini kiriting: "))
#                     sigim = int(input("Gurux sig'imini kiriting: "))
#                     saqla = Kurs(id=id, name=name, price=price, davomiylik=davomiylik, sigim=sigim)
#                     saqla.saqla()
#
#                 if tala_mentor == '2':
#                     print("______Mavjud kurslar______")
#                     info = Kurs()
#                     info.infokurs()
#                     print()
#                     num1 = int(input("Kurs ID sini kiriting: "))
#                     delate = Mentor()
#                     delate.delatekurs(id1=num1)
#
#                 if tala_mentor == '3':
#                     xisobot = Mentor(musername, mkod)
#                     xisobot.xsobot()
#                 if tala_mentor == '0':
#                     break
#             else:
#                 print("Xatolik bor qaytadan urining!")
#
#
#     if tanla == '2':
#         while True:
#             text_student = '''
#             1) Kirish
#             2) Ro'yxatdan utish
#             0) Exit
#             >>>>  '''
#             tanla_student = input(text_student)
#             if tanla_student == '1':
#                 username = input("Usernamengizni kiriting: ")
#                 kod = int(input("Parolingizni kiriting: "))
#                 student = Student(username=username, password=kod)
#                 while True:
#                     if student.check_username():
#                         text_student1 = '''
#                         1) Kursga qoshilish
#                         2) Kursdan chiqish
#                         3) Kusrlarni ko'rish
#                         0) Exit
#                         >>>>  '''
#                         tanla_student1 = input(text_student1)
#
#                         if tanla_student1 == '1':
#                             num = int(input("ID raqam kiriting: "))
#                             add = Student(username=username)
#                             add.addkurs(num)
#
#                         if tanla_student1 == '3':
#                             info = Kurs()
#                             info.infokurs()
#                             print()
#                         if tanla_student1 == '0':
#                             break
#
#
#             if tanla_student == '2':
#                 name = input("Ismingizni kiriting: ")
#                 username = input("Usernamengizni kiriting: ")
#                 kod = int(input("Parolingizni kiriting: "))
#                 phone = int(input("Telefon raqamingizni kiriting: "))
#                 reg = Student(name, username, kod, phone)
#                 if not reg.check_username():
#                     reg.regestratsiya()
#
#
#             if tanla_student == '0':
#                 break
#
#
#
#22222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222
# import json
#
# class File:
#     def __init__(self, filename):
#         self.filename = filename
#
#     def read(self):
#         with open(self.filename) as file:
#             try:
#                 l = json.load(file)
#             except:
#                 l = []
#             return l
#
#     def write(self, lists: list):
#         with open(self.filename, 'w') as file:
#             json.dump(lists, file, indent=4)
#
#
# class Student:
#     def __init__(self, name = None, username=None, password = None, phone_num = None, my_kurs = []):
#         self.name = name
#         self.username = username
#         self.password = password
#         self.phone_num = phone_num
#         self.my_kurs = my_kurs
#
#     def check_login(self):
#         obj = File('student.json').read()
#         for i in obj:
#             if i['username'] == self.username:
#                 print("Bunday nomli username band!")
#                 return True
#         else:
#             return
#
#     def check_username(self):
#         obj = File('student.json').read()
#         for i in obj:
#             if i['username'] == self.username and i['password'] == self.password:
#                 return True
#         else:
#             return False
#
#     def regestratsiya(self):
#         obj = File('student.json')
#         load = obj.read()
#         load.append(self.__dict__)
#         obj.write(load)
#
#     def addkurs(self, id = None):
#         obj = File('kurs.json').read()
#         new = []
#         for i in obj:
#             if i['id'] == id:
#                 new.append({
#                     "id": i['id'],
#                     "name": i['name'],
#                     "price": i['price'],
#                     "davomiylik": i['davomiylik']
#                 })
#         obj1 = File('student.json').read()
#         for i in obj1:
#             if i['username'] == self.username:
#                 i['my_kurs'].append(*new)
#         File('student.json').write(obj1)
# #
# #
#     def mykurs(self):
#         obj = File('student.json').read()
#         for i in obj:
#             if i['username'] == self.username:
#                 for j in i['my_kurs']:
#                     print("ID raqam:", j['id'], "  ", "Kurs nomi:", j['name'], "  ", "Kurs narxi:", j['price'], "  ", "Kurs davomiyligi:", j['davomiylik'])
#
#
#     def delmykurs(self, a):
#         obj = File('student.json').read()
#         for i in obj:
#             if i['username'] == self.username:
#                 for j in i['my_kurs']:
#                     if j['id'] == a:
#                         i['my_kurs'].remove(j)
#
#         File('student.json').write(obj)
#
# class Kurs:
#     def __init__(self, id = None, name = None, price = None, davomiylik = None, sigim = None ):
#         self.id = id
#         self.name = name
#         self.price = price
#         self.davomiylik = davomiylik
#         self.sigim = sigim
#
#     def infokurs(self):
#         obj = File('kurs.json').read()
#         for i in obj:
#             print("ID raqam:", i['id'], "  ", "Kurs nomi:", i['name'], "  ", "Kurs narxi:", i['price'], "  ", "Kurs davomiyligi:", i['davomiylik'], "  ", "Gurux sig'imi:", i['sigim'])
#
#     def saqla(self):
#         file = File('kurs.json')
#         load = file.read()
#         load.append(self.__dict__)
#         File('kurs.json').write(load)
#
#         newm = []
#         for i in load:
#             if i['id'] == self.id:
#                 newm.append({
#                     'id': i['id'],
#                     'name': i['name'],
#                     'price': i['price'],
#                     'davomiylik': i['davomiylik'],
#                     'sigim': i['sigim']
#                 })
#         file2 = File('mentor.json').read()
#
#         for i in file2:
#             if i['username'] == musername:
#                 i['add_my_kurs_m'].append(*newm)
#                 print("Kurs qushildi!")
#         File('mentor.json').write(file2)
#
# class Mentor:
#     def __init__(self, usernamem=None, passwordm=None, uziqushgan=None):
#         if uziqushgan is None:
#             uziqushgan = []
#         self.usernamem = usernamem
#         self.passwordm = passwordm
#         self.uziqushgan = uziqushgan
#
#
#     def check_login_mentor(self):
#         obj = File('mentor.json')
#         for i in obj.read():
#             if i['username'] == self.usernamem and i['password'] == self.passwordm:
#                 return True
#         else:
#             return False
#
#     def xsobot(self):
#         obj = File('mentor.json').read()
#         for i in obj:
#             if i['username'] == self.usernamem:
#                 for j in i['add_my_kurs_m']:
#                     print("ID raqam:", j['id'], "  ", "Kurs nomi:", j['name'], "  ", "Kurs narxi:", j['price'], "  ",
#                           "Kurs davomiyligi:", j['davomiylik'], "  ", "Gurux sig'imi:", j['sigim'])
#
#
#     def delatekurs(self, id1):
#         chek = False
#         obj = File('mentor.json').read()
#         for i in obj:
#             if i['username'] == self.usernamem:
#                 chek = True
#                 for j in i['add_my_kurs_m']:
#                     if j['id'] == id1:
#                         i['add_my_kurs_m'].remove(j)
#
#         File('mentor.json').write(obj)
#
#         ves = File('student.json').read()
#         for i in ves:
#             for j in i['my_kurs']:
#                 if j['id'] == id1:
#                     i['my_kurs'].remove(j)
#         File('student.json').write(ves)
#
#         if chek:
#             obj = File('kurs.json').read()
#             for i in range(len(obj)):
#                 if obj[i]['id'] == id1:
#                     obj.pop(i)
#             File('kurs.json').write(obj)
#             print("Amalyot bajarildi!")
#         else:
#             print("Bu kurs sizga tegishli emas!")
#
# print("_________________PDP_________________")
# print("Kim sifatida kirmoqchisiz!")
# while True:
#     text = '''
#     1) Mentor
#     2) Student
#     >>>>  '''
#     tanla = input(text)
#     if tanla == '1':
#         musername = input("Usernameingizni kiriting: ")
#         mkod = int(input("Passwordni kiriting: "))
#         chek = Mentor(usernamem=musername, passwordm=mkod)
#         chek.check_login_mentor()
#         while True:
#             if chek.check_login_mentor():
#                 text_mentor = '''
#                 1) Kurs qushish
#                 2) Kurs o'chirish
#                 3) O'zi qushgan kurslarni kurish
#                 0) Exit
#                 >>>  '''
#                 tala_mentor = input(text_mentor)
#                 if tala_mentor == '1':
#                     id = int(input("Kurs ID raqamini kiriting: "))
#                     name = input("Kurs nomini kiriting: ")
#                     price = int(input("Kurs narxini kiriting: "))
#                     davomiylik = int(input("Kurs davomiyligini kiriting: "))
#                     sigim = int(input("Gurux sig'imini kiriting: "))
#                     saqla = Kurs(id=id, name=name, price=price, davomiylik=davomiylik, sigim=sigim)
#                     saqla.saqla()
#
#                 if tala_mentor == '2':
#                     print("______Mavjud kurslar______")
#                     info = Kurs()
#                     info.infokurs()
#                     print()
#                     num1 = int(input("Kurs ID sini kiriting: "))
#                     delate = Mentor(usernamem=musername)
#                     delate.delatekurs(id1=num1)
#
#                 if tala_mentor == '3':
#                     xisobot = Mentor(musername, mkod)
#                     xisobot.xsobot()
#                 if tala_mentor == '0':
#                     break
#             else:
#                 print("Xatolik bor qaytadan urining!")
#                 break
#
#
#     if tanla == '2':
#         while True:
#             text_student = '''
#             1) Kirish
#             2) Ro'yxatdan utish
#             0) Exit
#             >>>>  '''
#             tanla_student = input(text_student)
#             if tanla_student == '1':
#                 username = input("Usernamengizni kiriting: ")
#                 kod = int(input("Parolingizni kiriting: "))
#                 student = Student(username=username, password=kod)
#                 while True:
#                     if student.check_username():
#                         text_student1 = '''
#                         1) Kursga qoshilish
#                         2) Kursdan chiqish
#                         3) Kusrlarni ko'rish
#                         0) Exit
#                         >>>>  '''
#                         tanla_student1 = input(text_student1)
#
#                         if tanla_student1 == '1':
#                             num = int(input("ID raqam kiriting: "))
#                             add = Student(username=username)
#                             add.addkurs(num)
#
#                         if tanla_student1 == '2':
#                             print("Mavjud kurslaringiz!")
#                             mykurs = Student(username=username)
#                             mykurs.mykurs()
#                             a = int(input("Chiqmoqchi bulgan kuringizning ID raqamini kiriting: "))
#                             mykurs.delmykurs(a)
#                             print("Amalyot bajarildi!")
#
#                         if tanla_student1 == '3':
#                             info = Kurs()
#                             info.infokurs()
#                             print()
#
#                         if tanla_student1 == '0':
#                             break
#
#
#             if tanla_student == '2':
#                 name = input("Ismingizni kiriting: ")
#                 username = input("Usernamengizni kiriting: ")
#                 kod = int(input("Parolingizni kiriting: "))
#                 phone = int(input("Telefon raqamingizni kiriting: "))
#                 reg = Student(name, username, kod, phone)
#                 if not reg.check_username():
#                     reg.regestratsiya()
#
#
#             if tanla_student == '0':
#                 break


#3333333333333333333333333333333333333333333333333333333333333333333333
# import json
#
# class File:
#     def __init__(self, filename):
#         self.filename = filename
#
#     def read(self):
#         with open(self.filename) as file:
#             try:
#                 l = json.load(file)
#             except:
#                 l = []
#             return l
#
#     def write(self, lists: list):
#         with open(self.filename, 'w') as file:
#             json.dump(lists, file, indent=4)
#
#
# class Student:
#     def __init__(self, name = None, username=None, password = None, phone_num = None, my_kurs = []):
#         self.name = name
#         self.username = username
#         self.password = password
#         self.phone_num = phone_num
#         self.my_kurs = my_kurs
#
#     def check_login(self):
#         obj = File('student.json').read()
#         for i in obj:
#             if i['username'] == self.username:
#                 print("Bunday nomli username band!")
#                 return True
#         else:
#             return
#
#     def check_username(self):
#         obj = File('student.json').read()
#         for i in obj:
#             if i['username'] == self.username and i['password'] == self.password:
#                 return True
#         else:
#             return False
#
#     def regestratsiya(self):
#         obj = File('student.json')
#         load = obj.read()
#         load.append(self.__dict__)
#         obj.write(load)
#
#     def addkurs(self, id = None):
#         obj = File('kurs.json').read()
#         new = []
#         for i in obj:
#             if i['id'] == id:
#                 new.append({
#                     "id": i['id'],
#                     "name": i['name'],
#                     "price": i['price'],
#                     "davomiylik": i['davomiylik']
#                 })
#         obj1 = File('student.json').read()
#         for i in obj1:
#             if i['username'] == self.username:
#                 i['my_kurs'].append(*new)
#         File('student.json').write(obj1)
# #
# #
#     def mykurs(self):
#         obj = File('student.json').read()
#         for i in obj:
#             if i['username'] == self.username:
#                 for j in i['my_kurs']:
#                     print("ID raqam:", j['id'], "  ", "Kurs nomi:", j['name'], "  ", "Kurs narxi:", j['price'], "  ", "Kurs davomiyligi:", j['davomiylik'])
#
#
#     def delmykurs(self, a):
#         obj = File('student.json').read()
#         for i in obj:
#             if i['username'] == self.username:
#                 for j in i['my_kurs']:
#                     if j['id'] == a:
#                         i['my_kurs'].remove(j)
#
#         File('student.json').write(obj)
#
# class Kurs:
#     def __init__(self, id = None, name = None, price = None, davomiylik = None, sigim = None ):
#         self.id = id
#         self.name = name
#         self.price = price
#         self.davomiylik = davomiylik
#         self.sigim = sigim
#
#     def infokurs(self):
#         obj = File('kurs.json').read()
#         for i in obj:
#             print("ID raqam:", i['id'], "  ", "Kurs nomi:", i['name'], "  ", "Kurs narxi:", i['price'], "  ", "Kurs davomiyligi:", i['davomiylik'], "  ", "Gurux sig'imi:", i['sigim'])
#
#     def saqla(self):
#         file = File('kurs.json')
#         load = file.read()
#         load.append(self.__dict__)
#         File('kurs.json').write(load)
#
#         newm = []
#         for i in load:
#             if i['id'] == self.id:
#                 newm.append({
#                     'id': i['id'],
#                     'name': i['name'],
#                     'price': i['price'],
#                     'davomiylik': i['davomiylik'],
#                     'sigim': i['sigim']
#                 })
#         file2 = File('mentor.json').read()
#
#         for i in file2:
#             if i['username'] == musername:
#                 i['add_my_kurs_m'].append(*newm)
#                 print("Kurs qushildi!")
#         File('mentor.json').write(file2)
#
# class Mentor:
#     def __init__(self, usernamem=None, passwordm=None, uziqushgan=None):
#         if uziqushgan is None:
#             uziqushgan = []
#         self.usernamem = usernamem
#         self.passwordm = passwordm
#         self.uziqushgan = uziqushgan
#
#     def check_reg_mentor(self):
#         obj = File('mentor.json').read()
#         for i in obj:
#             if i['username'] == self.usernamem:
#                 print("Bunday nomli username band!")
#                 return True
#         else:
#             return
#
#     def check_login_mentor(self):
#         obj = File('mentor.json')
#         for i in obj.read():
#             if i['username'] == self.usernamem and i['password'] == self.passwordm:
#                 return True
#         else:
#             return False
#
#     def regestratsiya_mentor(self):
#         obj = File('mentor.json')
#         load = obj.read()
#         load.append(self.__dict__)
#         obj.write(load)
#
#     def xsobot(self):
#         obj = File('mentor.json').read()
#         for i in obj:
#             if i['username'] == self.usernamem:
#                 for j in i['add_my_kurs_m']:
#                     print("ID raqam:", j['id'], "  ", "Kurs nomi:", j['name'], "  ", "Kurs narxi:", j['price'], "  ",
#                           "Kurs davomiyligi:", j['davomiylik'], "  ", "Gurux sig'imi:", j['sigim'])
#
#
#     def delatekurs(self, id1):
#         chek = False
#         obj = File('mentor.json').read()
#         for i in obj:
#             if i['username'] == self.usernamem:
#                 chek = True
#                 for j in i['add_my_kurs_m']:
#                     if j['id'] == id1:
#                         i['add_my_kurs_m'].remove(j)
#
#         File('mentor.json').write(obj)
#
#         ves = File('student.json').read()
#         for i in ves:
#             for j in i['my_kurs']:
#                 if j['id'] == id1:
#                     i['my_kurs'].remove(j)
#         File('student.json').write(ves)
#
#         if chek:
#             obj = File('kurs.json').read()
#             for i in range(len(obj)):
#                 if obj[i]['id'] == id1:
#                     obj.pop(i)
#             File('kurs.json').write(obj)
#             print("Amalyot bajarildi!")
#         else:
#             print("Bu kurs sizga tegishli emas!")
#
#
# def max_id1():
#     maxx1 = []
#     obj = File('ovqat.json').read()
#     for i in obj:
#         maxx1.append(i['id'])
#
#     return maxx1
#
#
#
#
# print("_________________PDP_________________")
# print("Kim sifatida kirmoqchisiz!")
# while True:
#     text = '''
#     1) Mentor
#     2) Student
#     3) Ro'yxatdan utish
#     >>>>  '''
#     tanla = input(text)
#     if tanla == '1':
#         musername = input("Usernameingizni kiriting: ")
#         mkod = int(input("Passwordni kiriting: "))
#         chek = Mentor(usernamem=musername, passwordm=mkod)
#         chek.check_login_mentor()
#         while True:
#             if chek.check_login_mentor():
#                 text_mentor = '''
#                 1) Kurs qushish
#                 2) Kurs o'chirish
#                 3) O'zi qushgan kurslarni kurish
#                 0) Exit
#                 >>>  '''
#                 tala_mentor = input(text_mentor)
#                 if tala_mentor == '1':
#                     a = max_id1()
#                     num = max(a) + 1
#                     name = input("Kurs nomini kiriting: ")
#                     price = int(input("Kurs narxini kiriting: "))
#                     davomiylik = int(input("Kurs davomiyligini kiriting: "))
#                     sigim = int(input("Gurux sig'imini kiriting: "))
#                     saqla = Kurs(id=num, name=name, price=price, davomiylik=davomiylik, sigim=sigim)
#                     saqla.saqla()
#
#                 if tala_mentor == '2':
#                     print("______Mavjud kurslar______")
#                     info = Kurs()
#                     info.infokurs()
#                     print()
#                     num1 = int(input("Kurs ID sini kiriting: "))
#                     delate = Mentor(usernamem=musername)
#                     delate.delatekurs(id1=num1)
#
#                 if tala_mentor == '3':
#                     xisobot = Mentor(musername, mkod)
#                     xisobot.xsobot()
#                 if tala_mentor == '0':
#                     break
#             else:
#                 print("Xatolik bor qaytadan urining!")
#                 break
#
#
#     if tanla == '2':
#         username = input("Usernamengizni kiriting: ")
#         kod = int(input("Parolingizni kiriting: "))
#         student = Student(username=username, password=kod)
#         while True:
#             if student.check_username():
#                 text_student1 = '''
#                 1) Kursga qoshilish
#                 2) Kursdan chiqish
#                 3) Kusrlarni ko'rish
#                 0) Exit
#                 >>>>  '''
#                 tanla_student1 = input(text_student1)
#
#                 if tanla_student1 == '1':
#                     num = int(input("ID raqam kiriting: "))
#                     add = Student(username=username)
#                     add.addkurs(num)
#
#                 if tanla_student1 == '2':
#                     print("Mavjud kurslaringiz!")
#                     mykurs = Student(username=username)
#                     mykurs.mykurs()
#                     a = int(input("Chiqmoqchi bulgan kuringizning ID raqamini kiriting: "))
#                     mykurs.delmykurs(a)
#                     print("Amalyot bajarildi!")
#
#                 if tanla_student1 == '3':
#                     info = Kurs()
#                     info.infokurs()
#                     print()
#
#                 if tanla_student1 == '0':
#                     break
#
#     if tanla == '3':
#         print("Kim sifatida ro'yxatdan o'tmoqchisiz!")
#         kim = '''
#         1) Mentor
#         2) Talaba
#         >>>  '''
#         s = input(kim)
#         if s == '1':
#             username = input("Usernamengizni kiriting: ")
#             kod = (input("Parolingizni kiriting: "))
#             reg = Student(username=username, password=kod)
#             a = Mentor(usernamem=username, passwordm=kod)
#             if not reg.check_login() and not a.check_reg_mentor():
#                 a.regestratsiya_mentor()
#
#         if s == '2':
#             name = input("Ismingizni kiriting: ")
#             username = input("Usernamengizni kiriting: ")
#             kod = (input("Parolingizni kiriting: "))
#             phone = int(input("Telefon raqamingizni kiriting: "))
#             reg = Student(name, username, kod, phone)
#             a = Mentor(usernamem=username, passwordm=kod)
#             if not reg.check_login() and not a.check_reg_mentor():
#                 reg.regestratsiya()


#44444444444444444444444444444444444444444444444444444444444444444444444444
import json

class File:
    def __init__(self, filename):
        self.filename = filename

    def read(self):
        with open(self.filename) as file:
            try:
                l = json.load(file)
            except:
                l = []
            return l

    def write(self, lists: list):
        with open(self.filename, 'w') as file:
            json.dump(lists, file, indent=4)


class Student:
    def __init__(self, username=None, password = None, my_kurs = []):
        self.username = username
        self.password = password
        self.my_kurs = my_kurs

    def check_login(self):
        obj = File('student.json').read()
        for i in obj:
            if i['username'] == self.username:
                print("Bunday nomli username band!")
                return True
        else:
            return

    def check_username(self):
        obj = File('student.json').read()
        for i in obj:
            if i['username'] == self.username and i['password'] == self.password:
                return True
        else:
            return False

    def regestratsiya(self):
        obj = File('student.json')
        load = obj.read()
        load.append(self.__dict__)
        obj.write(load)

    def addkurs(self, id = None):
        obj = File('kurs.json').read()
        new = []
        for i in obj:
            if i['id'] == id:
                new.append({
                    "id": i['id'],
                    "name": i['name'],
                    "price": i['price'],
                    "davomiylik": i['davomiylik']
                })
        obj1 = File('student.json').read()
        for i in obj1:
            if i['username'] == self.username:
                i['my_kurs'].append(*new)
        File('student.json').write(obj1)
#
#
    def mykurs(self):
        obj = File('student.json').read()
        for i in obj:
            if i['username'] == self.username:
                for j in i['my_kurs']:
                    print("ID raqam:", j['id'], "  ", "Kurs nomi:", j['name'], "  ", "Kurs narxi:", j['price'], "  ", "Kurs davomiyligi:", j['davomiylik'])


    def delmykurs(self, a):
        obj = File('student.json').read()
        for i in obj:
            if i['username'] == self.username:
                for j in i['my_kurs']:
                    if j['id'] == a:
                        i['my_kurs'].remove(j)

        File('student.json').write(obj)

class Kurs:
    def __init__(self, id = None, name = None, price = None, davomiylik = None, sigim = None ):
        self.id = id
        self.name = name
        self.price = price
        self.davomiylik = davomiylik
        self.sigim = sigim

    def infokurs(self):
        obj = File('kurs.json').read()
        for i in obj:
            print("ID raqam:", i['id'], "  ", "Kurs nomi:", i['name'], "  ", "Kurs narxi:", i['price'], "  ", "Kurs davomiyligi:", i['davomiylik'], "  ", "Gurux sig'imi:", i['sigim'])

    def saqla(self):
        file = File('kurs.json')
        load = file.read()
        load.append(self.__dict__)
        File('kurs.json').write(load)

        newm = []
        for i in load:
            if i['id'] == self.id:
                newm.append({
                    'id': i['id'],
                    'name': i['name'],
                    'price': i['price'],
                    'davomiylik': i['davomiylik'],
                    'sigim': i['sigim']
                })
        file2 = File('mentor.json').read()

        for i in file2:
            if i['username'] == musername:
                i['uziqushgan'].append(*newm)
                print("Kurs qushildi!")
        File('mentor.json').write(file2)

class Mentor:
    def __init__(self, username=None, password=None, uziqushgan=None):
        if uziqushgan is None:
            uziqushgan = []
        self.username = username
        self.password = password
        self.uziqushgan = uziqushgan

    def check_reg_mentor(self):
        obj = File('mentor.json').read()
        for i in obj:
            if i['username'] == self.username:
                print("Bunday nomli username band!")
                return True
        else:
            return

    def check_login_mentor(self):
        obj = File('mentor.json')
        for i in obj.read():
            if i['username'] == self.username and i['password'] == self.password:
                return True
        else:
            return False

    def regestratsiya_mentor(self):
        obj = File('mentor.json')
        load = obj.read()
        load.append(self.__dict__)
        obj.write(load)

    def xsobot(self):
        obj = File('mentor.json').read()
        for i in obj:
            if i['username'] == self.username:
                for j in i['uziqushgan']:
                    print("ID raqam:", j['id'], "  ", "Kurs nomi:", j['name'], "  ", "Kurs narxi:", j['price'], "  ",
                          "Kurs davomiyligi:", j['davomiylik'], "  ", "Gurux sig'imi:", j['sigim'])


    def delatekurs(self, id1):
        chek = False
        obj = File('mentor.json').read()
        for i in obj:
            if i['username'] == self.username:
                chek = True
                for j in i['add_my_kurs_m']:
                    if j['id'] == id1:
                        i['add_my_kurs_m'].remove(j)

        File('mentor.json').write(obj)

        ves = File('student.json').read()
        for i in ves:
            for j in i['my_kurs']:
                if j['id'] == id1:
                    i['my_kurs'].remove(j)
        File('student.json').write(ves)

        if chek:
            obj = File('kurs.json').read()
            for i in range(len(obj)):
                if obj[i]['id'] == id1:
                    obj.pop(i)
            File('kurs.json').write(obj)
            print("Amalyot bajarildi!")
        else:
            print("Bu kurs sizga tegishli emas!")


def max_id1():
    maxx1 = []
    obj = File('kurs.json').read()
    for i in obj:
        maxx1.append(i['id'])

    return maxx1




print("_________________PDP_________________")
while True:
    text = '''
    1) Kirish
    2) Ro'yxatdan utish
    >>>>  '''
    tanla = input(text)
    if tanla == '1':
        musername = input("Usernameingizni kiriting: ")
        mkod = input("Passwordni kiriting: ")
        chek = Mentor(username=musername, password=mkod)
        student = Student(username=musername, password=mkod)
        if chek.check_login_mentor():
            while True:
                text_mentor = '''
                1) Kurs qushish
                2) Kurs o'chirish
                3) O'zi qushgan kurslarni kurish
                0) Exit
                >>>  '''
                tala_mentor = input(text_mentor)
                if tala_mentor == '1':
                    a = max_id1()
                    num = max(a) + 1
                    name = input("Kurs nomini kiriting: ")
                    price = int(input("Kurs narxini kiriting: "))
                    davomiylik = int(input("Kurs davomiyligini kiriting: "))
                    sigim = int(input("Gurux sig'imini kiriting: "))
                    saqla = Kurs(id=num, name=name, price=price, davomiylik=davomiylik, sigim=sigim)
                    saqla.saqla()

                if tala_mentor == '2':
                    print("______Mavjud kurslar______")
                    info = Kurs()
                    info.infokurs()
                    print()
                    num1 = int(input("Kurs ID sini kiriting: "))
                    delate = Mentor(username=musername)
                    delate.delatekurs(id1=num1)

                if tala_mentor == '3':
                    xisobot = Mentor(musername, mkod)
                    xisobot.xsobot()
                if tala_mentor == '0':
                    break
        else:
            print("Xatolik bor")


        if student.check_username():
            while True:
                text_student1 = '''
                1) Kursga qoshilish
                2) Kursdan chiqish
                3) Kusrlarni ko'rish
                0) Exit
                >>>>  '''
                tanla_student1 = input(text_student1)

                if tanla_student1 == '1':
                    num = int(input("ID raqam kiriting: "))
                    add = Student(username=musername)
                    add.addkurs(num)

                if tanla_student1 == '2':
                    print("Mavjud kurslaringiz!")
                    mykurs = Student(username=musername)
                    mykurs.mykurs()
                    a = int(input("Chiqmoqchi bulgan kuringizning ID raqamini kiriting: "))
                    mykurs.delmykurs(a)
                    print("Amalyot bajarildi!")

                if tanla_student1 == '3':
                    info = Kurs()
                    info.infokurs()
                    print()

                if tanla_student1 == '0':
                    break

    if tanla == '2':
        username = input("Usernamengizni kiriting: ")
        kod = input("Parolingizni kiriting: ")
        print("_____Mentormisiz?_____")
        text4 = '''
        1) HA
        2) YUQ
        >>> '''
        tanla4 = input(text4)
        if tanla4 == '1':
            b = Student(username=username, password=kod)
            a = Mentor(username=username, password=kod)
            if not b.check_login() and not a.check_reg_mentor():
                a.regestratsiya_mentor()

        if tanla4 == '2':
            b = Student(username, kod)
            a = Mentor(username=username, password=kod)
            if not b.check_login() and not a.check_reg_mentor():
                b.regestratsiya()


