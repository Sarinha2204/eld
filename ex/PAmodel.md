# Documentação Técnica

**Arquivo:** `People Analytics Model.qvs`  
**Última atualização:** 07/08/2025 14:40:23

## Documentação Técnica do Script QlikView: People Analytics Model.qvs

**Nome do Arquivo:** People Analytics Model.qvs

**Data e Hora da Última Atualização:** 07/08/2025 13:50:00 (ou data mais recente se houver atualização)


**1. Resumo:**

Este script QlikView carrega e transforma dados para um modelo de *People Analytics*, integrando informações de diversas fontes QVD organizadas em camadas de dados (Bronze, Silver, Gold, fontes manuais, TI e externas). O script inicia configurando o ambiente (formatação de números, datas, localidade etc., em português-Brasil),  carrega dados em tabelas de fatos e dimensões, cria uma tabela de *link* para relacionar fatos e dimensões por meio de chaves únicas geradas pela função `AutoNumberHash128`, e finalmente remove campos redundantes das tabelas de fatos para otimizar desempenho e uso de memória.


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

* Cria uma tabela de link (`Link`) que contém as chaves únicas (`link_key`) e outras chaves relevantes de todas as tabelas de fatos. A construção da tabela `Link` utiliza `LOAD DISTINCT` e `RESIDENT` para carregar apenas valores distintos das chaves, otimizando o tamanho da tabela e garantindo a eficiência das junções. O script trata campos ausentes preenchendo-os com strings vazias.


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
* A função `AutoNumberHash128` garante a criação de chaves únicas para a integridade referencial do modelo.

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

Documentação Técnica
Arquivo: People Analytics Model.qvs
Última atualização: 07/08/2025 13:25:32
## Documentação Técnica do Script QlikView: People Analytics Model.qvs

**Nome do Arquivo:** People Analytics Model.qvs

**Data e Hora da Última Atualização:** 07/08/2025 13:12:24 (considerando a última atualização no script fornecido)

**1. Resumo:**

Este script QlikView carrega e transforma dados para um modelo de *People Analytics*, consolidando informações de diversas fontes QVD. O processo inicia com a definição de configurações de ambiente (formatação de números, datas, localidade etc.),  e o carregamento de dados em tabelas de fatos e dimensões.  Uma tabela de *link* é crucialmente criada para relacionar fatos e dimensões através de chaves comuns geradas pela função `AutoNumberHash128`. Por fim, campos redundantes são removidos das tabelas de fatos após a criação da tabela de *link*, otimizando o desempenho e o uso de memória.  O script está configurado para o ambiente Brasileiro (pt-BR).

**2. Principais Etapas:**

**2.1 Configuração do Ambiente:**

* Define variáveis para configurações regionais: separadores de milhar e decimal, formatos de moeda, hora, data e timestamp, primeiro dia da semana, tratamento de semanas incompletas, dia de referência, primeiro mês do ano e localidade (pt-BR).
* Define variáveis de caminho para diferentes pastas de dados, representando camadas de dados (bronze, silver, gold, manual_source, ti_layer e external_layer). Essas variáveis são usadas para especificar a localização dos arquivos QVD.


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
* Gera uma chave de ligação única (`link_key`) para cada tabela de fatos utilizando a função `AutoNumberHash128`, baseada em campos-chave de cada tabela.  Esta chave é fundamental para a ligação entre fatos e dimensões.
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

* Cria uma tabela de link (`Link`) que contém as chaves únicas (`link_key`) e outras chaves relevantes de todas as tabelas de fatos.  A construção da tabela `Link` utiliza `LOAD DISTINCT` e `RESIDENT` para carregar apenas valores distintos das chaves, otimizando o tamanho da tabela e garantindo a eficiência das junções.
* Padroniza os nomes dos campos e preenche campos ausentes com strings vazias para garantir consistência.


**2.5 Limpeza:**

* Remove campos desnecessários das tabelas de fatos após a construção da tabela de link, otimizando o uso da memória e removendo redundâncias.


**2.6 Saída do Script:**

* Finaliza a execução do script com `exit script;`.


**3. Notas Adicionais:**

* O script pressupõe que todos os arquivos QVD referenciados existam nos caminhos especificados nas variáveis `SET`.
* Os caminhos definidos nas variáveis `SET` devem ser ajustados de acordo com a localização dos arquivos QVD no ambiente.
* A tabela `Link` é crucial para a associação correta entre fatos e dimensões no modelo de dados.
* O script é otimizado para recarregamento em ambientes Qlik Sense Enterprise.

Documentação Técnica
Arquivo: People Analytics Model.qvs
Última atualização: 07/08/2025 13:12:24
## Documentação Técnica do Script QlikView: People Analytics Model.qvs

**Nome do Arquivo:** People Analytics Model.qvs

**Data e Hora da Última Atualização:** 07/08/2025 12:51:25 (considerando a última atualização no script fornecido)


**1. Resumo:**

Este script QlikView carrega e transforma dados para um modelo de People Analytics, consolidando informações de diversas fontes QVD. O processo envolve a definição de configurações de ambiente (formatação de números, datas, localidade etc.), o carregamento de dados em tabelas de fatos e dimensões, a criação de uma tabela de link para relacionar os fatos e dimensões através de chaves comuns, e a remoção de campos redundantes das tabelas de fatos após a criação da tabela de link para otimização do desempenho. O script está configurado para o ambiente Brasileiro (pt-BR).


**2. Principais Etapas:**

**2.1 Configuração do Ambiente:**

* Define variáveis para separadores de milhar e decimal, formatos de moeda, hora, data e timestamp, primeiro dia da semana, tratamento de semanas incompletas, dia de referência, primeiro mês do ano e localidade (pt-BR).
* Define variáveis de caminho para diferentes pastas de dados, representando camadas (bronze, silver, gold, manual_source, ti_layer e external_layer).  Essas variáveis são usadas para especificar a localização dos arquivos QVD.


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
* Gera uma chave de ligação única (`link_key`) para cada tabela de fatos utilizando a função `AutoNumberHash128`, baseada em campos-chave de cada tabela.  Esta chave é fundamental para a ligação entre fatos e dimensões.
* Emprega `Qualify` e `Unqualify` para gerenciar nomes de campos, evitando conflitos e criando aliases para consistência (ex: `pessoa_hc`, `pessoa_to`).


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

