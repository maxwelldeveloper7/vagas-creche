@startuml

left to right direction

actor Operador

rectangle  {

    usecase "Visualizar resumo da inscrição" as UC1
    usecase "Revisar dados do responsável" as UC2
    usecase "Revisar dados da criança" as UC3
    usecase "Revisar dados socioeconômicos" as UC4
    usecase "Editar informações" as UC5
    usecase "Confirmar registro da inscrição" as UC6
    usecase "Registrar inscrição no sistema" as UC7

}

Operador --> UC1

UC1 --> UC2 : <<include>>
UC1 --> UC3 : <<include>>
UC1 --> UC4 : <<include>>

UC5 ..> UC1 : <<extend>>

UC1 --> UC6
UC6 --> UC7 : <<include>>

@enduml