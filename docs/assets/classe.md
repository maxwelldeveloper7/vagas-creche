@startuml
hide methods
skinparam classAttributeIconSize 0
skinparam linetype ortho

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
  +unidade_id : UUID?  ' opcional
}

class Criterio <<ILF>> {
  +id
  +edital_id : UUID  ' ref EIF
  +descricao
  +pontos_ou_peso
  +tipo_dado  ' booleano, numerico, faixa, lista/enum, texto
  +nome_campo_formulario  ' ex.: renda_per_capita
}

class Aluno <<ILF>> {
  +id
  +nome
  +data_nascimento
  +cpf : string?  ' opcional
}

class Responsavel <<ILF>> {
  +id
  +nome
  +cpf
  +telefone
  +email : string?  ' opcional
  +endereco
}

class PreMatricula <<ILF>> {
  +id
  +edital_id : UUID  ' ref EIF
  +aluno_id : UUID
  +responsavel_id : UUID
  +unidade_pretendida_id : UUID
  +modalidade  ' Berçário I/II/III, 1º, 2º
  +turno       ' Manhã/Tarde/Integral
  +protocolo
  +status
  +data_hora
  +dados_socioeconomicos
  +lgpd_confirmado : bool
  +lgpd_confirmado_em : datetime?
  +lgpd_confirmado_por_usuario_id : UUID
}

class PreMatriculaCriterio <<ILF>> {
  +id
  +pre_matricula_id : UUID
  +criterio_id : UUID
  +valor_resposta
}

class VagaOfertada <<ILF>> {
  +id
  +edital_id : UUID  ' ref EIF
  +unidade_id : UUID
  +modalidade
  +turno
  +quantidade_total : int
  +quantidade_ocupada : int
}

class Convocacao <<ILF>> {
  +id
  +pre_matricula_id : UUID
  +data_hora_emissao
  +status
  +prazo : datetime?  ' opcional
}

class Matricula <<ILF>> {
  +id
  +pre_matricula_id : UUID
  +data_hora
  +usuario_atendente_id : UUID
  +status
}

class Auditoria <<ILF>> {
  +id
  +usuario_id : UUID
  +evento
  +entidade
  +entidade_id : UUID
  +data_hora
  +detalhes
}

class Notificacao <<ILF>> {
  +id
  +tipo  ' pre-matricula/convocacao/matricula
  +referencia_entidade
  +referencia_id : UUID
  +data_hora
  +status
}

' ====== RELACIONAMENTOS ======
Unidade "1" <-- "0..*" Usuario : vinculo(opcional)

Aluno "1" <-- "0..*" PreMatricula
Responsavel "1" <-- "0..*" PreMatricula
Unidade "1" <-- "0..*" PreMatricula : unidade_pretendida

PreMatricula "1" <-- "0..*" PreMatriculaCriterio : respostas
Criterio "1" <-- "0..*" PreMatriculaCriterio

Unidade "1" <-- "0..*" VagaOfertada

PreMatricula "1" <-- "0..*" Convocacao
PreMatricula "1" <-- "0..1" Matricula

Usuario "1" <-- "0..*" Auditoria
Usuario "1" <-- "0..*" Notificacao

' ====== REFERÊNCIAS AO EIF ======
Edital ..> Criterio : referencia
Edital ..> PreMatricula : referencia
Edital ..> VagaOfertada : referencia

' ====== NOTAS DE REGRAS ======
note right of VagaOfertada
UNIQUE(edital_id, unidade_id, modalidade, turno)
RN-19: DIRETOR/SECRETARIO só cadastram
vagas para sua própria unidade
end note

note right of Criterio
RN-12: campos do formulário derivados dos critérios
RN-13: coerência tipo_dado x nome_campo_formulario
RN-14: bloqueio alteração estrutural após uso
end note

note right of PreMatricula
RN-15: confirmação LGPD obrigatória
RN-04: matrícula remove outras pré-matrículas
end note

note top of Edital
<<EIF>> Edital é externo (RN-16):
não é criado/alterado/excluído pelo sistema.
end note

@enduml
