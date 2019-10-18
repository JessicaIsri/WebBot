# ```
# pip install pymongo
# ```
from pymongo import MongoClient

bd = MongoClient("mongodb+srv://admin:<password>@cluster0-vuh1j.azure.mongodb.net/test?retryWrites=true&w=majority")
db = db.get_database('BD_EMPRESAS')


collection = db.empresas
collection.count_documents({})

new_empresa = {
    'cnpj': '00000000000191',
    'cep': 12215100
}
#insere um documento no banco
collection.insert_one(new_empresa)

new_empresas = [
    {
        'cnpj': '00000000000191',
        'cep': 12215100
    },
    {
        'cnpj': '00000000000191',
        'cep': 12215100
    }
]
#insere VÁRIOS documentos no banco
collection.insert_many(new_empresas)


#encontra os documentos
list(collection.find())

#filtra o documento
collection.find_one({'roll_no': 123})

#update
empresa_updates = {
    'cnpj': '00000000000191'
}

collection.update_one({'roll_no': 123}, {'$set': student_updates})

#delete
collection.delete_one({'roll_no': 123})