* Cria uma tabela de link (`Link`) que contém as chaves únicas (`link_key`) e outras chaves relevantes de todas as tabelas de fatos.
* Usa `LOAD DISTINCT` e `RESIDENT` para carregar apenas valores distintos das chaves, otimizando o tamanho da tabela.
* Padroniza os nomes dos campos e preenche campos ausentes com strings vazias para garantir consistência.


**2.5 Limpeza:**

* Remove campos desnecessários das tabelas de fatos após a construção da tabela de link, otimizando o uso da memória e removendo redundâncias.


**2.6 Saída do Script:**

* Finaliza a execução do script com `exit script;`.


**3. Notas Adicionais:**

* O script pressupõe que todos os arquivos QVD referenciados existam nos caminhos especificados.
* Os caminhos definidos nas variáveis `SET` devem ser ajustados de acordo com a localização dos arquivos QVD no ambiente.
* A tabela `Link` é crucial para a associação correta entre fatos e dimensões no modelo de dados.
* O script é otimizado para recarregamento em ambientes Qlik Sense Enterprise.

Documentação Técnica
Arquivo: People Analytics Model.qvs
Última atualização: 07/08/2025 12:51:25
## Documentação Técnica do Script QlikView: People Analytics Model.qvs

**Última atualização:** 06/08/2025 13:05:51


**1. Resumo:**

Este script QlikView carrega e transforma dados para um modelo de People Analytics.  Ele define variáveis para caminhos de arquivos, carrega dados de arquivos QVD (QlikView Data) em tabelas de fatos e dimensões, cria uma tabela de link para conectar fatos e dimensões com base em chaves comuns, e otimiza o modelo removendo campos redundantes das tabelas de fatos após a criação da tabela de link. O script está configurado para o ambiente Brasileiro, utilizando formatação e localidade específica.


**2. Principais Etapas:**

**2.1 Configuração do Ambiente:**

* Define os separadores de milhar e decimal para números, o formato de moeda, horário, data e timestamp,  o primeiro dia da semana, o tratamento de semanas incompletas, o dia de referência, o primeiro mês do ano e a localidade (pt-BR).
* Define variáveis para os caminhos das pastas de diferentes camadas de dados:  `bronze_layer`, `silver_layer`, `gold_layer`, `manual_source`, `ti_layer` e `external_layer`.  Estas variáveis são usadas para especificar a localização dos arquivos QVD.


**2.2 Carregamento das Tabelas de Fatos:**

* Carrega dados de diversos arquivos QVD para as seguintes tabelas de fatos:
    * `gd_headcount_f` (Headcount)
    * `gd_termination_f` (Terminações)
    * `gd_excel_orcamento_historico_f` (Histórico de Orçamento em Excel)
    * `gd_posicoes_f` (Posições)
    * `gd_eventos_f` (Eventos)
    * `gd_custo_origem_opex_f` (Custo Origem OPEX)
    * `gd_producao_celulose_f` (Produção de Celulose)
    * `gd_vendas_celulose_f` (Vendas de Celulose)
    * `gd_receita_liquida_f` (Receita Líquida)
* Gera uma chave de ligação única (`link_key`) para cada tabela de fatos usando a função `AutoNumberHash128`.  Esta chave é crucial para a ligação entre fatos e dimensões.
* Utiliza `Qualify` e `Unqualify` para gerenciar o escopo dos nomes dos campos, evitando conflitos.  Cria aliases para garantir consistência nos nomes de campos em diferentes tabelas de fatos (ex: pessoa_hc, pessoa_to).


**2.3 Carregamento das Tabelas de Dimensões:**

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
*  As tabelas de dimensões são carregadas sem qualificação (`Unqualify *;`) para facilitar a junção com as tabelas de fatos.


**2.4 Criação da Tabela de Link:**

* Constrói uma tabela de link (`Link`) consolidada contendo as chaves únicas (`link_key`) e outras chaves relevantes de todas as tabelas de fatos.  
* Utiliza `LOAD DISTINCT` e `RESIDENT` para carregar apenas os valores distintos das chaves, otimizando o tamanho da tabela.
* Padroniza os nomes dos campos e preenche campos ausentes com strings vazias para garantir consistência.


**2.5 Limpeza:**

* Remove campos desnecessários das tabelas de fatos após a construção da tabela de link.  Isso otimiza o uso de memória e evita a redundância de chaves sintéticas.


**2.6 Saída do Script:**

* Finaliza a execução do script com `exit script;` após a conclusão de todas as etapas de carregamento e transformação de dados.


**3. Notas Adicionais:**

* O script assume que todos os arquivos QVD referenciados nas variáveis de caminho existem e estão atualizados.
* Os caminhos especificados nas variáveis `SET` devem ser ajustados de acordo com a localização dos arquivos QVD no ambiente de destino.
* A tabela `Link` é fundamental para a correta associação entre fatos e dimensões no modelo de dados.
* Este script é otimizado para recarregamento em ambientes Qlik Sense Enterprise.

Documentação Técnica
Arquivo: People Analytics Model.qvs
Última atualização: 07/08/2025 12:39:56


Documentação Técnica
Arquivo: People Analytics Model.qvs
Última atualização: 07/08/2025 12:33:41








Documentação Técnica do Script QlikView

## Nome do Arquivo
**People Analytics Model.qvs**

## Data e Hora da Última Atualização
**07/08/2025 10:01:00**

## Resumo do que o Script Faz
Este script carrega e transforma dados para o modelo de People Analytics. Ele define variáveis para caminhos de arquivos e carrega dados de arquivos QVD em tabelas de fatos e dimensões. Uma tabela de link é criada para associar os fatos com base em chaves comuns, facilitando a análise e a visualização dos dados.

## Principais Etapas

1. **Configuração do Ambiente**:
   - Define formatos numéricos, de data e hora, além de configurações de localidade para o Brasil.
   - Especifica os caminhos para diferentes camadas de dados (bronze, silver, gold, fontes manuais, TI e externas).

