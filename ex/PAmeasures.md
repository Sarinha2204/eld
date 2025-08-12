# Documentação Técnica

**Arquivo:** `People Analytics Measures.qvs`  
**Última atualização:** 12/08/2025 08:54:28

## Documentação Técnica do Script QlikView: People Analytics Measures.qvs

**1. Introdução**

**Nome do Arquivo:** People Analytics Measures.qvs

**Data e Hora da Última Atualização:**  A data e hora variam de acordo com a versão do script.  Referenciar a data presente no próprio script.

**Objetivo:** Este script QlikView calcula e carrega diversas métricas de People Analytics a partir da tabela de dados `gd_eventos_f`.  O foco principal são métricas de horas extras, absenteísmo e saldo de horas (banco de horas).  Utiliza comandos `SET` para definir variáveis que armazenam resultados intermediários e métricas finais.  Realiza cálculos de totais, médias, porcentagens e variações percentuais mês a mês (MoM) e ano a ano (YoY). O comando `TRACE` auxilia na depuração.


**2. Principais Etapas:**

O script está dividido em seções, cada uma calculando um conjunto específico de métricas:

* **2.1 Definição de Variáveis:** Define um extenso conjunto de variáveis usando comandos `SET`.  Estas variáveis armazenam resultados intermediários e as métricas finais calculadas posteriormente. Os nomes das variáveis geralmente indicam a métrica (ex: `horas_total_extras`, `custo_medio_he`, `dias_absenteismo`, `%_indice_absenteismo`, etc.).

* **2.2 Cálculo de Métricas de Horas Extras:** Calcula diversas métricas de horas extras, utilizando a tabela `gd_eventos_f` e filtrando eventos do tipo "Hora extra". As expressões combinam funções de agregação com filtros em campos como `tipo_evento`, `flag_hora_extra`, `nome_conta_debito`, `grupo_relatorio`, e `gd_eventos_f.load_date`.  As métricas calculadas incluem totais de horas extras, custos (totais e médios, por pessoa), média de horas extras por pessoa, número de funcionários elegíveis e inelegíveis, vários percentuais relacionados a horas extras, variações percentuais MoM e YoY de custos e horas extras, e valores monetários associados aos eventos de hora extra.  Variáveis como `horas_total_extras`, `custo_medio_he`, `media_he`, `pessoas_elegiveis_he`, `%_HE_pessoas_elegiveis`, `%_MoM_horas_extras`, `%_YoY_custo_medio_he` e outras são calculadas nesta seção.

* **2.3 Cálculo de Métricas de Absenteísmo:** Calcula métricas de absenteísmo considerando diferentes tipos de ausências na tabela `gd_eventos_f` (faltas, atestados, abonos, reembolsos, atrasos). A lógica utiliza filtros sobre `tipo_evento`, `flag_horas_nao_planejadas`, `grupo_relatorio` e `gd_eventos_f.load_date`.  As métricas incluem totais de dias e horas de absenteísmo, taxas de absenteísmo, comparações anuais e mensais das taxas de absenteísmo (MoM e YoY), valores monetários associados a eventos de falta e indicadores específicos para abonos.  Variáveis como `dias_absenteismo`, `%_indice_absenteismo`, `%_MoM_absenteismo`, `%_YoY_absenteismo`, `valor_eventos_faltas` e outras são calculadas aqui.

* **2.4 Cálculo de Métricas de Saldo de Horas (Banco de Horas):** Calcula métricas relacionadas ao banco de horas, filtrando eventos do tipo "Saldo Banco" na tabela `gd_eventos_f`. Os cálculos usam filtros em `tipo_evento`, `descricao_evento`, `codigo_evento` e `mes_nome`.  As métricas incluem o total de horas no banco de horas, saldo positivo e negativo, percentual de colaboradores com saldo no banco de horas e valor do saldo pago em março e setembro. Variáveis como `horas_total_saldo_banco`, `%_colaboradores_com_saldo_banco`, `valor_evento_saldo_banco_pago` e outras são calculadas.

* **2.5 Uso de Comandos `TRACE`:** O script usa o comando `TRACE` para marcar o início de cada seção, facilitando a depuração.

* **2.6 Finalização do Script:** O script termina com o comando `EXIT SCRIPT`.


**3. Observações:**

* O script utiliza expressões complexas dentro dos comandos `SET`, combinando funções de agregação (como `Sum`, `Count`, `Avg`) e funções de data do QlikView (como `Date`, `AddMonths`, `YearStart`, `YearEnd`, `MonthStart`, `MonthEnd`, `AddYears`). O formato de data utilizado parece ser "DD.MM.YYYY".
* As comparações YoY e MoM são baseadas em seleções de data, usando a função `Only(GetFieldSelections(gd_eventos_f.load_date))` para determinar o período nos cálculos.
* A lógica de cálculo das variáveis é complexa e requer análise detalhada do código fonte.
* A estrutura modular, com seções distintas para cada tipo de métrica, facilita a manutenção e a adição de novas métricas.


**4. Considerações Finais:**

Esta documentação fornece uma visão geral do script. Para uma compreensão completa, é necessária uma análise detalhada do código fonte e da estrutura da tabela `gd_eventos_f`. A complexidade das expressões exige análise cuidadosa.  Comentários e a tag `GEMINI 2.0 FLASH` presentes no código também auxiliam na compreensão.

# Documentação Técnica

**Arquivo:** `People Analytics Measures.qvs`  
**Última atualização:** 07/08/2025 14:40:08

# Documentação Técnica do Script QlikView: People Analytics Measures.qvs

**1. Introdução**

**Nome do Arquivo:** People Analytics Measures.qvs

**Data e Hora da Última Atualização:** 07/08/2025 (A data e hora podem variar dependendo da versão do script. Utilizar a data presente no próprio script como referência.)

**Objetivo:** Este script QlikView calcula e carrega diversas métricas de People Analytics a partir da tabela de dados `gd_eventos_f`. O foco principal é o cálculo de métricas relacionadas a horas extras, absenteísmo e saldo de horas (banco de horas).  O script utiliza comandos `SET` para definir variáveis que armazenam os resultados intermediários e as métricas finais, realizando cálculos de totais, médias, porcentagens e variações percentuais mês a mês (MoM) e ano a ano (YoY). O comando `TRACE` é usado para auxiliar na depuração.


**2. Principais Etapas**

O script está dividido em seções distintas, cada uma responsável por calcular um conjunto específico de métricas:

* **2.1 Definição de Variáveis:** A primeira etapa define um extenso conjunto de variáveis usando comandos `SET`. Essas variáveis armazenam resultados intermediários e as métricas finais calculadas posteriormente no script. Os nomes das variáveis geralmente indicam a métrica calculada (ex: `horas_total_extras`, `custo_medio_he`, `dias_absenteismo`, `%_indice_absenteismo`, etc.).

* **2.2 Cálculo de Métricas de Horas Extras:** Esta seção calcula diversas métricas relacionadas a horas extras, utilizando a tabela `gd_eventos_f` e filtrando eventos do tipo "Hora extra". As expressões utilizadas combinam funções de agregação com filtros baseados em campos como `tipo_evento`, `flag_hora_extra`, `nome_conta_debito`, `grupo_relatorio`, e `gd_eventos_f.load_date`.  São calculadas métricas como totais de horas extras, custos totais e médios, média de horas extras por pessoa, número de funcionários elegíveis e inelegíveis, vários percentuais relacionados a horas extras, variações percentuais MoM e YoY de custos e horas extras e valores monetários associados aos eventos de hora extra.

* **2.3 Cálculo de Métricas de Absenteísmo:** Esta seção calcula métricas de absenteísmo, considerando diferentes tipos de ausências na tabela `gd_eventos_f` (faltas, atestados, abonos, reembolsos, atrasos). A lógica utiliza filtros sobre `tipo_evento`, `flag_horas_nao_planejadas`, `grupo_relatorio` e `gd_eventos_f.load_date`. São calculadas métricas como totais de dias e horas de absenteísmo, taxas de absenteísmo, comparações anuais e mensais das taxas de absenteísmo (MoM e YoY), valores monetários associados a eventos de falta e indicadores específicos para abonos.

* **2.4 Cálculo de Métricas de Saldo de Horas (Banco de Horas):** Esta seção calcula métricas relacionadas ao banco de horas, filtrando eventos do tipo "Saldo Banco" na tabela `gd_eventos_f`. Os cálculos utilizam filtros em `tipo_evento`, `descricao_evento`, `codigo_evento` e `mes_nome`. As métricas calculadas incluem total de horas no banco de horas, saldo positivo e negativo, percentual de colaboradores com saldo no banco de horas e valor do saldo pago em março e setembro.

* **2.5 Uso de Comandos `TRACE`:** O script utiliza o comando `TRACE` para marcar o início de cada seção, facilitando a depuração e o acompanhamento da execução do script.

* **2.6 Finalização do Script:** O script termina com o comando `EXIT SCRIPT`.


**3. Observações:**

* O script utiliza expressões complexas dentro dos comandos `SET`, combinando funções de agregação (como `Sum`, `Count`, `Avg`) e funções de data do QlikView (como `Date`, `AddMonths`, `YearStart`, `YearEnd`, `MonthStart`, `MonthEnd`, `AddYears`). O formato de data utilizado parece ser "DD.MM.YYYY".
* As comparações YoY e MoM são baseadas em seleções de data, usando a função `Only(GetFieldSelections(gd_eventos_f.load_date))` para determinar o período nos cálculos.
* A lógica de cálculo das variáveis é complexa e requer análise detalhada do código fonte para total compreensão.
* A estrutura modular, com seções distintas para cada tipo de métrica, facilita a manutenção e a adição de novas métricas.


**4. Considerações Finais:**

Esta documentação fornece uma visão geral do script. Para uma compreensão completa, é necessária uma análise detalhada do código fonte e da estrutura da tabela `gd_eventos_f`. A complexidade das expressões exige análise cuidadosa.  A documentação presente no próprio código (como comentários e a tag `GEMINI 2.0 FLASH`) também auxilia na compreensão.

# Documentação Técnica

**Arquivo:** `People Analytics Measures.qvs`  
**Última atualização:** 07/08/2025 14:34:11

## Documentação Técnica do Script QlikView: People Analytics Measures.qvs

**Nome do Arquivo:** People Analytics Measures.qvs

**Data e Hora da Última Atualização:** 07/08/2025 (A data e hora podem variar dependendo da versão do script. Utilizar a data presente no próprio script como referência.)


**1. Resumo:**

Este script QlikView calcula e carrega diversas métricas de People Analytics a partir da tabela de dados `gd_eventos_f`. O foco principal é o cálculo de métricas relacionadas a horas extras, absenteísmo e saldo de horas (banco de horas). O script utiliza comandos `SET` para definir variáveis que armazenam os resultados intermediários e as métricas finais, realizando cálculos de totais, médias, porcentagens e variações percentuais mês a mês (MoM) e ano a ano (YoY).  O comando `TRACE` é usado para auxiliar na depuração.


**2. Principais Etapas:**

O script está dividido em seções distintas, cada uma responsável por calcular um conjunto específico de métricas:

* **2.1 Definição de Variáveis:** A primeira etapa define um extenso conjunto de variáveis usando comandos `SET`.  Essas variáveis armazenam resultados intermediários e as métricas finais calculadas posteriormente no script.  Os nomes das variáveis geralmente indicam a métrica calculada (ex: `horas_total_extras`, `custo_medio_he`, `dias_absenteismo`, `%_indice_absenteismo`, etc.).

* **2.2 Cálculo de Métricas de Horas Extras:** Esta seção calcula diversas métricas relacionadas a horas extras, utilizando a tabela `gd_eventos_f` e filtrando eventos do tipo "Hora extra". As expressões utilizadas combinam funções de agregação com filtros baseados em campos como `tipo_evento`, `flag_hora_extra`, `nome_conta_debito`, `grupo_relatorio`, e `gd_eventos_f.load_date`. As métricas calculadas incluem:
    * Totais de horas extras (`horas_total_extras`, `horas_extras_atual`, `horas_extras_anterior`).
    * Custos totais e médios de horas extras (`custo_medio_he`, `custo_medio_he_ano_anterior`, `custo_medio_he_ano_atual`, `custo_medio_por_pessoa_he`).
    * Média de horas extras por pessoa (`media_he`).
    * Número de funcionários elegíveis e inelegíveis para horas extras (`pessoas_elegiveis_he`, `pessoas_inelegiveis_he`, `pessoas_com_registro_he`).
    * Vários percentuais relacionados a horas extras (`%_HE_pessoas_elegiveis`, `%_HE_pessoas_inelegiveis`, `%_HE_remuneracao_total`, `%_hora_extra_esporadica`, `%_hora_extra_recorrente`, `%_HE_total_horas_trabalhadas`).
    * Variações percentuais mês a mês (MoM) e ano a ano (YoY) de custos e horas extras (`%_MoM_horas_extras_custo_medio_he`, `%_YoY_custo_medio_he`, `%_YoY_horas_extras_valor`, `%_YoY_hora_extra`, `%_MoM_horas_extras`, `%MoM_hora_extra_valor`).
    * Valores monetários associados aos eventos de hora extra (`valor_evento_horas_extras`, `valor_eventos_horas_extras_ano_atual`, `valor_eventos_horas_extras_ano_anterior`, `valor_evento_hora_extra_recorrente`, `valor_evento_horas_extras_anterior`, `valor_evento_horas_extras_atual`, `valor_evento_hora_extra_grafico`).

