@startuml

actor Administrador
actor Sistema

rectangle  {
    usecase "Definir Período de Inscrição" as UC1
    usecase "Validar Datas e Staus" as UC2
    usecase "Registro Fora do Período" as UC3
    usecase "Registro Fora do Período" as UC3
}

Administrador --> UC1
Sistema --> UC2
UC2 --> UC3 : Bloqueia

@enduml