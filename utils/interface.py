from src.parser import HH
from src.vacancy import Vacancy
from src.file import JSONSaver
def main():

    hh_parser = HH()


    keyword = input("Введите ключевое слово для поиска вакансий: ")
    n_vacancies = int(input("Сколько вакансий сохранить? "))


    vacancies = hh_parser.get_vacancies(keyword)[:n_vacancies]


    vacancies_list = [Vacancy(v['name'], v['url'], v.get('salary', {}).get('from'), v.get('salary', {}).get('to'), v.get('salary', {}).get('currency')) for v in vacancies]


    vacancies_data = [vacancy.to_dict() for vacancy in vacancies_list]


    saver = JSONSaver()
    filepath = "vacancies.json"
    saver.save_data(vacancies_data, filepath)

    print(f"Вакансии сохранены в файл {filepath}")

if __name__ == "__main__":
    main()