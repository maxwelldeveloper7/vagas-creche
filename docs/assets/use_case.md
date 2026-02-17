@startuml
left to right direction
skinparam packageStyle rectangle

actor "ADMIN" as admin
actor "SECRETARIA" as sec
actor "DIRETOR" as dir
actor "SECRETARIO" as secr

rectangle "Sistema Municipal de Gestão de Demanda por Vagas\n(Educação Infantil)" {

  usecase "UC-01\nAutenticar usuário" as UC01
  usecase "UC-03\nCadastrar critérios" as UC03
  usecase "UC-04\nCadastrar vagas" as UC04
  usecase "UC-05\nCadastrar pré-matrícula" as UC05
  usecase "UC-07\nListar classificação" as UC07
  usecase "UC-08\nConvocar candidato" as UC08
  usecase "UC-09\nEfetivar matrícula\n+ gerar ficha" as UC09
  usecase "UC-10\nConsultar dashboard" as UC10

  usecase "Registrar auditoria\n(RF-16)" as AUD
  usecase "Emitir notificações\n(RF-17)" as NOTIF
}

' ---- Acesso por perfil ----
admin --> UC01
admin --> UC03

sec --> UC01
sec --> UC07
sec --> UC10

dir --> UC01
dir --> UC04
dir --> UC05
dir --> UC07
dir --> UC08
dir --> UC09

secr --> UC01
secr --> UC04
secr --> UC05
secr --> UC07
secr --> UC08
secr --> UC09

' ---- Inclusões transversais ----
UC03 .> AUD : <<include>>
UC04 .> AUD : <<include>>
UC05 .> AUD : <<include>>
UC08 .> AUD : <<include>>
UC09 .> AUD : <<include>>

UC04 .> NOTIF : <<include>>
UC05 .> NOTIF : <<include>>
UC08 .> NOTIF : <<include>>
UC09 .> NOTIF : <<include>>

' ---- Notas de regras relevantes ----
note right of UC04
RN-19: Unidade fixa
para DIRETOR/SECRETARIO
end note

note right of UC03
RN-13: coerência tipo critério x campo
RN-14: imutabilidade após uso
end note

note right of UC05
RN-15: confirmação LGPD obrigatória
RN-12: campos conforme critérios
end note

note bottom
Edital é fonte externa (RN-16) e não possui UC de cadastro.
Responsável não acessa o sistema (RN-10).
end note

@enduml
