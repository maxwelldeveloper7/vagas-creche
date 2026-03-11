@startuml

left to right direction

actor "Operador\n(Diretor ou Secretário)" as Operador

rectangle {

    usecase "Gerar comprovante\nde inscrição" as UC1
    usecase "Gerar número\nde inscrição" as UC2
    usecase "Montar dados\ndo comprovante" as UC3
    usecase "Gerar PDF" as UC4
    usecase "Criptografar PDF\n(senha = CPF da criança)" as UC5
    usecase "Disponibilizar\npara impressão" as UC6
    usecase "Disponibilizar\npara download" as UC7

}

Operador --> UC1

UC1 --> UC2 : <<include>>
UC1 --> UC3 : <<include>>
UC1 --> UC4 : <<include>>

UC4 --> UC5 : <<include>>

UC1 --> UC6 : <<extend>>
UC1 --> UC7 : <<extend>>

@enduml