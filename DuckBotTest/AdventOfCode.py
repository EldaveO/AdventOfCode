import requests
import json


class MakeApiCall:

    def get_data(self, api):
        response = requests.get(f"{api}")
        if response.status_code == 200:
            print("sucessfully fetched the data")
            print(response.json())
            #self.formatted_print(response.json())
        else:
            print(
                f"Hello person, there's a {response.status_code} error with your request")

    def get_user_data(self, api, parameters):
        response = requests.get(f"{api}", params=parameters)
        if response.status_code == 200:
            print("sucessfully fetched the data with parameters provided")
            print(response.json())
            #self.formatted_print(response.json())
        else:
            print(
                f"Hello person, there's a {response.status_code} error with your request")

    def formatted_print(self, obj):
        text = json.dumps(obj, sort_keys=True, indent=4)
        print(text)

    def __init__(self, api):
        self.get_data(api)

        # parameters = {
        #     "username": "kedark"
        # }
        # self.get_user_data(api, parameters)


if __name__ == "__main__":
    api_call = MakeApiCall("https://adventofcode.com/2022/leaderboard/private/view/1884339.json",cookies={'cookies': '53616c7465645f5f0b197f5d16121e802a60afe040ade280df531feb410de651c279aac6563858909021e2f0dec4d969219557ec1039c75fcc8598b999c627e1'})