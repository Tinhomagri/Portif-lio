import os #importa a biblioteca para manipulação do S.O.
import mysql.connector #Importa o conector mySQL para o python

def conectarBD(host,user,password,database):
    connection=   mysql.connector.connect(
    host = "localhost", #ip do servidor do banco de dados
    user = "root", #usuário cadastrado no MySQL
    password = "admin", #Senha do usuário cadastrado no MySQL
    database = "pi" #Nome do database utilizado
)
    return connection

def insert_fornecedores(nome,email,cnpj,endereco,categoria,conn):
    connection = conn
    cursor = connection.cursor()
    sql =   'INSERT INTO FORNECEDORES (nome,email,cnpj,endereco,categoria) VALUES(%s,%s,%s,%s,%s)'
    data = (
    nome,
    email,
    cnpj,
    endereco,
    categoria
    )
    cursor.execute(sql,data)
    connection.commit()#edita o banco de dados.

    fornecedor_id = cursor.lastrowid
    cursor.close()
    connection.close()
    print("O seu fornecedor foi cadastrado de ID",fornecedor_id)


def read_fornecedores(conn):
    connection = conn #Recebe a conexão estabelecida com o banco
    cursor = connection.cursor() #Cursor para comunicação com o banco

    sql = "SELECT * FROM fornecedores"
    #Realizando um select para mostrar todas as linhas e colunas da tabela
    cursor.execute(sql) #Executa o comando SQL
    results = cursor.fetchall() #Obtendo todas as linhas geradas pelo select
    cursor.close() #Fecha o cursor
    connection.close() #Fecha a conexão com o banco

    for result in results: #Percorrer a lista com as linhas geradas pelo SELECT
        print(result) #Imprime cada linha gerada pelo SELECT


def update_fornecedores(nome,email,cnpj,endereco,categoria, id, conn):
    connection = conn #Recebe a conexão estabelecida com o banco
    cursor = connection.cursor() #Cursor para comunicação com o banco
    sql = "UPDATE FORNECEDORES SET NOME=%s, EMAIL=%s, CNPJ=%s, ENDERECO=%s , CATEGORIA=%s WHERE ID=%s"
    data = (
         nome,
        email,
        cnpj,
        endereco,
        categoria,
        id
    )
    cursor.execute(sql,data)
    connection.commit()
    recordsAffected = cursor.rowcount
    cursor.close()
    connection.close()
    print(recordsAffected, " registros atualizados do seu fornecedor.")

def delete_fornecedores(id, conn):
    connection = conn #Recebe a conexão estabelecida com o banco
    cursor = connection.cursor() #Cursor para comunicação com o banco
    sql = "DELETE FROM FORNECEDORES WHERE ID = %s"
    data = (id,)
    cursor.execute(sql,data)
    connection.commit()
    recordsAffected = cursor.rowcount
    cursor.close()
    connection.close()
    print(recordsAffected, " registros removidos")

def insert_funcionarios(nome,rg,cargo,conn):
    connection = conn
    cursor = connection.cursor()
    sql =   'INSERT INTO FUNCIONARIOS (nome,rg,cargo) VALUES(%s,%s,%s)'
    data = (
    nome,
    rg,
    cargo
    )
    cursor.execute(sql,data)
    connection.commit()#edita o banco de dados.

    funcionarios_id = cursor.lastrowid
    cursor.close()
    connection.close()
    print("O seu funcionario foi cadastrado de ID",funcionarios_id)


def read_funcionarios(conn):
    connection = conn #Recebe a conexão estabelecida com o banco
    cursor = connection.cursor() #Cursor para comunicação com o banco

    sql = "SELECT * FROM funcionarios"
    #Realizando um select para mostrar todas as linhas e colunas da tabela
    cursor.execute(sql) #Executa o comando SQL
    results = cursor.fetchall() #Obtendo todas as linhas geradas pelo select
    cursor.close() #Fecha o cursor
    connection.close() #Fecha a conexão com o banco

    for result in results: #Percorrer a lista com as linhas geradas pelo SELECT
        print(result) #Imprime cada linha gerada pelo SELECT