* **2.3 Cálculo de Métricas de Absenteísmo:** Esta seção calcula métricas de absenteísmo, considerando diferentes tipos de ausências na tabela `gd_eventos_f` (faltas, atestados, abonos, reembolsos, atrasos). A lógica utiliza filtros sobre `tipo_evento`, `flag_horas_nao_planejadas`, `grupo_relatorio` e `gd_eventos_f.load_date`. As métricas calculadas incluem:
    * Totais de dias e horas de absenteísmo para cada tipo de ausência (`dias_absenteismo`, `dias_nao_planejados`, `dias_abonos`, `dias_atestado`, `dias_faltas`, `dias_reembolso`, `dia_atraso`, `eventos_absenteismo`, `horas_total_absenteismo`, `horas_nao_planejadas`, `horas_total_abonos`).
    * Taxas de absenteísmo (geral e para ausências não planejadas) (`%_indice_absenteismo`, `%_indice_horas_nao_planejadas`).
    * Comparações anuais e mensais das taxas de absenteísmo (MoM e YoY) (`%_indice_absenteismo_ano_anterior`, `%_indice_absenteismo_ano_atual`, `%_indice_absenteismo_nao_planejado_ano_anterior`, `%_indice_absenteismo_nao_planejado_ano_atual`, `%_MoM_absenteismo`, `%_YoY_absenteismo`, `%_YoY_horas_nao_planejadas`, `%_MoM_horas_nao_planejadas`, `%_horas_nao_planejadas_tabela_atual`, `%_horas_nao_planejadas_tabela_ant`, `%_YoY_horas_nao_planejadas_tabela`).
    * Valores monetários associados a eventos de falta (`valor_eventos_faltas`, `valor_eventos_falta_ano_atual`, `valor_eventos_falta_ano_anterior`, `valor_evento_faltas_operacional`, `valor_evento_faltas_nao_operacional`, `%_MoM_valor_total_faltas`, `%_YoY_valor_total_faltas`, `valor_evento_falta_grafico`).
    * Indicadores específicos para abonos (`%_indice_abono`, `%_indice_abono_ano_atual`, `%_indice_abono_ano_anterior`, `%YoY_indice_abono`, `%MoM_indice_abono`, `%_abonos_atual_grafico`, `%_abono_anterior_grafico`).


* **2.4 Cálculo de Métricas de Saldo de Horas (Banco de Horas):** Esta seção calcula métricas relacionadas ao banco de horas, filtrando eventos do tipo "Saldo Banco" na tabela `gd_eventos_f`. Os cálculos utilizam filtros em `tipo_evento`, `descricao_evento`, `codigo_evento` e `mes_nome`. As métricas incluem:
    * Total de horas no banco de horas (`horas_total_saldo_banco`).
    * Saldo positivo e negativo de horas (`horas_total_saldo_banco_positivo`, `horas_total_saldo_banco_negativo`).
    * Percentual de colaboradores com saldo no banco de horas (`%_colaboradores_com_saldo_banco`).
    * Valor do saldo pago em março e setembro (`valor_evento_saldo_banco_pago`, `%_MAR_SET_pgt_banco`).

* **2.5 Uso de Comandos `TRACE`:** O script utiliza o comando `TRACE` para marcar o início de cada seção, facilitando a depuração e o acompanhamento da execução do script.

* **2.6 Finalização do Script:** O script termina com o comando `EXIT SCRIPT`.


**3. Observações:**

* O script utiliza expressões complexas dentro dos comandos `SET`, combinando funções de agregação (como `Sum`, `Count`, `Avg`) e funções de data do QlikView (como `Date`, `AddMonths`, `YearStart`, `YearEnd`, `MonthStart`, `MonthEnd`, `AddYears`). O formato de data utilizado parece ser "DD.MM.YYYY".
* As comparações YoY e MoM são baseadas em seleções de data, usando a função `Only(GetFieldSelections(gd_eventos_f.load_date))` para determinar o período nos cálculos.
* A lógica de cálculo das variáveis é complexa e requer análise detalhada do código fonte para total compreensão.
* A estrutura modular, com seções distintas para cada tipo de métrica, facilita a manutenção e a adição de novas métricas.


**4. Considerações Finais:**

Esta documentação fornece uma visão geral do script. Para uma compreensão completa, é necessária uma análise detalhada do código fonte e da estrutura da tabela `gd_eventos_f`. A complexidade das expressões exige análise cuidadosa. A documentação presente no próprio código (como comentários e a tag `GEMINI 2.0 FLASH`) também auxilia na compreensão.

# Documentação Técnica

**Arquivo:** `People Analytics Measures.qvs`  
**Última atualização:** 07/08/2025 14:26:31

## Documentação Técnica do Script QlikView: People Analytics Measures.qvs

**1. Introdução**

**Nome do Arquivo:** People Analytics Measures.qvs

**Data e Hora da Última Atualização:** 07/08/2025 (A data e hora podem variar dependendo da versão do script. Utilizar a data presente no próprio script como referência.)

**Objetivo:** Este script QlikView calcula e carrega diversas métricas de People Analytics a partir da tabela de dados `gd_eventos_f`.  O foco principal é o cálculo de métricas relacionadas a horas extras, absenteísmo e saldo de horas (banco de horas).  O script utiliza comandos `SET` para definir variáveis que armazenam os resultados intermediários e as métricas finais, realizando cálculos de totais, médias, porcentagens e variações percentuais mês a mês (MoM) e ano a ano (YoY). O comando `TRACE` é usado para auxiliar na depuração.


**2. Principais Etapas**

O script está dividido em seções distintas, cada uma responsável por calcular um conjunto específico de métricas:

* **2.1 Definição de Variáveis:**  A primeira etapa consiste na definição de um conjunto extenso de variáveis usando comandos `SET`. Essas variáveis armazenam resultados intermediários e as métricas finais calculadas posteriormente no script.  Os nomes das variáveis geralmente indicam a métrica calculada (ex: `horas_total_extras`, `custo_medio_he`, `dias_absenteismo`, `%_indice_absenteismo`, etc.).

* **2.2 Cálculo de Métricas de Horas Extras:** Esta seção calcula diversas métricas relacionadas a horas extras, utilizando a tabela `gd_eventos_f` e filtrando eventos do tipo "Hora extra".  As expressões utilizadas combinam funções de agregação com filtros baseados em campos como `tipo_evento`, `flag_hora_extra`, `nome_conta_debito`, `grupo_relatorio`, e `gd_eventos_f.load_date`.  As métricas calculadas incluem:
    * Totais de horas extras.
    * Custos totais e médios de horas extras, com valores separados para ano anterior e ano atual, e média por pessoa.
    * Média de horas extras por pessoa.
    * Número de funcionários elegíveis e inelegíveis para horas extras.
    * Vários percentuais relacionados a horas extras (ex: percentual de horas extras em relação à remuneração total, percentual de horas extras esporádicas e recorrentes).
    * Variações percentuais mês a mês (MoM) e ano a ano (YoY) de custos e horas extras.
    * Valores monetários associados aos eventos de hora extra.


* **2.3 Cálculo de Métricas de Absenteísmo:**  Esta seção calcula métricas de absenteísmo, considerando diferentes tipos de ausências na tabela `gd_eventos_f` (faltas, atestados, abonos, reembolsos, atrasos).  A lógica utiliza filtros sobre `tipo_evento`, `flag_horas_nao_planejadas`, `grupo_relatorio` e `gd_eventos_f.load_date`. As métricas calculadas incluem:
    * Totais de dias e horas de absenteísmo para cada tipo de ausência.
    * Taxas de absenteísmo (geral e para ausências não planejadas).
    * Comparações anuais e mensais das taxas de absenteísmo (MoM e YoY).
    * Valores monetários associados a eventos de falta, com separação entre eventos operacionais e não operacionais e comparações MoM e YoY.
    * Indicadores específicos para abonos, com comparações MoM e YoY.

* **2.4 Cálculo de Métricas de Saldo de Horas (Banco de Horas):** Esta seção calcula métricas relacionadas ao banco de horas, filtrando eventos do tipo "Saldo Banco" na tabela `gd_eventos_f`.  Os cálculos utilizam filtros em `tipo_evento`, `descricao_evento`, `codigo_evento` e `mes_nome`. As métricas incluem:
    * Total de horas no banco de horas.
    * Saldo positivo e negativo de horas.
    * Percentual de colaboradores com saldo no banco de horas.
    * Valor do saldo pago em março e setembro.

* **2.5 Uso de Comandos `TRACE`:**  O script utiliza o comando `TRACE` para marcar o início de cada seção, facilitando a depuração e o acompanhamento da execução do script.

* **2.6 Finalização do Script:** O script termina com o comando `EXIT SCRIPT`.


**3. Observações**

* O script utiliza expressões complexas dentro dos comandos `SET`, combinando funções de agregação (como `Sum`, `Count`, `Avg`) e funções de data do QlikView (como `Date`, `AddMonths`, `YearStart`, `YearEnd`, `MonthStart`, `MonthEnd`, `AddYears`). O formato de data utilizado parece ser "DD.MM.YYYY".
* As comparações YoY e MoM são baseadas em seleções de data, usando a função `Only(GetFieldSelections(gd_eventos_f.load_date))` para determinar o período nos cálculos.
* A lógica de cálculo das variáveis é complexa e requer análise detalhada do código fonte para total compreensão.
* A estrutura modular, com seções distintas para cada tipo de métrica, facilita a manutenção e a adição de novas métricas.


**4. Considerações Finais**

Esta documentação fornece uma visão geral do script. Para uma compreensão completa, é necessária uma análise detalhada do código fonte e da estrutura da tabela `gd_eventos_f`.  A complexidade das expressões exige análise cuidadosa. A documentação presente no próprio código (como comentários e a tag `GEMINI 2.0 FLASH`) também auxilia na compreensão.

Documentação Técnica
Arquivo: People Analytics Measures.qvs
Última atualização: 07/08/2025 13:49:45

## Documentação Técnica do Script QlikView: People Analytics Measures.qvs

**Nome do Arquivo:** People Analytics Measures.qvs

**Data e Hora da Última Atualização:** 07/08/2025 (A data e hora podem variar dependendo da versão do script.  Utilizar a data presente no próprio script como referência.)


**1. Resumo:**

Este script QlikView calcula e carrega diversas métricas de People Analytics a partir da tabela de dados `gd_eventos_f`. O script foca no cálculo de métricas relacionadas a horas extras, absenteísmo e saldo de horas (banco de horas).  Utiliza comandos `SET` para definir variáveis que armazenam resultados intermediários e as métricas finais.  Calcula totais, médias, porcentagens e variações percentuais mês a mês (MoM) e ano a ano (YoY) para cada área.  O comando `TRACE` é usado para auxiliar na depuração, marcando o início de cada seção.


**2. Principais Etapas:**

* **2.1 Definição de Variáveis:** O script começa definindo um conjunto de variáveis usando comandos `SET`. Essas variáveis armazenam resultados intermediários e as métricas finais calculadas posteriormente.  As variáveis incluem totais de horas extras, custos médios de horas extras, dias de absenteísmo, taxas de absenteísmo, saldo de horas no banco de horas, e diversas outras métricas, incluindo variações MoM e YoY.

* **2.2 Cálculo de Métricas de Horas Extras:**  Esta seção calcula várias métricas de horas extras, usando a tabela `gd_eventos_f` e filtrando eventos do tipo "Hora extra".  Os cálculos incluem:
    * Total de horas extras.
    * Custos totais e médios de horas extras (incluindo valores separados para ano anterior e ano atual, e média por pessoa).
    * Média de horas extras por pessoa.
    * Número de funcionários elegíveis e inelegíveis para horas extras.
    * Vários percentuais relacionados a horas extras (ex: percentual de horas extras em relação à remuneração total, percentual de horas extras esporádicas e recorrentes).
    * Variações percentuais mês a mês (MoM) e ano a ano (YoY) de custos e horas extras.
    * Valores monetários associados aos eventos de hora extra.