2. **Carregamento das Tabelas de Fatos**:
   - Carrega as principais tabelas de fatos, como:
     - `gd_headcount_f` (Tabela de Headcount)
     - `gd_termination_f` (Tabela de Terminações)
     - `gd_excel_orcamento_historico_f` (Tabela de Histórico de Orçamento)
     - `gd_posicoes_f` (Tabela de Posições)
     - `gd_eventos_f` (Tabela de Eventos)
     - `gd_custo_origem_opex_f` (Tabela de Custo Origem Opex)
     - `gd_producao_celulose_f` (Tabela de Produção de Celulose)
     - `gd_vendas_celulose_f` (Tabela de Vendas de Celulose)
     - `gd_receita_liquida_f` (Tabela de Receita Líquida)
   - Gera chaves de link únicas usando a função `AutoNumberHash128` para vinculação dos dados.

3. **Carregamento das Tabelas de Dimensões**:
   - Carrega tabelas de dimensões relevantes, como:
     - `gd_calendario_d` (Tabela de Calendário)
     - `gd_hierarquia_d` (Tabela de Hierarquia)
     - `gd_funcao_d` (Tabela de Função)
     - `gd_eldorado_entity_d` (Tabela de Entidade Eldorado)
     - `gd_employee_d` (Tabela de Funcionários)
     - `gd_situacao_d` (Tabela de Situação)
     - `gd_tipo_funcionario_d` (Tabela de Tipo de Funcionário)
     - `gd_esclada_d` (Tabela de Escalada)
     - `gd_idade_d` (Tabela de Idade)
     - `gd_contratacao_tipo_d` (Tabela de Tipo de Contratação)
     - `gd_tempo_companhia_d` (Tabela de Tempo na Companhia)
     - `gd_centro_de_custo_d` (Tabela de Centro de Custo)
     - `gd_secao_d` (Tabela de Seção)
     - `gd_status_d` (Tabela de Status)
     - `gd_evento_d` (Tabela de Evento)
     - `gd_conta_contabil_d` (Tabela de Conta Contábil)
     - `gd_custo_base_d` (Tabela de Custo Base)
     - `gd_custo_fonte_d` (Tabela de Custo Fonte)

4. **Criação da Tabela de Link**:
   - Constrói uma tabela de link consolidada, unindo chaves distintas de todas as tabelas de fatos.

5. **Limpeza**:
   - Remove campos desnecessários das tabelas de fatos após a criação da tabela de link para otimizar o uso de memória e evitar chaves sintéticas.

6. **Saída do Script**:
   - Finaliza a execução do script após a conclusão do carregamento e transformação dos dados.

TextBlock(citations=None, text='Documentação Técnica do Script QlikView\n\n## Nome do Arquivo\n**People Analytics Model.qvs**\n\n## Data e Hora da Última Atualização\n**07/08/2025 09:46:50**\n\n## Descrição do que o Script Faz\nEste script carrega e transforma dados para o modelo de People Analytics. Ele define variáveis para caminhos de arquivos e carrega dados de arquivos QVD em tabelas de fatos e dimensões. Uma tabela de link é criada para associar os fatos com base em chaves comuns, facilitando a análise e a visualização dos dados.\n\n## Lista Resumida dos Principais Componentes e Etapas\n\n1. **Configuração do Ambiente**:\n   - Define formatos numéricos, de data e hora, além de configurações de localidade para o Brasil.\n   - Especifica os caminhos para diferentes camadas de dados (bronze, silver, gold, fontes manuais, TI e externas).\n\n2. **Carregamento das Tabelas de Fatos**:\n   - Carrega as principais tabelas de fatos, como:\n     - `gd_headcount_f` (Tabela de Headcount)\n     - `gd_termination_f` (Tabela de Terminações)\n     - `gd_excel_orcamento_historico_f` (Tabela de Histórico de Orçamento)\n     - `gd_posicoes_f` (Tabela de Posições)\n     - `gd_eventos_f` (Tabela de Eventos)\n     - `gd_custo_origem_opex_f` (Tabela de Custo Origem Opex)\n     - `gd_producao_celulose_f` (Tabela de Produção de Celulose)\n     - `gd_vendas_celulose_f` (Tabela de Vendas de Celulose)\n     - `gd_receita_liquida_f` (Tabela de Receita Líquida)\n   - Gera chaves de link únicas usando a função `AutoNumberHash128` para vinculação dos dados.\n\n3. **Carregamento das Tabelas de Dimensões**:\n   - Carrega tabelas de dimensões relevantes, como:\n     - `gd_calendario_d` (Tabela de Calendário)\n     - `gd_hierarquia_d` (Tabela de Hierarquia)\n     - `gd_funcao_d` (Tabela de Função)\n     - `gd_eldorado_entity_d` (Tabela de Entidade Eldorado)\n     - `gd_employee_d` (Tabela de Funcionários)\n     - `gd_situacao_d` (Tabela de Situação)\n     - `gd_tipo_funcionario_d` (Tabela de Tipo de Funcionário)\n     - `gd_esclada_d` (Tabela de Escalada)\n     - `gd_idade_d` (Tabela de Idade)\n     - `gd_contratacao_tipo_d` (Tabela de Tipo de Contratação)\n     - `gd_tempo_companhia_d` (Tabela de Tempo na Companhia)\n     - `gd_centro_de_custo_d` (Tabela de Centro de Custo)\n     - `gd_secao_d` (Tabela de Seção)\n     - `gd_status_d` (Tabela de Status)\n     - `gd_evento_d` (Tabela de Evento)\n     - `gd_conta_contabil_d` (Tabela de Conta Contábil)\n     - `gd_custo_base_d` (Tabela de Custo Base)\n     - `gd_custo_fonte_d` (Tabela de Custo Fonte)\n\n4. **Criação da Tabela de Link**:\n   - Constrói uma tabela de link consolidada, unindo chaves distintas de todas as', type='text')

