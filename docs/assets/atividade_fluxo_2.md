@startuml
skinparam activity {
  BackgroundColor #FEFECE
  BorderColor #A80036
}

title Subfluxo - Inscrição Presencial (Unidade)

start

partition "Diretor/Secretário da Unidade" {
  :Iniciar inscrição;
  :Coletar dados da criança;
  :Coletar dados do(s) responsável(is);
  :Marcar termo LGPD em papel\n(assinado: Sim/Não);
}

partition "Sistema" {
  :Calcular faixa etária pelo corte do ciclo;
  if (Modalidade compatível?) then (Sim)
    if (Duplicidade municipal?) then (Sim)
      :Bloquear gravação;
      :Exibir cadastro existente/alerta;
      :Registrar tentativa em log;
      stop
    else (Não)
      :Calcular pontuação conforme critérios do ciclo;
      :Registrar inscrição na base municipal;
      :Gerar número de protocolo único;
      :Registrar log de inscrição;
    endif
  else (Não)
    :Rejeitar inscrição;\nexibir motivo (idade/modalidade);
    stop
  endif
}

partition "Diretor/Secretário da Unidade" {
  :Imprimir/entregar protocolo ao responsável;
}

stop
@enduml