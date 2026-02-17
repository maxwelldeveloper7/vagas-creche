@startuml
title Diagrama de Implantação (Deployment) - Sistema Municipal de Demanda por Vagas

skinparam linetype ortho
skinparam componentStyle rectangle

' ==== Clientes ====
node "Cliente\nPC/Notebook\n(Navegador Web)" as Client {
  artifact "Browser\n(HTML/CSS/JS)" as Browser
}

' ==== Rede / Internet-LAN ====
cloud "Rede Municipal / Internet\nHTTPS" as Net

' ==== Servidor Web ====
node "VM Webserver\nLinux" as WebVM {
  artifact "Nginx/Reverse Proxy" as Nginx
  artifact "App Flask (WSGI)\nGunicorn/uWSGI" as FlaskApp
  artifact "Worker Notificações\n(process/daemon)" as Worker
  artifact "Logs / Auditoria" as Logs
}

' ==== Servidor de Dados ====
node "VM Dataserver\nLinux" as DataVM {
  database "PostgreSQL" as PG
  artifact "Rotina Backup Diário\n(RNF-07)" as Backup
}

' ==== Conexões ====
Browser --> Net : HTTPS 443
Net --> Nginx : HTTPS 443
Nginx --> FlaskApp : HTTP local / socket
FlaskApp --> PG : TCP 5432\n(rede interna)
Worker --> PG : TCP 5432\n(rede interna)

FlaskApp --> Logs : grava logs/auditoria
Worker --> Logs : grava logs

Backup --> PG : dump/replicação\n(janela fora do expediente)

note right of WebVM
- Aplicação monolítica (Flask)\n- Até 15 usuários simultâneos\n- RBAC + segregação (RF-02/RN-08/RN-19)\n- LGPD: controle de acesso e minimização (RNF-06)
end note

note right of DataVM
- PostgreSQL com transações (RNF-02)\n- Índices para consultas de classificação\n- Backup diário (RNF-07)
end note

note bottom
Sugestão de segurança mínima:
- DB acessível apenas pela VM Web (rede interna)
- TLS obrigatório no acesso externo
- Senhas hash + políticas de acesso
end note

@enduml