* **2.3 Cálculo de Métricas de Absenteísmo:** Esta seção calcula métricas de absenteísmo, considerando diferentes tipos de ausências na tabela `gd_eventos_f` (faltas, atestados, abonos, reembolsos, atrasos). As métricas incluem:
    * Totais de dias e horas de absenteísmo para cada tipo de ausência.
    * Taxas de absenteísmo (geral e para ausências não planejadas).
    * Comparações anuais e mensais das taxas de absenteísmo (MoM e YoY).
    * Valores monetários associados a eventos de falta, com separação entre eventos operacionais e não operacionais e comparações MoM e YoY.
    * Indicadores específicos para abonos, com comparações MoM e YoY.

* **2.4 Cálculo de Métricas de Saldo de Horas (Banco de Horas):**  Esta seção calcula métricas relacionadas ao banco de horas, filtrando eventos do tipo "Saldo Banco" na tabela `gd_eventos_f`.  As métricas incluem:
    * Total de horas no banco de horas.
    * Saldo positivo e negativo de horas.
    * Percentual de colaboradores com saldo no banco de horas.
    * Valor do saldo pago em março e setembro.

* **2.5 Uso de Comandos `TRACE`:** O script utiliza o comando `TRACE` para indicar o início de cada seção, facilitando a depuração.

* **2.6 Finalização do Script:** O script termina com o comando `EXIT SCRIPT`.


**3. Observações:**

* O script usa expressões complexas dentro dos comandos `SET`, combinando funções de agregação e funções de data do QlikView. O formato de data utilizado parece ser "DD.MM.YYYY".
* As comparações YoY e MoM são baseadas em seleções de data, usando a função `Only(GetFieldSelections(gd_eventos_f.load_date))` para determinar o período nos cálculos.
* A lógica de cálculo das variáveis é complexa, envolvendo múltiplas condições e agregações.
* A estrutura modular, com seções distintas para cada tipo de métrica, facilita a manutenção e a adição de novas métricas.


**4. Considerações Finais:**

Esta documentação fornece uma visão geral do script.  Para uma compreensão completa, é necessária uma análise detalhada do código fonte e da estrutura da tabela `gd_eventos_f`. A complexidade das expressões exige análise cuidadosa. A documentação presente no próprio código (como comentários e a tag `GEMINI 2.0 FLASH`) também auxilia na compreensão.

Documentação Técnica
Arquivo: People Analytics Measures.qvs
Última atualização: 07/08/2025 13:25:12
## Documentação Técnica do Script QlikView: People Analytics Measures.qvs

**Nome do Arquivo:** People Analytics Measures.qvs

**Data e Hora da Última Atualização:** 07/08/2025 (A data e hora podem variar dependendo da versão do script)


**1. Resumo:**

Este script QlikView carrega e calcula diversas métricas de People Analytics a partir de uma tabela de dados chamada `gd_eventos_f`.  O foco principal está no cálculo de métricas relacionadas a horas extras, absenteísmo e saldo de horas (banco de horas).  O script utiliza comandos `SET` para definir variáveis que armazenam os resultados intermediários e as métricas finais.  Ele calcula totais, médias, porcentagens e variações percentuais mês a mês (MoM) e ano a ano (YoY) para cada área.  O comando `TRACE` é utilizado para auxiliar na depuração, indicando o início de cada seção do script.


**2. Principais Etapas:**

* **2.1 Definição de Variáveis:** O script inicia com a definição de um extenso conjunto de variáveis usando comandos `SET`. Essas variáveis armazenam resultados intermediários e as métricas finais calculadas posteriormente no script.  Exemplos incluem totais de horas extras, custos médios de horas extras, dias de absenteísmo, taxas de absenteísmo, saldo de horas no banco de horas, e diversas outras métricas calculadas a partir de variações MoM e YoY.

* **2.2 Cálculo de Métricas de Horas Extras:** Esta seção calcula diversas métricas relacionadas a horas extras, utilizando a tabela `gd_eventos_f` e filtrando eventos do tipo "Hora extra". Os cálculos incluem:
    * Total de horas extras (`horas_total_extras`).
    * Custos totais e médios de horas extras (`custo_medio_he`, `custo_medio_he_ano_anterior`, `custo_medio_he_ano_atual`, `custo_medio_por_pessoa_he`).
    * Média de horas extras por pessoa (`media_he`).
    * Número de funcionários elegíveis e inelegíveis para horas extras (`pessoas_elegiveis_he`, `pessoas_inelegiveis_he`, `pessoas_com_registro_he`).
    * Vários percentuais relacionados a horas extras (por exemplo, percentual de horas extras em relação à remuneração total, percentual de horas extras esporádicas e recorrentes) (`%_HE_pessoas_elegiveis`, `%_HE_pessoas_inelegiveis`, `%_HE_remuneracao_total`, `%_hora_extra_esporadica`, `%_hora_extra_recorrente`, `%_HE_total_horas_trabalhadas`).
    * Variações percentuais mês a mês (MoM) e ano a ano (YoY) em relação aos custos e horas extras (`%_MoM_horas_extras_custo_medio_he`, `%_YoY_custo_medio_he`, `%_YoY_horas_extras_valor`, `%_YoY_hora_extra`, `%_MoM_horas_extras`, `%MoM_hora_extra_valor`).
    * Valores monetários associados a eventos de hora extra (`valor_evento_horas_extras`, `valor_eventos_horas_extras_ano_atual`, `valor_eventos_horas_extras_ano_anterior`, `valor_evento_hora_extra_recorrente`, `valor_evento_horas_extras_anterior`, `valor_evento_horas_extras_atual`, `valor_evento_hora_extra_grafico`).


* **2.3 Cálculo de Métricas de Absenteísmo:**  Esta seção calcula métricas de absenteísmo, considerando diferentes tipos de ausências (faltas, atestados, abonos, reembolsos e atrasos) presentes na tabela `gd_eventos_f`.  As métricas incluem:
    * Totais de dias e horas de absenteísmo para cada tipo de ausência (`dias_absenteismo`, `dias_nao_planejados`, `dias_abonos`, `dias_atestado`, `dias_faltas`, `dias_reembolso`, `dia_atraso`, `eventos_absenteismo`, `horas_total_absenteismo`, `horas_nao_planejadas`, `horas_total_abonos`).
    * Taxas de absenteísmo (global e para ausências não planejadas) (`%_indice_absenteismo`, `%_indice_horas_nao_planejadas`).
    * Comparação anual e mensal das taxas de absenteísmo (MoM e YoY) (`%_indice_absenteismo_ano_anterior`, `%_indice_absenteismo_ano_atual`, `%_indice_absenteismo_nao_planejado_ano_anterior`, `%_indice_absenteismo_nao_planejado_ano_atual`, `%_MoM_absenteismo`, `%_YoY_absenteismo`, `%_YoY_horas_nao_planejadas`, `%_MoM_horas_nao_planejadas`, `%_horas_nao_planejadas_tabela_atual`, `%_horas_nao_planejadas_tabela_ant`, `%_YoY_horas_nao_planejadas_tabela`).
    * Valores monetários associados a eventos de falta (`valor_eventos_faltas`, `valor_eventos_falta_ano_atual`, `valor_eventos_falta_ano_anterior`, `valor_evento_faltas_operacional`, `valor_evento_faltas_nao_operacional`, `%_MoM_valor_total_faltas`, `%_YoY_valor_total_faltas`, `valor_evento_falta_grafico`).
    * Indicadores específicos para abonos, com comparações MoM e YoY (`%_indice_abono`, `%_indice_abono_ano_atual`, `%_indice_abono_ano_anterior`, `%YoY_indice_abono`, `%MoM_indice_abono`, `%_abonos_atual_grafico`, `%_abono_anterior_grafico`).

* **2.4 Cálculo de Métricas de Saldo de Horas (Banco de Horas):** Esta seção calcula métricas relacionadas ao banco de horas, filtrando eventos do tipo "Saldo Banco" na tabela `gd_eventos_f`:
    * Total de horas no banco de horas (`horas_total_saldo_banco`).
    * Saldo positivo e negativo de horas (`horas_total_saldo_banco_positivo`, `horas_total_saldo_banco_negativo`).
    * Percentual de colaboradores com saldo no banco de horas (`%_colaboradores_com_saldo_banco`).
    * Valor do saldo pago em março e setembro (`valor_evento_saldo_banco_pago`, `%_MAR_SET_pgt_banco`).

* **2.5 Uso de Comandos `TRACE`:** O script utiliza o comando `TRACE` para marcar o início de cada seção, facilitando a depuração e o monitoramento da execução.

* **2.6 Finalização do Script:** O script termina com o comando `EXIT SCRIPT`.


**3. Observações:**

* O script utiliza expressões complexas dentro dos comandos `SET`, combinando funções de agregação e funções de data do QlikView.  O formato de data aparentemente utilizado é "DD.MM.YYYY".
* As comparações YoY e MoM são baseadas em seleções de data, usando a função `Only(GetFieldSelections(gd_eventos_f.load_date))` para determinar o período de tempo considerado nos cálculos.
* A lógica de cálculo das variáveis é intrincada, envolvendo múltiplas condições e agregações.
* A estrutura modular, com seções distintas para cada tipo de métrica, facilita a manutenção e a adição de novas métricas.

**4. Considerações Finais:**

Esta documentação apresenta uma visão geral do script. Para uma compreensão completa, é necessário analisar o código fonte detalhadamente, juntamente com a estrutura e o conteúdo da tabela de origem `gd_eventos_f`. A complexidade das expressões calculadas exige análise cuidadosa para uma compreensão completa do funcionamento do script.  A documentação no próprio código (`GEMINI 2.0 FLASH` e comentários) também contribui para a compreensão.

Documentação Técnica
Arquivo: People Analytics Measures.qvs
Última atualização: 07/08/2025 13:12:10
## Documentação Técnica do Script QlikView: People Analytics Measures.qvs

**Nome do Arquivo:** People Analytics Measures.qvs

**Data e Hora da Última Atualização:** 07/08/2025 (última atualização no script fornecido)


**1. Resumo:**

Este script QlikView carrega e calcula diversas métricas de People Analytics a partir da tabela `gd_eventos_f`. As métricas calculadas se concentram em três áreas principais: horas extras, absenteísmo e saldo de horas (banco de horas). O script utiliza comandos `SET` para definir variáveis que armazenam os resultados intermediários e as métricas finais.  Ele realiza cálculos de totais, médias, porcentagens e comparações de tendências mês a mês (MoM) e ano a ano (YoY) para cada uma dessas áreas.  O comando `TRACE` é usado para facilitar a depuração, registrando o início de cada seção do script.


**2. Principais Etapas:**

* **2.1 Definição de Variáveis:** O script inicia definindo um grande número de variáveis usando comandos `SET`. Essas variáveis armazenam resultados intermediários e métricas finais, como totais de horas extras, custos médios, dias de absenteísmo, e saldo de horas no banco de horas.

* **2.2 Cálculo de Métricas de Horas Extras:** Esta seção calcula diversas métricas relacionadas a horas extras. Inclui cálculos de:
    * Total de horas extras.
    * Custos totais e médios de horas extras (com valores separados para ano anterior e ano atual, e média por pessoa).
    * Média de horas extras por pessoa.
    * Número de funcionários elegíveis e inelegíveis para horas extras.
    * Vários percentuais relacionados a horas extras (por exemplo, percentual de horas extras em relação à remuneração total, percentual de horas extras esporádicas e recorrentes).
    * Variações percentuais mês a mês (MoM) e ano a ano (YoY) em relação aos custos e horas extras.

* **2.3 Cálculo de Métricas de Absenteísmo:** Esta seção calcula métricas de absenteísmo, considerando diferentes tipos de ausências (faltas, atestados, abonos, reembolsos e atrasos). Inclui:
    * Totais de dias e horas de absenteísmo para cada tipo de ausência.
    * Taxas de absenteísmo (global e para ausências não planejadas).
    * Comparação anual e mensal das taxas de absenteísmo (MoM e YoY).
    * Valores monetários associados a eventos de falta, com separação entre eventos operacionais e não operacionais e comparações MoM e YoY.
    * Indicadores específicos para abonos, com comparações MoM e YoY.

* **2.4 Cálculo de Métricas de Saldo de Horas (Banco de Horas):**  Esta seção calcula métricas relacionadas ao banco de horas:
    * Total de horas no banco de horas.
    * Saldo positivo e negativo de horas.
    * Percentual de colaboradores com saldo no banco de horas.
    * Valor do saldo pago em março e setembro.

* **2.5 Uso de Comandos `TRACE`:** O script utiliza o comando `TRACE` para registrar o início de cada seção, auxiliando na depuração e no acompanhamento da execução.

* **2.6 Finalização do Script:** O script termina com o comando `EXIT SCRIPT`.


