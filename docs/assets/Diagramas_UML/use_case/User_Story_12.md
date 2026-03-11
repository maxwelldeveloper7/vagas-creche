@startuml
left to right direction

actor "Administrador" as Admin

rectangle  {

  usecase "Gerar Relatórios\nAdministrativos" as UC1

  usecase "Relatório\nLista Geral de Inscritos" as UC2
  usecase "Relatório por\nUnidade Escolar" as UC3
  usecase "Relatório por\nFaixa Etária / Vaga" as UC4
  usecase "Relatório por\nCritérios Sociais" as UC5

  usecase "Exportar Relatório\npara CSV" as UC6

}

Admin --> UC1

UC2 ..> UC1 : <<extend>>
UC3 ..> UC1 : <<extend>>
UC4 ..> UC1 : <<extend>>
UC5 ..> UC1 : <<extend>>

UC6 ..> UC1 : <<include>>

@enduml