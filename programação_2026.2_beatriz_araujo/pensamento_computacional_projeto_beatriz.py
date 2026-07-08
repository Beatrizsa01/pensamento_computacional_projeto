from tkinter import *
from tkinter import messagebox

'''
Isso é um bloco de comentário.

>PO (Como dono do negócio): Levantar as necessidades da padaria, definir prioridades e acompanhar o desenvolvimento.

>QA (Como cliente): Testar o sistema, verificar se tudo está funcionando corretamente e registrar possíveis erros.

>TECH (Como programador): Definir a estrutura técnica do sistema, orientar a equipe e revisar o código.

>DEV (Como programador): Desenvolver o sistema da padaria (cadastro de produtos, vendas, estoque, pedidos, etc).

>UX (Como designer de experiência do usuário): Criar telas simples e práticas para a funcionalidade dos clientes.

>IA (Como analista de dados): Analisar os dados coletados, identificar padrões e fornecer insights para melhorar o sistema e a experiência do usuário.
'''

p1_nome = 'Pão Francês'
p1_descricao = 'Pão Francês feito na hora!'
p1_validade = '04-07-2026'
p1_estoque = 50
p1_preco = 1.50

p2_nome = 'Croissant'
p2_descricao = 'Croissant de queijo'
p2_validade = '04-07-2026'
p2_estoque = 30
p2_preco = 8.00

p3_nome = 'Sonho'
p3_descricao = 'Sonho pequeno, Recheado - creme'
p3_validade = '04-07-2026'
p3_estoque = 20
p3_preco = 6.00

p4_nome = 'Café'
p4_descricao = 'Café expresso. 300ml. Feito na Hora!'
p4_validade = '08-07-2026'
p4_estoque = 40
p4_preco = 10.00

p5_nome = 'Suco de laranja'
p5_descricao = 'Suco natural. 300ml.' 
p5_validade = '08-07-2026'
p5_estoque = 40
p5_preco = 10.00

janela = Tk()
janela.title("Sistema de Vendas - PADARIA")
janela.geometry("800x650")
janela.resizable(False, False)

Label(
    janela,
    text="Bem-vindo ao projeto de desenvolvimento\n de um sistema de vendas para padaria!",
    font=("Arial", 16, "bold")
).pack(pady=10)

Label(janela, text="Digite a opção desejada:", font=("Arial", 12)).pack()

entrada = Entry(janela, width=10, font=("Arial", 12))
entrada.pack(pady=5)

resultado = Label(janela, text="", font=("Arial", 12), justify=LEFT)
resultado.pack(pady=10)


def executar():

    global p1_home, p2_nome, p3_nome

    opcao = entrada.get()

    if opcao == '1':

        resultado.config(text="Opção 1 - Cadastrando cliente...")

        tela = Toplevel(janela)
        tela.title("Cadastro do Cliente")
        tela.geometry("450x500")

        Label(tela, text="Nome do cliente").pack()
        nome_cliente = Entry(tela)
        nome_cliente.pack()

        Label(tela, text="Nome do produto").pack()
        nome_produto = Entry(tela)
        nome_produto.pack()

        Label(tela, text="Descrição do produto").pack()
        descricao_produto = Entry(tela)
        descricao_produto.pack()

        Label(tela, text="Lista do produto").pack()
        listar_produto = Entry(tela)
        listar_produto.pack()

        Label(tela, text="Realizar venda").pack()
        realizar_venda = Entry(tela)
        realizar_venda.pack()

        Label(tela, text="Cancelar produto").pack()
        cancelar_produto = Entry(tela)
        cancelar_produto.pack()

        Label(tela, text="Consultar estoque").pack()
        consultar_estoque = Entry(tela)
        consultar_estoque.pack()

        Label(tela, text="Cancelar produto").pack()
        cancelar_produto2 = Entry(tela)
        cancelar_produto2.pack()

        Label(tela, text="Histórico de vendas").pack()
        historico_vendas = Entry(tela)
        historico_vendas.pack()

        Label(tela, text="Gerar relatório").pack()
        gerar_relatorio = Entry(tela)
        gerar_relatorio.pack()

    elif opcao == '2':

        resultado.config(text="Opção 2 - Cadastrando produto...")

    elif opcao == '3':

        resultado.config(text="Opção 3 - Listando produtos...")

        if p1_home == " " and p2_nome == " " and p3_nome == " ":
            messagebox.showinfo(
                "Produtos",
                "Nenhum produto cadastrado no sistema ainda."
            )

    elif opcao == '4':

        resultado.config(text="Opção 4 - Realizando venda...")

    elif opcao == '5':

        resultado.config(text="Opção 5 - Cancelando produtos...")

    elif opcao == '6':

        resultado.config(text="Opção 6 - Consultando estoque...")

    elif opcao == '8':

        resultado.config(text="Opção 8 - Histórico de vendas...")

    elif opcao == '9':

        resultado.config(text="Opção 9 - Gerando relatório de vendas...")

    elif opcao == '0':

        janela.destroy()

    else:

        messagebox.showerror("Erro", "Opção inválida")


Button(
    janela,
    text="Executar",
    font=("Arial", 12),
    command=executar
).pack(pady=10)

Label(
    janela,
    text="""
1 - Cadastro do cliente
2 - Cadastro de produtos
3 - Listar produtos
4 - Realizar venda
5 - Cancelar produto
6 - Consultar estoque
7 - Cancelar produto
8 - Histórico de vendas
9 - Gerar relatório de venda
0 - Sair
""",
    justify=LEFT,
    font=("Arial", 11)
).pack(pady=20)

janela.mainloop()