**3. Observações:**

* O script utiliza expressões calculadas dentro das definições `SET`, combinadas com funções de data do QlikView (aparentemente com o formato "DD.MM.YYYY").
* As comparações YoY e MoM são baseadas em seleções de data, utilizando a função `Only(GetFieldSelections(gd_eventos_f.load_date))` para determinar o período de tempo considerado nos cálculos.
* A lógica de cálculo das variáveis demonstra complexidade, envolvendo múltiplas condições e agregações de dados.
* A estrutura modular facilita a manutenção e a adição de novas métricas.

**4. Considerações Finais:**

Esta documentação fornece uma visão geral do script. Para uma compreensão completa, é necessário analisar o código fonte detalhadamente,  bem como a estrutura e o conteúdo da tabela de origem `gd_eventos_f`.  A complexidade das expressões calculadas requer uma análise cuidadosa para total compreensão do funcionamento do script.

Documentação Técnica
Arquivo: People Analytics Measures.qvs
Última atualização: 07/08/2025 12:51:08
# Documentação Técnica do Script QlikView: People Analytics Measures.qvs

## 1. Introdução

**Nome do Arquivo:** People Analytics Measures.qvs

**Data e Hora da Última Atualização:** 07/08/2025 09:31:59

**Objetivo:** Este script calcula diversas métricas de análise de pessoas, focando em horas extras, absenteísmo e saldo de horas (banco de horas).  Utiliza dados da tabela `gd_eventos_f` e aplica filtros específicos para agregar e calcular métricas como custos, horas, porcentagens e tendências (mensais e anuais).

## 2. Principais Etapas

O script se estrutura em seções distintas, cada uma responsável por calcular um conjunto de métricas:

* **2.1 Definição de Variáveis:**  O script inicia definindo diversas variáveis que armazenam resultados intermediários e métricas finais. Essas variáveis são utilizadas posteriormente nos cálculos. Exemplos: `horas_total_extras`, `custo_medio_he`, `dias_absenteismo`, `horas_total_saldo_banco`, etc.  As variáveis são definidas usando comandos `SET`.

* **2.2 Cálculo de Métricas de Horas Extras:** Esta seção calcula diversas métricas relacionadas a horas extras, incluindo:
    * Total de horas extras (`horas_total_extras`).
    * Custos totais e médios de horas extras (`custo_medio_he`, `custo_medio_he_ano_anterior`, `custo_medio_he_ano_atual`, `custo_medio_por_pessoa_he`).
    * Média de horas extras por pessoa (`media_he`).
    * Número de funcionários elegíveis e inelegíveis para horas extras (`pessoas_elegiveis_he`, `pessoas_inelegiveis_he`, `pessoas_com_registro_he`).
    * Percentuais relacionados a horas extras (`%_HE_pessoas_elegiveis`, `%_HE_pessoas_inelegiveis`, `%_HE_remuneracao_total`, `%_hora_extra_esporadica`, `%_hora_extra_recorrente`, `%_HE_total_horas_trabalhadas`).
    * Variações mensais (MoM) e anuais (YoY) em relação a custos e horas extras (`%_MoM_horas_extras_custo_medio_he`, `%_YoY_custo_medio_he`, `%_YoY_horas_extras_valor`, `%_YoY_hora_extra`, `%_MoM_horas_extras`, `%MoM_hora_extra_valor`).

* **2.3 Cálculo de Métricas de Absenteísmo:**  Esta seção calcula métricas de absenteísmo, considerando diferentes tipos de ausências:
    * Total de dias de absenteísmo (`dias_absenteismo`).
    * Dias de faltas, atestados e abonos (`dias_faltas`, `dias_atestado`, `dias_abonos`, `dias_reembolso`, `dia_atraso`).
    * Total de horas de absenteísmo (`horas_total_absenteismo`, `horas_nao_planejadas`, `horas_total_abonos`).
    * Taxas de absenteísmo (global e para ausências não planejadas) (`%_indice_absenteismo`, `%_indice_horas_nao_planejadas`).
    * Comparação anual e mensal das taxas de absenteísmo (`%_indice_absenteismo_ano_anterior`, `%_indice_absenteismo_ano_atual`, `%_indice_absenteismo_nao_planejado_ano_anterior`, `%_indice_absenteismo_nao_planejado_ano_atual`, `%_MoM_absenteismo`, `%_YoY_absenteísmo`, `%_YoY_horas_nao_planejadas`, `%_MoM_horas_nao_planejadas`).
    * Valores associados a eventos de falta (`valor_eventos_faltas`, `valor_eventos_falta_ano_atual`, `valor_eventos_falta_ano_anterior`, `valor_evento_faltas_operacional`, `valor_evento_faltas_nao_operacional`, `%_MoM_valor_total_faltas`, `%_YoY_valor_total_faltas`, `valor_evento_falta_grafico`).
    * Indicadores específicos de abonos (`%_indice_abono`, `%_indice_abono_ano_atual`, `%_indice_abono_ano_anterior`, `%YoY_indice_abono`, `%MoM_indice_abono`, `%_abonos_atual_grafico`, `%_abono_anterior_grafico`).


* **2.4 Cálculo de Métricas de Saldo de Horas (Banco de Horas):** Esta seção calcula métricas relacionadas ao banco de horas:
    * Total de horas no banco (`horas_total_saldo_banco`).
    * Saldo positivo e negativo (`horas_total_saldo_banco_positivo`, `horas_total_saldo_banco_negativo`).
    * Percentual de colaboradores com saldo no banco (`%_colaboradores_com_saldo_banco`).
    * Valor do saldo pago em março e setembro (`valor_evento_saldo_banco_pago`, `%_MAR_SET_pgt_banco`).

* **2.5 Uso de Comandos TRACE:** O script utiliza o comando `TRACE` para registrar o início de cada seção, facilitando a depuração.

* **2.6 Finalização do Script:** O script finaliza com o comando `EXIT SCRIPT`.


## 3. Observações

* O script utiliza expressões calculadas e comandos `SET` para derivar as métricas.
* As comparações ano a ano (YoY) e mês a mês (MoM) são realizadas com base em seleções de data, utilizando funções de data do QlikView.  As funções de data parecem formatadas como "DD.MM.YYYY".
* A estrutura do script é modular, permitindo fácil modificação e adição de novas métricas. A lógica de cálculo das variáveis envolve muitas vezes o uso de `Only(GetFieldSelections(gd_eventos_f.load_date))` para definir o período considerado nos cálculos.

## 4. Considerações Finais

Esta documentação oferece uma visão geral do script.  Para uma compreensão completa, é necessário analisar o código fonte e a estrutura da tabela `gd_eventos_f`.

Documentação Técnica
Arquivo: People Analytics Measures.qvs
Última atualização: 07/08/2025 12:48:40


Documentação Técnica
Arquivo: People Analytics Measures.qvs
Última atualização: 07/08/2025 12:39:50


Documentação Técnica
Arquivo: People Analytics Measures.qvs
Última atualização: 07/08/2025 12:33:35










## Nome do Arquivo
**People Analytics Measures.qvs**

## Data e Hora da Última Atualização
**07/08/2025 09:31:59**

## Descrição do que o Script Faz
O script "People Analytics Measures" é responsável por calcular diversas métricas relacionadas à análise de pessoas, focando em horas extras, absenteísmo e saldo de horas (banco de horas). Ele utiliza dados da tabela `gd_eventos_f` e aplica filtros específicos para agregar e calcular métricas como custos, horas, porcentagens e tendências (mensais e anuais) para cada categoria. O script é estruturado em seções que tratam de horas extras, absenteísmo e saldo de horas.

## Lista Resumida dos Principais Componentes e Etapas

1. **Definição de Variáveis**:
   - O script define várias variáveis que armazenam cálculos e métricas, como horas totais extras, custos médios, taxas de absenteísmo e saldo de horas.

2. **Cálculo de Horas Extras**:
   - Calcula total de horas extras, custos associados, média de horas extras por pessoa, e percentual de funcionários elegíveis e inelegíveis para horas extras.

3. **Cálculo de Absenteísmo**:
   - Calcula dias de absenteísmo, incluindo faltas, atestados e abonos. Também calcula taxas de absenteísmo e compara dados anuais e mensais.

4. **Cálculo de Saldo de Horas (Banco de Horas)**:
   - Calcula o total de horas no banco, incluindo saldo positivo e negativo, e a porcentagem de colaboradores com saldo de banco.

5. **Comparações de Tendências**:
   - O script inclui lógica para calcular variações mensais (MoM) e anuais (YoY) em relação a horas extras, absenteísmo e valores de faltas.

6. **Uso de Comandos TRACE**:
   - O script utiliza o comando TRACE para registrar o início do carregamento de cada seção, facilitando a depuração e o acompanhamento do processo.

7. **Finalização do Script**:
   - O script é finalizado com o comando `EXIT SCRIPT`, encerrando a execução.

## Observações
- O script faz uso de expressões calculadas e comandos SET para derivar as métricas.
- As comparações de ano a ano (YoY) e mês a mês (MoM) são realizadas com base em seleções de data, utilizando funções de data do QlikView.
- A estrutura do script permite fácil modificação e adição de novas métricas conforme necessário.

Esta documentação fornece uma visão geral do funcionamento do script e pode ser utilizada como referência para futuras implementações ou modificações.

TextBlock(citations=None, text='Documentação Técnica do Script QlikView\n\n## Nome do Arquivo\n**People Analytics Measures.qvs**\n\n## Data e Hora da Última Atualização\n**06/08/2025 13:05:37**\n\n## Descrição do que o Script Faz\nO script "People Analytics Measures" é responsável por calcular diversas métricas relacionadas à análise de pessoas, focando em horas extras, absenteísmo e saldo de horas (banco de horas). Ele utiliza dados da tabela `gd_eventos_f` e aplica filtros específicos para agregar e calcular métricas como custos, horas, porcentagens e tendências (mensais e anuais) para cada categoria. O script é estruturado em seções que tratam de horas extras, absenteísmo e saldo de horas.\n\n## Lista Resumida dos Principais Componentes e Etapas\n\n1. **Definição de Variáveis**:\n   - O script define várias variáveis que armazenam cálculos e métricas, como horas totais extras, custos médios, taxas de absenteísmo e saldo de horas.\n\n2. **Cálculo de Horas Extras**:\n   - Calcula total de horas extras, custos associados, média de horas extras por pessoa, e percentual de funcionários elegíveis e inelegíveis para horas extras.\n\n3. **Cálculo de Absenteísmo**:\n   - Calcula dias de absenteísmo, incluindo faltas, atestados e abonos. Também calcula taxas de absenteísmo e compara dados anuais e mensais.\n\n4. **Cálculo de Saldo de Horas (Banco de Horas)**:\n   - Calcula o total de horas no banco, incluindo saldo positivo e negativo, e a porcentagem de colaboradores com saldo de banco.\n\n5. **Comparações de Tendências**:\n   - O script inclui lógica para calcular variações mensais (MoM) e anuais (YoY) em relação a horas extras, absenteísmo e valores de faltas.\n\n6. **Uso de Comandos TRACE**:\n   - O script utiliza o comando TRACE para registrar o início do carregamento de cada seção, facilitando a depuração e o acompanhamento do processo.\n\n7. **Finalização do Script**:\n   - O script é finalizado com o comando `EXIT SCRIPT`, encerrando a execução.\n\n## Observações\n- O script faz uso de expressões calculadas e comandos SET para derivar as métricas.\n- As comparações de ano a ano (YoY) e mês a mês (MoM) são realizadas com base em seleções de data, utilizando funções de data do QlikView.\n- A estrutura do script permite fácil modificação e adição de novas métricas conforme necessário.\n\nEsta documentação fornece uma visão geral do funcionamento do script e pode ser utilizada como referência para futuras implementações ou modificações.', type='text')

