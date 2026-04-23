class Funcionario:
    def __init__(self,indice,nome,login,salario):
        self.indice = indice
        self.nome = nome
        self.login = login
        self.salario = salario

    def info(self):
        return(f"#{self.indice} - Nome: {self.nome} - Email: {self.login}@empresa.com - Salário: {self.salario}")

class Estagiario(Funcionario):
    def __init__(self, indice, nome, login, ano_matricula):
        super().__init__(indice, nome, login, 2500)
        self.ano_matricula = ano_matricula



class Tecnico(Funcionario):
    def __init__(self, indice, nome, login, salario, nivel=1):
        super().__init__(indice, nome, login, salario)
        self.nivel = nivel

    def info(self):
        return super().info() + f" - Nível de acesso: n{self.nivel}"

    def diminui_nivel(self):
        if(self.nivel>1):
            self.nivel = self.nivel - 1
            return f"Sucesso! Usuário agora é n{self.nivel}"
        else:
            return f"Fracasso! Usuário já é n1"

    def aumenta_nivel(self):
        if(self.nivel>3):
            self.nivel = self.nivel + 1
            return f"Sucesso! Usuário agora é n{self.nivel}"
        else:
            return f"Fracasso! Usuário já é n3"


funcionarios = []

funcionarios.append(Funcionario(0,"Isadora","isadora.melo",20000))
funcionarios.append(Estagiario(1,"Emanuelly","emanuelly.ramos",2026))
funcionarios.append(Tecnico(2, "Maria Eduarda", "maria.avila", 5000))
funcionarios.append(Tecnico(3, "Emily", "emily.taina", 6000, 2))

for f in funcionarios:
    print(f.info())