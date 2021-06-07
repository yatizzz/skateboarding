
import unittest
import re
from datetime import datetime


#исходные данные
list_mail_uncor = ["1","wrw@ksjf...ksu","jhg.sds.dsf","","jsghfa"]
list_mail_cor = ["m.m@mail.ru", "m1@gmail.com","131m@mail.com","jjjjj@qwe.ds", "ap55@yandex.com"]

list_phone_uncor = ["", "123", "242342+34234", "45345", "//////////","8911-99", "-+91176", "a", "8911--762---45-45"]
list_phone_сor = ["89117628448", "9117628448", "911-762-8228", "(123)1234567", "(543)234-2345"]

list_data_uncor = ['2021-09-01','1999-3-17','2020-02-30','today','99-9-9', '12.01.2020','11/22/2009','20-04-2019','01-07-2010','2016.03.15']
list_data_cor = ['2021-01-01','1999-03-17','2020-02-29','2002-09-19']

#регулярные выражения
re_mail=r"^\w+@\w+(\.\w+)+$"
re_date = r"^[0-9]{4}-[0-9]{2}-[0-9]{2}$"
re_phone='(\d{3}[-\.\s]??\d{3}[-\.\s]??\d{4}|\(\d{3}\)\s*\d{3}[-\.\s]??\d{4}|\d{3}[-\.\s]??\d{4})'

#проверка имейла
def author_email_correct(email):
    return re.match(re_mail,email) is not None

#проверка даты
def written_date_correct(date_input):
        if re.match(re_date, date_input) is None:
            return False
        try:
            # перевод строки в datatime
            date = datetime.strptime(date_input, '%Y-%m-%d')
            # проверка того, что введенная дата не больше текущей
            if date <= datetime.today():
                return True
            else: return False
        except ValueError:
            return False

#проверка телефона
def author_phone(phone):
    return re.search(re_phone,phone)

