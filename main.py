from datetime import datetime 

# Lista com dados ficticíos para testar o código

lista_principal = [
{
    "id" : 0, "nome" : "Flávio", "manutenção" : "1","cpf" : "123456","tipo_veiculo" : "Moto","detalhe" : "Cor marrom", "valor_orcamento" : "3000", "servico" : "Pintar a lataria","data_entrada" : "23/10/2022","data_saida" : "28/10/2022", "status" : "M"
},
{
    "id" : 1, "nome" : "Juliana", "manutenção" : "2","cpf" : "070707","tipo_veiculo" : "Carro","detalhe" : "Aro 17 cor prata","valor_orcamento" : "3500","servico" : "Colocar novos aros e polir os arranhados","data_entrada" : "12/12/2021","data_saida" : "18/12/2021", "status" : "C"
},
{
    "id" : 2, "nome" : "Augusto", "manutenção" : "3","cpf" : "342919","tipo_veiculo" : "Moto","detalhe" : "Cor vermelha, Hornet","valor_orcamento" : "3500","servico" : "trocar o painel","data_entrada" : "25/06/2003","data_saida" : "30/06/2003", "status" : "M"
},
{
    "id" : 3, "nome" : "Kauã" , "manutenção" : "4","cpf" : "456","tipo_veiculo" : "Moto","detalhe" : "bis branca modelo 2013","valor_orcamento" : "1500","servico" : "pintar lataria","data_entrada" : "28/08/2004","data_saida" : "02/09/2004 ", "status" : "A"
},
{
    "id" : 4, "nome" : "Márcio", "manutenção" : "5","cpf" : "34422","tipo_veiculo" : "Moto","detalhe" : "Cor vermelha, 10.000 km rodados","valor_orcamento" : "","servico" : "","data_entrada" : "07/07/2003","data_saida" : "23/07/2003", "status" : "C"
},
{
    "id" : 5, "nome" : "Cléber", "manutenção" : "6","cpf" : "564","tipo_veiculo" : "Carro","detalhe" : "Cor branca, Peugeot","valor_orcamento" : "1500","servico" : "Trocar os faróis dianteiros","data_entrada" : "13/03/2003","data_saida" : "19/03/2003", "status" : "A"
},
{
    "id" : 6, "nome" : "Josué", "manutenção" : "7","cpf" : "2345","tipo_veiculo" : "Carro","detalhe" : "cor azul, Corsa","valor_orcamento" : "3000", "servico" : "arrumar os faróis traseiros, corrigir suspensão e polir arranhados","data_entrada" : "20/11/2022","data_saida" : "01/12/2022", "status" : "F"
},
{
    "id" : 7, "nome" : "Kauã", "manutenção" : "7","cpf" : "456","tipo_veiculo" : "Carro","detalhe" : "cor laranja, Chevette","valor_orcamento" : "2000", "servico" : "arrumar os vidros elétricos e polir arranhados","data_entrada" : "30/11/2022","data_saida" : "10/12/2022", "status" : "F"
}
]


# Função do menu principal printar as opções a serem escolhidas

def MenuPrincipal ():
   print ()
   print ("Menu Principal\n")
   print ("1 - Cadastrar Manutenção.")
   print ("2 - Alterar Manutenção.")
   print ("3 - Realizar Manutenção.")
   print ("4 – Finalizar Manutenção.")
   print ("5 - Relatórios.") 
   print ("6 – Sair. \n")

   global opcao
   opcao = str (input ("Digite a opção escolhida: "))
   return opcao

   
# Função de cadastramento onde pede todos os dados necessários

