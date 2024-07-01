class PlanoTelefone:
    def __init__(self, nome, saldo):
        self.__nome = nome
        self.__saldo = saldo

    def verificar_saldo(self):
        return self.__saldo

    def mensagem_personalizada(self):
        if self.__saldo < 10:
            return "Saldo insuficiente para fazer a chamada."
        else:
            return f"Chamada realizada com sucesso. Saldo: ${self.__saldo:.2f}"

    def custo_chamada(self, duracao):
        return 0.10 * duracao

    def deduzir_saldo(self, custo):
        self.__saldo -= custo

class UsuarioTelefone:
    def __init__(self, nome, telefone, saldo, plano):
        self.nome = nome
        self.telefone = telefone
        self.plano = plano
        self.__saldo = saldo

    def fazer_chamada(self, destinatario, duracao):
        custo = self.plano.custo_chamada(duracao)
        if custo <= self.__saldo:
            self.plano.deduzir_saldo(custo)
            return f"Chamada para {destinatario} realizada com sucesso. Saldo: ${self.plano.verificar_saldo():.2f}"
        else:
            return "Saldo insuficiente para fazer a chamada."

# Entradas do usuário (nome, telefone, saldo)
nome_usuario = input()
telefone_usuario = input()
saldo_inicial = float(input())
destinatario = input()
duracao_chamada = int(input())

# Criação de objetos para o plano de telefone e usuário de telefone
plano_usuario = PlanoTelefone(nome_usuario, saldo_inicial)
usuario = UsuarioTelefone(nome_usuario, telefone_usuario, saldo_inicial, plano_usuario)

# Realização da chamada
mensagem = usuario.fazer_chamada(destinatario, duracao_chamada)
print(mensagem)
