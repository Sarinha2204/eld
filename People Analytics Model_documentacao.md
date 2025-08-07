# Documentação Técnica

Documentação Técnica
Arquivo: People Analytics Model.qvs
Última atualização: 07/08/2025 13:50:00

## Documentação Técnica do Script QlikView: People Analytics Model.qvs

**Nome do Arquivo:** People Analytics Model.qvs

**Data e Hora da Última Atualização:** 07/08/2025 10:01:00 (ou a data mais recente se houver atualização)


**1. Resumo:**

Este script QlikView carrega e transforma dados para um modelo de *People Analytics*, consolidando informações de diversas fontes QVD localizadas em diferentes camadas de dados (Bronze, Silver, Gold, fontes manuais, TI e externas). O processo inicia com a definição de configurações de ambiente (formatação de números, datas, localidade etc., em português-Brasil),  seguido pelo carregamento de dados em tabelas de fatos e dimensões.  Uma tabela de *link* é criada para relacionar fatos e dimensões através de chaves comuns geradas pela função `AutoNumberHash128`.  Finalmente, campos redundantes são removidos das tabelas de fatos após a criação da tabela de *link*, otimizando o desempenho e o uso de memória.


**2. Principais Etapas:**

**2.1 Configuração do Ambiente:**

* Define variáveis para configurações regionais (separadores de milhar e decimal, formatos de moeda, hora, data e timestamp, primeiro dia da semana, tratamento de semanas incompletas, dia de referência, primeiro mês do ano e localidade: pt-BR).
* Define variáveis de caminho para diferentes pastas de dados, representando camadas de dados (bronze_layer, silver_layer, gold_layer, manual_source, ti_layer e external_layer). Essas variáveis são usadas para especificar a localização dos arquivos QVD.


**2.2 Carregamento de Tabelas de Fatos:**

* Carrega dados de vários arquivos QVD para as seguintes tabelas de fatos:
    * `gd_headcount_f` (Headcount)
    * `gd_termination_f` (Terminações)
    * `gd_excel_orcamento_historico_f` (Histórico de Orçamento em Excel)
    * `gd_posicoes_f` (Posições)
    * `gd_eventos_f` (Eventos)
    * `gd_custo_origem_opex_f` (Custo Origem OPEX)
    * `gd_producao_celulose_f` (Produção de Celulose)
    * `gd_vendas_celulose_f` (Vendas de Celulose)
    * `gd_receita_liquida_f` (Receita Líquida)
* Gera uma chave de ligação única (`link_key`) para cada tabela de fatos utilizando a função `AutoNumberHash128`, baseada em campos-chave de cada tabela. Esta chave é fundamental para a ligação entre fatos e dimensões.
* Utiliza `Qualify` e `Unqualify` para gerenciar nomes de campos, evitando conflitos e criando aliases para consistência (ex: `pessoa_hc`, `pessoa_to`).


**2.3 Carregamento de Tabelas de Dimensões:**

* Carrega dados de arquivos QVD para as seguintes tabelas de dimensões:
    * `gd_calendario_d` (Calendário)
    * `gd_hierarquia_d` (Hierarquia)
    * `gd_funcao_d` (Função)
    * `gd_eldorado_entity_d` (Entidade Eldorado)
    * `gd_employee_d` (Funcionários)
    * `gd_situacao_d` (Situação)
    * `gd_tipo_funcionario_d` (Tipo de Funcionário)
    * `gd_esclada_d` (Escalada)
    * `gd_idade_d` (Idade)
    * `gd_contratacao_tipo_d` (Tipo de Contratação)
    * `gd_tempo_companhia_d` (Tempo na Companhia)
    * `gd_centro_de_custo_d` (Centro de Custo)
    * `gd_secao_d` (Seção)
    * `gd_status_d` (Status)
    * `gd_evento_d` (Evento)
    * `gd_conta_contabil_d` (Conta Contábil)
    * `gd_custo_base_d` (Custo Base)
    * `gd_custo_fonte_d` (Custo Fonte)
* As dimensões são carregadas sem qualificação (`Unqualify *;`) para simplificar a junção com as tabelas de fatos.


**2.4 Criação da Tabela de Link:**

* Cria uma tabela de link (`Link`) que contém as chaves únicas (`link_key`) e outras chaves relevantes de todas as tabelas de fatos.  A construção da tabela `Link` utiliza `LOAD DISTINCT` e `RESIDENT` para carregar apenas valores distintos das chaves, otimizando o tamanho da tabela e garantindo a eficiência das junções.  O script trata campos ausentes preenchendo-os com strings vazias.


**2.5 Limpeza:**

* Remove campos desnecessários das tabelas de fatos após a construção da tabela de *link*, otimizando o uso da memória e removendo redundâncias.


**2.6 Saída do Script:**

* Finaliza a execução do script com `exit script;`.


**3. Notas Adicionais:**

* O script pressupõe que todos os arquivos QVD referenciados existam nos caminhos especificados nas variáveis `SET`.
* Os caminhos definidos nas variáveis `SET` devem ser ajustados de acordo com a localização dos arquivos QVD no ambiente.
* A tabela `Link` é crucial para a associação correta entre fatos e dimensões no modelo de dados.
* O script está configurado para o ambiente Brasileiro (pt-BR).
* Algumas tabelas de dimensão (ex: `gd_conta_debito_d`, `gd_centro_lucro_d`) estão comentadas no script.
* O script utiliza a função `AutoNumberHash128` para gerar chaves únicas, garantindo integridade referencial.