TextBlock(citations=None, text='## Nome do Arquivo\n**People Analytics Measures.qvs**\n\n## Data e Hora da Última Atualização\n**07/08/2025 09:31:59**\n\n## Descrição do que o Script Faz\nO script "People Analytics Measures" é responsável por calcular diversas métricas relacionadas à análise de pessoas, focando em horas extras, absenteísmo e saldo de horas (banco de horas). Ele utiliza dados da tabela `gd_eventos_f` e aplica filtros específicos para agregar e calcular métricas como custos, horas, porcentagens e tendências (mensais e anuais) para cada categoria. O script é estruturado em seções que tratam de horas extras, absenteísmo e saldo de horas.\n\n## Lista Resumida dos Principais Componentes e Etapas\n\n1. **Definição de Variáveis**:\n   - O script define várias variáveis que armazenam cálculos e métricas, como horas totais extras, custos médios, taxas de absenteísmo e saldo de horas.\n\n2. **Cálculo de Horas Extras**:\n   - Calcula total de horas extras, custos associados, média de horas extras por pessoa, e percentual de funcionários elegíveis e inelegíveis para horas extras.\n\n3. **Cálculo de Absenteísmo**:\n   - Calcula dias de absenteísmo, incluindo faltas, atestados e abonos. Também calcula taxas de absenteísmo e compara dados anuais e mensais.\n\n4. **Cálculo de Saldo de Horas (Banco de Horas)**:\n   - Calcula o total de horas no banco, incluindo saldo positivo e negativo, e a porcentagem de colaboradores com saldo de banco.\n\n5. **Comparações de Tendências**:\n   - O script inclui lógica para calcular variações mensais (MoM) e anuais (YoY) em relação a horas extras, absenteísmo e valores de faltas.\n\n6. **Uso de Comandos TRACE**:\n   - O script utiliza o comando TRACE para registrar o início do carregamento de cada seção, facilitando a depuração e o acompanhamento do processo.\n\n7. **Finalização do Script**:\n   - O script é finalizado com o comando `EXIT SCRIPT`, encerrando a execução.\n\n## Observações\n- O script faz uso de expressões calculadas e comandos SET para derivar as métricas.\n- As comparações de ano a ano (YoY) e mês a mês (MoM) são realizadas com base em seleções de data, utilizando funções de data do QlikView.\n- A estrutura do script permite fácil modificação e adição de novas métricas conforme necessário.\n\nEsta documentação fornece uma visão geral do funcionamento do script e pode ser utilizada como referência para futuras implementações ou modificações.', type='text')

# Documentação Técnica do Script QlikView

## Nome do Arquivo
**People Analytics Measures.qvs**

## Data e Hora da Última Atualização
**06/08/2025 13:05:37**

## Descrição do que o Script Faz
O script "People Analytics Measures" é responsável por calcular diversas métricas relacionadas à análise de pessoas, focando em horas extras, absenteísmo e saldo de horas (banco de horas). Ele utiliza dados da tabela `gd_eventos_f` e aplica filtros específicos para agregar e calcular métricas como custos, horas, porcentagens e tendências (mensais e anuais) para cada categoria. O script é estruturado em seções que tratam de horas extras, absenteísmo e saldo de horas.

## Lista Resumida dos Principais Componentes e Etapas

1. **Definição de Variáveis**:
   - O script define várias variáveis que armazenam cálculos e métricas, como horas totais extras, custos médios, taxas de absenteísmo e saldo de horas.

2. **Cálculo de Horas Extras**:
   - Calcula total de horas extras, custos associados, média de horas extras por pessoa, e percentual de funcionários elegíveis e inelegíveis para horas extras.

3. **Cálculo de Absenteísmo**:
   - Calcula dias de absenteísmo, incluindo faltas, atestados e abonos. Também calcula taxas de absenteísmo e compara dados anuais e mensais.

4. **Cálculo de Saldo de Horas (Banco de Horas)**:
   - Calcula o total de horas no banco, incluindo saldo positivo e negativo, e a porcentagem de colaboradores com saldo de banco.

5. **Comparações de Tendências**:
   - O script inclui lógica para calcular variações mensais (MoM) e anuais (YoY) em relação a horas extras, absenteísmo e valores de faltas.

6. **Uso de Comandos TRACE**:
   - O script utiliza o comando TRACE para registrar o início do carregamento de cada seção, facilitando a depuração e o acompanhamento do processo.

7. **Finalização do Script**:
   - O script é finalizado com o comando `EXIT SCRIPT`, encerrando a execução.

## Observações
- O script faz uso de expressões calculadas e comandos SET para derivar as métricas.
- As comparações de ano a ano (YoY) e mês a mês (MoM) são realizadas com base em seleções de data, utilizando funções de data do QlikView.
- A estrutura do script permite fácil modificação e adição de novas métricas conforme necessário.

Esta documentação fornece uma visão geral do funcionamento do script e pode ser utilizada como referência para futuras implementações ou modificações.



/** GEMINI 2.0 FLASH
 * @title People Analytics Measures Script
 * @description This script calculates various People Analytics measures related to overtime, absenteeism, and time-off (banked hours).
 * It defines SET statements to calculate metrics, including costs, hours, percentages, and trends (MoM and YoY) for each category.
 * The script uses data from the `gd_eventos_f` table and relies on specific event types and flags to filter and aggregate the data.
 *
 * @includes
 *  - Overtime Measures: Calculates total overtime hours, costs, and related metrics.
 *  - Absenteeism Measures: Calculates absenteeism rates, unplanned absence hours, and associated costs.
 *  - Time-Off (Banked Hours) Measures: Calculates the balance of banked hours and related metrics.
 *
 * @variables
 *  - horas_total_extras: Total overtime hours.
 *  - horas_extras_atual: Overtime hours for the current period.
 *  - horas_extras_anterior: Overtime hours for the previous period.
 *  - custo_medio_he: Average cost of overtime.
 *  - custo_medio_he_ano_anterior: Average cost of overtime in the previous year.
 *  - custo_medio_he_ano_atual: Average cost of overtime in the current year.
 *  - custo_medio_por_pessoa_he: Average overtime cost per person.
 *  - media_he: Average overtime hours.
 *  - pessoas_elegiveis_he: Number of employees eligible for overtime.
 *  - pessoas_com_registro_he: Number of employees with overtime records.
 *  - pessoas_inelegiveis_he: Number of employees ineligible for overtime.
 *  - qtd_eventos_he: Number of overtime events.
 *  - qtd_media_he_por_pessoa: Average number of overtime events per person.
 *  - valor_evento_hora_extra_recorrente: Value of recurring overtime events.
 *  - valor_evento_horas_extras_esporadicas: Value of sporadic overtime events.
 *  - %_HE_pessoas_elegiveis: Percentage of eligible employees with overtime.
 *  - %_HE_pessoas_inelegiveis: Percentage of ineligible employees with overtime.
 *  - %_HE_remuneracao_total: Percentage of overtime in total compensation.
 *  - %_hora_extra_esporadica: Percentage of sporadic overtime.
 *  - %_hora_extra_recorrente: Percentage of recurring overtime.
 *  - %_MoM_horas_extras_custo_medio_he: Month-over-month change in average overtime cost.
 *  - %_YoY_custo_medio_he: Year-over-year change in average overtime cost.
 *  - %_HE_total_horas_trabalhadas: Percentage of overtime in total worked hours.
 *  - %_YoY_horas_extras_valor: Year-over-year change in overtime value.
 *  - %_YoY_hora_extra: Year-over-year change in overtime hours.
 *  - %_MoM_horas_extras: Month-over-month change in overtime hours.
 *  - %MoM_hora_extra_valor: Month-over-month change in overtime value.
 *  - valor_evento_horas_extras: Total value of overtime events.
 *  - valor_eventos_horas_extras_ano_atual: Total value of overtime events in the current year.
 *  - valor_eventos_horas_extras_ano_anterior: Total value of overtime events in the previous year.
 *  - valor_evento_hora_extra_recorrente: Value of recurring overtime events.
 *  - valor_evento_horas_extras_anterior: Total value of overtime events in the previous period.
 *  - valor_evento_horas_extras_atual: Total value of overtime events in the current period.
 *  - valor_evento_hora_extra_grafico: Value of overtime events for the chart.
 *  - dias_absenteismo: Total days of absenteeism.
 *  - dias_nao_planejados: Total days of unplanned absences.
 *  - dias_abonos: Days of excused absence.
 *  - dias_atestado: Days of sick leave.
 *  - dias_faltas: Days of unexcused absence.
 *  - dias_reembolso: Days of reimbursement.
 *  - dia_atraso: Days of lateness.
 *  - eventos_absenteismo: Absenteeism events.
 *  - horas_total_absenteismo: Total hours of absenteeism.
 *  - horas_nao_planejadas: Unplanned absence hours.
 *  - horas_total_abonos: Total hours of excused absence.
 *  - media_faltantes: Average days of absence.
 *  - %_indice_absenteismo: Absenteeism rate.
 *  - %_indice_absenteismo_ano_anterior: Absenteeism rate in the previous year.
 *  - %_indice_absenteismo_ano_atual: Absenteeism rate in the current year.
 *  - %_indice_absenteismo_grafico: Absenteeism rate for the chart.
 *  - %_indice_horas_nao_planejadas: Unplanned absence hours rate.
 *  - %_indice_absenteismo_nao_planejado_ano_anterior: Unplanned absenteeism rate in the previous year.
 *  - %_indice_absenteismo_nao_planejado_ano_atual: Unplanned absenteeism rate in the current year.
 *  - %_MoM_absenteismo: Month-over-month change in absenteeism rate.
 *  - %_YoY_absenteismo: Year-over-year change in absenteeism rate.
 *  - %_YoY_horas_nao_planejadas: Year-over-year change in unplanned absence hours.
 *  - %_MoM_horas_nao_planejadas: Month-over-month change in unplanned absence hours.
 *  - %_horas_nao_planejadas_tabela_atual: Unplanned absence hours rate for the current table.
 *  - %_horas_nao_planejadas_tabela_ant: Unplanned absence hours rate for the previous table.
 *  - %_YoY_horas_nao_planejadas_tabela: Year-over-year change in unplanned absence hours rate for the table.
 *  - valor_eventos_faltas: Value of absence events.
 *  - valor_eventos_falta_ano_atual: Value of absence events in the current year.
 *  - valor_eventos_falta_ano_anterior: Value of absence events in the previous year.
 *  - valor_evento_faltas_operacional: Value of absence events for operational staff.
 *  - valor_evento_faltas_nao_operacional: Value of absence events for non-operational staff.
 *  - %_MoM_valor_total_faltas: Month-over-month change in total absence value.
 *  - %_YoY_valor_total_faltas: Year-over-year change in total absence value.
 *  - valor_evento_falta_grafico: Value of absence events for the chart.
 *  - %_indice_abono: Excused absence rate.
 *  - %_indice_abono_ano_atual: Excused absence rate in the current year.
 *  - %_indice_abono_ano_anterior: Excused absence rate in the previous year.
 *  - %YoY_indice_abono: Year-over-year change in excused absence rate.
 *  - %MoM_indice_abono: Month-over-month change in excused absence rate.
 *  - %_abonos_atual_grafico: Excused absence rate for the current chart.
 *  - %_abono_anterior_grafico: Excused absence rate for the previous chart.
 *  - valor_evento_saldo_banco_pago: Value of time-off (banked hours) paid.
 *  - %_colaboradores_com_saldo_banco: Percentage of employees with time-off (banked hours) balance.
 *  - %_MAR_SET_pgt_banco: Percentage of time-off (banked hours) paid in March and September.
 *  - horas_total_saldo_banco: Total time-off (banked hours).
 *  - horas_total_saldo_banco_positivo: Total positive time-off (banked hours).
 *  - horas_total_saldo_banco_negativo: Total negative time-off (banked hours).
 *
 * @remarks
 *  - The script uses a combination of SET statements and calculated expressions to derive the measures.
 *  - Date calculations rely on the `gd_eventos_f.load_date` field and the `Only(GetFieldSelections(gd_eventos_f.load_date))` function to determine the selected date range.
 *  - The script includes logic to handle year-over-year (YoY) and month-over-month (MoM) comparisons.
 *  - The script uses the TRACE statement to log the start of each section.
 *  - The script ends with an EXIT SCRIPT statement.
 *
 * @file People Analytics Measures.qvs
 * @filepath /c:/Users/ext.saraOM/Desktop/documentacao/documenta-o/SCRIPT PARA IMPLEMENTACAO/People Analytics Measures.qvs
 */



TRACE >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>Iniciando carregamento medidas de Hora extra<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<;
SET horas_total_extras = '{<tipo_evento={''Hora extra''}>} [#_hora_total]';
 
SEt horas_extras_atual = '{<gd_eventos_f.load_date = {"=$(=Date(AddMonths(Date#(MonthStart(Only(GetFieldSelections(gd_eventos_f.load_date))), ''DD.MM.YYYY''),1), ''DD.MM.YYYY''))"},ano = {"=$(=Year(Date#(Only(gd_eventos_f.load_date), ''DD.MM.YYYY'')))"}>} [#_horas_total_extras]';
 
SET horas_extras_anterior = '{<gd_eventos_f.load_date = {"=$(=Date(AddMonths(Date#(MonthStart(Only(GetFieldSelections(gd_eventos_f.load_date))), ''DD.MM.YYYY''),1), ''DD.MM.YYYY''))"},ano = {"$(=Year(AddYears(Date#(Only(gd_eventos_f.load_date), ''DD.MM.YYYY''), -1)))"}>} [#_horas_total_extras]';
 
