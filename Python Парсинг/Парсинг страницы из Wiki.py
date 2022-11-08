import requests
from bs4 import BeautifulSoup

# Объявляем константу.
WIKI_PAGE = (
    "https://ru.wikipedia.org/wiki/%D0%A1%D0%BF%D0%B8%D1%81%D0%BE%D0%B"
    "A_%D0%B3%D0%BE%D1%81%D1%83%D0%B4%D0%B0%D1%80%D1%81%D1%82%D0%B2"
)


def parse_countries():
    """Функция для парсинг сайта wiki."""
    response = requests.get(WIKI_PAGE)  # Получаем ответ на запрос с сайта
    soup = BeautifulSoup(
        response.text, "html.parser"
    )  # BeautifulSoup() поместит текст ответа в переменную soup
    tables = soup.find_all(
        "table", class_="wikitable"
    )  # Выбираем только таблицы класса wikitable
    # find_all()возвращает список всех тегов или строк,
    # соответствующих определенному критерию

    list_of_countries = []  # список стран
    first_letter_count = {}  # словарь стран начинающихся на первую букву

    # Перебор циклом таблиц (кроме третей таблицы т.к. страны в ней есть в первой таблице).
    for table in [*tables[:2], *tables[3:]]:
        countries_soup = table.find_all("tr")[
            1:
        ]  # Выбираем из таблиц <tr> все строки начиная с второго

        # Перебор циклом soup стран для получения заданных переменных
        for country_soup in countries_soup:
            country_name = country_soup.find("a").get(
                "title"
            )  # из soup страны найти("а").получить("название")
            full_country_name = country_soup.find_all("td")[-1].text.replace(
                "\n", ""
            )  # найти полное название страны
            flag_url = (
                country_soup.find("a").find("img").get("src")
            )  # найти("a") найти("img") получить("источник")
            words_in_full_country_name = len(
                full_country_name.split(" ")
            )  # кол-во слов в полном названии страны

            # Записываем данные в словарь
            list_of_countries.append(
                {
                    "country": country_name,
                    "full_country_name": full_country_name,
                    "words_in_full_country_name": words_in_full_country_name,
                    "same_letter_count": 0,
                    "flag_url": flag_url,
                }
            )

            # Считаем количество стран начинающихся на туже первую букву
            first_letter = country_name[0]
            if first_letter in first_letter_count:
                first_letter_count[first_letter] += 1
            else:
                first_letter_count[first_letter] = 1

    # Присваиваем количество страна с такой же буквой в каждой строке
    for country in list_of_countries:
        country["same_letter_count"] = first_letter_count[country.get("country")[0]]

    return list_of_countries


def print_country_data(country_name: str):
    """Функция, которая будет выводить словарь с данными конкретной страны по её короткому имени."""
    # Перебор циклом в функции parse_countries для получения данных страны по имени страны
    for country_data in parse_countries():
        if country_data["country"] == country_name:
            print(country_data)
            break


if __name__ == "__main__":
    print_country_data("Украина")
    print_country_data("Австралия")
    print_country_data("Литва")
