class User:
    def __init__(self, name, cpf, conta):
        self.name = name
        self.cpf = cpf
        self.conta = conta

    def saque(self):
        valor = int(input("Informe o valor que deseja sacar: "))
        if self.conta >= valor:
            self.conta -= valor
            print("\nSaque realizado com sucesso!\n")
        else:
            print("\nSaldo insuficiente!\n")

    def deposito(self):
        valor = int(input("Informe o valor que deseja depositar: "))
        self.conta += valor
        print("\nValor depositado com sucesso!\n")

    def extrato(self):
        print(f"""
    =========== EXTRATO ===========
        Nome:   {self.name:>15}
        CPF:    {self.cpf:>15}
        Saldo:   R$ {self.conta:>5.2f}
    ==============================
    """)

def main():
    usuario_exemplo = User("Exemplo", "12345678910", 2700)
    while True:
        escolha = int(input("""
__________Banco Python__________

Escolha uma das opções a seguir:
                                
        1 - Depósito
        2 - Saque
        3 - Extrato
        0 - Sair\n\n"""))

        if escolha == 1:
            usuario_exemplo.deposito()
        
        elif escolha == 2:
            usuario_exemplo.saque()

        elif escolha == 3:
            usuario_exemplo.extrato()

        elif escolha == 0:
            break
        else:
            print("\nOpção inválida! Tente novamente.\n")

main()