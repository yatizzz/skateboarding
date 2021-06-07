import bottle
from bottle import post, request, template
import json
import datetime
import module1

@post('/reviews', method='post')
# метод для добавления в файл информации о статьях
def module2():
    try:
        # берем введенные значения, а также текущую дату
        title = request.forms.get('TITLE')
        advantages = request.forms.get('ADVANTAGES')        
        limitations = request.forms.get('LIMITATIONS')
        author = request.forms.get('AUTHOR')
        phone = request.forms.get('PHONE')
        published_date = datetime.date.today().isoformat()
        author_email = request.forms.get('AUTHOR_EMAIL')
        written_date = request.forms.get('WRITTEN_DATE')

        # проверка того, все ли поля заполнены
        if title=="" or advantages=="" or limitations=="" or author=="" or author_email=="":
            return "Fill all the fields!"

        # вызов метода для проверки корректности ввода почты
        if not module1.author_email_correct(author_email):
            return "Please, put a correct email (like www@mail.com)"

        # вызов метода для проверки корректности ввода даты написания отзыва
        if not module1.written_date_correct(written_date):
            return "Data should have a format 'YYYY-MM-DD' and not be after today"

        # вызов метода для проверки корректности ввода номера телефона
        if not module1.author_phone(phone):
            return "Enter correct phone number!"

        # открытие файла для чтения для подсчета количества отзывов
        with open('./reviews.json', 'r') as file:
            reviews=json.load(file)
            reviews_number = len(reviews)

        # открытие файла для записи
        with open('./reviews.json', 'w') as file:
            reviews[reviews_number+1] = {'author':author, 'title':title,'advantages':advantages, 'limitations':limitations,
                                           'published_date': published_date,'written_date': written_date, 'phone':phone, 'author_email': author_email}
            json.dump(reviews, file)

        return "The review is added!"
    except Exception:
        return "The review is not added!"
        
    finally:
        pass

