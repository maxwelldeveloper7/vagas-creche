@startuml
title Diagrama de Estados - Convocacao

[*] --> EMITIDA : UC-08

EMITIDA --> NOTIFICADA : notificação gerada\n(RF-17)

NOTIFICADA --> ATENDIDA : responsável comparece\n(início UC-09)

ATENDIDA --> CONCLUIDA : matrícula efetivada\n(RF-11)

' Encerramento por gestão (opcional)
EMITIDA --> CANCELADA : cancelamento administrativo
NOTIFICADA --> CANCELADA : cancelamento administrativo

CONCLUIDA --> [*]
CANCELADA --> [*]

@enduml
