# 1. Estimativa de Esforço (Horas)

A produtividade típica varia:

| Nível                | Produtividade |
| -------------------- | ------------- |
| iniciante            | 4 PF / dia    |
| intermediário        | 6 PF / dia    |
| experiente           | 8 PF / dia    |
| altamente experiente | 10 PF / dia   |

Considerando seu perfil (desenvolvedor experiente e sistema bem especificado):

**Produtividade adotada: 8 PF / dia**

Carga horária padrão: **6 horas/dia efetivas**

---

## Cálculo

[
Esforço\ (dias) = \frac{161}{8} = 20,1 \approx 21\ dias
]

[
Esforço\ (horas) = 21 \times 6 = 126\ horas
]

---

# Resultado do esforço

**Esforço estimado:**

* **126 horas**
* **21 dias úteis**
* **4,2 semanas**

---

# 2. Estimativa de Prazo Realista (com margem técnica)

Pressman recomenda adicionar 20% a 30% para:

* testes
* ajustes
* correções
* implantação

Adotando **25% de margem**

[
126 \times 1,25 = 158\ horas
]

[
158 ÷ 6 = 26\ dias úteis
]

---

# Prazo final estimado

**Prazo total:**

* **158 horas**
* **26 dias úteis**
* **5,2 semanas**
* aproximadamente **1 mês e 1 semana**

---

# 3. Estimativa de Custo

Agora depende do valor/hora.

Vou usar três cenários realistas.

---

## Cenário A — custo conservador (R$ 40/h)

[
158 \times 40 = R$ 6.320
]

---

## Cenário B — valor médio Brasil (R$ 60/h)

[
158 \times 60 = R$ 9.480
]

---

## Cenário C — valor profissional especializado (R$ 100/h)

[
158 \times 100 = R$ 15.800
]

---

# 4. Resultado Final Consolidado

| Métrica            | Valor             |
| ------------------ | ----------------- |
| Pontos de Função   | 161 PF            |
| Esforço base       | 126 horas         |
| Esforço realista   | **158 horas**     |
| Prazo              | **26 dias úteis** |
| Prazo calendário   | **~5 semanas**    |
| Custo mínimo       | R$ 6.320          |
| Custo médio        | R$ 9.480          |
| Custo profissional | R$ 15.800         |

---

# 5. Estimativa mais realista para seu caso específico

Como:

* sistema pequeno/médio
* arquitetura simples
* sem API externa
* sem anexos
* sem alta concorrência

Estimativa mais precisa:

**140 a 180 horas**

---

# 6. Cronograma sugerido (engenharia de software correta)

Semana 1

* banco de dados
* autenticação
* cadastro de edital, critérios, vagas

Semana 2

* pré-matrícula
* classificação dinâmica

Semana 3

* convocação
* matrícula
* ficha de matrícula

Semana 4

* checklist
* dashboard
* auditoria

Semana 5

* testes
* correções
* implantação

---

# Conclusão técnica

Seu sistema é classificado como:

**Sistema de pequeno para médio porte (161 PF)**

Com:

* baixo risco técnico
* arquitetura simples
* esforço totalmente viável para 1 desenvolvedor
