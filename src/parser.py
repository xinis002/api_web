from abc import ABC, abstractmethod
import requests


class Parser(ABC):

    @abstractmethod
    def get_params(self, keyword: str):
        pass


    @abstractmethod
    def get_vacancies(self, keyword: str):
        pass





class HH(Parser):

    def __init__(self):
        self._url = "https://api.hh.ru/vacancies"


    def get_params(self,keyword: str):

        params = {
            'per_page': 100,
            'page': 1,
            'text': keyword
         }
        return params

    def get_vacancies(self, keyword: str):
        params = self.get_params(keyword)
        try:
            response = requests.get(self._url, params=params)
            response.raise_for_status()
            return response.json().get('items', [])
        except requests.RequestException as e:
            print(f"An error occurred: {e}")
            return []
