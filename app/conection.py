class Database:
    def __init__(self):
        self.host = 'localhost'
        self.dbname = 'Nome do banco!'
        self.user = 'admin/root'
        self.password = ''



class Conection:
    def __init__(self):
        try:
            self.conexao = Database()#Receberá instância do banco e suas informações

            print(f'Conexao feita com sucesso!{self.conexao}')
        
        except:
            print('A conexão não teve sucesso!')