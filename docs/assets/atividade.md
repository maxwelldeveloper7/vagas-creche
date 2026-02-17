@startuml
title UC-04 - Diagrama de Atividade (Cadastrar Vagas) - com RN-19 e UNIQUE

start
:Autenticar usuário (UC-01);
:Verificar perfil (RF-02);

if (Perfil é DIRETOR ou SECRETARIO?) then (Sim)
  :Definir unidade = unidade do usuário (RN-19);
else (Não)
  :Bloquear acesso à função UC-04;
  stop
endif

:Selecionar edital vigente (referência externa - RN-16);
:Selecionar modalidade (Berçário I/II/III, 1º, 2º);
:Selecionar turno (Manhã/Tarde/Integral);
:Informar quantidade de vagas;

:Validar campos obrigatórios;
:Validar quantidade >= 0;

:Verificar existência de oferta com\n(edital, unidade, modalidade, turno);
if (Já existe?) then (Sim)
  :Atualizar quantidade_total\n(regras RN-07 se aplicável);
else (Não)
  :Criar nova oferta_vaga;
endif

:Persistir em transação (RNF-02);
:Registrar auditoria (RF-16);
:Gerar notificação (RF-17) [opcional];

stop
@enduml
