# filename = open("kelias_iki_failo.txt")
# w - irasyti, r - skaityti

# with open("text.txt", "w") as f:
#     content = f.write("Hello world")

# with open("text.txt", "r") as f:
#     content = f.read()
#     print(content)

# filename = open("text.txt", "r")
# filename.read()
# print(filename)
#
# with open("text.txt", "a") as f:
#     content = f.write("Dar viena teksto eilute")
#     print(content)

#serverio status kodai:
# 200 OK
# 301-302 - File found / redirect http https:
# 403 Forbidden
# 404 File not found
# 500 Server error

# import requests
# from bs4 import BeautifulSoup
# import psycopg2
# # #
# # # url = "https://varle.lt"
# # #
# # response = requests.get(url)
# # print(response.status_code) #content jei irasyti vietoj status_code - rodo visa varles koda
#
# flats_data = []
# def create_and_insert_flats():
#     connection = psycopg2.connect(
#         host="localhost",
#         port=5432,
#         database="aruodas",
#         user="postgres",
#         password="Apelsinas2319278"
#     )
#
#     cursor = connection.cursor()
#
#     create_table_query = """
#         CREATE TABLE IF NOT EXISTS aruodas_top (
#             id SERIAL primary key,
#             flat_title VARCHAR(300),
#             flat_price DECIMAL(10,2)
#         )
#     """
#     cursor.execute(create_table_query)
#     print("Table created Successfully!")
#
#     url = "https://aruodas.lt"
#     response = requests.get(url)
#     soup = BeautifulSoup(response.content, "html.parser")
# #
#     content_block = soup.select('div.top-three-adverts__wrapper div')
# #     # text.strip() - prirasytas buvo, bet su juo toliau neveike, tai istryniau)
# #     # print(content_block)
# #
#     for content in content_block:
#         try:
#             flat_title = content.find("div", class_="top-three-adverts__advert__address").text.strip()
#             flat_price = content.find("span", class_="top-three-adverts__advert__price__price").text.strip()\
#                 .replace("€", "").replace(" ", "").split(sep="-")[0]
#
#             # print(flat_title, flat_price)
#             # flats_data.append((flat_title, flat_price))
#             insert_query = "INSERT INTO aruodas_top (flat_title, flat_price) VALUES (%s, %s)"
#             cursor.execute(insert_query, (flat_title, flat_price))
#         except AttributeError:
#             continue
#     print("Flats inserted successfully!")
#
#
#     connection.commit()

# create_and_insert_flats()



    # KITAS BUDAS rasyti po for
    #     if flat_title and flat_price:
    #         flats_data.append((flat_title, flat_price))
    #         continue
    #     else:
    #         print(flats_data)

    # df = pd.DataFrame(flats_data,columns=['Title','Price'])
    # print(df)

###IDEDAME NAUJUS DUOMENIS

import requests
from bs4 import BeautifulSoup
import psycopg2

# flats_data = []
# def create_and_insert_flats():
#     connection = psycopg2.connect(
#         host="localhost",
#         port=5432,
#         database="aruodas",
#         user="postgres",
#         password="Apelsinas2319278"
#     )
#
#     cursor = connection.cursor()
#
#     create_table_query = """
#         CREATE TABLE IF NOT EXISTS aruodas_uzsienis (
#             id SERIAL primary key,
#             flat_title VARCHAR(300),
#             flat_price DECIMAL(10,2)
#         )
#         """
#     cursor.execute(create_table_query)
#     print("Table created Successfully!")
#
#     url = "https://www.aruodas.lt/uzsienio-objektai/"
#     response = requests.get(url)
#     soup = BeautifulSoup(response.content, "html.parser")
#     content_block = soup.select('div.project-list-content div') ###project-list-item reikejo rinktis
#
#     for content in content_block:
#         try:
#             flat_title = content.find("h2", class_="project-title-full project-title").text.strip()
#             flat_price = content.find("h3", class_="project-title-full project-min-values").text.strip()\
#                 .split(sep='Kaina:')[1].replace(" ", "").replace("€", "")
#             cursor.execute("select 1 from aruodas_uzsienis where flat_title=%s and flat_price = %s",(flat_title, float(flat_price)))
#             exists = cursor.fetchone()
#             if not exists:
#                 cursor.execute("INSERT INTO aruodas_uzsienis (flat_title, flat_price) VALUES (%s, %s)",(flat_title, float(flat_price)))
#
#             # print(flat_title, flat_price)
#             # flats_data.append((flat_title, flat_price))
#
#         except AttributeError:
#             continue
#     print("Flats inserted successfully!")
#
#     connection.commit()
#
# create_and_insert_flats()


