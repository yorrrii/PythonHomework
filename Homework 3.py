import requests

class newPlace:
    """Работа с place_id"""
    base_url = 'https://rahulshettyacademy.com'
    resource = '/maps/api/place/add/json'
    def post_place_id(self):
        """Получение place_id"""
        key_value = '?key=qaclick123'
        url = f'{self.base_url}{self.resource}{key_value}'
        json_new_location = {
            "location": {
                "lat": -38.383494,
                "lng": 33.427362
            }, "accuracy": 50,
            "name": "Frontline house",
            "phone_number": "(+91) 983 893 3937",
            "address": "29, side layout, cohen 09",
            "types": [
                "shoe park",
                "shop"
            ],
            "website": "http://google.com",
            "language": "French-IN"
        }
        response = requests.post(url, json=json_new_location)
        response_result = response.json()
        place_id = response_result.get('place_id')
        assert response.status_code == 200, 'Ошибка получения place_id'
        return place_id
    def text_place_id(self):
        """Запись place_id в документ"""
        count = 0
        while count < 5:
            place_id = self.post_place_id()
            with open('file_1.txt','a') as file1:
                file1.write(place_id + '\n')
            count +=1
            """Получение данных из документа"""
        with open('file_1.txt','r') as file_1:
            content = file_1.readlines()
        return content
    def get_place_id(self):
        """Проверка place_id"""
        place_id_list = self.text_place_id()
        key_value = '?key=qaclick123&place_id='
        for i in place_id_list:
            get_url = f'{self.base_url}{self.resource}{key_value}{i.strip()}'
            result_get = requests.get(get_url)
            print(result_get.text)
            assert result_get.status_code == 200, 'Ошибка, локация с таким place_id отсутствует'

place_id_create = newPlace()
place_id_create.get_place_id()
