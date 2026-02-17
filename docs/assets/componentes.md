@startuml
title Diagrama de Componentes - Monólito Flask (Sistema de Demanda por Vagas)

skinparam componentStyle rectangle
skinparam linetype ortho

package "Cliente" {
  [Navegador Web\n(HTML/CSS/JS)] as Browser
}

package "Aplicação Web (Flask - Monólito)" {

  package "Controllers (Rotas/Views)" {
    [AuthController] as AuthC
    [CriterioController] as CritC
    [VagasController] as VagasC
    [PreMatriculaController] as PMC
    [ClassificacaoController] as ClassC
    [ConvocacaoController] as ConvC
    [MatriculaController] as MatC
    [DashboardController] as DashC
  }

  package "Services (Regras de Negócio)" {
    [AuthService] as AuthS
    [CriterioService] as CritS
    [VagasService] as VagasS
    [PreMatriculaService] as PMS
    [ClassificacaoService] as ClassS
    [ConvocacaoService] as ConvS
    [MatriculaService] as MatS
    [DashboardService] as DashS

    [AuditoriaService] as AudS
    [NotificacaoService] as NotifS
    [DocumentoService\n(Ficha Matrícula)] as DocS
  }

  package "Persistência" {
    [SQLAlchemy Repositories] as Repo
    [Modelos ORM] as ORM
  }

  package "Infra / Cross-cutting" {
    [RBAC/Autorização\n(RF-02)] as RBAC
    [Validações\n(RN-12/13/15/19)] as VAL
    [Transações\n(RNF-02)] as TX
  }
}

component "Worker de Notificações" as Worker
database "PostgreSQL" as DB

' ===== Cliente -> Controllers =====
Browser --> AuthC
Browser --> CritC
Browser --> VagasC
Browser --> PMC
Browser --> ClassC
Browser --> ConvC
Browser --> MatC
Browser --> DashC

' ===== Controllers -> Services =====
AuthC --> AuthS
CritC --> CritS
VagasC --> VagasS
PMC --> PMS
ClassC --> ClassS
ConvC --> ConvS
MatC --> MatS
DashC --> DashS

' ===== Cross-cutting =====
AuthS --> RBAC
CritS --> RBAC
VagasS --> RBAC
PMS --> RBAC
ClassS --> RBAC
ConvS --> RBAC
MatS --> RBAC
DashS --> RBAC

CritS --> VAL
VagasS --> VAL
PMS --> VAL
MatS --> VAL

VagasS --> TX
PMS --> TX
MatS --> TX

' ===== Serviços transversais =====
CritS --> AudS
VagasS --> AudS
PMS --> AudS
ClassS --> AudS
ConvS --> AudS
MatS --> AudS
DashS --> AudS

VagasS --> NotifS
PMS --> NotifS
ConvS --> NotifS
MatS --> NotifS

MatS --> DocS

' ===== Persistência =====
AuthS --> Repo
CritS --> Repo
VagasS --> Repo
PMS --> Repo
ClassS --> Repo
ConvS --> Repo
MatS --> Repo
DashS --> Repo
AudS --> Repo
NotifS --> Repo

Repo --> ORM
ORM --> DB

' ===== Worker =====
Worker --> NotifS
Worker --> DB

note right of RBAC
Regras-chave:
- RN-08/09 (segregação por unidade)
- RN-19 (unidade fixa em UC-04)
end note

note right of VAL
Validações-chave:
- RN-12 (campos conforme critérios)
- RN-13 (coerência tipo_dado x campo)
- RN-15 (LGPD obrigatório)
end note

note right of DocS
Gera ficha de matrícula para impressão (RF-11)
end note

@enduml
