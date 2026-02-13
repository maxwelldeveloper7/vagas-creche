@startuml

skinparam activity {
  BackgroundColor #FEFECE
  BorderColor #A80036
}

title Subfluxo - Vagas Remanescentes (Desistência / Não Comparecimento / Próxima Convocação)

start

partition "Diretor/Secretário da Unidade" {
  :Identificar vaga disponível/remanescente\n(desistência, transferência, ampliação);
  :Abrir lista de espera\n(unidade/modalidade);
}

partition "Sistema" {
  :Exibir lista ordenada;\nSugerir próximo elegível;
}

partition "Diretor/Secretário da Unidade" {
  :Selecionar candidato;
  if (Seleciona fora da ordem?) then (Sim)
    :Informar justificativa obrigatória;
  endif
  :Informar tipo de atendimento\n(Integral/Parcial + turno quando aplicável);
  :Confirmar convocação;
}

partition "Sistema" {
  :Atualizar status = Convocado;
  :Remover candidato das demais listas;
  :Registrar log de convocação\n(+ justificativa);
  :Enviar notificação ao(s) responsável(is)\n(se configurado);
  :Iniciar contagem de prazo de comparecimento\n(configurável pela SME);
}

partition "Diretor/Secretário da Unidade" {
  :Aguardar comparecimento do responsável;
  if (Responsável compareceu dentro do prazo?) then (Sim)
    :Realizar matrícula presencial (subfluxo matrícula);
    stop
  else (Não)
    :Registrar tentativas de contato\n(data/hora/resultado);
    if (Responsável responde e aceita a vaga?) then (Sim)
      :Agendar comparecimento (se aplicável);
      stop
    else (Não)
      if (Prazo expirou?) then (Sim)
        :Registrar motivo:\nDesistência formal OU Não comparecimento;
        :Decidir liberação da vaga\n(controle manual);
      else (Ainda há prazo)
        :Continuar tentativas de contato\naté expirar o prazo;
        stop
      endif
    endif
  endif
}

partition "Sistema" {
  if (Motivo = Desistência?) then (Desistência)
    :Atualizar status = Desistente;
    :Registrar log de desistência;
  else (Não comparecimento)
    :Atualizar status = Encerrado/Perda de Prazo;
    :Registrar log de perda de prazo;
  endif
}

partition "Diretor/Secretário da Unidade" {
  :Liberar vaga manualmente no sistema;
  :Selecionar próximo candidato\nna lista de espera;
}

partition "Sistema" {
  :Registrar log de liberação de vaga;
  :Sugerir próximo elegível;
}

partition "Diretor/Secretário da Unidade" {
  :Confirmar nova convocação\n(reinicia o subfluxo);
}

stop
@enduml
