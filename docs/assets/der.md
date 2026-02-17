@startuml
' DER / Modelo Entidade-Relacionamento (corrigido e consistente com NESMA)
' ILF = mantido pelo sistema | EIF = referenciado (externo)

hide circle
skinparam linetype ortho
skinparam classAttributeIconSize 0

' ====== EIF (externo) ======
class Edital <<EIF>> {
  +id
  +ano
  +numero
  +periodo_pre_matricula_ini
  +periodo_pre_matricula_fim
  +periodo_matricula_ini
  +periodo_matricula_fim
  +status
}

' ====== ILFs (internos) ======
class Unidade <<ILF>> {
  +id
  +nome
  +codigo
}

class Usuario <<ILF>> {
  +id
  +login
  +senha_hash
  +perfil  ' ADMIN/SECRETARIA/DIRETOR/SECRETARIO
  +unidade_id (FK, opcional)
}

class Criterio <<ILF>> {
  +id
  +edital_id (ref EIF)
  +descricao
  +pontos_ou_peso
  +tipo_dado  ' booleano, numerico, faixa, lista/enum, texto
  +nome_campo_formulario  ' ex.: renda_per_capita, possui_deficiencia
}

class Aluno <<ILF>> {
  +id
  +nome
  +data_nascimento
  +cpf (opcional)
}

class Responsavel <<ILF>> {
  +id
  +nome
  +cpf
  +telefone
  +email (opcional)
  +endereco
}

class PreMatricula <<ILF>> {
  +id
  +edital_id (ref EIF)
  +aluno_id (FK)
  +responsavel_id (FK)
  +unidade_pretendida_id (FK)
  +modalidade
  +turno
  +protocolo
  +status
  +data_hora
  +dados_socioeconomicos
  +lgpd_confirmado (S/N)
  +lgpd_confirmado_em
  +lgpd_confirmado_por_usuario_id (FK)
}

class PreMatriculaCriterio <<ILF>> {
  +id
  +pre_matricula_id (FK)
  +criterio_id (FK)
  +valor_resposta
}

class VagaOfertada <<ILF>> {
  +id
  +edital_id (ref EIF)
  +unidade_id (FK)
  +modalidade
  +turno
  +quantidade_total
  +quantidade_ocupada
}

class Convocacao <<ILF>> {
  +id
  +pre_matricula_id (FK)
  +data_hora_emissao
  +status
  +prazo (opcional)
}

class Matricula <<ILF>> {
  +id
  +pre_matricula_id (FK)
  +data_hora
  +usuario_atendente_id (FK)
  +status
}

class Auditoria <<ILF>> {
  +id
  +usuario_id (FK)
  +evento
  +entidade
  +entidade_id
  +data_hora
  +detalhes
}

class Notificacao <<ILF>> {
  +id
  +tipo  ' pre-matricula/convocacao/matricula
  +referencia_entidade
  +referencia_id
  +data_hora
  +status
}

' ====== RELACIONAMENTOS ======

' Usuário/unidade
Unidade "1" <-- "0..*" Usuario : vinculo(opcional)

' Pré-matrícula (núcleo)
Aluno "1" <-- "0..*" PreMatricula
Responsavel "1" <-- "0..*" PreMatricula
Unidade "1" <-- "0..*" PreMatricula : unidade_pretendida

PreMatricula "1" <-- "0..*" PreMatriculaCriterio : respostas
Criterio "1" <-- "0..*" PreMatriculaCriterio

' Vagas por oferta
Unidade "1" <-- "0..*" VagaOfertada

note right of VagaOfertada
Restrição recomendada:
UNIQUE(edital_id, unidade_id, modalidade, turno)
end note

' Convocação e matrícula
PreMatricula "1" <-- "0..*" Convocacao
PreMatricula "1" <-- "0..1" Matricula

' Auditoria e notificações
Usuario "1" <-- "0..*" Auditoria
Usuario "1" <-- "0..*" Notificacao

' ====== REFERÊNCIAS ao EIF (sem “manter” o edital) ======
Edital ..> Criterio : referência normativa
Edital ..> PreMatricula : referência normativa
Edital ..> VagaOfertada : referência normativa

note top of Edital
<<EIF>> Edital é fonte externa (RN-16):
- não é criado/alterado/excluído pelo sistema
- apenas referenciado
end note

note right of Criterio
nome_campo_formulario:
- identifica o campo exibido no formulário (RN-12)
- usado para validação de coerência (RN-13)
end note

@enduml
