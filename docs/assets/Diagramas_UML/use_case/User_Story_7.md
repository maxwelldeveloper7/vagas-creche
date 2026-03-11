@startuml

left to right direction

actor "Operador\n(Diretor ou Secretário)" as Operador

rectangle  {

    usecase "Cadastrar irmão" as UC1
    usecase "Reutilizar dados do responsável" as UC2
    usecase "Preencher automaticamente\nnome do pai e da mãe" as UC3
    usecase "Editar dados da criança" as UC4
    usecase "Confirmar cadastro do irmão" as UC5

}

Operador --> UC1

UC1 --> UC2 : <<include>>
UC1 --> UC4 : <<include>>
UC1 --> UC5 : <<include>>

UC3 ..> UC1 : <<extend>>

@enduml