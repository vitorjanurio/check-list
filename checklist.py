import sqlite3



class Checklist:
    
    def __init__(self, db_checklist):
        self.checklist = db_checklist
        self.conexao = sqlite3.connect(self.checklist)  
        self.cursor = self.conexao.cursor()
        self.criar_tabelas()

    def criar_tabelas(self):
        
        self.cursor.execute(
            '''
            CREATE TABLE IF NOT EXISTS funcionario (
                idCpf INTEGER PRIMARY KEY,
                nome VARCHAR(100),
                cargo VARCHAR(45)
            );
            '''
        )

       
        self.cursor.execute(
            '''
            CREATE TABLE IF NOT EXISTS avaria (
                idAvaria INTEGER PRIMARY KEY,
                detalheAvaria VARCHAR(45) NOT NULL
            );
            '''
        )

        
        self.cursor.execute(
            '''
            CREATE TABLE IF NOT EXISTS retorno (
                idRetorno INTEGER PRIMARY KEY,
                diaRetorno DATETIME NOT NULL, 
                horaRetorno TIME NOT NULL,
                retorno VARCHAR(45) NOT NULL
            );
            '''
        )

        
        self.cursor.execute(
            '''
            CREATE TABLE IF NOT EXISTS horarios (
                idHorarios INTEGER PRIMARY KEY,
                horarioRetirada TIME NOT NULL,
                horarioChegada TIME NOT NULL,
                diaRetirada DATE,
                idRetorno INTEGER,
                FOREIGN KEY (idRetorno) REFERENCES retorno(idRetorno)
            );
            '''
        )

        
        self.cursor.execute(
            '''
            CREATE TABLE IF NOT EXISTS destino (
                idDestino INTEGER PRIMARY KEY,
                cep VARCHAR(45),
                numero INTEGER,
                complemento TEXT,
                idParada INTEGER,
                FOREIGN KEY (idParada) REFERENCES parada(idParada)
            );
            '''
        )

        
        self.cursor.execute(
            '''
            CREATE TABLE IF NOT EXISTS veiculo (
                idVeiculo INTEGER PRIMARY KEY AUTOINCREMENT,
                placa VARCHAR(45),
                cor VARCHAR(45),
                quilometragemAtual INTEGER,
                idDestino INTEGER,
                idCpf INTEGER,
                idAvaria INTEGER,
                idHorarios INTEGER,
                FOREIGN KEY (idDestino) REFERENCES destino(idDestino),
                FOREIGN KEY (idCpf) REFERENCES funcionario(idCpf),
                FOREIGN KEY (idAvaria) REFERENCES avaria(idAvaria),
                FOREIGN KEY (idHorarios) REFERENCES horarios(idHorarios)
            );
            '''
        )

       
        self.cursor.execute(
            '''
            CREATE TABLE IF NOT EXISTS parada (
                idParada INTEGER PRIMARY KEY,
                horaParada TIME NOT NULL,
                horaSaida TIME NOT NULL,
                cidade VARCHAR(45) NOT NULL
            );
            '''
        )   


        self.conexao.commit()


    def fechar_conexao(self):
        self.conexao.close()     

