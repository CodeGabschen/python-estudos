class ContaBanco:
    def __init__(self,nome,dinheiro):
        self.nome = nome
        self._saldo = dinheiro
    def depositar(self,valor):
        if valor > 0:
            self._saldo += valor
        else:
            print('A operação foi cancelada,pois o valor negativo não é aceito.')
    def sacar(self,valor):
        if valor <= self._saldo :
            self._saldo = self._saldo - valor
        else:
            print('Não é possível sacar um valor maior do que o disponível na conta.')
    def ver_saldo(self):
        return self._saldo
    def __str__(self):
        return f"Conta de {self.nome} | Saldo: R$ {self._saldo}"

class ContaPoupanca(ContaBanco):
    def __init__(self, nome, dinheiro):
        super().__init__(nome, dinheiro)
        self.rendimento_total = 0
    def render_juros(self,taxa_percentual):
        valor_rendido = (self._saldo * taxa_percentual) / 100
        self._saldo += valor_rendido
        self.rendimento_total = self.rendimento_total + valor_rendido
    def __str__(self):
        return f"Conta de {self.nome} | Saldo: R$ {self._saldo} | Rendimento: {self.rendimento_total} "

class ContaEmpresarial(ContaBanco):
    def __init__(self, nome, dinheiro, empresa):
        super().__init__(nome, dinheiro)
        self.empresa = empresa
    def __str__(self):
        return f"Conta de {self.nome} | Saldo: R$ {self._saldo} | Empresa: {self.empresa} "

      
usuario1 = ContaBanco("usuario1",100)
usuario1.depositar(200)
usuario1.sacar(400)
usuario1.sacar(250)
print(usuario1.ver_saldo())

usuario2 = ContaPoupanca("usuario2",1000)
usuario2.render_juros(1)
usuario2.render_juros(2)
print(usuario2.ver_saldo())
print(usuario2.rendimento_total) 

usuario3 = ContaEmpresarial("usuario3",10000,"brielinc")
contas = [usuario1,usuario2,usuario3]
for usuarios in contas :
    print(usuarios)
    