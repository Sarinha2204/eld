# Documentação Técnica

Documentação Técnica
Arquivo: gd_headcount.qvs
Última atualização: 07/08/2025 13:49:31

Documentação Técnica do Script QlikView: gd_headcount.qvs

**1. Resumo:**

O script `gd_headcount.qvs` processa dados de *headcount* (contagem de funcionários) para criar um modelo de dados para análise em QlikView.  Ele extrai dados de arquivos QVD na camada *silver*, cria e popula tabelas de dimensões e fatos, realiza a limpeza e transformação dos dados, e armazena os resultados em arquivos QVD na camada *gold*. O processo inclui a geração de tabelas auxiliares para calendário e tempo de serviço na empresa.


**2. Principais Etapas:**

* **2.1 Configurações:** Define as configurações regionais e de formatação para português (Brasil), incluindo separadores decimais e de milhares, formatos de moeda, data e hora, nomes de dias e meses, e o primeiro dia da semana. Define variáveis para os caminhos de acesso aos arquivos de dados em diferentes camadas (bronze, silver, gold), fontes externas e internas, utilizando `lib://` para indicar armazenamento na biblioteca de arquivos do Qlik.

* **2.2 Criação da Tabela de Calendário:**  Cria uma tabela de dimensão (`gd_calendario_d`) contendo informações detalhadas sobre datas, como ano, mês, dia da semana, semana do ano, trimestre, semestre, e o status do período (histórico ou futuro).  A tabela é armazenada em um arquivo QVD na camada *gold*.

* **2.3 Criação da Tabela de Tempo na Companhia:** Cria uma tabela de dimensão (`gd_tempo_companhia_d`) categorizando o tempo de serviço dos funcionários em grupos (baseados em faixas de tempo em meses e anos, com diferenciação entre gerencial e operacional). A tabela é salva como um QVD na camada *gold*.

* **2.4 Carregamento de Dados Brutos:** Carrega dados brutos de *headcount*, demissões, orçamento histórico e posições de funcionários a partir de arquivos QVD na camada *silver*. Chaves *hash* (Hash128) são geradas para otimizar os relacionamentos entre as tabelas, utilizando diversas colunas para gerar uma chave única e otimizada para cada tabela.

* **2.5 Criação de Dimensões:** Cria diversas tabelas de dimensão a partir dos dados brutos, incluindo: `gd_employee_d` (funcionários), `gd_hierarquia_d` (hierarquia organizacional), `gd_funcao_d` (funções/cargos), `gd_eldorado_entity_d` (entidades Eldorado), `gd_secao_d` (seções), `gd_centro_de_custo_d` (centros de custo), `gd_situacao_d` (situação do funcionário), `gd_status_d` (status do *headcount*), `gd_tipo_funcionario_d` (tipo de funcionário), `gd_esclada_d` (jornada e escala de trabalho), `gd_idade_d` (idade e geração do funcionário), e `gd_contratacao_tipo_d` (tipo de contratação). Todas são armazenadas em arquivos QVD na camada *gold*. A dimensão `gd_employee_d` utiliza `FirstSortedValue` para selecionar o valor mais recente de cada campo em caso de duplicatas para uma mesma pessoa.

* **2.6 Criação de Fatos:** Cria tabelas de fatos consolidando informações relevantes: `gd_headcount_f` (*headcount*), `gd_termination_f` (demissões), `gd_excel_hc_orcamento_historico_f` (orçamento histórico), e `gd_posicoes_f` (posições). Campos desnecessários são removidos para otimização. As tabelas de fatos são armazenadas em arquivos QVD na camada *gold*.

* **2.7 Criação de Dimensões de Demissão:** As dimensões `gd_situacao_d`, `gd_status_d` e `gd_tipo_funcionario_d` são atualizadas/concatenadas com dados específicos de demissão utilizando a instrução `Concatenate`.

* **2.8 Limpeza de Dados:** Tabelas temporárias e dados brutos não mais necessários são removidos utilizando `Drop Table`.

* **2.9 Armazenamento dos Resultados:** Todas as tabelas (dimensões e fatos) são armazenadas em arquivos QVD na camada *gold*.

* **2.10 Finalização:** O script termina com `Exit Script`.