TextBlock(citations=None, text='Documentação Técnica do Script QlikView\n\n## Nome do Arquivo\n**People Analytics Model.qvs**\n\n## Data e Hora da Última Atualização\n**07/08/2025 09:32:51**\n\n## Descrição do que o Script Faz\nEste script carrega e transforma dados para o modelo de People Analytics. Ele define variáveis para caminhos de arquivos e carrega dados de arquivos QVD em tabelas de fatos e dimensões. Uma tabela de link é criada para associar os fatos com base em chaves comuns, facilitando a análise e a visualização dos dados.\n\n## Lista Resumida dos Principais Componentes e Etapas\n\n1. **Configuração do Ambiente**:\n   - Define formatos numéricos, de data e hora, além de configurações de localidade para o Brasil.\n   - Especifica os caminhos para diferentes camadas de dados (bronze, silver, gold, fontes manuais, TI e externas).\n\n2. **Carregamento das Tabelas de Fatos**:\n   - Carrega as principais tabelas de fatos, como:\n     - `gd_headcount_f` (Tabela de Headcount)\n     - `gd_termination_f` (Tabela de Terminações)\n     - `gd_excel_orcamento_historico_f` (Tabela de Histórico de Orçamento)\n     - `gd_posicoes_f` (Tabela de Posições)\n     - `gd_eventos_f` (Tabela de Eventos)\n     - `gd_custo_origem_opex_f` (Tabela de Custo Origem Opex)\n     - `gd_producao_celulose_f` (Tabela de Produção de Celulose)\n     - `gd_vendas_celulose_f` (Tabela de Vendas de Celulose)\n     - `gd_receita_liquida_f` (Tabela de Receita Líquida)\n   - Gera chaves de link únicas usando a função `AutoNumberHash128` para vinculação dos dados.\n\n3. **Carregamento das Tabelas de Dimensões**:\n   - Carrega tabelas de dimensões relevantes, como:\n     - `gd_calendario_d` (Tabela de Calendário)\n     - `gd_hierarquia_d` (Tabela de Hierarquia)\n     - `gd_funcao_d` (Tabela de Função)\n     - `gd_eldorado_entity_d` (Tabela de Entidade Eldorado)\n     - `gd_employee_d` (Tabela de Funcionários)\n     - `gd_situacao_d` (Tabela de Situação)\n     - `gd_tipo_funcionario_d` (Tabela de Tipo de Funcionário)\n     - `gd_esclada_d` (Tabela de Escalada)\n     - `gd_idade_d` (Tabela de Idade)\n     - `gd_contratacao_tipo_d` (Tabela de Tipo de Contratação)\n     - `gd_tempo_companhia_d` (Tabela de Tempo na Companhia)\n     - `gd_centro_de_custo_d` (Tabela de Centro de Custo)\n     - `gd_secao_d` (Tabela de Seção)\n     - `gd_status_d` (Tabela de Status)\n     - `gd_evento_d` (Tabela de Evento)\n     - `gd_conta_contabil_d` (Tabela de Conta Contábil)\n     - `gd_custo_base_d` (Tabela de Custo Base)\n     - `gd_custo_fonte_d` (Tabela de Custo Fonte)\n\n4. **Criação da Tabela de Link**:\n   - Constrói uma tabela de link consolidada, unindo chaves distintas de todas as', type='text')

# Documentação Técnica do Script QlikView

## Nome do Arquivo
**People Analytics Model.qvs**

## Data e Hora da Última Atualização
**06/08/2025 13:05:51**

## Descrição do que o Script Faz
Este script carrega e transforma dados para o modelo de People Analytics. Ele define variáveis para caminhos de arquivos e carrega dados de arquivos QVD em tabelas de fatos e dimensões. Uma tabela de link é criada para associar os fatos com base em chaves comuns, facilitando a análise e a visualização dos dados.

## Lista Resumida dos Principais Componentes e Etapas

1. **Configuração do Ambiente**:
   - Define formatos numéricos, de data e hora, além de configurações de localidade para o Brasil.
   - Especifica os caminhos para diferentes camadas de dados (bronze, silver, gold, fontes manuais, TI e externas).

2. **Carregamento das Tabelas de Fatos**:
   - Carrega as principais tabelas de fatos, como:
     - `gd_headcount_f` (Tabela de Headcount)
     - `gd_termination_f` (Tabela de Terminações)
     - `gd_excel_orcamento_historico_f` (Tabela de Histórico de Orçamento)
     - `gd_posicoes_f` (Tabela de Posições)
     - `gd_eventos_f` (Tabela de Eventos)
     - `gd_custo_origem_opex_f` (Tabela de Custo Origem Opex)
     - `gd_producao_celulose_f` (Tabela de Produção de Celulose)
     - `gd_vendas_celulose_f` (Tabela de Vendas de Celulose)
     - `gd_receita_liquida_f` (Tabela de Receita Líquida)
   - Gera chaves de link únicas usando a função `AutoNumberHash128` para vinculação dos dados.

3. **Carregamento das Tabelas de Dimensões**:
   - Carrega tabelas de dimensões relevantes, como:
     - `gd_calendario_d` (Tabela de Calendário)
     - `gd_hierarquia_d` (Tabela de Hierarquia)
     - `gd_funcao_d` (Tabela de Função)
     - `gd_eldorado_entity_d` (Tabela de Entidade Eldorado)
     - `gd_employee_d` (Tabela de Funcionários)
     - `gd_situacao_d` (Tabela de Situação)
     - `gd_tipo_funcionario_d` (Tabela de Tipo de Funcionário)
     - `gd_esclada_d` (Tabela de Escalada)
     - `gd_idade_d` (Tabela de Idade)
     - `gd_contratacao_tipo_d` (Tabela de Tipo de Contratação)
     - `gd_tempo_companhia_d` (Tabela de Tempo na Companhia)
     - `gd_centro_de_custo_d` (Tabela de Centro de Custo)
     - `gd_secao_d` (Tabela de Seção)
     - `gd_status_d` (Tabela de Status)
     - `gd_evento_d` (Tabela de Evento)
     - `gd_conta_contabil_d` (Tabela de Conta Contábil)
     - `gd_custo_base_d` (Tabela de Custo Base)
     - `gd_custo_fonte_d` (Tabela de Custo Fonte)

4. **Criação da Tabela de Link**:
   - Constrói uma tabela de link consolidada, unindo chaves distintas de todas as tabelas de fatos.
   - Padroniza os nomes dos campos e preenche campos ausentes com strings vazias para consistência do modelo.

5. **Limpeza**:
   - Remove campos desnecessários das tabelas de fatos após a criação da tabela de link para otimizar o uso de memória e evitar chaves sintéticas.

6. **Saída do Script**:
   - Finaliza a execução do script após a conclusão do carregamento e transformação dos dados.

## Notas Adicionais
- É importante garantir que todos os arquivos QVD estejam presentes nos caminhos especificados na camada gold.
- Ajustar as variáveis SET para caminhos e formatos específicos do ambiente conforme necessário.
- A tabela de link é central para associar fatos e dimensões no modelo de dados.
- Este script é projetado para recarregamento em ambientes Qlik Sense Enterprise.






