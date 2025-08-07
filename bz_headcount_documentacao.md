# Documentação Técnica

Documentação Técnica
Arquivo: bz_headcount.qvs
Última atualização: 07/08/2025 13:49:14

## Documentação Técnica do Script QVS: bz_headcount.qvs

**Data:** 07/08/2025

**Versão:** 1.0

**Autor:** (Nome do Autor - a ser preenchido)


**1. Resumo:**

Este script QlikView (QVS) carrega e processa dados de recursos humanos (headcount) de múltiplas fontes,  incluindo arquivos QVD e planilhas Excel.  As fontes de dados abrangem informações diversas, como dados históricos e atuais de headcount, detalhes de funcionários, hierarquia organizacional, funções, filiais, salários, centros de custo e informações sobre posições (ocupadas e vagas).  O script estrutura os dados em tabelas individualizadas, todas prefixadas com "bz_", e os armazena em uma camada bronze, em arquivos QVD separados. Após o carregamento e armazenamento em QVD, as tabelas são descartadas da memória do QlikView para otimizar o uso de recursos.  O script inclui a definição de variáveis para gerenciamento de caminhos de diretórios e formatação de dados.


**2. Principais Etapas:**

**2.1 Configuração Inicial:**

*   O script inicia definindo parâmetros de configuração de formato de dados: separadores de milhar e decimal, formato monetário, formato de data, hora e timestamp, primeiro dia da semana, tratamento de semanas incompletas, dia de referência, primeiro mês do ano, localização, criação de índice de busca e nomes de meses e dias da semana (abreviados e completos).
*   Define variáveis de caminho para os diretórios das fontes de dados: `bronze_layer`, `silver_layer`, `gold_layer`, `manual_source`, `ti_layer` e `external_layer`.  Observa-se que as definições originais das variáveis de caminho foram comentadas e substituídas por novas definições.


**2.2 Carregamento e Armazenamento de Dados de Headcount (Fatos):**

*   **`bz_headcount_f`:** Carrega dados do arquivo `0STA_RHRMV012_001.qvd` (localizado em `$(ti_layer)`), armazena em um arquivo QVD individual e descarta a tabela da memória.
*   **`bz_headcount_hist_f`:** Carrega dados históricos de headcount da planilha `hc_historica_f.xlsx` (localizada em `$(manual_source)`), armazena em um arquivo QVD e descarta a tabela da memória.
*   **`bz_headcount_latest_f`:** Carrega os dados mais recentes de headcount do arquivo `0STA_DRMFUNSAL_001.qvd` (localizado em `$(ti_layer)`).  Renomeia a coluna `[Funcionário (Salário)]` para `[Funcionário]` e adiciona a coluna `[Funcionário TEXT]`. Armazena em QVD e descarta a tabela da memória.
*   **`bz_movimentos_f`:** Carrega dados de movimentos de funcionários do arquivo `0STA_RHRMV043_001.qvd` (localizado em `$(ti_layer)`), armazena em QVD e descarta a tabela.
*   **`bz_posicoes_f`:** Carrega dados de posições do arquivo `0STA_RHRMV033_001.qvd` (localizado em `$(ti_layer)`), armazena em QVD e descarta a tabela.
*   **`bz_headcount_offshore_f`:** Carrega dados de headcount offshore do arquivo `0STA_RHRMV046_001.qvd` (localizado em `$(ti_layer)`), armazena em QVD e descarta a tabela.
*   **`bz_excel_posicoes_f`:** Carrega dados de posições abertas da planilha `posicoes_abertas.xlsx` (localizada em `$(manual_source)`), armazena em QVD e descarta a tabela.
*   **`bz_excel_hc_orcamento_historico_f`:** Carrega dados do histórico de orçamento de headcount da planilha `hc_orcamento_historico.xlsx` (localizada em `$(manual_source)`), armazena em QVD e descarta a tabela.


**2.3 Carregamento e Armazenamento de Dados Dimensionais:**

*   **`bz_pessoa_d`:** Carrega informações de funcionários do arquivo `0STA_DRMPESSOA_001.qvd` (localizado em `$(ti_layer)`), armazena em QVD e descarta a tabela.
*   **`bz_hierarquia_d`:** Carrega dados de hierarquia do arquivo `0STA_RHRMV007_001.qvd` (localizado em `$(ti_layer)`), armazena em QVD e descarta a tabela.
*   **`bz_excel_funcao_d`:** Carrega dados de funções da planilha `funcoes_d.xlsx` (localizada em `$(manual_source)`), armazena em QVD e descarta a tabela.
*   **`bz_excel_filial_d`:** Carrega dados de filiais da planilha `filial_d.xlsx` (localizada em `$(manual_source)`), armazena em QVD e descarta a tabela.
*   **`bz_excel_salario_d`:** Carrega dados de tabelas salariais da planilha `tabela_salarial_d.xlsx` (localizada em `$(manual_source)`), armazena em QVD e descarta a tabela.
*   **`bz_excel_estrutura_cc_d`:** Carrega dados da estrutura de centro de custo da planilha `centro_de_custo_d.xlsx` (localizada em `$(manual_source)`), armazena em QVD e descarta a tabela.
*   **`bz_externo_centro_custo_d`:** Carrega dados de centro de custo externo do arquivo `TRFN_CC.CL.qvd` (localizado em `$(external_layer)`), armazena em QVD e descarta a tabela.


**2.4 Armazenamento em QVDs e Limpeza:**

*   Todos os dados carregados são armazenados em arquivos QVD individuais no diretório especificado pela variável `$(bronze_layer)`.
*   Todas as tabelas carregadas são descartadas da memória do QlikView após o armazenamento, utilizando a instrução `DROP TABLE`.


**2.5 Encerramento:**

*   O script finaliza com a instrução `EXIT Script`.  Um bloco de código comentado, aparentemente relacionado a um carregamento de dados de histórico de orçamento, foi removido do script.


**3. Observações:**

*   O script apresenta comentários indicando fontes de dados antigas que foram substituídas.
*   A documentação reflete o estado do script na data e hora da última atualização.


**4. Diagrama de Fluxo (opcional):**  A inclusão de um diagrama de fluxo seria benéfica para a visualização do processo.

**5. Glossário de Termos (opcional):**  Um glossário definindo os termos técnicos usados (nomes de tabelas, campos e abreviações) aumentaria a clareza da documentação.
