# Documentação Técnica

**Arquivo:** `People Analytics Measures.qvs`  
**Última atualização:** 15/08/2025 09:44:07

# **Documentação do Script de Cálculo de Indicadores de Gestão de Pessoas**
*(Horas Extras, Absenteísmo e Banco de Horas)*

---

## **1. Introdução**
Este documento explica um script utilizado para calcular **indicadores relacionados à gestão de horas trabalhadas, absenteísmo e banco de horas** em uma organização. Esses indicadores ajudam a analisar:
- **Horas extras**: Quantidade, custos e impacto na remuneração.
- **Absenteísmo**: Faltas, atrasos, atestados e abonos, além de seus custos.
- **Banco de horas**: Saldo positivo/negativo e pagamentos realizados.

O script define **fórmulas (medidas)** que são usadas em relatórios ou painéis para apoiar decisões gerenciais.

---

## **2. Estrutura do Script**
O script está dividido em **três seções principais**, cada uma focada em um tipo de indicador:

1. **Horas Extras** – Cálculos sobre horas extras trabalhadas, custos e comparações com períodos anteriores.
2. **Absenteísmo** – Análise de faltas, atrasos, atestados e seus impactos financeiros.
3. **Banco de Horas** – Controle de saldos e pagamentos do banco de horas.

Cada seção começa com um **marcador (`TRACE`)** para facilitar a identificação no sistema.

---

## **3. Detalhamento das Medidas**

### **3.1. Horas Extras**
Esta seção calcula indicadores para entender **quando, quanto e como as horas extras são utilizadas**, além de seus custos e impacto na folha de pagamento.

#### **Principais Medidas e Seu Significado**

| **Medida**                          | **O que calcula**                                                                 | **Exemplo Prático**                                                                 |
|-------------------------------------|-----------------------------------------------------------------------------------|------------------------------------------------------------------------------------|
| **`horas_total_extras`**            | Total de horas extras registradas no período.                                     | Se 10 funcionários fizeram 2h extras cada, o total é **20 horas**.                |
| **`horas_extras_atual`**            | Horas extras no **mês atual** (comparado ao mês selecionado).                     | Em janeiro de 2024, foram registradas **50 horas extras**.                         |
| **`horas_extras_anterior`**         | Horas extras no **mesmo mês do ano anterior**.                                    | Em janeiro de 2023, foram **40 horas extras** (para comparar com 2024).           |
| **`custo_medio_he`**               | Custo médio por hora extra (valor total dividido pelas horas trabalhadas).         | Se R$ 2.000 foram pagos por 100h extras, o custo médio é **R$ 20/hora**.         |
| **`pessoas_com_registro_he`**      | Número de funcionários que registraram horas extras.                             | Se 50 de 200 funcionários fizeram hora extra, **25%** o fizeram.                 |
| **`%_HE_pessoas_elegiveis`**        | Percentual de funcionários **elegíveis** (que podem fazer hora extra) que o fizeram. | Se 80 são elegíveis e 50 fizeram, **62,5%** aproveitaram.                        |
| **`%_MoM_horas_extras`**           | Variação (%) das horas extras **mês a mês**.                                      | Se em dezembro foram 100h e em janeiro 120h, houve **aumento de 20%**.          |
| **`%_YoY_horas_extras`**           | Variação (%) das horas extras **ano a ano**.                                      | Se em janeiro/2023 foram 80h e em 2024 foram 100h, houve **aumento de 25%**.   |
| **`valor_evento_horas_extras`**     | Valor total pago em horas extras.                                                 | Se 100h extras custaram R$ 3.000, este é o valor total.                          |
| **`%_hora_extra_recorrente`**      | Percentual de horas extras **recorrentes** (previstas) vs. esporádicas.           | Se de R$ 3.000, R$ 2.000 são recorrentes, **66,6%** são recorrentes.              |

---

#### **Como as Comparações Funcionam**
Algumas medidas comparam períodos para identificar **tendências**:
- **`MoM` (Month-over-Month)**: Compara um mês com o mês anterior.
  - Exemplo: `%_MoM_horas_extras` mostra se as horas extras **aumentaram ou diminuíram** em relação ao mês passado.
- **`YoY` (Year-over-Year)**: Compara um período com o mesmo período do ano anterior.
  - Exemplo: `%_YoY_horas_extras` indica se as horas extras **cresceram ou caíram** em relação ao ano passado.

---

### **3.2. Absenteísmo**
Esta seção analisa **faltas, atrasos, atestados e abonos**, calculando seu impacto em horas perdidas e custos para a empresa.

#### **Principais Medidas e Seu Significado**

