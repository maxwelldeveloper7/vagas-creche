@startuml

left to right direction

actor Operador
actor Sistema

rectangle {

  usecase "Cadastrar Criança" as UC1
  usecase "Verificar inscrição\nexistente por CPF" as UC2
  usecase "Calcular idade na\ndata de corte (31/03)" as UC3
  usecase "Registrar dados" as UC4  
  usecase "Bloquear inscrição\nduplicada" as UC5

}

Operador --> UC1

UC1 --> UC4 : <<include>>


Sistema --> UC3
Sistema --> UC2
UC2 --> UC5 : <<include>>

@enduml