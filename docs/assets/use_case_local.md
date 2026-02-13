@startuml
left to right direction
actor "Diretor/Secretário" as Inst #FFF8DC
actor "Serviço de Notificações" as Notif #FFF8DC

rectangle "Operação Local - Unidade" {
  usecase "Cadastrar Turmas e Vagas" as T #FFF8DC
  usecase "Registrar Inscrição Presencial" as I #FFF8DC
  usecase "Registrar Responsáveis" as R #FFF8DC
  usecase "Registrar Aceite LGPD (campo)" as L #FFF8DC
  usecase "Consultar Lista de Espera" as Q #FFF8DC
  usecase "Alocar Vaga\n(informar Integral/Parcial)" as A #FFF8DC
  usecase "Gerar Ficha de Matrícula" as F #FFF8DC
  usecase "Validar Documentos na Matrícula" as V #FFF8DC
  usecase "Confirmar Matrícula" as C #FFF8DC
  usecase "Enviar Notificação" as N #FFF8DC

  I --> R : <<include>>
  I --> L : <<include>>
  A --> N : <<include>>
  C --> N : <<include>>
  V ..> F : <<extend>>
}

Inst --> T
Inst --> I
Inst --> Q
Inst --> A
Inst --> F
Inst --> V
Inst --> C

Notif <-- N
@enduml
