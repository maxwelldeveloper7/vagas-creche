@startuml
title Fluxo 6.2 — Registro de Inscrição (Diagrama de Sequência)

actor Operador
participant "Navegador" as Browser
participant "Blueprint Inscrições" as BP
participant "InscricaoService" as Service
participant "Repositories" as Repo
participant "AuditService" as Audit
database "PostgreSQL" as DB

Operador -> Browser : Preenche formulário
Browser -> BP : POST /inscricoes/nova (dados)

BP -> Service : registrar_inscricao(dados, operador)

Service -> Repo : buscar_periodo_aberto()
Repo -> DB : SELECT periodo aberto
DB --> Repo : periodo / null
Repo --> Service : periodo

alt Período fechado
    Service --> BP : erro("Período fechado")
    BP --> Browser : resposta erro
else Período aberto

    Service -> Repo : existe_inscricao(crianca, periodo)
    Repo -> DB : SELECT inscrição
    DB --> Repo : existe / não existe
    Repo --> Service : resultado

    alt Inscrição duplicada
        Service --> BP : erro("Inscrição existente")
        BP --> Browser : resposta erro: Informa local e dada de onde foi realziada
    else Não duplicada

        Service -> Repo : buscar_ou_criar_responsavel()
        Repo -> DB : UPSERT responsável

        Service -> Repo : buscar_ou_criar_crianca()
        Repo -> DB : UPSERT criança

        Service -> Repo : garantir_vinculo()
        Repo -> DB : INSERT vínculo

        Service -> Service : gerar_numero_inscricao()

        Service -> Repo : criar_inscricao()
        Repo -> DB : INSERT inscrição
        DB --> Repo : inscrição
        Repo --> Service : inscrição

        Service -> Audit : registrar(operação)
        Audit -> DB : INSERT audit_log

        Service --> BP : inscrição

        BP -> BP : gerar comprovante (PDF)
        BP --> Browser : confirmação + comprovante

    end
end

@enduml