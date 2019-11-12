import pymongo
import folium



from pymongo import MongoClient

db = MongoClient('mongodb+srv://admin:admin@cluster0-vuh1j.azure.mongodb.net/test?retryWrites=true&w=majority')
db = db.get_database('BD_EMPRESAS')

collection = db.empresas


cnpj = []
qtd_cnpj = []
latitude = []
longitude = []
qtd_range = []



latitude = db.get_collection('empresas').distinct("latitude")
qtd_range = len(latitude)
longitude = db.get_collection('empresas').distinct("longitude")

mapa = folium.Map(location=[-23.223701,-45.9009074],zoom_start=12)

for i in range(qtd_range):
    folium.Marker([latitude[i], longitude[i]]).add_to(mapa)


mapa.save("mapa.html")