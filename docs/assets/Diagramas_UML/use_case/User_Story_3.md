@startuml
left to right direction
skinparam packageStyle rectangle

actor Operador

rectangle {
    usecase "Cadastrar Turma" as UC1
    usecase "Editar Turma" as UC2
    usecase "Listar Turmas" as UC3
    usecase "Definir Vagas Disponíveis" as UC4
}

Operador --> UC1
Operador --> UC2
Operador --> UC3
UC1 --> UC4 : includes
UC2 --> UC4 : includes

@enduml