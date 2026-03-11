@startuml


left to right direction

actor Administrador

rectangle  {

  usecase "Consultar inscrições\n da rede municipal" as UC1
  
  usecase "Buscar inscrição\n por nome da criança" as UC2
  usecase "Buscar inscrição\n por CPF da criança" as UC3
  usecase "Buscar inscrição\n por número da inscrição" as UC4
  
  usecase "Visualizar dados\n completos da inscrição" as UC5
  
  usecase "Reemitir comprovante\n de inscrição" as UC6
}

Administrador --> UC1

UC1 --> UC2 : <<include>>
UC1 --> UC3 : <<include>>
UC1 --> UC4 : <<include>>

UC1 --> UC5 : <<include>>
UC5 --> UC6 : <<extend>>

@enduml