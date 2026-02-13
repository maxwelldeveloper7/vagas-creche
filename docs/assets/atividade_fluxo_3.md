@startuml
title Subfluxo - Alocação de Vaga (com Integral/Parcial)

start

partition "Diretor/Secretário da Unidade" {
  :Abrir lista de espera\n(unidade/modalidade);
  :Verificar vagas disponíveis na turma;
}

partition "Sistema" {
  :Exibir lista ordenada por pontuação\n(e regras do ciclo);
  :Sugerir próximo elegível;
}

partition "Diretor/Secretário da Unidade" {
  if (Seleciona o 1º da lista?) then (Sim)
    :Prosseguir;
  else (Não)
    :Selecionar outro candidato;
    :Informar justificativa obrigatória;
  endif

  :Informar tipo de atendimento:\nIntegral ou Parcial\n(+ turno quando aplicável);
  :Confirmar alocação;
}

partition "Sistema" {
  :Atualizar status = Convocado;
  :Remover candidato das demais listas;
  :Registrar log de alocação\n(+ justificativa);
  :Enviar notificação ao(s) responsável(is)\n(se configurado);
}

stop
@enduml