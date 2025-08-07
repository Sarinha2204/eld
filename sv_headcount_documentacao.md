# Documentação Técnica

Documentação Técnica
Arquivo: sv_headcount.qvs
Última atualização: 07/08/2025 13:50:16

## Documentação Técnica do Script QlikView: `sv_headcount.qvs`

**Data da Última Atualização:** 07/08/2025 (A data pode variar dependendo da versão do script)

**1. Resumo:**

O script `sv_headcount.qvs` executa um processo ETL (Extração, Transformação e Carga) de dados de recursos humanos, consolidando informações de diversas tabelas QVD na camada "bronze" para gerar quatro tabelas finais em formato QVD na camada "silver". Essas tabelas são otimizadas para análise de headcount, desligamentos, histórico de orçamento e informações de posições.  O script inclui etapas de limpeza de dados e criação de tabelas de mapeamento para garantir a consistência dos dados.

**2. Principais Etapas:**

**2.1 Configuração Inicial:**

* Define as configurações de localização e formatação (separadores de milhar e decimal, formato de moeda, data e hora, etc.).
* Define variáveis para os caminhos das pastas das camadas de dados ("bronze", "silver", "gold", "manual_source", "ti_layer" e "external_layer").

**2.2 Carregamento de Dados Brutos:**

* Carrega dados de múltiplas tabelas QVD da camada "bronze", algumas com filtros de data (a partir de 01/01/2019).  As tabelas carregadas incluem:
    * `bz_headcount_f`
    * `bz_headcount_hist_f`
    * `bz_headcount_latest_f`
    * `bz_posicoes_f`
    * `bz_excel_hc_orcamento_historico_f`
    * `bz_headcount_offshore_f`
    * `bz_excel_posicoes_f`
    * `bz_excel_estrutura_cc_d`
    * `bz_pessoa_d`
    * `bz_hierarquia_d`
    * `bz_excel_funcao_d`
    * `bz_excel_range_salario_d`
    * `bz_excel_filial_d`
    * `bz_externo_centro_custo_d`

**2.3 Criação de Tabelas de Mapeamento:**

* Cria tabelas de mapeamento para garantir consistência e qualidade dos dados:
    * `coligada_d`: Mapeamento de códigos de coligadas para seus nomes.
    * `CLASSIFICAÇÃO_MAP`: Mapeamento de tipos de demissão para classificação (voluntário/involuntário).
    * `MAP_EVENTOS`: Mapeamento de códigos de eventos para seus tipos.
    * `Map_funcao`: Mapeamento de códigos de função para seus nomes (incluindo transformações como capitalização).


**2.4 Transformação e Preparação de Dados:**

* Realiza diversas transformações, incluindo:
    * Cálculo de campos derivados (idade, tempo de empresa, etc.).
    * Capitalização de nomes e formatação de datas.
    * Limpeza e tratamento de dados inconsistentes.
    * Junções (`JOIN` e `LEFT JOIN`) entre tabelas.
    * Filtragem de registros.
    * Criação e uso de tabelas temporárias (`headcount_temp_1`, `headcount_temp_2`, `termination_temp_1`, `termination_temp_2`, `Temp_Clean`, `Positions_Monthly`, `bz_admitidos_demitidos_temp`).


**2.5 Geração de Tabelas Finais:**

* Gera as tabelas finais em formato QVD na camada "silver":
    * `sv_headcount_f`: Dados consolidados de headcount.
    * `sv_termination_f`: Dados de desligamentos de funcionários.
    * `sv_excel_hc_orcamento_historico_f`: Histórico de orçamento de headcount.
    * `sv_posicoes_f`: Informações de posições.

**2.6 Armazenamento dos Resultados:**

* Armazena as tabelas finais como arquivos QVD na camada "silver".

**2.7 Limpeza de Dados:**

* Remove tabelas temporárias e dados brutos não mais necessários.

**2.8 Finalização do Script:**

* O comando `Exit Script` encerra a execução.


**3. Observações:**

O script utiliza diversas funções do QlikView para manipulação de dados, como `LOAD`, `JOIN`, `CONCATENATE`, `IF`, `MATCH`
`APPLYMAP`, `FirstSortedValue`, `AutoNumberHash128`, `Peek`, `KeepChar`, `Trim`, `Capitalize`, `MonthEnd`, `MonthStart`,
`AddMonths`, etc. A complexidade reflete um processo ETL robusto para a preparação dos dados de RH para análise.  Esta documentação 
descreve o script sem oferecer sugestões de melhoria. As datas de atualização registradas no cabeçalho do script podem ser 
diferentes da data real de atualização do código.
