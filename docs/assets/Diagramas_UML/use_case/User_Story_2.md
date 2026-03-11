@startuml
left to right direction
skinparam packageStyle rectangle

actor Administrador

package " " {
    usecase "Cadastrar Unidade Escolar" as UC1
    usecase "Editar Unidade Escolar" as UC2
    usecase "Listar Unidades Escolares" as UC3

    usecase "Cadastrar Diretor" as UC4
    usecase "Editar Diretor" as UC5
    usecase "Listar Diretores" as UC6

    usecase "Cadastrar Secretário" as UC7
    usecase "Editar Secretário" as UC8
    usecase "Listar Secretários" as UC9
}

Administrador --> UC1
Administrador --> UC2
Administrador --> UC3
Administrador --> UC4
Administrador --> UC5
Administrador --> UC6
Administrador --> UC7
Administrador --> UC8
Administrador --> UC9

@enduml