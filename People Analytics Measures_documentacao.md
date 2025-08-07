# Documentação Técnica

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
