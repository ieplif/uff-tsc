# Sistema bancário

class Agencia(object):
    """Representa contas e suas movimentações numa agência bancária."""
    def __init__(self):
        """Cria uma nova agência sem nenhuma conta cadastrada."""

        self.contas = {}

    def cadastradas(self):
        """Retorna uma lista de todas as contas cadastradas nesta agência
        ordenadas por número."""

        return sorted(self.contas.keys())

    def saldo(self,nConta):
        """Retorna o saldo da conta nConta."""

        return sum(self.contas[nConta]["mov"])

    def limite(self,nConta):
        """Retorna o limite para saque a descoberto da conta nConta."""

        return self.contas[nConta]["limite"]

    def alteraLimite(self,nConta,vLimite):
        """Altera o limite para saque a descoberto da conta nConta para vLimite,
        que deve ser 0 ou um número negativo. Caso a conta já tenha 
        um saldo negativo menor que o valor, a operação não é feita,
        causando uma exceção do tipo ValueError."""

        if self.saldo(nConta)<vLimite: 
            raise ValueError("Conta com saldo negativo inferior ao limite dado")
        self.contas[nConta]["limite"] = vLimite

    def movimenta (self,nConta,valor):
        """Faz um deposito ou saque. nConta é o número da conta e valor
        é quantia a ser depositada (se positiva) ou a ser sacada (se negativa).
        Se a conta não existe, ela é criada, desde que valor > 0.
        Saques só são permitidos se não ultrapassarem o limite de saques
        a descoberto da conta (0, por default). Se a movimentação não
        for permitida, causa uma exceção do tipo ValueError."""
        # @see https://www.digitalocean.com/community/tutorials/understanding-dictionaries-in-python-3
        # @see https://www.programiz.com/python-programming/nested-dictionary

        if nConta not in self.contas:
            if valor>0: 
                # um dicionário de dicionário (chaves devem ser objetos imutáveis)
                # o primeiro possui como chave o número da conta e
                # o segundo possui como chaves strings: o 'limite' e a 
                # movimentação 'mov' (associada uma uma lista de valores)
                self.contas[nConta]={"limite":0,"mov":[valor]}
            else:  
                raise ValueError("Conta nao pode ser criada com mov negativa")
        else:
            if self.saldo(nConta)+valor>self.limite(nConta):
                self.contas[nConta]["mov"].append(valor)
            else: raise ValueError("Conta sem saldo suficiente p saque")

    def extrato(self,nConta):
        """Retorna uma lista de todas as movimentações da conta nConta."""

        return self.contas[nConta]["mov"]

    def __str__(self):
        """Retorna uma string que representa o conteúdo dessa agência."""

        str = ""
        for c in self.cadastradas():
            str += "conta %d: limite = %.2f" % (c,self.limite(c))
            str += ", extrato = %s, saldo = %.2f\n" % \
                   (self.extrato(c),self.saldo(c))
        return str

a = Agencia()
a.movimenta(5,100)
a.movimenta(7,200)
a.movimenta(5,-50)
a.movimenta(2,400)
print(a)
try:
    a.movimenta(7,-300)
except ValueError as v:
    print (v)
try: 
    a.movimenta(8,-10)
except ValueError as v:
    print (v)
a.alteraLimite(7,-400)
a.movimenta(7,-300)
print(a)
