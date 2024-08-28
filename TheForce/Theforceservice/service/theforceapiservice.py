import requests

class SwapiService:
    BASE_URL = "https://swapi.dev/api/people/"

    @staticmethod
    def fetch_people_data():
        try:
            response = requests.get(SwapiService.BASE_URL)
            response.raise_for_status()  
            data = response.json()
            return SwapiService.sort_people_by_name(data['results'])
        except requests.exceptions.RequestException as e:
            raise Exception(f"Unable to get data from SWAPI: {str(e)}")

    @staticmethod
    def sort_people_by_name(people):
        return sorted(people, key=lambda person: person['name'])