/**
 * @title People Analytics Model Script - Gemini 2.0 Flash
 * @description This script loads and transforms data for the People Analytics model.
 * It defines variables for file paths and loads data from QVD files into fact and dimension tables.
 * A link table is created to associate facts based on common keys.
 *
 * @includes Sets for:
 * ThousandSep, DecimalSep, MoneyThousandSep, MoneyDecimalSep, MoneyFormat, TimeFormat, DateFormat, TimestampFormat, FirstWeekDay, BrokenWeeks, ReferenceDay, FirstMonthOfYear, CollationLocale, CreateSearchIndexOnReload, MonthNames, LongMonthNames, DayNames, LongDayNames, NumericalAbbreviation
 *
 * @variables
 * @var {string} bronze_layer - Path to the bronze layer folder.
 * @var {string} silver_layer - Path to the silver layer folder.
 * @var {string} gold_layer - Path to the gold layer folder.
 * @var {string} manual_source - Path to the manual source folder.
 * @var {string} ti_layer - Path to the TI layer folder.
 * @var {string} external_layer - Path to the external sources folder.
 *
 * @factTables
 * @table gd_headcount_f - Headcount fact table.
 * @table gd_termination_f - Termination fact table.
 * @table gd_excel_orcamento_historico_f - Excel budget history fact table.
 * @table gd_posicoes_f - Positions fact table.
 * @table gd_eventos_f - Events fact table.
 * @table gd_custo_origem_opex_f - Cost origin Opex fact table.
 * @table gd_producao_celulose_f - Cellulose production fact table.
 * @table gd_vendas_celulose_f - Cellulose sales fact table.
 * @table gd_receita_liquida_f - Net revenue fact table.
 *
 * @dimensionTables
 * @table gd_calendario_d - Calendar dimension table.
 * @table gd_hierarquia_d - Hierarchy dimension table.
 * @table gd_funcao_d - Function dimension table.
 * @table gd_eldorado_entity_d - Eldorado Entity dimension table.
 * @table gd_employee_d - Employee dimension table.
 * @table gd_situacao_d - Situation dimension table.
 * @table gd_tipo_funcionario_d - Employee Type dimension table.
 * @table gd_esclada_d - Esclada dimension table.
 * @table gd_idade_d - Age dimension table.
 * @table gd_contratacao_tipo_d - Hiring Type dimension table.
 * @table gd_tempo_companhia_d - Company Time dimension table.
 * @table gd_centro_de_custo_d - Cost Center dimension table.
 * @table gd_secao_d - Section dimension table.
 * @table gd_status_d - Status dimension table.
 * @table gd_evento_d - Event dimension table.
 * @table gd_conta_contabil_d - Accounting Account dimension table.
 * @table gd_custo_base_d - Cost Base dimension table.
 * @table gd_custo_fonte_d - Cost Source dimension table.
 *
 * @linkTable
 * @table Link - Consolidated link table for fact tables.
 *
 * @transformation
 * The script performs the following transformations:
 * - Loads data from QVD files into fact and dimension tables.
 * - Creates a synthetic key (link_key) for each fact table using AutoNumberHash128 function.
 * - Creates a link table by concatenating distinct link_key values from all fact tables.
 * - Drops unnecessary fields from fact tables after creating the link table.
 *
 * @exitScript
 * The script exits after completing the data loading and transformation.
 */


/*
    -----------------------------------------------------------------------------
    Qlik Sense ETL Script Documentation - People Analytics Model - GPT -4.1
    -----------------------------------------------------------------------------

    This script loads and transforms data for the People Analytics Model, organizing
    information from multiple QVD sources into a unified data model for analysis.

    1. Environment Setup:
        - Sets locale, formatting, and folder paths for data layers (bronze, silver, gold, manual, TI, external).
        - Configures date, time, and number formats for Brazilian Portuguese.

    2. Fact Tables Loading:
        - Loads main fact tables (headcount, termination, budget, positions, events, costs, production, sales, revenue).
        - Generates unique link keys for each fact table using AutoNumberHash128 for data model linking.
        - Aliases key fields for consistency (e.g., pessoa_hc, pessoa_to).

    3. Dimension Tables Loading:
        - Loads all relevant dimension tables (calendar, hierarchy, function, entity, employee, situation, type, age, hiring type, company time, cost center, section, status, event, account, cost base/source).
        - Ensures all dimensions are available for model enrichment and analysis.

    4. Link Table Construction:
        - Builds a unified link table by concatenating distinct keys from all fact tables.
        - Standardizes field names and fills missing fields with empty strings for model consistency.
        - Facilitates star schema linking between facts and dimensions.

    5. Cleanup:
        - Drops redundant fields from fact tables after link table creation to optimize memory and avoid synthetic keys.

    6. Script Exit:
        - Terminates script execution after model construction.

    -----------------------------------------------------------------------------
    Usage Notes:
        - Ensure all QVD files are present in the specified gold layer path.
        - Adjust SET variables for environment-specific paths and formats as needed.
        - The link table is central for associating facts and dimensions in the data model.
        - This script is designed for reload in Qlik Sense Enterprise environments.

    -----------------------------------------------------------------------------
    Author: [Your Name]
    Last Updated: [Date]
    -----------------------------------------------------------------------------
*/


