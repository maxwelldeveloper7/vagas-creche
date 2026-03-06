@startuml
title Sistema de Inscrição em Creche — Diagrama ER

entity Usuario {
  +id_usuario : int <<PK>>
  nome : text
  login : text
  senha_hash : text
}

entity Administrador {
  +id_usuario : int <<PK,FK>>
}

entity Operador {
  +id_usuario : int <<PK,FK>>
  id_unidade : int <<FK>>
  tipo_operador : enum
}

entity UnidadeEscolar {
  +id_unidade : int <<PK>>
  nome_unidade : text
}

entity Responsavel {
  +id_responsavel : int <<PK>>
  nome : text
  cpf : text
  rg : text
  telefone : text
  parentesco : enum
  endereco : text
  ponto_referencia : text
  comprovante_endereco : boolean
  mae_vinculo_empregaticio : boolean
  comprovante_endereco_trabalho : boolean
  demonstrativo_credito_beneficio : boolean
  loas_bpc_seguro_desemprego : boolean
  autonomo : boolean
  mae_matriculada_rede_publica : boolean
  vulnerabilidade_social : boolean
  declaracao_mae_adolescente : boolean
  renda_percapita : decimal
}

entity Crianca {
  +id_crianca : int <<PK>>
  nome : text
  data_nascimento : date
  cpf : text
  nome_pai : text
  nome_mae : text
  nis : text
  cartao_sus : text
  situacao : enum
  vaga_pleiteada : enum
  certidao_sem_pai_ou_mae : boolean
  irmao_matriculado : boolean
  encaminhamento_institucional : boolean
  laudo_deficiencia_neoplasia : boolean
  laudo_intolerancia_alimentar : boolean
  laudo_neurodivergente : boolean
}

entity Inscricao {
  +id_inscricao : int <<PK>>
  numero_inscricao : text
  data_inscricao : datetime
  id_usuario : int <<FK>>
  id_unidade : int <<FK>>
  id_responsavel : int <<FK>>
  id_crianca : int <<FK>>
}

' HERANÇA
Usuario ||--|| Administrador
Usuario ||--|| Operador

' RELACIONAMENTOS
UnidadeEscolar ||--o{ Operador : possui
UnidadeEscolar }o--o{ Administrador : cadastra
Operador ||--o{ Inscricao : realiza
Operador ||--o{ Administrador : cadastra

Responsavel ||--o{ Crianca : responsavel_por
Crianca ||--|| Inscricao : gera

UnidadeEscolar ||--o{ Inscricao : recebe
Administrador ||--o{ Inscricao : visualiza

@enduml