SET custo_medio_he = '{<tipo_evento={''Hora extra''}, flag_hora_extra={''1''}>} [#_valor_evento_total] / count({<flag_hora_extra={''1''}>} gd_eventos_f.hora_total)';
 
SET custo_medio_he_ano_anterior = '{<gd_eventos_f.load_date = {"=$(=Date(AddMonths(Date#(MonthStart(Only(GetFieldSelections(gd_eventos_f.load_date))), ''DD.MM.YYYY''),1), ''DD.MM.YYYY''))"},ano = {"$(=Year(AddYears(Date#(Only(gd_eventos_f.load_date), ''DD.MM.YYYY''), -1)))"}>}[#_custo_medio_he]';
 
SET custo_medio_he_ano_atual = '{<[gd_eventos_f.load_date] = {"=$(=Date(AddMonths(Date#(MonthStart(Only(GetFieldSelections(gd_eventos_f.load_date))), ''DD.MM.YYYY''),1), ''DD.MM.YYYY''))"}, ano = {"=$(=Year(Date#(Only(gd_eventos_f.load_date), ''DD.MM.YYYY'')))"}>}[#_custo_medio_he]';
 
SET custo_medio_por_pessoa_he = '[#_valor_evento_horas_extras]/[#_pessoas_com_registro_he]';
 
SET media_he = '{<flag_hora_extra={''1''}>}[#_horas_total_extras]/count({<flag_hora_extra={''1''}>} gd_eventos_f.hora_total)';
 
SET pessoas_elegiveis_he= 'count({<flag_hora_extra={''1''}, grupo_relatorio={''8 - Demais''}>}distinct pessoa)';
 
SET pessoas_com_registro_he = 'count({<flag_hora_extra={''1''}>}distinct pessoa)';
 
SET pessoas_inelegiveis_he = 'count({<flag_hora_extra={''1''}, grupo_relatorio-={''8 - Demais''}>}distinct pessoa)';
 
SET qtd_eventos_he= 'count({<flag_hora_extra={''1''}>} gd_eventos_f.hora_total)';
 
SET qtd_media_he_por_pessoa = '[#_qtd_eventos_he]/[#_pessoas_com_registro_he]';
 
SET valor_evento_hora_extra_recorrente = '{<nome_conta_debito={''Recorrente''}>}[#_valor_evento_horas_extras]';
 
SET valor_evento_horas_extras_esporadicas = '{<nome_conta_debito={''Esporádico''}>}[#_valor_evento_horas_extras]';
 
SET %_HE_pessoas_elegiveis = '[#_pessoas _elegiveis_he]/[#_pessoas_com_registro_he]';
 
SET %_HE_pessoas_inelegiveis = '([#_pessoas_com_registro_he] - [#_pessoas _elegiveis_he])/[#_pessoas_com_registro_he]';
 
SET %_HE_remuneracao_total = '([#_valor_evento_horas_extras])/(({<flag_hora_extra={''1''}, grupo_relatorio={''4 - Coordenador'',''8 - Demais''}>}[#_salario]) +  [#_valor_evento_horas_extras])';
 
SET %_hora_extra_esporadica = '[#_valor_evento_horas_extras_esporadicas]/[#_valor_evento_horas_extras]';
 
SET %_hora_extra_recorrente = '[#_valor_evento_hora_extra_recorrente]/[#_valor_evento_horas_extras]';
 
