# А теперь сделай рекурсивную функцию, которая принимает на вход название страны,
# и выводит данные по этой стране. Функция должна принимать только 3 страны (сам выбери какие).
# # Если ввел что то другое, должен сработать принт "вы ввели хуйню.
# # Можно вводить только.. и перечисление стран"
# Функция должна вызывать сама себя, до тех пор пока не введется правильная страна
import requests

url = "https://covid-19-coronavirus-statistics.p.rapidapi.com/v1/total"

headers = {
    'x-rapidapi-host': "covid-19-coronavirus-statistics.p.rapidapi.com",
    'x-rapidapi-key': "183e4230e7msh004b9846f66517dp10b0ddjsnef33d4b83bf7"
}


def stats_for_3_countries(strana):
    querystring = {"country": f"{strana.title()}"}
    possible_country = ("ukraine", "australia", "canada")
    response = requests.request("GET", url, headers=headers, params=querystring)
    location = response.json()['data']['location']
    confirmed = response.json()['data']['confirmed']
    recovered = response.json()['data']['recovered']
    death = response.json()['data']['deaths']
    if strana in possible_country:
        print('Страна:', location)
        print('Зафиксировано:', confirmed)
        print('Выздоровело:', recovered)
        print('Умерло:', death)
    else:
        print('Info only for Ukraine, Canada, Australia. Try again')
        stats_for_3_countries(str(input()).lower())


enter = str(input()).lower()


stats_for_3_countries(enter)









