@startuml
title Fluxo 6.2 — Registro de Inscrição (Diagrama de Atividade)

start

:Operador acessa formulário de nova inscrição;

:Preenche dados do responsável, criança e inscrição;

:Envia requisição POST /inscricoes/nova;

:Verificar se há período de inscrição aberto;
if (Período aberto?) then (Sim)

  :Verificar se já existe inscrição para a criança no período;
  if (Inscrição já existe?) then (Sim)
    :Exibir erro "Inscrição Existente";
    :Exibir data e local de onde foi realizada;
    stop
  else (Não)

    :Garantir cadastro do responsável;
    :Garantir cadastro da criança;
    :Garantir vínculo responsável-criança;

    :Gerar número de inscrição;

    :Persistir inscrição no banco;

    :Registrar operação no audit_log;

    :Gerar comprovante (PDF);

    :Exibir confirmação e disponibilizar comprovante;

  endif

else (Não)
  :Exibir erro "Período de inscrição fechado";
endif

stop

@enduml