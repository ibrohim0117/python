import json
import hashlib
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
        c = []
        d = False
        aa = File('student.json').read()
        for i in aa:
            for j in i['my_kurs']:
                c.append(j['id'])

        for i in c:
            if i == id:
                d = False
            else:
                d = True

        if d:
            obj = File('kurs.json').read()
            new = []
            a = False
            for i in obj:
                if i['id'] == id:
                    new.append({
                        "id": i['id'],
                        "name": i['name'],
                        "price": i['price'],
                        "davomiylik": i['davomiylik']
                    })
                    a = True
            if a:
                obj1 = File('student.json').read()
                for i in obj1:
                    if i['username'] == self.username:
                        i['my_kurs'].append(*new)
                File('student.json').write(obj1)
        else:
            print("Siz bu kursga azosiz!")


    def mykurs(self):
        obj = File('student.json').read()
        for i in obj:
            if i['username'] == self.username:
                for j in i['my_kurs']:
                    print("ID raqam:", j['id'], "  ", "Kurs nomi:", j['name'], "  ", "Kurs narxi:", j['price'], "  ", "Kurs davomiyligi:", j['davomiylik'])


    def delmykurs(self, a):
        obj = File('student.json').read()
        l = 0
        for i in obj:
            if i['username'] == self.username:
                l = len(i['my_kurs'])

        if l != 0:
            for i in obj:
                if i['username'] == self.username:
                    for j in i['my_kurs']:
                        if j['id'] == a:
                            i['my_kurs'].remove(j)

            File('student.json').write(obj)

        else:
            print("Sizda kurslar mavjud emas!")

class Kurs:
    def __init__(self, id = None, name = None, price = None, davomiylik = None):
        self.id = id
        self.name = name
        self.price = price
        self.davomiylik = davomiylik


    def infokurs(self):
        obj = File('kurs.json').read()
        for i in obj:
            print("ID raqam:", i['id'], "  ", "Kurs nomi:", i['name'], "  ",
                  "Kurs narxi:", i['price'], "  ", "Kurs davomiyligi:", i['davomiylik'])

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
                    'davomiylik': i['davomiylik']
                })
        file2 = File('mentor.json').read()

        for i in file2:
            if i['username'] == username:
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
                          "Kurs davomiyligi:", j['davomiylik'])


    def delatekurs(self, id1):
        chek = False
        obj = File('mentor.json').read()
        for i in obj:
            if i['username'] == self.username:
                chek = True
                for j in i['uziqushgan']:
                    if j['id'] == id1:
                        i['uziqushgan'].remove(j)

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
        username = input("Usernameingizni kiriting: ")
        password = input("Passwordni kiriting: ")
        string1 = hashlib.md5(b'password')
        hesh = string1.hexdigest()
        chek = Mentor(username=username, password=hesh)
        student = Student(username=username, password=hesh)
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
                    if len(a) != 0:
                        num = max(a) + 1
                    else:
                        num = 1
                    name = input("Kurs nomini kiriting: ")
                    price = int(input("Kurs narxini kiriting: "))
                    davomiylik = int(input("Kurs davomiyligini kiriting: "))
                    saqla = Kurs(id=num, name=name, price=price, davomiylik=davomiylik)
                    saqla.saqla()

                if tala_mentor == '2':
                    print("______Mavjud kurslar______")
                    info = Kurs()
                    info.infokurs()
                    print()
                    num1 = int(input("Kurs ID sini kiriting: "))
                    delate = Mentor(username=username)
                    delate.delatekurs(id1=num1)

                if tala_mentor == '3':
                    xisobot = Mentor(username, password)
                    xisobot.xsobot()
                if tala_mentor == '0':
                    break


        if student.check_username():
            while True:
                text_student1 = '''
                1) Kursga qoshilish
                2) Kursdan chiqish
                3) Kusrlarni ko'rish
                4) Qushilgan kusrlarni ko'rish
                0) Exit
                >>>>  '''
                tanla_student1 = input(text_student1)

                if tanla_student1 == '1':
                    num = int(input("ID raqam kiriting: "))
                    add = Student(username=username)
                    add.addkurs(num)

                if tanla_student1 == '2':
                    print("Mavjud kurslaringiz!")
                    mykurs = Student(username=username)
                    mykurs.mykurs()
                    print()
                    a = int(input("Chiqmoqchi bulgan kuringizning ID raqamini kiriting: "))
                    print()
                    mykurs.delmykurs(a)
                    print("Amalyot yakunlandi!")

                if tanla_student1 == '3':
                    info = Kurs()
                    info.infokurs()
                    print()

                if tanla_student1 == '4':
                    print("Mavjud kurslaringiz!")
                    mykurs = Student(username=username)
                    mykurs.mykurs()

                if tanla_student1 == '0':
                    break

    if tanla == '2':
        username = input("Usernamengizni kiriting: ")
        password = input("Parolingizni kiriting: ")
        string1 = hashlib.md5(b'password')
        hesh = string1.hexdigest()
        print("_____Mentormisiz?_____")
        text4 = '''
        1) HA
        2) YUQ
        >>> '''
        tanla4 = input(text4)
        if tanla4 == '1':
            a = Mentor(username=username, password=hesh)
            b = Student(username=username, password=hesh)
            if not b.check_login() and not a.check_reg_mentor():
                a.regestratsiya_mentor()

        if tanla4 == '2':
            a = Mentor(username=username, password=hesh)
            b = Student(username=username, password=hesh)
            if not b.check_login() and not a.check_reg_mentor():
                b.regestratsiya()