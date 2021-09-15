class Cadastro:
    def __init__(self, nome, cep, numeroResidencia):
        self.nome = nome
        self.cep = cep
        self.numeroResidencia = numeroResidencia
        self.pets = []
        self.telefones = []

    def inserirTelefone(self, telefone):
        self.telefones.append(telefone)

    def inserirPet(self, pet):
        self.pets.append(pet)

    def __str__(self):
        out = f"{self.nome} possui {len(self.pets)} pets e mora no cep {self.cep} numero {self.numeroResidencia}\nContatos:\n"
        for t in self.telefones:
            out = out + str(t) + "\n"
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

class TelefoneConta:
    def __init__(self, numero, proprietario, celular=False, apenasEmergencias=False):
        self.numero = numero
        self.proprietario = proprietario
        self.celular = celular
        self.apenasEmergencias = apenasEmergencias

    def __str__(self):
        return f"{self.numero}, Apenas emergencias: {self.apenasEmergencias}"


bruno = Cadastro("Bruno", "000000", "1234")
bruno.inserirPet(Pet("Terry", 5, "cão", "Cairn Terrier", "preto", bruno))
bruno.inserirTelefone(TelefoneConta("1234-5678", bruno, True, False))
print(bruno)