/* GPT -4o
This script is a QlikView or Qlik Sense load script designed to load and transform data for a People Analytics Model. 
It includes the following key sections:

1. **SET Statements**:
    - Configures environment variables such as number formatting, date/time formats, locale settings, and other global settings.

2. **Layer Paths**:
    - Defines paths for different data layers (bronze, silver, gold, manual source, TI layer, and external sources) using `SET` variables.

3. **Fact Tables Loading**:
    - Loads data from various QVD files into fact tables (`gd_headcount_f`, `gd_termination_f`, `gd_excel_orcamento_historico_f`, `gd_posicoes_f`, `gd_eventos_f`, etc.).
    - Uses `AutoNumberHash128` to generate unique `link_key` fields for data linking.

4. **Dimension Tables Loading**:
    - Loads data from QVD files into dimension tables (`gd_calendario_d`, `gd_hierarquia_d`, `gd_funcao_d`, `gd_eldorado_entity_d`, etc.).
    - These tables provide descriptive attributes for the fact tables.

5. **Link Table Creation**:
    - Creates a `Link` table by consolidating `link_key` and other relevant fields from the fact tables.
    - Ensures distinct records are loaded for efficient data linking.

6. **Field Dropping**:
    - Drops unnecessary fields from the fact tables after the `Link` table is created to optimize memory usage.

7. **Exit Script**:
    - Ends the script execution with the `exit script` statement.

### Key Features:
- **Qualify/Unqualify**:
  - Uses `Qualify` and `Unqualify` to control field naming conventions and avoid field name conflicts.
  
- **Data Transformation**:
  - Generates `link_key` fields using `AutoNumberHash128` for consistent and efficient data linking.
  
- **Layered Architecture**:
  - Organizes data into bronze, silver, and gold layers for better data management and processing.

- **Modular Design**:
  - Separates fact and dimension table loading for clarity and maintainability.

### Notes:
- Some sections of the script are commented out (e.g., `gd_conta_debito_d`, `gd_centro_lucro_d`) and may require review for inclusion.
- Ensure that the paths defined in the `SET` variables are correctly mapped to the actual data storage locations.
- The script assumes that all QVD files are pre-generated and available in the specified paths.
*/


/*
Title: People Analytics Model QlikView Script Documentation o3-mini

Description:
    This script sets up the environment and loads data for the People Analytics Model.
    It is organized into several sections:

1. Environment Configuration:
    - Sets numeric and date formatting, including settings for thousand separators, decimal separators, and currency.
    - Defines locale-specific settings (e.g., language-specific month and day names).
    - Specifies file paths for various data layers (Bronze, Silver, Gold), manual sources, and staging areas.
    
2. Loading Fact Tables:
    - Loads multiple fact tables (e.g., headcount, termination, budget history, positions, events, costs, production, sales, and revenue) from QVD files stored in the Gold layer.
    - Uses the AutoNumberHash128 function to generate synthetic link keys from key fields, ensuring unique identifiers for joining data.
    - Additional fields are created for specific purposes (e.g., distinguishing between headcount and termination data).

3. Loading Dimension Tables:
    - Loads dimension tables that provide additional context to the fact data, such as calendar, hierarchy, function, entity, employee, situation, and others.
    - Ensures these dimensions are unqualified to allow consistent field naming across multiple tables.

4. Building the Link Table:
    - Consolidates key fields from the fact tables into a single Link table using RESIDENT loads.
    - Merges keys from multiple data sources while handling missing or inapplicable fields by aliasing them to empty strings.
    - This step aids in creating a consistent data model and simplifies associations among tables.

5. Cleanup:
    - Drops unnecessary fields from the fact tables after creating the Link table to optimize the data model.
    - Concludes the script execution with an exit command.

Notes:
    - The extensive use of AutoNumberHash128 ensures consistency and uniqueness in join keys across the model.
    - The script is designed to work with localized formats, particularly for Brazilian Portuguese settings (e.g., date and currency formats).
    - Field qualification (Qualify/Unqualify) is used to manage field namespaces and avoid naming conflicts in the data model.
*/


SET ThousandSep='.';
SET DecimalSep=',';
SET MoneyThousandSep='.';
SET MoneyDecimalSep=',';
SET MoneyFormat='R$#.##0,00;-R$#.##0,00';
SET TimeFormat='hh:mm:ss';
SET DateFormat='DD.MM.YYYY';
SET TimestampFormat='DD.MM.YYYY hh:mm:ss[.fff]';
SET FirstWeekDay=6;
SET BrokenWeeks=1;
SET ReferenceDay=0;
SET FirstMonthOfYear=1;
SET CollationLocale='pt-BR';
SET CreateSearchIndexOnReload=1;
SET MonthNames='jan;fev;mar;abr;mai;jun;jul;ago;set;out;nov;dez';
SET LongMonthNames='janeiro;fevereiro;marÃƒÆ’Ã‚Â§o;abril;maio;junho;julho;agosto;setembro;outubro;novembro;dezembro';
SET DayNames='seg;ter;qua;qui;sex;sÃƒÆ’Ã‚Â¡b;dom';
SET LongDayNames='segunda-feira;terÃƒÆ’Ã‚Â§a-feira;quarta-feira;quinta-feira;sexta-feira;sÃƒÆ’Ã‚Â¡bado;domingo';
SET NumericalAbbreviation='3:k;6:M;9:G;12:T;15:P;18:E;21:Z;24:Y;-3:m;-6:ÃƒÅ½Ã‚Â¼;-9:n;-12:p;-15:f;-18:a;-21:z;-24:y';

//SET gold_layer = '\\BRSPOWVQDEV01\QlikSharedFolder\CustomData\Eldorado Brasil\3. Recursos Humanos\People Analytics\01. HR Medallion\03. Gold\';

SET bronze_layer = 'lib://Eldorado Data Folder - 3 Recursos Humanos - People Analytics/01. HR Medallion/01. Bronze/';
SET silver_layer = 'lib://Eldorado Data Folder - 3 Recursos Humanos - People Analytics/01. HR Medallion/02. Silver/';
SET gold_layer = 'lib://Eldorado Data Folder - 3 Recursos Humanos - People Analytics/01. HR Medallion/03. Gold/';
SET manual_source = 'lib://Eldorado Data Folder - 3 Recursos Humanos - People Analytics/02. Manual Source/';
SET ti_layer = 'lib://Staging Recursos Humanos/';
SET external_layer = 'lib://Eldorado Data Folder - 3 Recursos Humanos - People Analytics/04. Fontes Externas/';



// LOAD FATOS

Qualify *;
UNQUALIFY [link_key], [date_key], [hierarquia_sk], [funcao_sk],[eldorado_entity_sk],[pessoa], [situacao_sk], [tipo_funcionario_sk]
, [jornada_sk], [idade], [contratacao_tipo_sk], [pessoa_hc], [pessoa_to], [tempo_empresa_key], [secao_sk]
, [centro_de_custo_sk], [status_sk], [evento_sk]
, [conta_contabil_sk], [custo_base_sk], [custo_fonte_sk];


