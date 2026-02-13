@startuml
left to right direction
skinparam packageStyle rectangle

actor "Administrador do Sistema (TI)" as Admin #FFF8DC
actor "Secretaria Municipal de Educação (SME)" as SME #FFF8DC
actor "Diretor/Secretário da Instituição" as Inst #FFF8DC
actor "Serviço de Notificações" as Notif #FFF8DC

rectangle "Sistema Municipal de Demanda - Educação Infantil" {

  package "Gestão de Ciclo e Normas" #F0F8FF{
    usecase "Criar Ciclo Letivo" as UC_CicloCriar #FFF8DC
    usecase "Configurar Calendário do Ciclo" as UC_CicloCalendario #FFF8DC
    usecase "Parametrizar Faixas Etárias" as UC_Faixas #FFF8DC
    usecase "Parametrizar Critérios e Pesos" as UC_Criterios #FFF8DC
    usecase "Publicar/Encerrar Inscrições" as UC_Publicacao #FFF8DC
  }

  package "Gestão Institucional" #F0F8FF{
    usecase "Cadastrar Instituição" as UC_Instituicao #FFF8DC
    usecase "Cadastrar Usuário Institucional" as UC_Usuario #FFF8DC
    usecase "Vincular Usuário à Unidade" as UC_Vinculo #FFF8DC
  }

  package "Operação Local (Unidades)" #F0F8FF{
    usecase "Cadastrar Turmas e Vagas" as UC_Turmas #FFF8DC
    usecase "Solicitar Ajuste de Vagas (após bloqueio)" as UC_AjusteVagas #FFF8DC
    usecase "Registrar Inscrição Presencial" as UC_Inscricao #FFF8DC
    usecase "Registrar Responsáveis" as UC_Responsaveis #FFF8DC
    usecase "Registrar Aceite LGPD (campo)" as UC_LGPD #FFF8DC
    usecase "Consultar Lista de Espera" as UC_Lista #FFF8DC
    usecase "Alocar Vaga" as UC_Alocar #FFF8DC
    usecase "Gerar Ficha de Matrícula" as UC_Ficha #FFF8DC
    usecase "Validar Documentos na Matrícula" as UC_ValidDoc #FFF8DC
    usecase "Confirmar Matrícula" as UC_Confirmar #FFF8DC
    usecase "Registrar Desistência/Indeferimento" as UC_Desistencia #FFF8DC
  }

  package "Auditoria e Relatórios" #F0F8FF{
    usecase "Consultar Logs e Trilhas" as UC_Logs #FFF8DC
    usecase "Exportar Listas/Relatórios" as UC_Relatorios #FFF8DC
  }

  package "Notificações" #F0F8FF{
    usecase "Enviar Notificação" as UC_Notificar #FFF8DC
  }

  ' Relacionamentos include/extend
  UC_Inscricao --> UC_Responsaveis : <<include>>
  UC_Inscricao --> UC_LGPD : <<include>>
  UC_Alocar --> UC_Notificar : <<include>>
  UC_Confirmar --> UC_Notificar : <<include>>
  UC_Ficha --> UC_ValidDoc : <<extend>>
  UC_AjusteVagas ..> UC_Turmas : <<extend>>
  UC_Publicacao ..> UC_Criterios : <<include>>
  UC_Publicacao ..> UC_CicloCalendario : <<include>>
}

Admin --> UC_Usuario
Admin --> UC_Logs

SME --> UC_CicloCriar
SME --> UC_CicloCalendario
SME --> UC_Faixas
SME --> UC_Criterios
SME --> UC_Publicacao
SME --> UC_Instituicao
SME --> UC_Usuario
SME --> UC_Vinculo
SME --> UC_Logs
SME --> UC_Relatorios

Inst --> UC_Turmas
Inst --> UC_AjusteVagas
Inst --> UC_Inscricao
Inst --> UC_Lista
Inst --> UC_Alocar
Inst --> UC_Ficha
Inst --> UC_ValidDoc
Inst --> UC_Confirmar
Inst --> UC_Desistencia
Inst --> UC_Relatorios

Notif <-- UC_Notificar
@enduml