def CadastrarManutencao ():
    print ()
    print ("Cadastro de manutenção\n")

    dados = {

        "id" : len (lista_principal) ,

        "nome" : str (input ("Nome da pessoa titular: ")),

        "cpf" : str (input ("Digite o CPF do titular:")),

        "tipo_veiculo" : str (input ("Digite o tipo do veículo (C – Carro, M – Moto, O – Outros: ")),

        "detalhe" : str (input ("Digite um detalhe do carro: ex: Marca, Modelo, Cor: ")),

        "valor_orcamento" : str (input ("Digite o valor do orçamento:")),

        "servico" : str (input ("Digite a descrição do serviço:")),

        "data_entrada" : str (input ("Digite a data de entrada: ex: dia/mês/ano: ")),

        "data_saida" : '',

        "status" : "A"
    }


# If de validação para caso algum campo obrigatório não tenha sido preenchido

    if  dados ["nome"] == '' or dados ["cpf"] == '' or dados ["detalhe"] == '' or dados ["valor_orcamento"] == '' or  dados ["data_entrada"] == '':
        print ()
        print ("Você esqueceu de digitar algum dos campos obrigatorios!\n")
        return CadastrarManutencao ()
    else:
        lista_principal.append(dados)
        print () 
        print ("Cadastro realizado com sucesso!")


# Função de realiação de manutencão, onde o usuario busca manutenções através do CPF
               
def RealizarManutencao (): 
    cpf = str (input ("Digite o seu Cpf: "))
    itens = []
    for i in range (len (lista_principal)):
        if cpf == lista_principal [i] ["cpf"]: 
            itens.append(lista_principal [i])   
    
    if len(itens) == 0: 
        print ()
        print ("Nenhuma manutenção encontrada!")
        return 
    elif len(itens) == 1:
        item = itens[0]
        item ["status"] = "M"
        lista_principal[item["id"]] = item
        print ()
        print ("Status da manutenção", item["id"] ,"alterada com sucesso!")
    else: 
        print () 
        print ("Manutenções Cadastradas ")
        for i in range (len (itens)):
            print (str (itens[i]["nome"]), " - " , str (itens[i]["id"]) , " - " , str(itens[i]["data_entrada"] ))
        id = int (input("Digite o ID da manutenção a ser alterada :"))  
        item = lista_principal[id]
        item ["status"] = "M"
        lista_principal[item["id"]] = item
        print ()
        print ("Status da manutenção", item["id"] ,"alterada com sucesso!\n")
        print ("A manutenção está sendo iniciada!")


# Função para encerrar alguma manutenção existente no sistema
        
def FinalizarManutencao():
    cpf = str (input ("Digite o seu Cpf: "))
    itens = []
    for i in range (len (lista_principal)):
       if cpf == lista_principal [i] ["cpf"]: 
            itens.append(lista_principal [i])
    
    if len(itens) == 0: 
        print ("Nenhuma manutenção encontrada")
        return 
    elif len(itens) == 1:
        item = itens[0]
        item ["data_saida"] = datetime.now()
        item ["status"] = "F"
        lista_principal[item["id"]] = item
        print ()
        print ("Manutenção", item["id"] ,"finalizada com sucesso!")
    else:  
        for i in range (len (itens)):
            print (str (itens[i]["nome"]), " - " , str (itens[i]["id"]) , " - " , str(itens[i]["data_entrada"] ))
        id = int (input("Digite o ID da manutenção a ser finalizada :"))  
        item = lista_principal[id]
        item ["data_saida"] = datetime.now()
        lista_principal[item["id"]] = item
        print ()
        print ("Manutenção", item["id"] ,"finalizada com sucesso!")

                
# Função de alteração de manutenções no sistema

