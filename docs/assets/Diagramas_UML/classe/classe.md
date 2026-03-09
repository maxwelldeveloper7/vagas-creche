@startuml

class Usuario {
    id: int
    nome: string
    email: string
    senhaHash: string
    perfil: string
    ativo: boolean
}

class UnidadeEscolar {
    id: int
    nome: string
    endereco: string
    ativa: boolean
}

class Responsavel {
    id: int
    nome: string
    cpf: string
    rg: string
    telefone: string
    endereco: string
    pontoReferencia: string
    rendaPercapita: decimal
}

class Crianca {
    id: int
    nome: string
    dataNascimento: date
    cpf: string
    nomePai: string
    nomeMae: string
    nis: string
    cartaoSus: string
}

class Inscricao {
    id: int
    numeroInscricao: string
    dataInscricao: datetime
    vagaPleiteada: string
    situacao: string
}

Usuario "1" -- "1" UnidadeEscolar
UnidadeEscolar "1" -- "0..*" Inscricao
Responsavel "1" -- "0..*" Inscricao
Crianca "1" -- "1" Inscricao

@enduml