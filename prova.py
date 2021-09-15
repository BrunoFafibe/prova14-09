class Cadastro:
    def __init__(self, nome, cep, numeroResidencia):
        self.nome = nome
        self.cep = cep
        self.numeroResidencia = numeroResidencia
        self.pets = []
        self.mensagens = []

    def inserirMensagem(self, telefone):
        self.mensagens.append(telefone)

    def inserirPet(self, pet):
        self.pets.append(pet)

    def __str__(self):
        out = f"{self.nome} possui {len(self.pets)} pets e mora no cep {self.cep} numero {self.numeroResidencia}\nMensagens:\n"
        for m in self.mensagens:
            out = out + str(m) + "\n"
        out = out + "Pets:\n"
        for p in self.pets:
            out = out + str(p) + "\n"
        return out

class Pet:
    def __init__(self, nome, idade, especie, raca, cor, dono):
        self.nome = nome
        self.idade = idade
        self.especie = especie
        self.raca = raca
        self.cor = cor
        self.dono = dono

    def __str__(self):
        return f"{self.nome} é um {self.especie} ({self.raca}) de cor {self.cor} com {self.idade} anos"

class Mensagem:
    def __init__(self, destino, texto, data):
        self.texto = texto
        self.destino = destino
        self.data = data

    def __str__(self):
        return f"{self.data}: {self.texto}"


bruno = Cadastro("Bruno", "000000", "1234")
bruno.inserirPet(Pet("Terry", 5, "cão", "Cairn Terrier", "preto", bruno))
bruno.inserirMensagem(Mensagem(bruno, "Agendamento confirmado", "10/06/19"))
print(bruno)