SET %_MoM_horas_extras_custo_medio_he = '(({<gd_eventos_f.load_date={">=$(=Date(MonthStart(Max(gd_eventos_f.load_date)), ''DD.MM.YYYY''))<=$(=Date(MonthEnd(Max(gd_eventos_f.load_date)), ''DD.MM.YYYY''))"}>} [#_custo_medio_he])
-
                                        ({<gd_eventos_f.load_date={">=$(=Date(MonthStart(AddMonths(Max(gd_eventos_f.load_date), -1)), ''DD.MM.YYYY''))<=$(=Date(MonthEnd(AddMonths(Max(gd_eventos_f.load_date), -1)), ''DD.MM.YYYY''))"}>} [#_custo_medio_he]))
/
                                        ({<gd_eventos_f.load_date={">=$(=Date(MonthStart(AddMonths(Max(gd_eventos_f.load_date), -1)), ''DD.MM.YYYY''))<=$(=Date(MonthEnd(AddMonths(Max(gd_eventos_f.load_date), -1)), ''DD.MM.YYYY''))"}>} [#_custo_medio_he])';
 
 
SET %_YoY_custo_medio_he = '(({<gd_eventos_f.load_date={">=$(=Date(YearStart(Max(gd_eventos_f.load_date)), ''DD.MM.YYYY'')) <=$(=Date(YearEnd(Max(gd_eventos_f.load_date)), ''DD.MM.YYYY''))"}>} [#_custo_medio_he])
    -
({<gd_eventos_f.load_date = {">=$(=Date(YearStart(AddYears(Max(gd_eventos_f.load_date), -1)), ''DD.MM.YYYY''))<=$(=Date(YearEnd(AddYears(Max(gd_eventos_f.load_date), -1)), ''DD.MM.YYYY''))"}>} [#_custo_medio_he]))
/
({<gd_eventos_f.load_date = {">=$(=Date(YearStart(AddYears(Max(gd_eventos_f.load_date), -1)), ''DD.MM.YYYY'')) <=$(=Date(YearEnd(AddYears(Max(gd_eventos_f.load_date), -1)), ''DD.MM.YYYY''))"}>} [#_custo_medio_he])';
 
 
SET %_HE_total_horas_trabalhadas = '[#_horas_total_extras]/([#_horas_total_jornada_mensal] + [#_horas_total_extras])';
 
SET %_YoY_horas_extras_valor  = '({<gd_eventos_f.load_date={">=$(=Date(YearStart(Max(gd_eventos_f.load_date)), ''DD.MM.YYYY'')) <=$(=Date(YearEnd(Max(gd_eventos_f.load_date)), ''DD.MM.YYYY''))"}>} [#_valor_evento_horas_extras])
-
({<gd_eventos_f.load_date = {">=$(=Date(YearStart(AddYears(Max(gd_eventos_f.load_date), -1)), ''DD.MM.YYYY''))<=$(=Date(YearEnd(AddYears(Max(gd_eventos_f.load_date), -1)), ''DD.MM.YYYY''))"}>} [#_valor_evento_horas_extras]))
/
({<gd_eventos_f.load_date = {">=$(=Date(YearStart(AddYears(Max(gd_eventos_f.load_date), -1)), ''DD.MM.YYYY'')) <=$(=Date(YearEnd(AddYears(Max(gd_eventos_f.load_date), -1)), ''DD.MM.YYYY''))"}>} [#_valor_evento_horas_extras])';
 
 
SET %_YoY_hora_extra =  '({<gd_eventos_f.load_date={">=$(=Date(YearStart(Max(gd_eventos_f.load_date)), ''DD.MM.YYYY'')) <=$(=Date(YearEnd(Max(gd_eventos_f.load_date)), ''DD.MM.YYYY''))"}>} #_horas_total_extras)
-
Sum({<gd_eventos_f.load_date = {">=$(=Date(YearStart(AddYears(Max(gd_eventos_f.load_date), -1)), ''DD.MM.YYYY''))<=$(=Date(YearEnd(AddYears(Max(gd_eventos_f.load_date), -1)), ''DD.MM.YYYY''))"}>} #_horas_total_extrasl))
/
Sum({<gd_eventos_f.load_date = {">=$(=Date(YearStart(AddYears(Max(gd_eventos_f.load_date), -1)), ''DD.MM.YYYY'')) <=$(=Date(YearEnd(AddYears(Max(gd_eventos_f.load_date), -1)), ''DD.MM.YYYY''))"}>} #_horas_total_extras)';
 
 
SET %_MoM_horas_extras = '(({<gd_eventos_f.load_date = {">=$(=Date(Monthstart(Max(gd_eventos_f.load_date)), ''DD.MM.YYYY''))<=$(=Date(MonthEnd(Max(gd_eventos_f.load_date)), ''DD.MM.YYYY''))"}>} #_horas_total_extras) -
Sum({<gd_eventos_f.load_date = {">=$(=Date(MonthStart(AddMonths(Max(gd_eventos_f.load_date), -1)), ''DD.MM.YYYY''))<=$(=Date(Monthend(AddMonths(Max(gd_eventos_f.load_date), -1)), ''DD.MM.YYYY''))"}>} #_horas_total_extras))
/
Sum({<gd_eventos_f.load_date = {">=$(=Date(MonthStart(AddMonths(Max(gd_eventos_f.load_date), -1)), ''DD.MM.YYYY''))<=$(=Date(Monthend(AddMonths(Max(gd_eventos_f.load_date), -1)), ''DD.MM.YYYY''))"}>} #_horas_total_extras)';
 
 
SET %MoM_hora_extra_valor = '({<gd_eventos_f.load_date = {">=$(=Date(Monthstart(Max(gd_eventos_f.load_date)), ''DD.MM.YYYY''))<=$(=Date(MonthEnd(Max(gd_eventos_f.load_date)), ''DD.MM.YYYY''))"}>} valor_evento_horas_extras) -
({<gd_eventos_f.load_date = {">=$(=Date(MonthStart(AddMonths(Max(gd_eventos_f.load_date), -1)), ''DD.MM.YYYY''))<=$(=Date(Monthend(AddMonths(Max(gd_eventos_f.load_date), -1)), ''DD.MM.YYYY''))"}>}valor_evento_horas_extras))
/
({<gd_eventos_f.load_date = {">=$(=Date(MonthStart(AddMonths(Max(gd_eventos_f.load_date), -1)), ''DD.MM.YYYY''))<=$(=Date(Monthend(AddMonths(Max(gd_eventos_f.load_date), -1)), ''DD.MM.YYYY''))"}>} valor_evento_horas_extrasl)';
 
 
SET valor_evento_horas_extras =  '{<tipo_evento={''Hora extra''}>} [#_valor_evento_total]';
 
SET valor_eventos_horas_extras_ano_atual = '{<gd_eventos_f.load_date = {"=$(=Date(AddMonths(Date#(MonthStart(Only(GetFieldSelections(gd_eventos_f.load_date))), ''DD.MM.YYYY''),1), ''DD.MM.YYYY''))"},ano = {"=$(=Year(Date#(Only(gd_eventos_f.load_date), ''DD.MM.YYYY'')))"}>}[#_valor_evento_horas_extras]';
 
SET valor_eventos_horas_extras_ano_anterior = '{<gd_eventos_f.load_date = {"=$(=Date(AddMonths(Date#(MonthStart(Only(GetFieldSelections(gd_eventos_f.load_date))), ''DD.MM.YYYY''),1), ''DD.MM.YYYY''))"},ano = {"$(=Year(AddYears(Date#(Only(gd_eventos_f.load_date), ''DD.MM.YYYY''), -1)))"}>}[#_valor_evento_horas_extras]';
 
 
SET valor_evento_hora_extra_recorrente = '{<nome_conta_debito={''Recorrente''}>}[#_valor_evento_horas_extras]';
 
SET valor_evento_horas_extras_anterior= '{<gd_eventos_f.load_date = {"=$(=Date(AddMonths(Date#(MonthStart(Only(GetFieldSelections(gd_eventos_f.load_date))), ''DD.MM.YYYY''),1), ''DD.MM.YYYY''))"},ano = {"$(=Year(AddYears(Date#(Only(gd_eventos_f.load_date), ''DD.MM.YYYY''), -1)))"}>} [#_valor_evento_horas_extras]';
 
SET valor_evento_horas_extras_atual = '{<gd_eventos_f.load_date = {"=$(=Date(AddMonths(Date#(MonthStart(Only(GetFieldSelections(gd_eventos_f.load_date))), ''DD.MM.YYYY''),1), ''DD.MM.YYYY''))"},ano = {"=$(=Year(Date#(Only(gd_eventos_f.load_date), ''DD.MM.YYYY'')))"}>}[#_valor_evento_horas_extras]';
 
SET valor_evento_hora_extra_grafico = '{<gd_eventos_f.load_date = {"=$(=Date(AddMonths(Date#(MonthStart(Only(GetFieldSelections(gd_eventos_f.load_date))), ''DD.MM.YYYY''),1), ''DD.MM.YYYY''))"},ano = {"=$(=Year(Date#(Only(gd_eventos_f.load_date), ''DD.MM.YYYY'')))"}>}[#_valor_evento_horas_extras]';
 
 TRACE >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>Iniciando carregamento medidas de Absenteísmo  <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<;
 
 
SET dias_absenteismo =  '[#_dias_atestado]+ [#_dias_faltas] +[#_dia_atraso] +[#_dias_abonos]';
 
SET dias_nao_planejados = '[#_dias_faltas] + [#_dia_atraso]';
 
SET dias_abonos = 'Sum(aggr(sum({<tipo_evento = {''Abonos''}>} gd_eventos_f.hora_total) * 30 / sum({<tipo_evento = {''Jornada''}>} distinct gd_eventos_f.hora_total),mes_nome, gd_eventos_f.chapa))';
 
SET dias_atestado = 'Sum(aggr(sum({<tipo_evento = {''Atestado''}>} [gd_eventos_f.hora_total]) * 30 

    / 

    sum({<tipo_evento = {''Jornada''}>} distinct [gd_eventos_f.hora_total]),gd_eventos_f.chapa, (mes_nome)))';
 
 
SEt dias_faltas = 'Sum(aggr(sum({<tipo_evento = {''Falta''}>} [gd_eventos_f.hora_total]) * 30 

    / 

    sum({<tipo_evento = {''Jornada''}>} distinct [gd_eventos_f.hora_total]),gd_eventos_f.chapa, (mes_nome)))';
 
 
SET dias_reembolso = 'Sum(aggr(sum({<tipo_evento = {''Reembolso''}>} [gd_eventos_f.hora_total]) * 30 

    / 

    sum({<tipo_evento = {''Jornada''}>} distinct [gd_eventos_f.hora_total]),mes_nome, gd_eventos_f.chapa))';
 
 
SET dia_atraso = 'Sum(aggr(sum({<tipo_evento = {''Atraso''}>} [gd_eventos_f.hora_total]) * 30 

  / 

   sum({<tipo_evento = {''Jornada''}>} distinct [gd_eventos_f.hora_total]),mes_nome, [gd_eventos_f.chapa]))';

 
SET eventos_absenteismo = '{<tipo_evento-={''Jornada'',''Hora extra'', ''Abonos'', ''Saldo Banco'',''Reembolso''}>}[#_hora_total]';
 
SET horas_total_absenteismo = '[#_horas_total_atestado] + [#_horas_total_atrasos] + [#_horas_total_faltas] + [#_horas_total_abonos]';
 
SET horas_nao_planejadas = '[#_horas_total_faltas] + [#_horas_total_atrasos]';
 
SET horas_total_abonos = '{<tipo_evento={''Abonos''}>} [#_hora_total]';
 
SET media_faltantes = 'num(([#_dias_faltas] +[#_dia_atraso])/count({<flag_horas_nao_planejadas={''1''}>}distinct pessoa),''#,##'') & '' dias''';
 
 
SET %_indice_absenteismo = '[#_horas_total_absenteismo]/[#_horas_total_jornada_mensal]';
 
 
SET %_indice_absenteismo_ano_anterior = '{<gd_eventos_f.load_date = {"=$(=Date(AddMonths(Date#(MonthStart(Only(GetFieldSelections(gd_eventos_f.load_date))), ''DD.MM.YYYY''),1), ''DD.MM.YYYY''))"}, ano = {"$(=Year(AddYears(Date#(Only(gd_eventos_f.load_date), ''DD.MM.YYYY''), -1)))"}>} [#_horas_total_absenteismo]

/

{< gd_eventos_f.load_date = {"=$(=Date(AddMonths(Date#(MonthStart(Only(GetFieldSelections(gd_eventos_f.load_date))), ''DD.MM.YYYY''),1), ''DD.MM.YYYY''))"},ano = {"$(=Year(AddYears(Date#(Only(gd_eventos_f.load_date), ''DD.MM.YYYY''), -1)))"}>} [#_horas_total_jornada_mensal]';
 
 
SET %_indice_absenteismo_ano_atual= '{< [gd_eventos_f.load_date] = {"=$(=Date(AddMonths(Date#(MonthStart(Only(GetFieldSelections(gd_eventos_f.load_date))), ''DD.MM.YYYY''),1), ''DD.MM.YYYY''))"},ano = {"=$(=Year(Date#(Only(gd_eventos_f.load_date), ''DD.MM.YYYY'')))"}>} [#_horas_total_absenteismo]

/{<gd_eventos_f.load_date = {"=$(=Date(AddMonths(Date#(MonthStart(Only(GetFieldSelections(gd_eventos_f.load_date))), ''DD.MM.YYYY''),1), ''DD.MM.YYYY''))"},ano = {"=$(=Year(Date#(Only(gd_eventos_f.load_date), ''DD.MM.YYYY'')))"}
>} [#_horas_total_jornada_mensal]';
 
 
SET %_indice_absenteismo_grafico = '({< [gd_eventos_f.load_date] = {"=$(=Date(AddMonths(Date#(MonthStart(Only(GetFieldSelections(gd_eventos_f.load_date))), ''DD.MM.YYYY''),1), ''DD.MM.YYYY''))"},ano = {"=$(=Year(Date#(Only(gd_eventos_f.load_date), ''DD.MM.YYYY'')))"}>} [#_horas_total_absenteismo])

/

({<gd_eventos_f.load_date = {"=$(=Date(AddMonths(Date#(MonthStart(Only(GetFieldSelections(gd_eventos_f.load_date))), ''DD.MM.YYYY''),1), ''DD.MM.YYYY''))"},ano = {"=$(=Year(Date#(Only(gd_eventos_f.load_date), ''DD.MM.YYYY'')))"}>} [#_horas_total_jornada_mensal])';
 
SET %_indice_horas_nao_planejadas = '#_horas_nao_planejadas/[#_horas_total_jornada_mensal]';
 
SET %_indice_absenteismo_nao_planejado_ano_anterior= '{<gd_eventos_f.load_date = {"=$(=Date(AddMonths(Date#(MonthStart(Only(GetFieldSelections(gd_eventos_f.load_date))), ''DD.MM.YYYY''),1), ''DD.MM.YYYY''))"},

  ano = {"$(=Year(AddYears(Date#(Only(gd_eventos_f.load_date), ''DD.MM.YYYY''), -1)))"}>} [#_horas_nao_planejadas]

/

{<gd_eventos_f.load_date = {"=$(=Date(AddMonths(Date#(MonthStart(Only(GetFieldSelections(gd_eventos_f.load_date))), ''DD.MM.YYYY''),1), ''DD.MM.YYYY''))"},

  ano = {"$(=Year(AddYears(Date#(Only(gd_eventos_f.load_date), ''DD.MM.YYYY''), -1)))"}
>} [#_horas_total_jornada_mensal]';
 
 
SET %_indice_absenteismo_nao_planejado_ano_atual = '{<gd_eventos_f.load_date = {"=$(=Date(AddMonths(Date#(MonthStart(Only(GetFieldSelections(gd_eventos_f.load_date))), ''DD.MM.YYYY''),1), ''DD.MM.YYYY''))"},ano = {"=$(=Year(Date#(Only(gd_eventos_f.load_date), ''DD.MM.YYYY'')))"}>} [#_horas_nao_planejadas]

/

{<gd_eventos_f.load_date = {"=$(=Date(AddMonths(Date#(MonthStart(Only(GetFieldSelections(gd_eventos_f.load_date))), ''DD.MM.YYYY''),1), ''DD.MM.YYYY''))"},ano = {"=$(=Year(Date#(Only(gd_eventos_f.load_date), ''DD.MM.YYYY'')))"}>} [#_horas_total_jornada_mensal]';
 
 
SET %_MoM_absenteismo = '({<gd_eventos_f.load_date = {">=$(=Date(Monthstart(Max(gd_eventos_f.load_date)), ''DD.MM.YYYY''))<=$(=Date(MonthEnd(Max(gd_eventos_f.load_date)), ''DD.MM.YYYY''))"}>} [%_indice_absenteismo] -

{<gd_eventos_f.load_date = {">=$(=Date(MonthStart(AddMonths(Max(gd_eventos_f.load_date), -1)), ''DD.MM.YYYY''))<=$(=Date(Monthend(AddMonths(Max(gd_eventos_f.load_date), -1)), ''DD.MM.YYYY''))"}>}[%_indice_absenteismo])

/

({<gd_eventos_f.load_date = {">=$(=Date(MonthStart(AddMonths(Max(gd_eventos_f.load_date), -1)), ''DD.MM.YYYY''))<=$(=Date(Monthend(AddMonths(Max(gd_eventos_f.load_date), -1)), ''DD.MM.YYYY''))"}>}[%_indice_absenteismo])'

;
 
SET %_YoY_absenteismo=  '({<[gd_eventos_f.load_date] = {">=$(=Date(YearStart(Max(gd_eventos_f.load_date)), ''DD.MM.YYYY'')) <=$(=Date(YearEnd(Max(gd_eventos_f.load_date)), ''DD.MM.YYYY''))"}>} [%_indice_absenteismo] -

{<[gd_eventos_f.load_date] = {">=$(=Date(YearStart(AddYears(Max(gd_eventos_f.load_date), -1)), ''DD.MM.YYYY''))<=$(=Date(YearEnd(AddYears(Max(gd_eventos_f.load_date), -1)), ''DD.MM.YYYY''))"}>}[%_indice_absenteismo])

/

({<[gd_eventos_f.load_date] = {">=$(=Date(YearStart(AddYears(Max(gd_eventos_f.load_date), -1)), ''DD.MM.YYYY''))<=$(=Date(YearEnd(AddYears(Max(gd_eventos_f.load_date), -1)), ''DD.MM.YYYY''))"}>}[%_indice_absenteismo])'

;
 
 
SET %_YoY_horas_nao_planejadas = '({<gd_eventos_f.load_date = {">=$(=Date(YearStart(Max(gd_eventos_f.load_date)), ''DD.MM.YYYY'')) <=$(=Date(YearEnd(Max(gd_eventos_f.load_date)), ''DD.MM.YYYY''))"}>} [%_indice_horas_nao_planejadas] -

{<gd_eventos_f.load_date = {">=$(=Date(YearStart(AddYears(Max(gd_eventos_f.load_date), -1)), ''DD.MM.YYYY''))<=$(=Date(YearEnd(AddYears(Max(gd_eventos_f.load_date), -1)), ''DD.MM.YYYY''))"}>}[%_indice_horas_nao_planejadas])

/

({<gd_eventos_f.load_date = {">=$(=Date(YearStart(AddYears(Max(gd_eventos_f.load_date), -1)), ''DD.MM.YYYY''))<=$(=Date(YearEnd(AddYears(Max(gd_eventos_f.load_date), -1)), ''DD.MM.YYYY''))"}>}[%_indice_horas_nao_planejadas])';
 
SET %_MoM_horas_nao_planejadas = '({<gd_eventos_f.load_date = {">=$(=Date(Monthstart(Max(gd_eventos_f.load_date)), ''DD.MM.YYYY''))<=$(=Date(MonthEnd(Max(gd_eventos_f.load_date)), ''DD.MM.YYYY''))"}>} [%_indice_horas_nao_planejadas] -

{<gd_eventos_f.load_date = {">=$(=Date(MonthStart(AddMonths(Max(gd_eventos_f.load_date), -1)), ''DD.MM.YYYY''))<=$(=Date(Monthend(AddMonths(Max(gd_eventos_f.load_date), -1)), ''DD.MM.YYYY''))"}>}[%_indice_horas_nao_planejadas])

/

({<gd_eventos_f.load_date = {">=$(=Date(MonthStart(AddMonths(Max(gd_eventos_f.load_date), -1)), ''DD.MM.YYYY''))<=$(=Date(Monthend(AddMonths(Max(gd_eventos_f.load_date), -1)), ''DD.MM.YYYY''))"}>}[%_indice_horas_nao_planejadas])';
 
SET %_horas_nao_planejadas_tabela_atual = '{<gd_eventos_f.load_date = {"=$(=Date(AddMonths(Date#(MonthStart(Only(GetFieldSelections(gd_eventos_f.load_date))), ''DD.MM.YYYY''),1), ''DD.MM.YYYY''))"}, ano = {"=$(=Year(Date#(Only(gd_eventos_f.load_date), ''DD.MM.YYYY'')))"}>} [#_horas_nao_planejadas]

/

{<gd_eventos_f.load_date = {"=$(=Date(AddMonths(Date#(MonthStart(Only(GetFieldSelections(gd_eventos_f.load_date))), ''DD.MM.YYYY''),1), ''DD.MM.YYYY''))"},ano = {"=$(=Year(Date#(Only(gd_eventos_f.load_date), ''DD.MM.YYYY'')))"}>} [#_horas_total_jornada_mensal]';
 
 
SET %_horas_nao_planejadas_tabela_ant = '{<gd_eventos_f.load_date = {"=$(=Date(AddMonths(Date#(MonthStart(Only(GetFieldSelections(gd_eventos_f.load_date))), ''DD.MM.YYYY''),1), ''DD.MM.YYYY''))"},ano = {"$(=Year(Date#(Only(gd_eventos_f.load_date), ''DD.MM.YYYY''))) - 1"}>} [#_horas_nao_planejadas]

/

{<gd_eventos_f.load_date = {"=$(=Date(AddMonths(Date#(MonthStart(Only(GetFieldSelections(gd_eventos_f.load_date))), ''DD.MM.YYYY''),1), ''DD.MM.YYYY''))"},ano = {"$(=Year(Date#(Only(gd_eventos_f.load_date), ''DD.MM.YYYY''))) - 1"}>} [#_horas_total_jornada_mensal]';
 
SET %_YoY_horas_nao_planejadas_tabela = '([%_horas_nao_planejadas_tabela] - [%_horas_nao_planejadas_tabela-ant])/[%_horas_nao_planejadas_tabela-ant]';
 
 
SET valor_eventos_faltas = '{<tipo_evento={''Falta'',''Reembolso''}>} [#_valor_evento_total]';
 
 
SET valor_eventos_falta_ano_atual = '{<gd_eventos_f.load_date = {"=$(=Date(AddMonths(Date#(MonthStart(Only(GetFieldSelections(gd_eventos_f.load_date))), ''DD.MM.YYYY''),1), ''DD.MM.YYYY''))"},ano = {"=$(=Year(Date#(Only(gd_eventos_f.load_date), ''DD.MM.YYYY'')))"}>} [#_valor_evento_faltas]';
 
 
SET valor_eventos_falta_ano_anterior ='{<gd_eventos_f.load_date = {"=$(=Date(AddMonths(Date#(MonthStart(Only(GetFieldSelections(gd_eventos_f.load_date))), ''DD.MM.YYYY''),1), ''DD.MM.YYYY''))"},ano = {"$(=Year(AddYears(Date#(Only(gd_eventos_f.load_date), ''DD.MM.YYYY''), -1)))"}>} [#_valor_evento_faltas]';
 
 
SET valor_evento_faltas_operacional = '{<tipo_evento={''Falta'',''Reembolso''}, grupo_relatorio={''8 - Demais''}>} [#_valor_evento_total]';
 
 
SET valor_evento_faltas_nao_operacional = '{<tipo_evento={''Falta'',''Reembolso''}, grupo_relatorio={''7 - Líder''}>} [#_valor_evento_total]';
 
 
SET %_MoM_valor_total_faltas = '({<gd_eventos_f.load_date = {">=$(=Date(Monthstart(Max(gd_eventos_f.load_date)), ''DD.MM.YYYY''))<=$(=Date(MonthEnd(Max(gd_eventos_f.load_date)), ''DD.MM.YYYY''))"}>} #_valor_eventos_falta -

{<gd_eventos_f.load_date = {">=$(=Date(MonthStart(AddMonths(Max(gd_eventos_f.load_date), -1)), ''DD.MM.YYYY''))<=$(=Date(Monthend(AddMonths(Max(gd_eventos_f.load_date), -1)), ''DD.MM.YYYY''))"}>}#_valor_eventos_falta)

/

({<gd_eventos_f.load_date = {">=$(=Date(MonthStart(AddMonths(Max(gd_eventos_f.load_date), -1)), ''DD.MM.YYYY''))<=$(=Date(Monthend(AddMonths(Max(gd_eventos_f.load_date), -1)), ''DD.MM.YYYY''))"}>}#_valor_eventos_falta)';
 
 
SET %_YoY_valor_total_faltas= '({<gd_eventos_f.load_date = {">=$(=Date(YearStart(Max(gd_eventos_f.load_date)), ''DD.MM.YYYY'')) <=$(=Date(YearEnd(Max(gd_eventos_f.load_date)), ''DD.MM.YYYY''))"}>} #_valor_eventos_falta -

{<gd_eventos_f.load_date = {">=$(=Date(YearStart(AddYears(Max(gd_eventos_f.load_date), -1)), ''DD.MM.YYYY''))<=$(=Date(YearEnd(AddYears(Max(gd_eventos_f.load_date), -1)), ''DD.MM.YYYY''))"}>}#_valor_eventos_falta)

/

({<gd_eventos_f.load_date = {">=$(=Date(YearStart(AddYears(Max(gd_eventos_f.load_date), -1)), ''DD.MM.YYYY''))<=$(=Date(YearEnd(AddYears(Max(gd_eventos_f.load_date), -1)), ''DD.MM.YYYY''))"}>}#_valor_eventos_falta)';
 
 
 
SET valor_evento_falta_grafico = '{<gd_eventos_f.load_date = {"=$(=Date(AddMonths(Date#(MonthStart(Only(GetFieldSelections(gd_eventos_f.load_date))), ''DD.MM.YYYY''),1), ''DD.MM.YYYY''))"},ano = {"=$(=Year(Date#(Only(gd_eventos_f.load_date), ''DD.MM.YYYY'')))"}>} [#_valor_eventos_falta]';
 
SET %_indice_abono = '[#_horas_total_abonos]/[#_horas_total_jornada_mensal]';
 
SET %_indice_abono_ano_atual = 

'{<gd_eventos_f.load_date = {"=$(=Date(AddMonths(Date#(MonthStart(Only(GetFieldSelections(gd_eventos_f.load_date))), ''DD.MM.YYYY''),1), ''DD.MM.YYYY''))"},ano = {"=$(=Year(Date#(Only(gd_eventos_f.load_date), ''DD.MM.YYYY'')))"}>}[#_horas_total_abonos]

/

{<gd_eventos_f.load_date = {"=$(=Date(AddMonths(Date#(MonthStart(Only(GetFieldSelections(gd_eventos_f.load_date))), ''DD.MM.YYYY''),1), ''DD.MM.YYYY''))"},ano = {"=$(=Year(Date#(Only(gd_eventos_f.load_date), ''DD.MM.YYYY'')))"}>}[#_horas_total_jornada_mensal]';
 
 
SET %_indice_abono_ano_anterior= '{<gd_eventos_f.load_date = {"=$(=Date(AddMonths(Date#(MonthStart(Only(GetFieldSelections(gd_eventos_f.load_date))), ''DD.MM.YYYY''),1), ''DD.MM.YYYY''))"},ano = {"$(=Year(AddYears(Date#(Only(gd_eventos_f.load_date), ''DD.MM.YYYY''), -1)))"}>}[#_horas_total_abonos]

/

{<gd_eventos_f.load_date = {"=$(=Date(AddMonths(Date#(MonthStart(Only(GetFieldSelections(gd_eventos_f.load_date))), ''DD.MM.YYYY''),1), ''DD.MM.YYYY''))"},ano = {"$(=Year(AddYears(Date#(Only(gd_eventos_f.load_date), ''DD.MM.YYYY''), -1)))"}>}[#_horas_total_jornada_mensal]';
 
 
SET %YoY_indice_abono = '({<gd_eventos_f.load_date = {">=$(=Date(YearStart(Max(gd_eventos_f.load_date)), ''DD.MM.YYYY'')) <=$(=Date(YearEnd(Max(gd_eventos_f.load_date)), ''DD.MM.YYYY''))"}>} [%_indice_abono] -

{<gd_eventos_f.load_date = {">=$(=Date(YearStart(AddYears(Max(gd_eventos_f.load_date), -1)), ''DD.MM.YYYY''))<=$(=Date(YearEnd(AddYears(Max(gd_eventos_f.load_date), -1)), ''DD.MM.YYYY''))"}>}[%_indice_abono])

/

({<gd_eventos_f.load_date = {">=$(=Date(YearStart(AddYears(Max(gd_eventos_f.load_date), -1)), ''DD.MM.YYYY''))<=$(=Date(YearEnd(AddYears(Max(gd_eventos_f.load_date), -1)), ''DD.MM.YYYY''))"}>}[%_indice_abono])';
 
 
SET %MoM_indice_abono = '({<gd_eventos_f.load_date = {">=$(=Date(Monthstart(Max(gd_eventos_f.load_date)), ''DD.MM.YYYY''))<=$(=Date(MonthEnd(Max(gd_eventos_f.load_date)), ''DD.MM.YYYY''))"}>} [%_indice_abono] -

{<gd_eventos_f.load_date = {">=$(=Date(MonthStart(AddMonths(Max(gd_eventos_f.load_date), -1)), ''DD.MM.YYYY''))<=$(=Date(Monthend(AddMonths(Max(gd_eventos_f.load_date), -1)), ''DD.MM.YYYY''))"}>}[%_indice_abono])

/

({<gd_eventos_f.load_date = {">=$(=Date(MonthStart(AddMonths(Max(gd_eventos_f.load_date), -1)), ''DD.MM.YYYY''))<=$(=Date(Monthend(AddMonths(Max(gd_eventos_f.load_date), -1)), ''DD.MM.YYYY''))"}>}[%_indice_abono])';
 
 
SET %_abonos_atual_grafico= '{<gd_eventos_f.load_date = {"=$(=Date(AddMonths(Date#(MonthStart(Only(GetFieldSelections(gd_eventos_f.load_date))), ''DD.MM.YYYY''),1), ''DD.MM.YYYY''))"},ano = {"=$(=Year(Date#(Only(gd_eventos_f.load_date), ''DD.MM.YYYY'')))"}>}[#_horas_total_abonos]

/

{<gd_eventos_f.load_date = {"=$(=Date(AddMonths(Date#(MonthStart(Only(GetFieldSelections(gd_eventos_f.load_date))), ''DD.MM.YYYY''),1), ''DD.MM.YYYY''))"},ano = {"=$(=Year(Date#(Only(gd_eventos_f.load_date), ''DD.MM.YYYY'')))"}>}[#_horas_total_jornada_mensal]';
 
 
SET %_abono_anterior_grafico= '{<gd_eventos_f.load_date = {"=$(=Date(AddMonths(Date#(MonthStart(Only(GetFieldSelections(gd_eventos_f.load_date))), ''DD.MM.YYYY''),1), ''DD.MM.YYYY''))"},ano = {"$(=Year(AddYears(Date#(Only(gd_eventos_f.load_date), ''DD.MM.YYYY''), -1)))"}>}[#_horas_total_abonos]

/

{<gd_eventos_f.load_date = {"=$(=Date(AddMonths(Date#(MonthStart(Only(GetFieldSelections(gd_eventos_f.load_date))), ''DD.MM.YYYY''),1), ''DD.MM.YYYY''))"},ano = {"$(=Year(AddYears(Date#(Only(gd_eventos_f.load_date), ''DD.MM.YYYY''), -1)))"}>}[#_horas_total_jornada_mensal]';

 
TRACE >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>Iniciando carregamento medidas de Banco Horas  <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<;
 
 
SET valor_evento_saldo_banco_pago ='{<codigo_evento = {''695'',''696'',''698''}, mes_nome = {"mar*", "set*"}>} [#_valor_evento_horas_extras]';
 
SET %_colaboradores_com_saldo_banco =  'count({<tipo_evento={''Saldo Banco''}>}distinct pessoa)/count(Total distinct pessoa)';
 
SET %_MAR_SET_pgt_banco= 'If(WildMatch(Date(Max(gd_eventos_f.load_date), ''DD/MM''), ''15/03'', ''15/09''),

(Sum({1<gd_eventos_f.load_date = {">=$(=Date(Monthstart(Max(gd_eventos_f.load_date)), ''DD.MM.YYYY''))<=$(=Date(MonthEnd(Max(gd_eventos_f.load_date)), ''DD.MM.YYYY''))"},codigo_evento={''695'',''698'',''696''}>} gd_eventos_f.valor_evento_total) -

Sum({1<gd_eventos_f.load_date = {">=$(=Date(MonthStart(AddMonths(Max(gd_eventos_f.load_date), -6)), ''DD.MM.YYYY''))<=$(=Date(Monthend(AddMonths(Max(gd_eventos_f.load_date), -6)), ''DD.MM.YYYY''))"}, codigo_evento={''696'',''695'',''698''}>} gd_eventos_f.valor_evento_total))

/

Sum({1<gd_eventos_f.load_date = {">=$(=Date(MonthStart(AddMonths(Max(gd_eventos_f.load_date), -6)), ''DD.MM.YYYY''))<=$(=Date(Monthend(AddMonths(Max(gd_eventos_f.load_date), -6)), ''DD.MM.YYYY''))"}, codigo_evento={''696'',''695'',''698''}>} gd_eventos_f.valor_evento_total)

,

null()

)';
 
 
SET horas_total_saldo_banco = '{<tipo_evento= {''Saldo Banco''}>} [#_hora_total]';
 
SET horas_total_saldo_banco_positivo ='{<tipo_evento= {''Saldo Banco''}, descricao_evento={''SALDO POSITIVO''}>} [#_hora_total]';
 
SET horas_total_saldo_banco_negativo = '{<tipo_evento= {''Saldo Banco''}, descricao_evento={''SALDO NEGATIVO''}>} [#_hora_total]';
 
 
 
 
 
exit script;
 
 