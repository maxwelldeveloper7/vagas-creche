@startuml

skinparam state {
  BackgroundColor #FEFECE
  BorderColor #A80036
}

title Diagrama de Estados - Inscrição / Atendimento Educação Infantil

hide empty description

[*] --> Rascunho : iniciar inscrição (unidade)

state Rascunho {
  [*] --> EmPreenchimento
  EmPreenchimento --> Cancelado : cancelar pelo operador
  EmPreenchimento --> ValidacaoSistema : finalizar preenchimento
}

state ValidacaoSistema {
  [*] --> Validando
  Validando --> Rejeitado : modalidade incompatível\nou dados obrigatórios ausentes
  Validando --> DuplicadoBloqueado : duplicidade (CPF + data nasc.)
  Validando --> Inscrito : validações OK\npontuação calculada\nprotocolo gerado
}

DuplicadoBloqueado --> [*] : encerramento sem inscrição
Rejeitado --> [*] : corrigir e reiniciar (novo registro)

Inscrito --> Classificado : inscrição registrada\nentra na lista (ordenada)

' Convocação / Alocação
Classificado --> Convocado : alocar vaga\n(informar Integral/Parcial\n+ turno quando aplicável)

' Exceção: alocação fora da ordem exige justificativa
Classificado --> Convocado : alocar fora da ordem\n[justificativa registrada]

' Prazo de comparecimento
Convocado --> AguardandoMatricula : notificação enviada\nprazo iniciado

state AguardandoMatricula {
  [*] --> AguardandoComparecimento
  AguardandoComparecimento --> EmMatricula : responsável comparece
  AguardandoComparecimento --> PerdaDePrazo : prazo expirado\n(sem comparecimento)
  AguardandoComparecimento --> Desistente : desistência formal registrada
}

' Matrícula e validação documental (apenas na matrícula)
state EmMatricula {
  [*] --> ValidacaoDocumental
  ValidacaoDocumental --> PendenteDocumentos : pendências identificadas
  ValidacaoDocumental --> Indeferido : documentos inválidos\nou não apresentados
  ValidacaoDocumental --> Matriculado : documentação completa\nficha assinada\nconfirmação no sistema
}

' Pendência documental pode virar matrícula ou indeferimento
PendenteDocumentos --> EmMatricula : regularizar e retornar\npara validação documental
PendenteDocumentos --> Indeferido : não regularizou\nou decisão administrativa

' Estados finais
Matriculado --> [*]
Indeferido --> [*]
Desistente --> [*]
PerdaDePrazo --> VagaLiberada : liberação manual pela unidade

' Controle manual de liberação e remanescentes
VagaLiberada --> [*] : vaga liberada e registrada em log
@enduml
