import pymongo
from bson import ObjectId
import pandas as pd








class BancoDeDados:

    def conectar_db(self):
        try:
            self.conn = pymongo.MongoClient("mongodb://localhost:27017/")
        except:
            print("Não foi possivel conectar ao banco de dados!")
            return False

        self.db = self.conn['meudb']

        self.usuarios = self.db['usuarios']

        print("Conectado ao banco!")
        return True

    def executar_select(self, tipo_busca: int, campo):
        if tipo_busca == 1:
            return self.usuarios.find({})
        elif tipo_busca == 2:
            return self.usuarios.find({"_id": ObjectId(campo)})
        elif tipo_busca == 3:
            return self.usuarios.find({"nome": campo})
        elif tipo_busca == 4:
            return self.usuarios.find({"cpf": campo})
        elif tipo_busca == 5:
            return self.usuarios.find({"idade": campo})
        elif tipo_busca == 6:
            return self.usuarios.find({"altura": campo})


    def executar_insert(self, dados: dict):
        self.usuarios.insert_one(dados)
        print("inserido com sucesso! " + str(dados))
        return True

    def executar_update(self, id: ObjectId, dados: dict):
        self.usuarios.update_one({"_id": id}, {"$set": dados})
        print("atualizado com sucesso")
        return True

    def executar_delete(self, id: ObjectId):
        self.usuarios.delete_one({"_id": id})
        print("deletado com sucesso")
        return True