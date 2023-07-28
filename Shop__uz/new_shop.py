import json
import hashlib
from datetime import datetime

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

    def write(self, lists):
        with open(self.filename, 'w') as file:
            json.dump(lists, file, indent=4)


class User:
    def __init__(self,username=None, password=None, myproduct = []):
        self.username = username
        self.password = password
        self.myproduct = myproduct

    def check_reg(self):
        obj = File('user.json').read()
        for i in obj:
            if i['username'] == self.username:
                return True
        else:
            return False

    def check_login(self):
        obj = File('user.json').read()
        for i in obj:
            if i['username'] == self.username and i['password'] == self.password:
                return True
        else:
            return

    def save_user(self):
        obj = File('user.json')
        l = obj.read()
        l.append(self.__dict__)
        obj.write(l)

    def info_myproduct(self):
        obj = File('user.json').read()
        for i in obj:
            if i['username'] == self.username:
                for j in i['myproduct']:
                    print("ID raqam:", j['id'], "  ", "Maxsulot nomi:", j['name'], "  ", "Maxsulot narxi:", j['price'], "  ",
                          "Olgan maxsulotingiz soni :", j['amount'],  "Xaridqilingan vaqt: ", j['vaqti'])

    def by_product(self, id, count):
        new = []
        a = False
        now = datetime.now()
        dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
        obj = File('product.json').read()
        for i in obj:
            if i['id'] == id and i['amount'] >= count:
                new.append({
                    "id": i['id'],
                    "name": i['name'],
                    "price": i['price'],
                    "amount": count,
                    "vaqti": dt_string
                })
                a = True
                i['amount'] -= count
        File('product.json').write(obj)

        if a:
            obj1 = File('user.json').read()
            for i in obj1:
                if i['username'] == self.username:
                    i['myproduct'].append(*new)
            File('user.json').write(obj1)

            obj3 = File('xisobot.json').read()
            obj3.append(*new)
            File('xisobot.json').write(obj3)


class Admin:
    def __init__(self, username=None, password=None):
        self.username = username
        self.password = password

    def check_reg_admin(self):
        obj = File('admin.json').read()
        for i in obj:
            if i['username'] == self.username:
                return True
        else:
            return False

    def check_login_admin(self):
        obj = File('admin.json').read()
        for i in obj:
            if i['username'] == self.username and i['password'] == self.password:
                return True
        else:
            return

    def save_admin(self):
        obj = File('admin.json')
        l = obj.read()
        l.append(self.__dict__)
        obj.write(l)




    def xisobot(self):
        print("_________________Sotilgan axsulotlar xaqida malumotlar_________________________")
        obj = File('xisobot.json').read()
        summa = 0
        for i in obj:
            summa += i['amount'] * i['price']
            print("ID raqam:", i['id'], "  ", "Sotilgan maxsulot nomi:", i['name'], "  ", "Sotilgan maxsulot narxi:",
                  i['price'], "  ", "Sotilgan maxsulot miqdori :", i['amount'], "Sotib olingan vaqti: ", i['vaqti'])
        print("Jami sotilgan maxsulotlar summasi--> ", summa)






class Product:
    def __init__(self, id = None, name = None, price = None, amount = None):
        self.id = id
        self.name = name
        self.price = price
        self.amount = amount

    def save_product(self):
        products = File('product.json').read()
        products.append(self.__dict__)
        File('product.json').write(products)

    def kurish(self):
        product = File('product.json').read()
        print("_________________________Maxsulotlar xaqida malumotlar_________________________")
        for i in product:
            print("ID raqam:",i['id'], "  ", "Maxsulot nomi:", i['name'], "  ", "Maxsulot narxi:",i['price'], "  ", "Maxsulot soni:",i['amount'])



def max_id():
    maxx = []
    obj = File('product.json').read()
    for i in obj:
        maxx.append(i['id'])

    return maxx




print("_________________Malika bozor_________________")
while True:
    text = '''
    1 - Kirish
    2 - Regestratsiya
    0 - Exit
    Choose ---> '''
    choose = input(text)
    if choose == '1':
        username = input("Username kiriting: ")
        password = input("Password kiriting: ")
        string1 = hashlib.md5(b'password')
        hesh = string1.hexdigest()
        admin = Admin(username=username, password=hesh)
        user = User(username=username, password=hesh)
        if admin.check_login_admin():
            while True:
                text2 = '''
                1 - Maxsulot qo'shish
                2 - Xisobot
                0 - Exit
                Choose ---> '''

                choose2 = input(text2)
                if choose2 == '1':
                    print("_____Hozir mavjud maxsulotlar_____")
                    tmp = Product()
                    tmp.kurish()
                    print("____Maxsulot qushish____")
                    a = max_id()
                    num = max(a) + 1
                    name = input("Maxsulot nomini kiriting: ")
                    price = int(input("Maxsulot narxini kiriting: "))
                    amount = int(input("Maxsulot miqdorini kiriting: "))
                    product = Product(id=num, name=name, price=price, amount=amount)
                    product.save_product()
                    print("Maxsulot qushildi")

                if choose2 == '2':
                    kurish = Product()
                    kurish.kurish()
                    print()
                    info = Admin()
                    info.xisobot()

                if choose2 == '0':
                    break

        if user.check_login():
            while True:
                text3 = '''
                1 - Maxsulot sotib olish
                2 - Oldingi xaridlarim
                0 - Exit
                Choose --->  '''

                choose3 = input(text3)
                if choose3 == '1':
                    kurish = Product()
                    kurish.kurish()
                    xarid = User(username=username)
                    id = int(input("Xarid qilmoqchi bo'lgan maxsulotingiz ID raqamini kiriting: "))
                    soni = int(input("Xarid qilmoqchi bo'lgan maxsulotingiz miqdorini  kiriting: "))
                    if soni >= 0:
                        xarid.by_product(id, soni)
                    else:
                        print("Qaytadan urining!")

                if choose3 == '2':
                    a = User(username=username)
                    a.info_myproduct()

                if choose3 == '0':
                    break



    if choose == '2':
        username = input("Username kiriting: ")
        password = input("Password kiriting: ")
        string1 = hashlib.md5(b'password')
        hesh = string1.hexdigest()
        print("_____Adminmisiz?_____")
        text4 = '''
        1) HA
        2) YUQ
        >>> '''
        tanla4 = input(text4)
        if tanla4 == '1':
            a = User(username, hesh)
            b = Admin(username, hesh)
            if not a.check_reg() and not b.check_reg_admin():
                b.save_admin()
                print("Muvofaqiyatli saqlandi!")
            else:
                print("Bunday username nomi mavjud!")


        if tanla4 == '2':
            a = User(username, hesh)
            b = Admin(username, hesh)
            if not a.check_reg() and not b.check_reg_admin():
                a.save_user()
                print("Muvofaqiyatli saqlandi!")
            else:
                print("Bunday username nomi mavjud!")

    if choose == '0':
        break
