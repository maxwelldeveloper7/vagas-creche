@startuml




actor "Operador\n(Diretor ou Secretário)" as Operador

rectangle {

  usecase "Iniciar Cadastro do Responsável" as UC1
  usecase "Registrar Dados de Identificação" as UC2
  usecase "Registrar Endereço" as UC3
  usecase "Registrar Situação Socioeconômica" as UC4
  usecase "Salvar Cadastro do Responsável" as UC5

}

Operador --> UC1

UC1 --> UC2 : <<include>>
UC2 --> UC3 : <<include>>
UC3 --> UC4 : <<include>>
UC4 --> UC5 : <<include>>

@enduml