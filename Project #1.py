



class User():
    balance = 0

    def __init__(self, login, password, name):
        self.login = login
        self.password = password
        self.name = name
        self.comment = {}

class Company():

    balance = 0

    def __init__(self, login, password, company_name):
        self.login = login
        self.password = password
        self.company_name = company_name
        self.company_catalog = {}

    def info(self):
        print(self.company_catalog)

class ErrorLogin(Exception):
    def __init__(self, text):
        self.text = text
    def __str__(self):
        return self.text 
        
def maimenu(users,companies):
    print('Здравствуйте, вы попали на какой-то сайт\nНажмите 1 если вы покупатель,\nЕсли вы продавец 2')
    # Выясняем роль
    try:
        role= int(input())
        if role < 1 or role > 2:
            print('ОШИБКА\nВведите 1 или 2')
            return maimenu(users,companies)
    except Exception:
        print('Error')
        return maimenu(users,companies)
    #User
    if role == 1:
        print('Нажмите 1, чтобы зарегистрироваться\n2 Чтобы войти в кабинет\n0 Чтобы вернуться назад')
        response = int(input())
        if response == 1:
            return newLogUser(users,companies)
        elif response == 2:
            return logUser(users,companies)
        elif response == 0:
            return maimenu(users,companies)
    #Company
    elif role ==2:
        print('Нажмите 1, чтобы зарегистрироваться\n2 Чтобы войти в кабинет\n0 Чтобы вернуться назад')
        response = int(input())
        if response == 1:
            return newLogCompany(users,companies)
        elif response == 2:
            return logCompany(users,companies)
        elif response == 0:
            return maimenu(users,companies)
#Регистрируем User    
def newLogUser(users,companies):
    try:
        logName = input('Введите новый логин:')
        if len(logName) < 3 or len(logName) > 6: 
            raise Exception

    except Exception:
        print('Логин должен составлять не меньше 3-х символов, и не больше 6-и')
        return newLogUser(users,companies)
    try: 
        pass1 = input('Введите новый пароль:')
        pass2 = input('Введите пароль повторно:')
        if len(pass1) <3 or len(pass1)>6:
            raise Exception
        elif pass1 != pass2:
            raise Exception
    except Exception:
        print('Пароль должен составлять не меньше 3-х символов, и не больше 6-и\n Или пароли не совпадают, введите еще раз')
        return newLogUser(users,companies)
        
    nameUser = input('Введите ваше Имя:')
        
    # Проверяем, если пароли совпадают, то переходим на регистрацию пользователя
    if pass1 == pass2:
        user = User(logName, pass1, nameUser)
        users.append(user)
    print('Вы успешно зарегистрировались\nЧтобы войти в аккаунт, введите ваш логин и пароль')
    return logUser(users, companies)
#Регистрируем Company
def newLogCompany(users,companies):
        try:
            logName = input('Введите новый логин:')
            if len(logName) < 3 or len(logName) > 6: 
                    raise Exception

        except Exception:
            print('Логин должен составлять не меньше 3-х символов, и не больше 6-и')
            return newLogCompany(users,companies)
        try:
            pass1 = input('Введите новый пароль:')
            pass2 = input('Введите пароль повторно:')
            if len(pass1) <3 or len(pass1)>6:
                raise Exception
            elif pass1 != pass2:
                raise Exception
        except Exception:
            print('Пароль должен составлять не меньше 3-х символов, и не больше 6-и\n Или пароли не совпадают, введите еще раз')
            return newLogCompany(users,companies)
        nameCompany = input('Введите имя вашей Компании:')
        if pass1 == pass2:
            company = Company(logName, pass1, nameCompany)
            companies.append(company)
        print('Вы успешно зарегистрировались\nЧтобы войти в аккаунт, введите ваш логин и пароль')
        return logCompany(users, companies)
#Log USER
def logUser(users,companies):
    print('Введите логин:')
    log = input()
    print('Введите пароль:')
    pas = input()
    for i in users:
        
        if i.login == log and i.password == pas:
            user = i 
            print('Приветствуем, ' + user.name + '!')
            return menuUser(i)
    print('Неверый логин или пароль, попробуйте еще раз')
    return logUser(users, companies)
#Log Company
def logCompany(users,companies):
    print('Введите логин:')
    log = input()
    print('Введите пароль:')
    pas = input()
    for i in companies:
        if i.login == log and i.password == pas:
            company_name = i 
            print('Приветствуем, ' + company_name.company_name + '!')
            return menuCompany(i)   
    print('Неверый логин или пароль, попробуйте еще раз')
    return logCompany(users, companies)