gd_headcount_f:
Load
*
,AutoNumberHash128(date_key, hierarquia_sk, funcao_sk, eldorado_entity_sk, pessoa, situacao_sk, tipo_funcionario_sk, jornada_sk, idade, contratacao_tipo_sk, tempo_empresa_key, secao_sk, centro_de_custo_sk, status_sk) as link_key
,pessoa 																																									   as pessoa_hc
FROM [$(gold_layer)gd_headcount_f.QVD]
(qvd);



gd_termination_f:
Load
*
,AutoNumberHash128(date_key, hierarquia_sk, funcao_sk, eldorado_entity_sk, pessoa, situacao_sk, tipo_funcionario_sk, jornada_sk, idade, contratacao_tipo_sk, tempo_empresa_key, secao_sk, centro_de_custo_sk) as link_key
,pessoa 																																									   as pessoa_to

FROM [$(gold_layer)gd_termination_f.QVD]
(qvd);


gd_excel_orcamento_historico_f:
Load
*
,AutoNumberHash128(date_key, funcao_sk, eldorado_entity_sk, centro_de_custo_sk) as link_key


FROM [$(gold_layer)gd_excel_hc_orcamento_historico_f.QVD]
(qvd);


gd_posicoes_f:
Load
*
,AutoNumberHash128( funcao_sk, centro_de_custo_sk, date_key) as link_key

FROM [$(gold_layer)gd_posicoes_f.QVD]
(qvd);


gd_eventos_f:
Load
*
,AutoNumberHash128(date_key, hierarquia_sk, funcao_sk, eldorado_entity_sk, pessoa,situacao_sk, jornada_sk, idade
,  contratacao_tipo_sk, tempo_empresa_key, secao_sk, centro_de_custo_sk
,conta_contabil_sk, evento_sk   ) as link_key


FROM [$(gold_layer)gd_eventos_f.qvd]
(qvd);

// -----------------------------------------------------------

gd_custo_origem_opex_f:
Load *
,AutoNumberHash128([date_key], [centro_de_custo_sk], [conta_contabil_sk]   
    , [custo_base_sk], [custo_fonte_sk]	)													as link_key

FROM [$(gold_layer)gd_custo_origem_opex_f.QVD]
(qvd);



gd_producao_celulose_f:
Load *
,AutoNumberHash128(
	date_key
)																		as link_key

FROM [$(gold_layer)gd_producao_celulose_f.QVD]
(qvd);



gd_vendas_celulose_f:
Load *
,AutoNumberHash128(
	date_key
)																		as link_key

FROM [$(gold_layer)gd_vendas_celulose_f.QVD]
(qvd);


gd_receita_liquida_f:
Load *
,AutoNumberHash128(
	date_key
)																		as link_key

FROM [$(gold_layer)gd_receita_liquida_f.QVD]
(qvd);




// LOAD DIMENSOES
Unqualify *;

gd_calendario_d:
Load
*
FROM [$(gold_layer)gd_calendario_d.QVD]
(qvd);


gd_hierarquia_d:
Load
*
FROM [$(gold_layer)gd_hierarquia_d.QVD]
(qvd);

gd_funcao_d:
Load
*
FROM [$(gold_layer)gd_funcao_d.QVD]
(qvd);

gd_eldorado_entity_d:
Load
*
FROM [$(gold_layer)gd_eldorado_entity_d.QVD]
(qvd);

gd_employee_d:
Load
*
FROM [$(gold_layer)gd_employee_d.QVD]
(qvd);

gd_situacao_d:
Load
*
FROM [$(gold_layer)gd_situacao_d.QVD]
(qvd);

gd_tipo_funcionario_d:
Load
*
FROM [$(gold_layer)gd_tipo_funcionario_d.QVD]
(qvd);


gd_esclada_d:
Load
*
FROM [$(gold_layer)gd_esclada_d.QVD]
(qvd);


gd_idade_d:
Load
*
FROM [$(gold_layer)gd_idade_d.QVD]
(qvd);

gd_contratacao_tipo_d:
Load
*
FROM [$(gold_layer)gd_contratacao_tipo_d.QVD]
(qvd);

gd_tempo_companhia_d:
Load
*
FROM [$(gold_layer)gd_tempo_companhia_d.QVD]
(qvd);

gd_centro_de_custo_d:
Load
*
FROM [$(gold_layer)gd_centro_de_custo_d.QVD]
(qvd);

gd_secao_d:
Load
*
FROM [$(gold_layer)gd_secao_d.QVD]
(qvd);

gd_status_d:
Load
*
FROM [$(gold_layer)gd_status_d.QVD]
(qvd);

//gd_conta_debito_d:
//Load
//*
//FROM [$(gold_layer)gd_conta_debito_d.QVD]
//(qvd);


gd_evento_d:
Load
*
FROM [$(gold_layer)gd_evento_d.QVD]
(qvd);

// gd_centro_lucro_d:
// Load
// *
// FROM [$(gold_layer)gd_centro_lucro_d.QVD]
// (qvd);


gd_conta_contabil_d:
Load
*
FROM [$(gold_layer)gd_conta_contabil_d.QVD]
(qvd);



gd_custo_base_d:
Load
*
FROM [$(gold_layer)gd_custo_base_d.QVD]
(qvd);


gd_custo_fonte_d:
Load
*
FROM [$(gold_layer)gd_custo_fonte_d.QVD]
(qvd);







Link:
LOAD DISTINCT
    link_key
    ,date_key
    ,tempo_empresa_key
    ,hierarquia_sk
    ,funcao_sk
    ,eldorado_entity_sk
    ,secao_sk
    ,centro_de_custo_sk
    ,pessoa
    ,situacao_sk
    ,tipo_funcionario_sk
    ,jornada_sk
    ,idade
    ,contratacao_tipo_sk
    ,status_sk
 //   ,'' as conta_debito_sk
    ,'' as evento_sk
//     ,'' as centro_de_lucro_sk
    ,'' as conta_contabil_sk
    ,'' as custo_base_sk
    ,'' as custo_fonte_sk

RESIDENT gd_headcount_f;

LOAD DISTINCT
    link_key
    ,date_key
    ,tempo_empresa_key
    ,hierarquia_sk
    ,funcao_sk
    ,eldorado_entity_sk
    ,secao_sk
    ,centro_de_custo_sk
    ,pessoa
    ,situacao_sk
    ,tipo_funcionario_sk
    ,jornada_sk
    ,idade
    ,contratacao_tipo_sk
    ,'' as status_sk
 //   ,'' as conta_debito_sk
    ,'' as evento_sk