def AlterarManutencao():
    cpf = str (input ("Digite o seu Cpf: "))
    itens = []

    for i in range (len (lista_principal)):
        if cpf == lista_principal[i] ["cpf"]: 
            itens.append(lista_principal [i])

    if len(itens) == 0: 
        print ("Nenhuma manutenção encontrada!")
        return 
    elif len(itens) == 1:
        item = itens[0]
        lista_principal[item["id"]] = item
        print ()

        id = lista_principal[item["id"]]
        

        lista_principal[id]["detalhe"] = str (input ("Digite o detalhe a ser alterado, ex: Marca, modelo, cor:"))
        

        lista_principal[id]["valor_orcamento"] = str (input ("Digite o valor do orçamento a ser alterado:"))
    

        lista_principal[id]["servico"] = str (input ("Digite a nova descrição do serviço:"))
       

        lista_principal[id]["status"] = str (input ("Digite o novo status da manutenção, ex: A – Aguardando para manutenção, M – Em manutenção, C - Cancelado, F - Finalizado: "))
     
        print ()
        
        print ("Manutenção", str (id),"alterada com sucesso!")
    else:  
        for i in range (len (itens)):
            print (str (itens[i]["nome"]), " - " , str (itens[i]["id"]) , " - " , str(itens[i]["data_entrada"] ))

        id = int (input("Digite o ID da manutenção a ser alterado:"))  
        

        lista_principal[id]["detalhe"] = str (input ("Digite o detalhe a ser alterado, ex: Marca, modelo, cor:"))
        

        lista_principal[id]["valor_orcamento"] = str (input ("Digite o valor do orçamento a ser alterado:"))
    

        lista_principal[id]["servico"] = str (input ("Digite a nova descrição do serviço:"))


        lista_principal[id]["status"] = str (input ("Digite o novo status da manutenção, ex: A – Aguardando para manutenção, M – Em manutenção, C - Cancelado, F - Finalizado: "))

        print ()

        print ("Manutenção", str (id) ,"alterada com sucesso!")


# Função para printar todos os relatórios de reservas no sistema