def update_funcionarios(nome,rg,cargo, id, conn):
    connection = conn #Recebe a conexão estabelecida com o banco
    cursor = connection.cursor() #Cursor para comunicação com o banco
    sql = "UPDATE FUNCIONARIOS SET NOME=%s, RG=%s, CARGO=%s WHERE ID=%s"
    data = (
        nome,
        rg,
        cargo,
        id
    )
    cursor.execute(sql,data)
    connection.commit()
    recordsAffected = cursor.rowcount
    cursor.close()
    connection.close()
    print(recordsAffected, " registros atualizados dos funcionários.")

def delete_funcionarios(id, conn):
    connection = conn #Recebe a conexão estabelecida com o banco
    cursor = connection.cursor() #Cursor para comunicação com o banco
    sql = "DELETE FROM FUNCIONARIOS WHERE ID = %s"
    data = (id,)
    cursor.execute(sql,data)
    connection.commit()
    recordsAffected = cursor.rowcount
    cursor.close()
    connection.close()
    print(recordsAffected, " registros removidos")


def insert_hardware(tipo,descricao,marca,data_aquisicao,fornecedor,departamento,condicao,conn):
    connection = conn
    cursor = connection.cursor()
    sql =   'INSERT INTO HARDWARE (tipo,descricao,marca,data_aquisicao,fornecedor,departamento,condicao) VALUES(%s,%s,%s,%s,%s,%s,%s)'
    data = (
    tipo,
    descricao,
    marca,
    data_aquisicao,
    fornecedor,
    departamento,
    condicao
    )
    cursor.execute(sql,data)
    connection.commit()#edita o banco de dados.

    hardware_id = cursor.lastrowid
    cursor.close()
    connection.close()
    print("O Hardware foi cadastrado de ID",hardware_id)


def read_hardware(conn):
    connection = conn #Recebe a conexão estabelecida com o banco
    cursor = connection.cursor() #Cursor para comunicação com o banco

    sql = "SELECT * FROM hardware"
    #Realizando um select para mostrar todas as linhas e colunas da tabela
    cursor.execute(sql) #Executa o comando SQL
    results = cursor.fetchall() #Obtendo todas as linhas geradas pelo select
    cursor.close() #Fecha o cursor
    connection.close() #Fecha a conexão com o banco

    for result in results: #Percorrer a lista com as linhas geradas pelo SELECT
        print(result) #Imprime cada linha gerada pelo SELECT


def update_hardware(tipo,descricao,marca,data_aquisicao,fornecedor,departamento,condicao, id, conn):
    connection = conn #Recebe a conexão estabelecida com o banco
    cursor = connection.cursor() #Cursor para comunicação com o banco
    sql = "UPDATE HARDWARE SET TIPO=%s, DESCRICAO=%s, MARCA=%s , DATA_AQUISICAO=%s, FORNECEDOR=%s, DEPARTAMENTO=%s, CONDICAO=%s WHERE ID=%s"
    data = (
        tipo,
        descricao,
        marca,
        data_aquisicao,
        fornecedor,
        departamento,
        condicao,
        id
    )
    cursor.execute(sql,data)
    connection.commit()
    recordsAffected = cursor.rowcount
    cursor.close()
    connection.close()
    print(recordsAffected, " registros atualizados dos software.")

def delete_hardware(id, conn):
    connection = conn #Recebe a conexão estabelecida com o banco
    cursor = connection.cursor() #Cursor para comunicação com o banco
    sql = "DELETE FROM HARDWARE WHERE ID = %s"
    data = (id,)
    cursor.execute(sql,data)
    connection.commit()
    recordsAffected = cursor.rowcount
    cursor.close()
    connection.close()
    print(recordsAffected, " registros removidos")


def insert_software(nome,versao,fabricante,data_aquisicao,condicao,conn):
    connection = conn
    cursor = connection.cursor()
    sql =   'INSERT INTO SOFTWARE (nome,versao,fabricante,data_aquisicao,condicao) VALUES(%s,%s,%s,%s,%s)'
    data = (
    nome,
    versao,
    fabricante,
    data_aquisicao,
    condicao
    )
    cursor.execute(sql,data)
    connection.commit()#edita o banco de dados.

    software_id = cursor.lastrowid
    cursor.close()
    connection.close()
    print("O Software foi cadastrado de ID",software_id)


def read_software(conn):
    connection = conn #Recebe a conexão estabelecida com o banco
    cursor = connection.cursor() #Cursor para comunicação com o banco

    sql = "SELECT * FROM software"
    #Realizando um select para mostrar todas as linhas e colunas da tabela
    cursor.execute(sql) #Executa o comando SQL
    results = cursor.fetchall() #Obtendo todas as linhas geradas pelo select
    cursor.close() #Fecha o cursor
    connection.close() #Fecha a conexão com o banco

    for result in results: #Percorrer a lista com as linhas geradas pelo SELECT
        print(result) #Imprime cada linha gerada pelo SELECT


