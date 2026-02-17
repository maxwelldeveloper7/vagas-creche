@startuml
title Diagrama de Estados - PreMatricula

[*] --> CADASTRADA : UC-05 concluído\n(RN-15 confirmado)

CADASTRADA --> CLASSIFICADA : consulta dinâmica\n(RN-02)

CLASSIFICADA --> CONVOCADA : UC-08\n(convocação emitida)

CONVOCADA --> EM_ATENDIMENTO : início do atendimento\n(matrícula)

EM_ATENDIMENTO --> MATRICULADA : UC-09 concluído\n(RN-06/RN-11)

' Remoção automática após matrícula em qualquer unidade
CADASTRADA --> REMOVIDA_AUTOMATICAMENTE : matrícula efetivada\n(RN-04)
CLASSIFICADA --> REMOVIDA_AUTOMATICAMENTE : matrícula efetivada\n(RN-04)
CONVOCADA --> REMOVIDA_AUTOMATICAMENTE : matrícula efetivada\n(RN-04)
EM_ATENDIMENTO --> REMOVIDA_AUTOMATICAMENTE : matrícula efetivada\n(RN-04)

' Encerramentos administrativos (opcional)
CADASTRADA --> CANCELADA : cancelamento administrativo
CLASSIFICADA --> CANCELADA : cancelamento administrativo
CONVOCADA --> CANCELADA : cancelamento administrativo

MATRICULADA --> [*]
CANCELADA --> [*]
REMOVIDA_AUTOMATICAMENTE --> [*]

note right of CLASSIFICADA
Estado lógico/derivado:
a “classificação” é uma visão
obtida por consulta (RN-02).
end note

@enduml