| **Medida**                          | **O que calcula**                                                                 | **Exemplo Prático**                                                                 |
|-------------------------------------|-----------------------------------------------------------------------------------|------------------------------------------------------------------------------------|
| **`dias_absenteismo`**              | Total de dias perdidos por **faltas, atrasos, atestados e abonos**.              | Se em um mês houve 10 faltas, 5 atrasos e 3 atestados, totaliza **18 dias**.       |
| **`%_indice_absenteismo`**          | Percentual de horas perdidas em relação à jornada total.                          | Se 200h foram perdidas em 8.000h de jornada, o índice é **2,5%**.                |
| **`dias_nao_planejados`**           | Dias perdidos por **faltas e atrasos** (exclui atestados e abonos).              | Se houve 10 faltas e 5 atrasos, totaliza **15 dias não planejados**.               |
| **`valor_eventos_faltas`**          | Custo total de **faltas e reembolsos**.                                           | Se faltas custaram R$ 5.000 à empresa, este é o valor.                            |
| **`%_MoM_absenteismo`**             | Variação (%) do absenteísmo **mês a mês**.                                        | Se em dezembro o índice foi 2% e em janeiro 3%, houve **aumento de 50%**.        |
| **`media_faltantes`**               | Média de dias perdidos **por funcionário com faltas/atrasos**.                    | Se 10 funcionários perderam 20 dias, a média é **2 dias por pessoa**.              |
| **`%_indice_abono`**               | Percentual de horas de **abono** em relação à jornada total.                      | Se 50h foram abonadas em 8.000h, o índice é **0,625%**.                           |

---

#### **Como os Dias de Absenteísmo São Calculados**
Algumas medidas convertem **horas perdidas em dias**, usando a seguinte lógica:
- **Fórmula**: `(Horas perdidas × 30) / Horas de jornada mensal por funcionário`.
  - Exemplo: Se um funcionário perdeu **8 horas** e sua jornada mensal é **200h**, o cálculo é:
    `(8 × 30) / 200 = 1,2 dias` (arredondado para **1 dia**).

---

### **3.3. Banco de Horas**
Esta seção gerencia o **saldo de horas** (positivo ou negativo) e os pagamentos realizados.

#### **Principais Medidas e Seu Significado**

| **Medida**                          | **O que calcula**                                                                 | **Exemplo Prático**                                                                 |
|-------------------------------------|-----------------------------------------------------------------------------------|------------------------------------------------------------------------------------|
| **`horas_total_saldo_banco`**       | Total de horas no **banco de horas** (positivas e negativas).                     | Se 50 funcionários têm +10h e 20 têm -5h, o total é **+300h**.                    |
| **`horas_total_saldo_banco_positivo`** | Horas **positivas** (a favor do funcionário).                                   | Se 100 funcionários têm +8h cada, totaliza **+800h**.                             |
| **`valor_evento_saldo_banco_pago`** | Valor pago em **março e setembro** (períodos de pagamento do banco).              | Se em março foram pagas 200h a R$ 30/hora, o valor é **R$ 6.000**.                |
| **`%_colaboradores_com_saldo_banco`** | Percentual de funcionários **com saldo no banco de horas**.                     | Se 150 de 500 funcionários têm saldo, **30%** estão nesta situação.                |
| **`%_MAR_SET_pgt_banco`**          | Variação (%) no pagamento do banco de horas **entre março e setembro**.           | Se em março/2023 foram pagos R$ 5.000 e em setembro R$ 7.000, houve **aumento de 40%**. |

---

#### **Pagamento do Banco de Horas**
O pagamento do saldo do banco de horas ocorre **duas vezes por ano (março e setembro)**. A medida `%_MAR_SET_pgt_banco` calcula:
- **Quanto foi pago neste período** vs. **o mesmo período 6 meses antes**.
- **Exemplo**:
  - Em **março/2024**, foram pagos R$ 10.000.
  - Em **setembro/2023**, foram pagos R$ 8.000.
  - A variação é: `(10.000 - 8.000) / 8.000 = 25%` (aumento).

---

## **4. Como as Medidas São Usadas**
As medidas definidas neste script são utilizadas em:
- **Relatórios gerenciais**: Para acompanhar custos com horas extras e absenteísmo.
- **Painéis (dashboards)**: Gráficos que mostram tendências (ex.: aumento de faltas).
- **Tomada de decisão**: Identificar se é necessário:
  - Reduzir horas extras (se custos estão altos).
  - Investigar causas de absenteísmo (se índices subiram).
  - Ajustar políticas de banco de horas (se saldos estão muito negativos).

---

## **5. Exemplo Prático de Aplicação**
**Cenário**: Uma empresa quer analisar suas **horas extras em janeiro/2024**.

| **Medida**               | **Valor em Jan/2024** | **Valor em Jan/2023** | **Análise**                                                                 |
|--------------------------|-----------------------|-----------------------|-----------------------------------------------------------------------------|
| `horas_total_extras`      | 150h                  | 120h                  | **Aumento de 30h (25%)** em relação ao ano anterior.                       |
| `custo_medio_he`         | R$ 25/hora            | R$ 20/hora            | O custo por hora extra **subiu R$ 5 (25%)**.                                |
| `%_HE_pessoas_elegiveis` | 60%                   | 50%                   | Mais funcionários estão fazendo hora extra (**aumento de 10%**).           |
| `valor_evento_horas_extras` | R$ 3.750           | R$ 2.400              | **Aumento de R$ 1.350 (56%)** no gasto com horas extras.                   |

**Ação sugerida (hipotética)**:
- Investigar por que mais pessoas estão fazendo hora extra.
- Verificar se o aumento de custo é justificado (ex.: demanda sazonal).

---

## **6. Considerações Finais**
- O script **não altera dados**, apenas define **fórmulas para cálculos**.
- As medidas são **dinâmicas**: mudam conforme os dados são atualizados (ex.: novos registros de horas extras).
- Algumas medidas usam **filtros de data** para comparar períodos específicos (mês atual vs. mês anterior, ano atual vs. ano anterior).

---
**Fim da Documentação**
