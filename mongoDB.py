import pymongo
from bson import ObjectId
import pandas as pd

conn = pymongo.MongoClient("mongodb://localhost:27017/")

db = conn['meudb']

usuarios = db['usuarios']

# usuarios_list = usuarios.find({})
#
# for pessoa in usuarios_list:
#     print(pessoa)
#     print(pessoa['nome'] + ' ' + str(pessoa['idade']) + ' ' + str(pessoa['cor_favorita']))

# print(pd.DataFrame(usuarios.find({})))
#
usuarios.update_one({"_id": ObjectId("607ec554ea30d725c4c58132")}, {"$set": {"nome": "Orlando", "idade": 25, "cor_favorita": "Azul Serenity"}})
#
# usuarios.insert_one({"nome": "Francielle", "idade": 26, "cor_favorita": "Laranja"})
#
# usuarios.delete_one({"_id": ObjectId("607edbdd56b382c8fc095cb8")})

usuarios.insert_one({'nome': 'Orlando', 'cpf': '09423784909', 'idade': 25, 'altura': 1.8})

df = pd.DataFrame(usuarios.find({}, {"_id": 0}))

print(df)

# usuarios_list = usuarios.find({})
#
# for pessoa in usuarios_list:
#     print(
#             pessoa['nome']
#             + ' ' + str(pessoa['idade'])
#             + ' ' + str(pessoa['cor_favorita'])
#             + ' ' + str(pessoa['cpf'])
#             + ' ' + str(pessoa['adress']['pais'])
#             + ' ' + str(pessoa['adress']['estado'])
#             + ' ' + str(pessoa['adress']['uf-estado'])
#             + ' ' + str(pessoa['adress']['cidade'])
#             + ' ' + str(pessoa['adress']['bairro'])
#             + ' ' + str(pessoa['adress']['rua'])
#             + ' ' + str(pessoa['adress']['complemento'])
#           )
