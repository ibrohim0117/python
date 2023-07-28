import json
from datetime import datetime


class File:
    def __init__(self, file_name):
        self.file_name = file_name

    def uqish(self):
        with open(self.file_name, 'r') as f:
            try:
                l = json.load(f)
            except:
                l = []
            return l

    def yozish(self, lists: list)-> None:
        with open(self.file_name, 'w') as f:
            json.dump(lists, f, indent=4)


class User:
    def __init__(self, name=None, username=None, password=None, balans=None, myproduct = []):
        self.name = name
        self.username = username
        self.password = password
        self.balans = balans
        self.myproduct = myproduct

    def foydalanuvci_saqlash(self):
        obj = File('user.json')
        l = obj.uqish()
        l.append(self.__dict__)
        obj.yozish(l)

    def check_username(self):
        obj = File('user.json')
        for i in obj.uqish():
            if self.username == i['username']:
                return True
        else:
            return False

    def check_login(self):
        obj = File('user.json')
        for i in obj.uqish():
            if i['username'] == self.username and i['password'] == self.password:
                return True
        else:
            return

    def my_prod(self):
        etc = File('user.json').uqish()
        for i in etc:
            if i['username'] == self.username:
                print(i['myproduct'])

    def buy_product(self, id, amount):
        file2 = File('product.json').uqish()
        new = []
        now = datetime.now()
        dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
        a = False
        for i in file2:
            if i['id'] == id and i['amount'] >= amount:
                new.append({
                    "id": i['id'],
                    "name": i['name'],
                    "price": i['price'],
                    "amount": amount,
                    "vaqti": dt_string
                })
                a = True

                i['amount'] -= amount
        File('product.json').yozish(file2)


        if a:
            obj1 = File('user.json').uqish()
            for i in obj1:
                if i['username'] == self.username:
                    i['myproduct'].append(*new)
            File('user.json').yozish(obj1)

            obj3 = File('xisobot.json').uqish()
            obj3.append(*new)
            File('xisobot.json').yozish(obj3)



class Product:
    def __init__(self, id = None, name = None, price = None, amount = None):
        self.id = id
        self.name = name
        self.price = price
        self.amount = amount

    def save_product(self):
        products = File('product.json').uqish()
        products.append(self.__dict__)
        File('product.json').yozish(products)

    def kurish(self):
        product = File('product.json').uqish()
        print("_________________________Maxsulotlar xaqida malumotlar_________________________")
        for i in product:
            print("ID raqam:",i['id'], "  ", "Maxsulot nomi:", i['name'], "  ", "Maxsulot narxi:",i['price'], "  ", "Maxsulot soni:",i['amount'])



    def xisobot(self):
        print("_________________Sotilgan axsulotlar xaqida malumotlar_________________________")
        obj = File('xisobot.json').uqish()
        summa = 0
        for i in obj:
            summa += i['amount'] * i['price']
            print("ID raqam:", i['id'], "  ", "Sotilgan maxsulot nomi:", i['name'], "  ", "Sotilgan maxsulo narxi:",
                  i['price'], "  ", "Sotilgan maxsulo miqdori :", i['amount'], "Sotib olingan vaqti: ", i['vaqti'])
        print("Jami sotilgan maxsulotlar summasi--> ", summa)



class Admin:
    def __init__(self, username = None, password = None):
        self.username = username
        self.password = password

    def check_username(self):
        obj = File('admin.json')
        for i in obj.uqish():
            if self.username == i['username']:
                return True
        else:
            return False

    def check_login_admin(self):
        obj = File('admin.json')
        for i in obj.uqish():
            if i['username'] == self.username and i['password'] == self.password:
                return True
        else:
            return



print("_________________Malika bozor_________________")
print("Kim sifatida kirmoqchisiz!")
while True:
    text = '''
    1) Admin
    2) Foydalanuvchi
    >>>  '''
    tanla = input(text)
    if tanla == '1':
        username = input("Username kiriting: ")
        kod = int(input("Parol kiriting: "))
        admin = Admin(username=username, password=kod)
        while True:
            if admin.check_login_admin():
                andmin_text = '''
                1) Maxsulot qushish
                2) Xisobot
                0) Exit
                >>>  '''
                adtanla = input(andmin_text)
                if adtanla == '1':
                    id = int(input("Maxsulot ID raqamini kiriting: "))
                    name = input("Maxsulot nomini kiriting: ")
                    price = int(input("Maxsulot narxini kiriting: "))
                    amount = int(input("Maxsulot miqdorini kiriting: "))
                    seve = Product(id, name, price, amount)
                    seve.save_product()
                    print('Product qushildi')

                if adtanla == '2':
                    xisobot = Product()
                    xisobot.xisobot()

                if adtanla == '0':
                    break


    if tanla == '2':
        while True:
            text1 = '''
            1) Krish
            2) Ro'yxatdan utish
            0) Exit
            >>>  '''

            tanla1 = input(text1)

            if tanla1 == '1':
                username = input("Username kiriting: ")
                kod = int(input("Parol kiriting: "))
                user = User(username=username, password=kod)

                #2-menyu ochiladigan joy
                while True:
                    if user.check_login():
                        text2 = '''
                        1) Product and purchase
                        2) My product
                        3) Balans
                        0) Exit
                        >>>  '''
                        tanla2 = input(text2)
                        if tanla2 == '1':
                            info = Product()
                            info.kurish()
                            print("_______________Sotib olish!_________________")
                            num = int(input("ID raqam kiriting: "))
                            amount = int(input("Qancha kerak: "))
                            buy = User(username=username)
                            buy.buy_product(num, amount)
                            now = datetime.now()
                            dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
                            print('Vaqti: ', dt_string)

                        if tanla2 == '2':
                            malumot = User(username=username)
                            malumot.my_prod()
                            print()

                        if tanla2 == '0':
                            break

                    else:
                        print("Xatolik bor yoki ro'yxatdan utmagansiz qaytadan urining!")
                        break

                    #1-tanlaning else qismi


            if tanla1 == "2":
                name = input("Ismingizni kiriting: ")
                username = input("Foydalanuvchi nomini kiriting: ")
                kod = int(input("Parol kiriting: "))
                balans = int(input("Balansingizni kiriting: "))
                reg = User(name, username, kod, balans)
                if not reg.check_username():
                    reg.foydalanuvci_saqlash()
                    print("Muvofaqiyatli saqlandi!")
                else:
                    print("Bunday foydalanuvchi nomi mavjud!")

            if tanla1 == '0':
                break






















