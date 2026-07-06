'''
Isso é um bloco de comentário. 

>PO (Como dono do negócio): Levantar as necessidades da padaria, definir prioridades e acompanhar o desenvolvimento.

>QA (Como cliente):Testar o sistema, verificar se tudo está funcionando corretamente e registrar possiveis erros.

>TECH (Como programador): Definir a estrutura técnica do sistema, orientar a equipe e revisar o código.

>DEV (como programador): Desenvolver o sistema da padaria (cadastro de produtos, vendas, estoque, pedidos, etc).

>UX (Como designer de experiência do usuário): Criar telas simples e práticas para a funcionalidade dos clientes.

>IA (Como analista de dados):  Analisar os dados coletados, identificar padrões e fornecer insights para melhorar o sistema e a experiencia do usúario.


'''

p1_nome = 'Pão Francês'
p1_estoque = 170
p1_preco = 0.90
p1_validade = '2 dias'
p1_descricao = 'Clássico Pão Francês feito com ingredientes selecionados, feito e assado na hora.'

p2_nome = 'Croissant'
p2_estoque =70
p2_preco = 7.00
p2_validade = '2 dias'
p2_descricao = 'Massa folhada, leve e amanteigada, feita diariamente.'


p3_nome = 'Cappuccino'
p3_estoque = 150
p3_preco = 8.00
p3_validade = 'Consumo imediato.'
p3_descricao = 'Cappuccino cremoso feito com café selecionado.'


# Isso é um comentário de linha. Finalmente quebramos a maldição 
# print('Olá, mundo!')
# print('\n---------------------\n')

while True:

    print('-' * 48 + '\n')
    print('Bem-vindo ao projeto de desenvolvimento de um sistema de vendas para açaiteria!\n')
    print('1 - Cadastro do cliente...')
    print('2 - Cadastro de produtos...')
    print('3 - Listar produtos...')
    print('4 - Realizar venda...')
    print('5 - Cancelar produto...')
    print('6 - Consultar estoque...')
    print('7 - Cancelar produto...')
    print('8 - Histórico de vendas...')
    print('9 - Gerar relatório de venda...')
    print('0 - Sair')

    opcao = input('Digite a opção desejada:')
    if opcao == '1':
        print('Opção 1 - Cadastrando cliente...\n')

        if p1_nome == "":
            p1_nome = input('Digite o nome do produto: ')
            p1_estoque = int(input('Digite a quantidade em estoque: '))
            p1_preco = float(input('Digite o preço do produto: '))
            p1_validade = input('Digite a validade do produto: ')    
            p1_descricao = input('Digite a descrição do produto: ')
            print(f'\n🎉 Produto "{p1_nome}" cadastrado na vaga 1!') 
                   
        elif p2_nome == "":
                p2_nome = input('Digite o nome do produto: ')
                p2_estoque = int(input('Digite a quantidade em estoque: '))
                p2_preco = float(input('Digite o preço do produto: '))
                p2_validade = input('Digite a validade do produto: ')    
                p2_descricao = input('Digite a descrição do produto: ')
                print(f'\n🎉 Produto "{p2_nome}" cadastrado na vaga 2!')    

        elif p3_nome == "":
            p3_nome = input('Digite o nome do produto: ')
            p3_estoque = int(input('Digite a quantidade em estoque: '))
            p3_preco = float(input('Digite o preço do produto: '))
            p3_validade = input('Digite a validade do produto: ')    
            p3_descricao = input('Digite a descrição do produto: ')
            print(f'\n🎉 Produto "{p3_nome}" cadastrado na vaga 3!')  


        elif opcao == '2':  
            print('Opção 2 - Cadastrando produto')

        
        elif opcao == '3':
            print('Opção 3 - Listando produtos')

            if p1_home == " " and p2_nome == " " and p3_nome == " "
            print('Nenhum produto cadastrado no sistema ainda.')


        elif opcao == '4':
            print('Opção 4 -Realizando venda')

        elif opcao == '5':
            print('Opção 5 - Cancelando produtos')

        elif opcao == '6':
            print('Opção 6 - Consultando estoque')

        elif opcao == '8':
            print('Opção 8 - Histórico de vendas')

        elif opcao == '9':
            print('Opção 9 - Gerando relatório de vendas')

        elif opcao == '0':
         print('Opção 0 - Sair')
        
    else:
            print('❌ Opção inválida!')
s