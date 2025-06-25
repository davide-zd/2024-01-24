from dataclasses import dataclass

@dataclass
class Prodotto:
    id: int
    nome: str
    p_vendita_tot: int

    def __str__(self):
        return f"{self.id}, {self.nome}"

    def __hash__(self):
        return hash(self.id)