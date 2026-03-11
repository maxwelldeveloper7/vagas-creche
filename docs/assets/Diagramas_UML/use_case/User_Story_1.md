@startuml
left to right direction
skinparam packageStyle rectangle

actor "Usuário Autorizado" as User

rectangle {
  
  usecase "Inserir Usuário e Senha" as UC1
  usecase "Validar Credenciais" as UC2
  usecase "Identificar Perfil" as UC3
  usecase "Redirecionar ao Painel Correspondente" as UC4
  usecase "Bloquear Acesso" as UC5

}

User --> UC1
UC1 --> UC2
UC2 --> UC3 : se válido
UC2 --> UC5 : se inválido
UC3 --> UC4

@enduml