def update_software(nome,versao,fabricante,data_aquisicao,condicao, id, conn):
    connection = conn #Recebe a conexão estabelecida com o banco
    cursor = connection.cursor() #Cursor para comunicação com o banco
    sql = "UPDATE SOFTWARE SET NOME=%s, VERSAO=%s, FABRICANTE=%s , DATA_AQUISICAO=%s, CONDICAO=%s WHERE ID=%s"
    data = (
        nome,
        versao,
        fabricante,
        data_aquisicao,
        condicao,
        id
    )
    cursor.execute(sql,data)
    connection.commit()
    recordsAffected = cursor.rowcount
    cursor.close()
    connection.close()
    print(recordsAffected, " registros atualizados do Software.")

def delete_software(id, conn):
    connection = conn #Recebe a conexão estabelecida com o banco
    cursor = connection.cursor() #Cursor para comunicação com o banco
    sql = "DELETE FROM SOFTWARE WHERE ID = %s"
    data = (id,)
    cursor.execute(sql,data)
    connection.commit()
    recordsAffected = cursor.rowcount
    cursor.close()
    connection.close()
    print(recordsAffected, " registros removidos")



while(True):
    print(":::::: GERENCIADOR EMPRESA INFRATECH ::::::")
    print("1 - Fornecedores")
    print("2 - Funcionários")
    print("3 - Hardwares")
    print("4 - Software")
    print("5 - Sair")

    opcao_principal = input("Digite a opção desejada:")

    if(opcao_principal == "1"):
        print("\n\n:::::: VOCÊ ENTROU NA ÁREA DE FORNECEDORES ::::::")
        print("1 - Cadastrar fornecedor:")
        print("2 - Exibir fornecedores cadastrados:")
        print("3 - Atualizar dados do fornecedor:")
        print("4 - Deletar cadastro do fornecedor:")
        print("5 - Sair")

        opcao_fornecedores = input("Digite a opção desejada:")

        if(opcao_fornecedores == "1"):
            nome = input("Digite o nome do fornecedor:")
            email = input("Digite o email:")
            cnpj = input("Digite o CNPJ:")
            endereco = input("Digite o endereço:")
            categoria = input("Digite a categoria:")

            connection = conectarBD("localhost","root", "admin", "pi")
            insert_fornecedores(nome,email,cnpj,endereco,categoria,connection)
        elif(opcao_fornecedores == "2"):
            connection = conectarBD("localhost","root", "admin", "pi")
            read_fornecedores(connection)
        elif(opcao_fornecedores == "3"):
            connection = conectarBD("localhost","root", "admin", "pi")
            id = input("Informe o ID do fornecedor:")
            nome = input("Informe o nome atualizado:")
            email = input("Informe o novo email:")
            cnpj = input("Informe o CNPJ:")
            endereco = input("Informe o novo endereço:")
            categoria = input("Digite qual é a categoria:")

            update_fornecedores(nome,email,cnpj,endereco,categoria, id, connection)
        elif (opcao_fornecedores == "4"):
                connection = conectarBD("localhost","root", "admin", "pi")
                id = input("Informe o ID do fornecedor:")
                delete_fornecedores(id, connection)
        else :
            print("Sair")
        
    elif(opcao_principal == "2"):
        print(":::::: VOCÊ ENTROU NA ÁREA DOS FUNCIONÁRIOS ::::::")
        print("1 - Cadastrar funcionários")
        print("2 - Exibir funcionários cadastrados")
        print("3 - Atualizar dados dos funcionários")
        print("4 - Deletar cadastro de funcionários")
        print("5 - Sair")

        opcao_funcionarios = input("Digite a opção desejada:")

        if(opcao_funcionarios == "1"):
            nome = input("Digite o nome do funcionário:")
            rg = input("Digite o RG do funcionário:")
            cargo= input("Digite o cargo:")
        
            connection = conectarBD("localhost","root", "admin", "pi")
            insert_funcionarios(nome,rg,cargo,connection)
        elif(opcao_funcionarios == "2"):
            connection = conectarBD("localhost","root", "admin", "pi")
            read_funcionarios(connection)
        elif(opcao_funcionarios == "3"):
            connection = conectarBD("localhost","root", "admin", "pi")
            id = input("Informe o ID do funcionário:")
            nome = input("Informe o nome do funcionário:")
            rg = input("Informe o novo rg do funcionário:")
            cargo = input("Informe o cargo do funcionário:")
    
            update_funcionarios(nome,rg,cargo, id, connection)
        elif (opcao_funcionarios == "4"):
            connection = conectarBD("localhost","root", "admin", "pi")
            id = input("Informe o ID do funcionário:")
            delete_funcionarios(id, connection)
        elif (opcao_funcionarios == "5"):
            print("Sair")

    elif(opcao_principal == "3"):
            print(":::::: VOCÊ ENTROU NA ÁREA DOS HARDWARES ::::::")
            print("1 - Cadastrar hardware")
            print("2 - Exibir hardware cadastrados")
            print("3 - Atualizar dados dos hardwares")
            print("4 - Deletar cadastro dos hardwares")
            print("5 - Sair")

            opcao_hardware = input("Digite a opção desejada:")

            if(opcao_hardware == "1"):
                tipo = input("Digite o tipo de hardware:")
                descricao = input("Digite a descrição do hardware:")
                marca = input("Digite a marca do hardware:")
                data_aquisicao = input("Digite a data de aquisição:")
                fornecedor = input("Digite o fornecedor do hardware:")
                departamento = input("Digite o nome do departamento:")
                condicao = input("Digite a condição do produto:")
        
                connection = conectarBD("localhost","root", "admin", "pi")
                insert_hardware(tipo,descricao,marca,data_aquisicao,fornecedor,departamento,condicao,connection)
            elif(opcao_hardware == "2"):
                connection = conectarBD("localhost","root", "admin", "pi")
                read_hardware(connection)
            elif(opcao_hardware == "3"):
                connection = conectarBD("localhost","root", "admin", "pi")
                id = input("Informe o ID do hardware:")
                tipo = input("Digite o tipo de hardware:")
                descricao = input("Digite a descrição do hardware:")
                marca = input("Digite a marca do hardware:")
                fornecedor = input("Digite o fornecedor do hardware:")
                data_aquisicao = input("Digite a data da aquisição do hardware:")
                departamento = input("Digite o departamento:")
                condicao = input("Digite a condição do hardware:")
                update_hardware(tipo,descricao,marca,data_aquisicao,fornecedor,departamento,condicao, id, connection)
            elif (opcao_hardware == "4"):
                connection = conectarBD("localhost","root", "admin", "pi")
                id = input("Informe o ID do hardware:")
                delete_hardware(id, connection)
            elif (opcao_hardware == "5"):
                print("Sair")

    elif(opcao_principal == "4"):
            print(":::::: VOCÊ ENTROU NA ÁREA DOS SOFTWARE ::::::")
            print("1 - Cadastrar software")
            print("2 - Exibir software cadastrados")
            print("3 - Atualizar dados dos softwares")
            print("4 - Deletar cadastro dos softwares")
            print("5 - Sair")

            opcao_software = input("Digite a opção desejada:")

            if(opcao_software == "1"):
                nome = input("Digite o tipo de software:")
                versao = input("Digite a descrição do software:")
                fabricante = input("Digite a marca do software:")
                data_aquisicao = input("Digite a data de aquisição:")
                condicao = input("Digite a condição do produto:")
        
                connection = conectarBD("localhost","root", "admin", "pi")
                insert_software(nome,versao,fabricante ,data_aquisicao,condicao,connection)
            elif(opcao_software == "2"):
                connection = conectarBD("localhost","root", "admin", "pi")
                read_software(connection)
            elif(opcao_software == "3"):
                connection = conectarBD("localhost","root", "admin", "pi")
                id = input("Informe o ID do software:")
                nome = input("Digite o tipo de softare:")
                versao = input("Digite a descrição do software:")
                fabricante = input("Digite o fabricante do produto:")
                data_aquisicao = input("Digite a data de aquisição do Software:")
                condicao = input("Digite a condição do software:")
    
                update_software(nome,versao,fabricante ,data_aquisicao,condicao, id, connection)
            elif (opcao_software == "4"):
                connection = conectarBD("localhost","root", "admin", "pi")
                id = input("Informe o ID do software:")
                delete_software(id, connection)
            elif (opcao_software == "5"):
                break