#Menu Company
def menuCompany(company):
    print('Выберите действие:', '\n1 - добавить товар',
          '\n2 - посмотреть список товаров', '\n3 - изменить цену товара',
          '\n4 - посмотреть баланс', '\n5 - удалить товар', '\n6 - Выйти')
    x = int(input())
    if x == 1:
        return tovarPlus(company)
    if x == 2:
        return allTovars(company)
    if x == 3:
        return izmenitCen(company)
    if x == 4:
        return balanceCheck(company)
    if x == 5:
        return delTovar(company)
    else:
        return maimenu(users, companies)
#Функция возврата или выхода
def comebackCom(company):
    print('1 - вернуться в главное меню', '\n2 - выйти')
    x = int(input())
    if x == 1:
        return print('Главное меню'), menuCompany(company)
    else:
        return maimenu(users, companies)
#Добавляем товар 
def tovarPlus(company):
    print('Наименование товара:')
    tovar = input()
    print('Цена товара:')
    price = int(input())
    company.company_catalog[tovar] = price
    print('Товар добавлен')
    for i, j in company.company_catalog.items():
        print(i, j)
    return comebackCom(company)
#Список товаров
def allTovars(company):
    for i, j in company.company_catalog.items():
            print(i, j)
    return comebackCom(companies)
#Изменить цену товара
def izmenitCen(company):
    print('Напишите название товара, у которого хотите поменять цену')
    for i, j in company.company_catalog.items():
        print(i, j)
    x = input()
    print('Напишите новую цену:')
    y = int(input())
    if x in company.company_catalog.keys():
        company.company_catalog[x] = y
        for i, j in company.company_catalog.items():
            print(i, j)
    return comebackCom(company)
#Узнать баланс
def balanceCheck(company):
    print('Ваш баланс: ', company.balance)
    return comebackCom(company)
#Удаление товара
def delTovar(company):
    print('Напишите наименование товара:')
    for i, j in company.company_catalog.items():
        print(i, j)
    x = input()
    if x in company.company_catalog.keys():
        del company.company_catalog[x]
        print('Товар удален')
        return comebackCom(company)
    else:
        print('Товар не найден')
        return comebackCom(company)

#Menu User
def menuUser(user):
    print('Выберите действие:', '\n1 - посмотреть список всех товаров',
      '\n2 - посмотреть товар выбранной компании', '\n3 - купить товар',
      '\n4 - пополнить баланс', '\n5 - написать отзыв', '\n6 - Выйти')
    x = int(input())
    if x == 1:
        return tovary(user)
    if x == 2:
        return tovaryCom(user)
    if x == 3:
        return byeTovar(user)
    if x == 4:
        return balancePlus(user)
    if x == 5:
        return comment(user)
    else:
        return maimenu(users, companies)
#Функция возврата или выхода  
def comeback_u(user):
    print('1 - Вернуться в главное меню', '\n2 - Выйти')
    x = int(input())
    if x == 1:
        return print('Главное меню'), menuUser(user)
    else:
        return maimenu(users, companies)
# Список товаров
def tovary(user):
    print('Товары')
    for i in companies:
        for j, k in i.company_catalog.items():
            print(j, k)
    return comeback_u(user)
# Товары компании
def tovaryCom(user):
    print('Выберите компанию и напишите наименование:')
    for i in companies:
        print(i.company_name)
    x = input()
    for i in allTovars(companies):
        if i.company_name == x:
            for k, y in i.company_catalog.items():
                print(k, y)
        return comeback_u(user)
    else:
        print('Нет такой компании')
        return comeback_u(user)  
# Пополнить баланс
def balancePlus(user):
    print('Ваш баланс:',user.balance)
    print('Введите сумму пополнения:')
    x = int(input())
    user.balance += x
    print('Ваш баланс:', user.balance )
    return comeback_u(user)
# Оставить отзыв
def comment(user):
    print('Оставте отзыв ниже:')
    x = input()
    comments.append(x)
    print('Спасибо за ваш отзыв:' + x)
    return comeback_u(user)
# Купить товар
def byeTovar(user):
    print('Какой товар хотите купить')
    print('Список товаров:')
    for i in companies:
        for j, k in i.company_catalog.items():
            print(j, k)
    x = input()
    for i in companies:
        if x in i.company_catalog.keys():
            a = i.company_catalog[x]
            print(a)
            if user.balance >= a:
                print('Вы купили ' + x)
                user.balance -= a
                i.balance += a
                del i.company_catalog[x]
            else:
                print('У вас недостаточно средств')
        return comeback_u(user)
    else:
        print('Такого товара нет в каталоге или вы ввели неверное имя')
        return comeback_u(user)

users = []
companies = []
comments = []

user1 = User('max', 'Qwer', 'Max')
user2 = User('asd', 'qwer', 'Asd')

users.append(user1)
users.append(user2)

company1 = Company("lg", "qwer", 'LG')
companies.append(company1)
company1.company_catalog['TV'] = 5000

company2 = Company("abs", "qwer", 'ABS')
companies.append(company2)
company2.company_catalog['Phone'] = 2000
company2.company_catalog['Lamp'] = 500

maimenu(users, companies)