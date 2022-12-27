from conta import Conta
from cliente import Cliente

# def cria_conta(numero, titular, saldo, limite):
#     conta = {"numero": numero, "titular": titular, "saldo": saldo, "limite": limite}
   
#     return conta

# def deposita(conta, valor): 
#     conta["saldo"] += valor

# def saca(conta, valor):
#     conta["saldo"] -= valor

# def extrato(conta):
#     print("Saldo é {}".format(conta["saldo"]))

conta = Conta(123, "Leandro", 55.0, 1000.0)

print(conta)
print(vars(conta))
# print(conta.titular)

conta.extrato()
conta.deposita(500)
conta.extrato()
conta.saca(100)
conta.extrato()

conta.saca(5000)

codigos = Conta.codigos_bancos()
print(codigos)
print(codigos['BB'])

cliente = Cliente("leandro Cliente")

print(cliente)

# chamando a @property
print(cliente.nome)