//     ,'' as centro_de_lucro_sk
    ,'' as conta_contabil_sk
    ,'' as custo_base_sk
    ,'' as custo_fonte_sk

RESIDENT gd_termination_f;


LOAD DISTINCT
    link_key
    ,date_key
    ,'' as tempo_empresa_key
    ,'' as hierarquia_sk
    , funcao_sk
    , eldorado_entity_sk
    ,'' as secao_sk
    ,centro_de_custo_sk
    ,'' as pessoa
    ,'' as situacao_sk
    ,'' as tipo_funcionario_sk
    ,'' as jornada_sk
    ,'' as idade
    ,'' as contratacao_tipo_sk
    ,'' as status_sk
 //   ,'' as conta_debito_sk
    ,'' as evento_sk
//     ,'' as centro_de_lucro_sk
    ,'' as conta_contabil_sk
    ,'' as custo_base_sk
    ,'' as custo_fonte_sk

Resident gd_excel_orcamento_historico_f;


LOAD DISTINCT
    link_key
    ,date_key
    ,'' as tempo_empresa_key
    ,'' as hierarquia_sk
    ,funcao_sk
    ,'' as eldorado_entity_sk
    ,'' as secao_sk
    ,centro_de_custo_sk
    ,'' as pessoa
    ,'' as situacao_sk
    ,'' as tipo_funcionario_sk
    ,'' as jornada_sk
    ,'' as idade
    ,'' as contratacao_tipo_sk
    ,'' as status_sk
//    ,'' as conta_debito_sk
    ,'' as evento_sk
//     ,'' as centro_de_lucro_sk
    ,'' as conta_contabil_sk
    ,'' as custo_base_sk
    ,'' as custo_fonte_sk

Resident gd_posicoes_f;


LOAD DISTINCT
    link_key
    ,date_key
    ,tempo_empresa_key
    ,hierarquia_sk
    ,funcao_sk
    ,eldorado_entity_sk
    ,secao_sk
    ,centro_de_custo_sk
    ,pessoa
    ,situacao_sk
    ,'' as tipo_funcionario_sk
    ,jornada_sk
    ,idade
    ,contratacao_tipo_sk
    ,'' as status_sk
//    ,conta_debito_sk
    ,evento_sk
//  ,'' as centro_de_lucro_sk
    ,conta_contabil_sk
    ,'' as custo_base_sk
    ,'' as custo_fonte_sk

Resident gd_eventos_f;



LOAD Distinct
     link_key
    ,date_key
    ,'' as tempo_empresa_key
    ,'' as hierarquia_sk
    ,'' as funcao_sk
    ,'' as eldorado_entity_sk
    ,'' as secao_sk
    ,centro_de_custo_sk
    ,'' as pessoa
    ,'' as situacao_sk
    ,'' as tipo_funcionario_sk
    ,'' as jornada_sk
    ,'' as idade
    ,'' as contratacao_tipo_sk
    ,'' as status_sk
//    ,'' as conta_debito_sk
    ,'' as evento_sk
//     ,centro_de_lucro_sk
    ,conta_contabil_sk
    ,custo_base_sk
    ,custo_fonte_sk

Resident gd_custo_origem_opex_f;

LOAD Distinct
     link_key
    ,date_key
    ,'' as tempo_empresa_key
    ,'' as hierarquia_sk
    ,'' as funcao_sk
    ,'' as eldorado_entity_sk
    ,'' as secao_sk
    ,'' as centro_de_custo_sk
    ,'' as pessoa
    ,'' as situacao_sk
    ,'' as tipo_funcionario_sk
    ,'' as jornada_sk
    ,'' as idade
    ,'' as contratacao_tipo_sk
    ,'' as status_sk
 //   ,'' as conta_debito_sk
    ,'' as evento_sk
//     ,'' as centro_de_lucro_sk
    ,'' as conta_contabil_sk
    ,'' as custo_base_sk
    ,'' as custo_fonte_sk

Resident gd_producao_celulose_f;

LOAD Distinct
     link_key
    ,date_key
    ,'' as tempo_empresa_key
    ,'' as hierarquia_sk
    ,'' as funcao_sk
    ,'' as eldorado_entity_sk
    ,'' as secao_sk
    ,'' as centro_de_custo_sk
    ,'' as pessoa
    ,'' as situacao_sk
    ,'' as tipo_funcionario_sk
    ,'' as jornada_sk
    ,'' as idade
    ,'' as contratacao_tipo_sk
    ,'' as status_sk
//    ,'' as conta_debito_sk
    ,'' as evento_sk
//     ,'' as centro_de_lucro_sk
    ,'' as conta_contabil_sk
    ,'' as custo_base_sk
    ,'' as custo_fonte_sk

Resident gd_vendas_celulose_f;


LOAD Distinct
     link_key
    ,date_key
    ,'' as tempo_empresa_key
    ,'' as hierarquia_sk
    ,'' as funcao_sk
    ,'' as eldorado_entity_sk
    ,'' as secao_sk
    ,'' as centro_de_custo_sk
    ,'' as pessoa
    ,'' as situacao_sk
    ,'' as tipo_funcionario_sk
    ,'' as jornada_sk
    ,'' as idade
    ,'' as contratacao_tipo_sk
    ,'' as status_sk
//    ,'' as conta_debito_sk
    ,'' as evento_sk
//     ,'' as centro_de_lucro_sk
    ,'' as conta_contabil_sk
    ,'' as custo_base_sk
    ,'' as custo_fonte_sk

Resident gd_receita_liquida_f;



DROP FIELDS pessoa, date_key, hierarquia_sk,funcao_sk, eldorado_entity_sk, situacao_sk, tipo_funcionario_sk, jornada_sk, idade, contratacao_tipo_sk, tempo_empresa_key, secao_sk
,  centro_de_custo_sk, status_sk, evento_sk
, conta_contabil_sk, custo_base_sk, custo_fonte_sk

FROM gd_headcount_f, gd_termination_f, gd_excel_orcamento_historico_f, gd_posicoes_f, gd_eventos_f
,gd_custo_origem_opex_f, gd_producao_celulose_f, gd_vendas_celulose_f, gd_receita_liquida_f;

exit script;