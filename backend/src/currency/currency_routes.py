import requests
from bs4 import BeautifulSoup
from flask import Blueprint

currency_routes = Blueprint("currency_routes", __name__)


@currency_routes.route("/currency", methods=["GET"])
def currency_table():
    URL = "https://m.centkantor.pl/"
    page = requests.get(URL)
    URL2 = "http://www.kantorpolonez.pl/"
    page2 = requests.get(URL2)
    URL3 = "https://kantorplex.pl/"
    page3 = requests.get(URL3)

    list_kantorplex_buy = []
    list_kantorplex_sell = []
    list_kantorplex_total = []
    list_kantorplex_result = []

    list_centkantor_names = []
    list_centkantor_buy = []
    list_centkantor_sell = []
    list_centkantor_total = []

    list_kantorpolonez_names = ["USD", "EUR"]
    list_kantorpolonez_buy = []
    list_kantorpolonez_sell = []
    list_kantorpolonez_total = []

    soup = BeautifulSoup(page.content, "html.parser")
    soup2 = BeautifulSoup(page2.content, "html.parser")
    soup3 = BeautifulSoup(page3.content, "html.parser")

    results = soup.find(id="ex_table")
    results2 = soup2.find_all("table")
    results3 = soup3.find_all("table")
    currencies_names = soup.find_all("td", class_="c_symbol")
    currencies_buy = soup.find_all("td", class_="c_buy")
    currencies_sell = soup.find_all("td", class_="c_sell")
    currencies_buy2 = soup2.find_all("td", id="K")
    currencies_sell2 = soup2.find_all("td", id="S")
    currencies3 = soup3.find_all("td", class_="kurs")
    # print(results)

    for value3 in currencies3:
        val = value3
        list_kantorplex_total.append(val.text)

    for value2 in currencies_sell2:
        sell_rate = value2
        comprehended = sell_rate.text.replace("Sprzedaż:", "")
        list_kantorpolonez_sell.append(comprehended)

    for value2 in currencies_buy2:
        buy_rate = value2
        comprehended = buy_rate.text.replace("Kupno:", "")
        list_kantorpolonez_buy.append(comprehended)

    for value1 in currencies_names:
        title_curr = value1
        # buy_rate = value1.find(class_="c_buy")
        # sell_rate = value1.find(class_="c_sell")
        list_centkantor_names.append(title_curr.text)
        # print(title_curr)
        # print(buy_rate)
        # print(sell_rate)
        # print()
    for value1 in currencies_buy:
        buy_rate = value1
        list_centkantor_buy.append(buy_rate.text)
    for value1 in currencies_sell:
        sell_rate = value1
        list_centkantor_sell.append(sell_rate.text)

    list_centkantor_total.append(list_centkantor_names[0])
    list_centkantor_total.append(list_centkantor_buy[0])
    list_centkantor_total.append(list_centkantor_sell[0])
    list_centkantor_total.append(list_centkantor_names[2])
    list_centkantor_total.append(list_centkantor_buy[2])
    list_centkantor_total.append(list_centkantor_sell[2])

    list_kantorpolonez_total.append(list_kantorpolonez_names[1])
    list_kantorpolonez_total.append(list_kantorpolonez_buy[1])
    list_kantorpolonez_total.append(list_kantorpolonez_sell[1])
    list_kantorpolonez_total.append(list_kantorpolonez_names[0])
    list_kantorpolonez_total.append(list_kantorpolonez_buy[0])
    list_kantorpolonez_total.append(list_kantorpolonez_sell[0])

    list_kantorplex_result.append(list_kantorplex_total[0])
    list_kantorplex_result.append(list_kantorplex_total[1])
    list_kantorplex_result.append(list_kantorplex_total[2])
    list_kantorplex_result.append(list_kantorplex_total[3])
    list_kantorplex_result.append(list_kantorplex_total[4])
    list_kantorplex_result.append(list_kantorplex_total[5])

    dict_total = {
        "centkantor": list_centkantor_total,
        "kantorpolonez": list_kantorpolonez_total,
        "kantorplex": list_kantorplex_result,
    }
    # print (list_centkantor_names)
    # print (list_centkantor_buy)
    # print (list_centkantor_sell)
    print(list_centkantor_total)
    # print (results2)
    # print (list_kantorpolonez_buy)
    # print(list_kantorpolonez_sell)
    print(list_kantorpolonez_total)
    # print (list_kantorplex_total)
    print(list_kantorplex_result)
    # jsontest = json.dumps(list_total)
    # print (jsontest)
    # print (type(jsontest))
    # print (jsontest[0])

    return dict_total
    # print(results.prettify())
