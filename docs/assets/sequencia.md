@startuml
title UC-04 - Diagrama de Sequência (Cadastrar/Alterar Vagas) - RN-19 + UNIQUE

actor "Usuário\n(DIRETOR/SECRETARIO)" as U
boundary "UI Web" as UI
control "VagasController" as C
control "VagasService" as S
database "PostgreSQL" as DB
control "AuditoriaService" as AUD
control "NotificacaoService" as NOTIF

U -> UI : Abrir tela de cadastro de vagas
UI -> C : carregarTela()

C -> S : obterContextoUsuario(usuario)
S -> DB : SELECT perfil, unidade_id FROM usuario WHERE id=?
DB --> S : perfil, unidade_id
S --> C : perfil, unidade_id

alt Perfil não autorizado
  C --> UI : 403 (acesso negado)
else Perfil autorizado (RN-19)
  C --> UI : Renderizar formulário\n(unidade travada)

  U -> UI : Informar edital, modalidade, turno, quantidade
  UI -> C : salvarOferta(edital_id, modalidade, turno, qtd)

  C -> S : salvarOferta(usuario, edital_id, modalidade, turno, qtd)

  S -> S : validarQtd(qtd >= 0)
  S -> S : fixarUnidade = unidade_id do usuário (RN-19)

  S -> DB : BEGIN
  S -> DB : SELECT id FROM vaga_ofertada\nWHERE edital_id=? AND unidade_id=?\nAND modalidade=? AND turno=?
  DB --> S : oferta_id?

  alt oferta existe
    S -> DB : UPDATE vaga_ofertada\nSET quantidade_total=?\nWHERE id=?
  else oferta não existe
    S -> DB : INSERT vaga_ofertada\n(edital_id, unidade_id, modalidade, turno,\n quantidade_total, quantidade_ocupada=0)
    note right of DB
    Restrição: UNIQUE(edital_id, unidade_id, modalidade, turno)
    end note
  end

  S -> AUD : registrarEvento("VAGA_SALVA", usuario)
  S -> NOTIF : emitir("vaga_ofertada", referencia_id)

  S -> DB : COMMIT

  S --> C : sucesso
  C --> UI : confirmar operação
end

@enduml
