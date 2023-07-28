import json
import hashlib
from datetime import datetime

class File():
    def __init__(self, filename):
        self.filename = filename

    def read(self):
        with open(self.filename) as file:
            try:
                l = json.load(file)
            except:
                l = []
        return l

    def write(self, lists):
        with open(self.filename ,'w') as file:
            json.dump(lists, file, indent=4)


class Boss:
    def __init__(self, username = None, password = None):
        self.username = username
        self.password = password

    def check_username(self):
        obj = File('boshliq.json').read()
        for i in obj:
            if i['username'] == self.username and i['password'] == self.password:
                return True
        else:
            return

    def check_red_boshliq(self):
        obj = File('boshliq.json').read()
        for i in obj:
            if i['username'] == self.username:
                return True
        else:
            return


    def add_boss(self):
        obj = File('boshliq.json')
        load = obj.read()
        load.append(self.__dict__)
        obj.write(load)

    def malumot(self):
        obj = File('xisobot.json').read()
        for i in obj:
            print("ID raqam:", i['id'], "  ", "Sotilgan maxsulot nomi:", i['name'], "  ", "Sotilgan maxsulot narxi:", i['price'], "  ", "Sotilgan maxsulot miqdori :", i['Soni'],  "Xaridqilingan vaqt: ", i['vaqti'])



class Taom:
    def __init__(self, id=None, name=None, price=None, amout=None):
        self.id = id
        self.name = name
        self.price = price
        self.amout = amout

    def add_meal(self):
        obj = File('ovqat.json')
        load = obj.read()
        load.append(self.__dict__)
        obj.write(load)

    def add_ichimlik(self):
        obj = File('ichimlik.json')
        load = obj.read()
        load.append(self.__dict__)
        obj.write(load)


class Mijoz:
    def __init__(self, username=None, password = None, by_food=[], by_water=[]):
        self.username = username
        self.password = password
        self.by_food = by_food
        self.by_water = by_water


    def check_login(self):
        obj = File('mijoz.json').read()
        for i in obj:
            if i['username'] == self.username and i['password'] == self.password:
                return True
        else:
            return

    def check_red(self):
        obj = File('mijoz.json').read()
        for i in obj:
            if i['username'] == self.username:
                return True
        else:
            return

    def add_user(self):
        obj = File('mijoz.json')
        load = obj.read()
        load.append(self.__dict__)
        obj.write(load)



    def taom_ol(self, id = None, pors = None):
        obj = File('ovqat.json').read()
        new1 = []
        now = datetime.now()
        dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
        a = False
        for i in obj:
            if i['id'] == id and i['amout'] >= pors:
                new1.append({
                    "id": i['id'],
                    "name": i['name'],
                    "price": i['price'],
                    "Soni": pors,
                    "vaqti": dt_string
                })
                a = True
                i['amout'] -= pors
                File('ovqat.json').write(obj)

        if a:
            obj1 = File('mijoz.json').read()
            for i in obj1:
                if i['username'] == self.username:
                    i['by_food'].append(*new1)
            File('mijoz.json').write(obj1)

            obj3 = File('xisobot.json').read()
            obj3.append(*new1)
            File('xisobot.json').write(obj3)
        else:
            print("Qaytadan urining!")

    def ichimlik_ol(self, id, amoult):
        obj = File('ichimlik.json').read()
        new2 = []
        now = datetime.now()
        dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
        b = False
        for i in obj:
            if i['id'] == id and i['amout'] >= amoult:
                new2.append({
                    "id": i['id'],
                    "name": i['name'],
                    "price": i['price'],
                    "Soni": amoult,
                    "vaqti": dt_string
                })
                b = True
                i['amout'] -= amoult
                File('ichimlik.json').write(obj)

        if b:
            obj1 = File('mijoz.json').read()
            for i in obj1:
                if i['username'] == self.username:
                    i['by_water'].append(*new2)
            File('mijoz.json').write(obj1)

            obj3 = File('xisobot.json').read()
            obj3.append(*new2)
            File('xisobot.json').write(obj3)

    def info_ovqat(self):
        obj = File('ovqat.json').read()
        for i in obj:
            print("ID raqam:", i['id'], "  ", "Ovqat nomi:", i['name'], "  ", "Ovqat narxi:", i['price'], "  ", "Ovqatni qolgan miqdori (PORS):", i['amout'])

    def info_water(self):
        obj = File('ichimlik.json').read()
        for i in obj:
            print("ID raqam:", i['id'], "  ", "Ichimlik nomi:", i['name'], "  ", "Ichimlik narxi:", i['price'], "  ", "Ichimlikni qolgan miqdori (DONADA):", i['amout'])


    def oldingi_xarid_o(self):
        obj = File('mijoz.json').read()
        for i in obj:
            if i['username'] == self.username:
                for j in i['by_food']:
                    print("ID raqam:", j['id'], "  ", "Ovqat nomi:", j['name'], "  ", "Ovqat narxi:", j['price'], "  ", "Ovqatni qolgan miqdori (PORS):", j['Soni'],  "Xaridqilingan vaqt: ", j['vaqti'])

    def oldingi_xarid_s(self):
        obj = File('mijoz.json').read()
        for i in obj:
            if i['username'] == self.username:
                for j in i['by_water']:
                    print("ID raqam:", j['id'], "  ", "Ovqat nomi:", j['name'], "  ", "Ovqat narxi:", j['price'], "  ", "Ovqatni qolgan miqdori (PORS):", j['Soni'] , "Xaridqilingan vaqt: ", j['vaqti'])


