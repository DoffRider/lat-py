import requests

respon = requests.get("https://gitlab.com/api/v4/users/nanuchi/projects")

my_project = respon.json()

# print(type(respon))

for i in my_project:
    print(f"Project Name : {i['name']} \nProject Url : {i['web_url']} \n")