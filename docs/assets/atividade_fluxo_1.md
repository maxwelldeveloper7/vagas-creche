@startuml

skinparam activity {
  BackgroundColor #FEFECE
  BorderColor #A80036
}

title Fluxo Principal - Demanda Educação Infantil (Inscrição até Matrícula)

start

partition "Secretaria Municipal de Educação (SME)" {
  :Criar Ciclo Letivo;
  :Configurar calendário do ciclo\n(inscrições, matrícula, prazos);
  :Parametrizar faixas etárias e corte etário;
  :Parametrizar critérios e pesos do edital;
  :Publicar período de inscrições;
}

partition "Diretor/Secretário da Unidade" {
  :Cadastrar turmas e previsão de vagas\n(modalidade/turno/vagas);
}

partition "Sistema" {
  :Bloquear edição de vagas\napós início das inscrições;
}

partition "Diretor/Secretário da Unidade" {
  while (Inscrições abertas?) is (Sim)
    :Atender responsável presencialmente;
    :Registrar dados da criança;
    :Registrar dados dos responsáveis\n(múltiplos);
    :Marcar "Termo LGPD assinado em papel" = Sim/Não;
  endwhile (Não)
}

partition "Sistema" {
  :Validar modalidade x idade\n(corte etário do ciclo);
  if (Duplicidade municipal?\n(CPF + data nasc.)) then (Sim)
    :Bloquear novo cadastro;\nExibir alerta;
    :Registrar tentativa em log;
    stop
  else (Não)
    :Calcular pontuação automaticamente;
    :Inserir criança na(s) lista(s)\npor unidade/modalidade;
    :Gerar protocolo de inscrição;
    :Registrar log de inscrição;
  endif
}

partition "Secretaria Municipal de Educação (SME)" {
  :Encerrar inscrições;
  :Disponibilizar listas para as unidades;
}

partition "Diretor/Secretário da Unidade" {
  :Consultar lista de espera\n(unidade/modalidade);
  if (Existem vagas disponíveis?) then (Sim)
    :Selecionar candidato (preferencialmente o 1º da lista);
    :Informar tipo de vaga:\nIntegral ou Parcial\n(e turno quando aplicável);
    if (Seleção fora da ordem?) then (Sim)
      :Informar justificativa obrigatória;
    endif
    :Confirmar alocação;
  else (Não)
    :Aguardar disponibilidade de vaga;
    stop
  endif
}

partition "Sistema" {
  :Atualizar status = Convocado;
  :Remover candidato das demais listas;
  :Registrar log de alocação\n(+ justificativa, se houver);
  :Acionar notificação ao(s) responsável(is)\n(se configurado);
}

partition "Diretor/Secretário da Unidade" {
  :Receber responsável para matrícula presencial;
  :Conferir documentos físicos;
  :Registrar validação documental:\nCompleta / Pendência / Indeferido;
  if (Documentação completa?) then (Sim)
    :Gerar ficha de matrícula (pré-preenchida);
    :Coletar assinaturas no documento impresso;
    :Confirmar matrícula no sistema;
  else (Pendência)
    :Orientar responsável e registrar pendências;
    stop
  endif
}

partition "Sistema" {
  :Atualizar status = Matriculado;
  :Registrar log de matrícula;
  :Acionar notificação de confirmação\n(se configurado);
}

stop
@enduml