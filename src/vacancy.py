import json


class Vacancy:
    def __init__(self, name, url, salary_from, salary_to, currency):
        self.name = name
        self.url = self.validate_url(url)
        self.salary_from = self.is_salary(salary_from)
        self.salary_to = 0
        self.currency = currency





    def validate_url(url):
        return url if url and isinstance(url, str) else "URL не указан"

    def is_salary(self, value):
        if value:
            return value
        return 0

    def __lt__(self, other):
        get_salary = lambda salary: 0 if isinstance(salary, str) else salary
        return get_salary(self.salary_from) < get_salary(other.salary_from)


    def __eq__(self, other):
        return self.salary_from == other.salary_from and self.salary_to == other.salary_to


    def to_dict(self):
        return {
            'name': self.name,
            'url': self.url,
            'salary_from': self.salary_from,
            'salary_to': self.salary_to,
            'currency': self.currency
        }


    @classmethod
    def from_dict(cls, data):
        return cls(**data)

    @staticmethod
    def from_json(json_data):
        data = json.loads(json_data)
        return Vacancy.from_dict(data)