def RelatórioReservas ():
    print ()
    print ("Relatório de Reservas\n")
    print ("1 - Relatório de todas as manutenções.")
    print ("2 - Relatório de todas as manutenções com status A. ")
    print ("3 - Relatório de todas as manutenções com status M.")
    print ("4 - Relatório de todas as manutenções com status C.")
    print ("5 - Relatório de todas as manutenções com status F.")
    print ("6 - Relatório total recebido (somar valor de todas as manutenções finalizadas)")
    print ("7 – Relatório de manutenções por pessoa (Pesquisa por CPF)\n")

    escolha_relatorio = str (input ("Digite a opção a ser escolhida de acordo com o número: "))
    print ()

    relatorios = lista_principal

    if (escolha_relatorio == '1'):
        print ()
        print ("Relatório de todas as manutenções\n")
        
        for item in lista_principal:
            print("Id: " + str(item['id']) + " - " + "Nome: " + str (item['nome']) + " - " + "Serviço: " + 
            str (item['servico'])  + " - " + "CPF: " + (item ['cpf']) + " - " + "Tipo Veículo: " + str (item['tipo_veiculo']) + " - " + "Detalhe: " + str (item['detalhe']) + " - " + "Orçamento: " + str (item['valor_orcamento']) + " - " + "Data entrada: " + str(item['data_entrada']) + " - " + "Data saída: " + str(item['data_saida']) + " - " + "Status: " + str (item['status'])) 
            print ()
        
    elif (escolha_relatorio == '2'):
        print ("Relatório de todas as manutenções com status A: \n")
            
        for item in lista_principal:
            if item ["status"] == "A":
                print("Id: " + str(item['id']) + " - " + "Nome: " + str (item['nome']) + " - " + "Serviço: " + 
                str (item['servico'])  + " - " + "CPF: " + (item ['cpf']) + " - " + "Tipo Veículo: " + str (item['tipo_veiculo']) + " - " + "Detalhe: " + str (item['detalhe']) + " - " + "Orçamento: " + str (item['valor_orcamento']) + " - " + "Data entrada: " + str(item['data_entrada']) + " - " + "Data saída: " + str(item['data_saida']) + " - " + "Status: " + str (item['status'])) 
                print ()
            
    elif (escolha_relatorio == '3'):
        print ("Relatório de todas as manutenções com status M: \n")

        for item in lista_principal:
            if item ["status"] == "M":
                print("Id: " + str(item['id']) + " - " + "Nome: " + str (item['nome']) + " - " + "Serviço: " + 
                str (item['servico'])  + " - " + "CPF: " + (item ['cpf']) + " - " + "Tipo Veículo: " + str (item['tipo_veiculo']) + " - " + "Detalhe: " + str (item['detalhe']) + " - " + "Orçamento: " + str (item['valor_orcamento']) + " - " + "Data entrada: " + str(item['data_entrada']) + " - " + "Data saída: " + str(item['data_saida']) + " - " + "Status: " + str (item['status'])) 
                print ()
            
    elif (escolha_relatorio == '4'):
        print ("Relatório de todas as manutenções com status C: \n")

        for item in lista_principal:
            if item ["status"] == "C":
                print("Id: " + str(item['id']) + " - " + "Nome: " + str (item['nome']) + " - " + "Serviço: " + 
                str (item['servico'])  + " - " + "CPF: " + (item ['cpf']) + " - " + "Tipo Veículo: " + str (item['tipo_veiculo']) + " - " + "Detalhe: " + str (item['detalhe']) + " - " + "Orçamento: " + str (item['valor_orcamento']) + " - " + "Data entrada: " + str(item['data_entrada']) + " - " + "Data saída: " + str(item['data_saida']) + " - " + "Status: " + str (item['status'])) 
                print ()
    
    elif (escolha_relatorio == '5'):
        print ("Relatório de todas as manutenções com status F: \n")

        for item in lista_principal:
            if item ["status"] == "F":
                print("Id: " + str(item['id']) + " - " + "Nome: " + str (item['nome']) + " - " + "Serviço: " + 
                str (item['servico'])  + " - " + "CPF: " + (item ['cpf']) + " - " + "Tipo Veículo: " + str (item['tipo_veiculo']) + " - " + "Detalhe: " + str (item['detalhe']) + " - " + "Orçamento: " + str (item['valor_orcamento']) + " - " + "Data entrada: " + str(item['data_entrada']) + " - " + "Data saída: " + str(item['data_saida']) + " - " + "Status: " + str (item['status'])) 
                print ()

    elif (escolha_relatorio == '6'):
        print ("Relatório do valor total recebido:\n")
        total_recebido = 0

        for item in lista_principal:
            if item["status"] == "F":
                total_recebido += float(item["valor_orcamento"])

        print ('O total recebido foi de R$ ',total_recebido)

    elif (escolha_relatorio == '7'):
        cpf = str (input ("Digite seu Cpf: "))
        print ()

        for item in lista_principal: 
            if cpf == item["cpf"]: 
                print("Id: " + str(item['id']) + " - " + "Nome: " + str (item['nome']) + " - " + "Serviço: " + 
                str (item['servico'])  + " - " + "CPF: " + (item ['cpf']) + " - " + "Tipo Veículo: " + str (item['tipo_veiculo']) + " - " + "Detalhe: " + str (item['detalhe']) + " - " + "Orçamento: " + str (item['valor_orcamento']) + " - " + "Data entrada: " + str(item['data_entrada']) + " - " + "Data saída: " + str(item['data_saida']) + " - " + "Status: " + str (item['status'])) 
                print ()

            
# While para executar cada função de acordo com a opção escolhida do usuário 

while True:
    opcao = MenuPrincipal()

    if (opcao == '1'):
        CadastrarManutencao()
    
    elif (opcao == '2'):
        AlterarManutencao()

    elif (opcao == '3'):
        RealizarManutencao()

    elif (opcao == '4'):
        FinalizarManutencao()
    
    elif (opcao == '5'):
        RelatórioReservas()
         
    elif (opcao == '6'):
        print ()
        print ("Você saiu do sistema!\n")
        break        