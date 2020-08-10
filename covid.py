import requests

url = "https://covid-19-coronavirus-statistics.p.rapidapi.com/v1/total"

querystring = {"country": "Ukraine"}

headers = {
    'x-rapidapi-host': "covid-19-coronavirus-statistics.p.rapidapi.com",
    'x-rapidapi-key': "183e4230e7msh004b9846f66517dp10b0ddjsnef33d4b83bf7"
}

response = requests.request("GET", url, headers=headers, params=querystring)
location = response.json()['data']['location']
confirmed = response.json()['data']['confirmed']
recovered = response.json()['data']['recovered']
death = response.json()['data']['deaths']
print('Страна:', 'Украина')  # location
print('Зафиксировано:', confirmed)
print('Выздоровело:', recovered)
print('Умерло:', death)
