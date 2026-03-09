@startuml

left to right direction

actor Administrador
actor Diretor
actor Secretario

rectangle "Sistema de Inscrição em Creche" {

    Administrador -- (Cadastrar Unidade Escolar)
    Administrador -- (Cadastrar Diretor)
    Administrador -- (Cadastrar Secretário)
    Administrador -- (Consultar Inscrições)
    Administrador -- (Gerar Relatórios)

    Diretor -- (Registrar Inscrição)
    Diretor -- (Consultar Inscrições da Unidade)
    Diretor -- (Reemitir Comprovante)

    Secretario -- (Registrar Inscrição)
    Secretario -- (Consultar Inscrições da Unidade)
    Secretario -- (Reemitir Comprovante)

    (Registrar Inscrição) .> (Cadastrar Responsável) : <<include>>
    (Registrar Inscrição) .> (Cadastrar Criança) : <<include>>
    (Registrar Inscrição) .> (Conferir Dados da Inscrição) : <<include>>
    (Registrar Inscrição) .> (Gerar Comprovante) : <<include>>

}

@enduml