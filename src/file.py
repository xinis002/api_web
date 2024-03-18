from abc import ABC, abstractmethod
import json

class FileStorage(ABC):

    @abstractmethod
    def save_data(self, data, filepath):
        pass

    @abstractmethod
    def get_data(self, criteria, filepath):
        pass

    @abstractmethod
    def delete_data(self, criteria, filepath):
        pass

class JSONSaver(FileStorage):
    def save_data(self, data, filepath):
        try:
            with open(filepath, 'w') as file:
                json.dump(data, file)
        except IOError as e:
            print(f"An error occurred while saving data: {e}")

    def get_data(self, criteria, filepath):
        try:
            with open(filepath, 'r') as file:
                data = json.load(file)
                filtered_data = [d for d in data if criteria(d)]
                return filtered_data
        except IOError as e:
            print(f"An error occurred while reading data: {e}")
            return []

    def delete_data(self, criteria, filepath):
        try:
            with open(filepath, 'r') as file:
                data = json.load(file)
            data = [d for d in data if not criteria(d)]
            with open(filepath, 'w') as file:
                json.dump(data, file)
        except IOError as e:
            print(f"An error occurred while deleting data: {e}")

