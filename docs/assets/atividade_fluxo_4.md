@startuml

skinparam activity {
  BackgroundColor #FEFECE
  BorderColor #A80036
}

title Subfluxo - Matrícula Presencial (Validação Documental)

start

partition "Diretor/Secretário da Unidade"{
  :Abrir inscrição com status = Convocado;
  :Receber responsável na unidade;
  :Conferir documentos físicos;
  :Registrar resultado da conferência\n(Completa/Pendência/Indeferido);
}

partition "Sistema" {
  if (Resultado = Completa?) then (Sim)
    :Liberar geração da ficha de matrícula;
  else (Não)
    if (Resultado = Pendência?) then (Pendência)
      :Manter status (Convocado/Pendente)\nconforme regra do ciclo;
      :Registrar log de pendência;
      stop
    else (Indeferido)
      :Atualizar status = Indeferido;
      :Registrar log de indeferimento\n(com motivo);
      stop
    endif
  endif
}

partition "Diretor/Secretário da Unidade" {
  :Gerar ficha de matrícula padronizada;
  :Imprimir ficha e coletar assinaturas;
  :Confirmar matrícula no sistema;
}

partition "Sistema" {
  :Atualizar status = Matriculado;
  :Registrar log de matrícula;
  :Enviar notificação de confirmação\n(se configurado);
}

stop
@enduml