def max_id1():
    maxx1 = []
    obj = File('ovqat.json').read()
    for i in obj:
        maxx1.append(i['id'])

    return maxx1

def max_id2():
    maxx2 = []
    obj = File('ichimlik.json').read()
    for i in obj:
        maxx2.append(i['id'])

    return maxx2



print("____________________Burak_uz____________________")
while True:
    text = '''
   1) Kirish
   2) Ro'yxatdan o'tish
    >>>  '''
    ttext = input(text)
    if ttext == '1':
        username = input("Username kiriting: ")
        password = input("Parolni kiriting: ")
        string1 = hashlib.md5(b'password')
        hesh = string1.hexdigest()

        boss = Boss(username=username, password=hesh)
        mijoz = Mijoz(username=username, password=hesh)
        if boss.check_username():
            while True:
                text2 = '''
                1) Ovqat qo'shish
                2) Ichimlik qo'shish
                3) Hisobot
                0) Exit
                '''
                ttext2 = input(text2)
                if ttext2 == '1':
                    print("_____Mavjud taomlar_____")
                    ovqat = Mijoz(username=username)
                    ovqat.info_ovqat()
                    print("_____Taom qushish_____")
                    a = max_id1()
                    num = max(a) + 1
                    name = input("Taomning nomini kiriting: ")
                    price = int(input("Taomning narxini kiriting: "))
                    amout = int(input("Taomning miqdorini kiriting: "))
                    qushish = Taom(num, name, price, amout)
                    qushish.add_meal()
                    print("Taom qushildi!")

                if ttext2 == '2':
                    print("_____Mavjud ichimliklar_____")
                    ichimlik = Mijoz(username=username)
                    ichimlik.info_water()
                    print("_____Ichimlik qushish_____")
                    b = max_id2()
                    num2 = max(b) + 1
                    name = input("Ichimlikning nomini kiriting: ")
                    price = int(input("Ichimlikning narxini kiriting: "))
                    amout = int(input("Ichimlikning sonini kiriting: "))
                    saqla = Taom(num2, name, price, amout)
                    saqla.add_ichimlik()
                    print("Ichimlik qushildi!")

                if ttext2 == '3':
                    print("_____Mavjud taomlar_____")
                    ovqat = Mijoz(username=username)
                    ovqat.info_ovqat()
                    print()
                    print("_____Mavjud ichimliklar_____")
                    ichimlik = Mijoz(username=username)
                    ichimlik.info_water()
                    print()
                    print("_____Bugungi savdo!_____")
                    malumot = Boss()
                    malumot.malumot()

                if ttext2 == '0':
                    break

        if mijoz.check_login() :
            while True:
                mijoz = '''
                1) Ovqatga buyurtma
                2) Ichimlikga buyurtma
                3) Oldingi buyurtmalari
                0) Exit
                >>>  '''
                tanla1 = input(mijoz)
                if tanla1 == '1':
                    ovqat = Mijoz(username=username)
                    ovqat.info_ovqat()
                    print("___Kerakli bo'lgan taomning ID raqamini kiriting: ")
                    num = int(input("ID raqam kiriting: "))
                    pors = int(input("Ovqat miqdorini kiriting (PORS): "))
                    if pors >= 0:
                        ovqat.taom_ol(num, pors)
                    else:
                        print("Bekzod aka b*a!")

                if tanla1 == '2':
                    ichimlik = Mijoz(username=username)
                    ichimlik.info_water()
                    print("___Kerakli bo'lgan ichimlikning ID raqamini kiriting: ")
                    num1 = int(input("ID raqam kiriting: "))
                    dona = int(input("Ichimlikning miqdorini kiriting (DONA): "))
                    if dona >= 0:
                        ichimlik.ichimlik_ol(num1, dona)
                    else:
                        print("Bekzod aka b*a!")

                if tanla1 == '3':
                    eski = Mijoz(username=username)
                    print("Siz harid qilgan taomlar")
                    eski.oldingi_xarid_o()
                    print()
                    print("Siz harid qilgan ichimliklar")
                    eski.oldingi_xarid_s()
                if tanla1 == '0':
                    break


    if ttext == '2':
        username = input("Username kiriting: ")
        password = input("Parol quying: ")
        string1 = hashlib.md5(b'password')
        hesh = string1.hexdigest()
        print("_____Adminmisiz?_____")
        text4 = '''
        1) HA
        2) YUQ
        >>> '''
        tanla4 = input(text4)
        if tanla4 == '1':
            a = Mijoz(username=username, password=hesh)
            b = Boss(username=username, password=hesh)
            if not a.check_red() and not b.check_red_boshliq():
                b.add_boss()
                print("Ro'yxatdan o'tdingiz!")
            else:
                print("Xatolik bor!")
        if tanla4 == '2':
            a = Mijoz(username=username, password=hesh)
            b = Boss(username=username, password=hesh)
            if not a.check_red() and not b.check_red_boshliq():
                a.add_user()
                print("Ro'yxatdan o'tdingiz!")
            else:
                print("Xatolik bor!")





