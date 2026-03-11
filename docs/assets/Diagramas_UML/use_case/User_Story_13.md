@startuml

left to right direction

actor Administrador
actor Operador

rectangle  {

  usecase "Realizar Operação\n(Create / Read / Update)" as UC1
  usecase "Registrar Log de Auditoria" as UC2
  usecase "Registrar Alteração de Campos\n(valor anterior / novo valor)" as UC3
  usecase "Registrar Metadados da Operação\n(usuario, perfil, data, unidade, IP)" as UC4
  usecase "Consultar Logs de Auditoria" as UC5

}

Operador --> UC1
Administrador --> UC1

UC1 --> UC2 : <<include>>
UC2 --> UC3 : <<include>>
UC2 --> UC4 : <<include>>

Administrador --> UC5

@enduml