# Documentação Técnica

**Arquivo:** `gd_headcount.qvs`  
**Última atualização:** 07/08/2025 14:39:37

# Documentação Técnica do Script QlikView: gd_headcount.qvs

**Última Atualização:** 07/08/2025 (Atualize esta data após cada modificação)

**1. Resumo:**

O script `gd_headcount.qvs` processa dados de *headcount* (contagem de funcionários) para construir um modelo de dados em QlikView, destinado à análise de recursos humanos.  Ele utiliza arquivos QVD da camada *silver* como fonte de dados, criando e populando tabelas de dimensões e fatos.  O script realiza limpeza e transformação de dados, incluindo a geração de tabelas auxiliares, como calendário e tempo de serviço na empresa. Os dados processados são armazenados em arquivos QVD na camada *gold*.  O script emprega funções como `Hash128` para gerar chaves únicas e otimizadas, e `FirstSortedValue` para lidar com valores duplicados. A utilização de `lib://` indica que os arquivos QVD são referenciados a partir da biblioteca do Qlik.


**2. Principais Etapas:**

* **2.1 Configurações Locais e de Formatação:** O script inicia definindo as configurações de idioma e formatação para português (Brasil), incluindo separadores decimais e de milhares, formatos de moeda, data e hora, nomes de dias e meses, e o primeiro dia da semana. Define variáveis para os caminhos de acesso aos arquivos de dados em diferentes camadas (*bronze*, *silver*, *gold*), fontes externas e internas, utilizando `lib://` para referenciar a biblioteca de arquivos do Qlik.

* **2.2 Criação da Tabela de Calendário (`gd_calendario_d`):** Uma tabela de dimensão de calendário é criada, contendo informações detalhadas sobre datas, como ano, mês, dia da semana, semana do ano, trimestre, semestre e o status do período (histórico ou futuro). A tabela é salva em um arquivo QVD na camada *gold*.

* **2.3 Criação da Tabela de Tempo na Companhia (`gd_tempo_companhia_d`):** Uma tabela de dimensão é gerada, categorizando o tempo de serviço dos funcionários em grupos (baseados em faixas de tempo em meses e anos, com diferenciação entre gerencial e operacional). A tabela é armazenada como um QVD na camada *gold*.

* **2.4 Carregamento de Dados Brutos:** Dados brutos de *headcount*, demissões, orçamento histórico e posições de funcionários são carregados de arquivos QVD na camada *silver*. Chaves *hash* (Hash128) são geradas a partir de várias colunas para criar chaves únicas e otimizadas, melhorando o desempenho dos relacionamentos entre as tabelas.

* **2.5 Criação de Dimensões:**  Diversas tabelas de dimensão são criadas a partir dos dados brutos carregados: `gd_employee_d` (funcionários), `gd_hierarquia_d` (hierarquia organizacional), `gd_funcao_d` (funções/cargos), `gd_eldorado_entity_d` (entidades Eldorado), `gd_secao_d` (seções), `gd_centro_de_custo_d` (centros de custo), `gd_situacao_d` (situação do funcionário), `gd_status_d` (status do *headcount*), `gd_tipo_funcionario_d` (tipo de funcionário), `gd_esclada_d` (jornada e escala de trabalho), `gd_idade_d` (idade e geração do funcionário), e `gd_contratacao_tipo_d` (tipo de contratação). Todas as dimensões são armazenadas em arquivos QVD na camada *gold*. A dimensão `gd_employee_d` utiliza a função `FirstSortedValue` para selecionar o valor mais recente de cada campo em caso de duplicatas para o mesmo funcionário.

* **2.6 Criação de Fatos:** Tabelas de fatos são criadas a partir dos dados brutos, consolidando informações relevantes: `gd_headcount_f` (*headcount*), `gd_termination_f` (demissões), `gd_excel_hc_orcamento_historico_f` (orçamento histórico), e `gd_posicoes_f` (posições). Campos desnecessários são removidos para otimização. As tabelas de fatos são armazenadas em arquivos QVD na camada *gold*.

* **2.7 Concatenação de Dimensões de Demissão:** As dimensões `gd_situacao_d`, `gd_status_d`, e `gd_tipo_funcionario_d` são concatenadas com informações específicas de demissão utilizando a instrução `Concatenate`.

* **2.8 Limpeza de Dados:** As tabelas temporárias e dados brutos não mais necessários são removidos usando a instrução `Drop Table`.

* **2.9 Armazenamento dos Resultados:** Todas as tabelas (dimensões e fatos) são armazenadas em arquivos QVD na camada *gold*.

* **2.10 Finalização:** O script termina com a instrução `Exit Script`.


**Observação:** Esta documentação descreve o funcionamento do script sem propor alterações ou melhorias. A escolha da ordem de carregamento (`-load_date`) na função `FirstSortedValue` é crucial para a consistência dos dados na tabela `gd_employee_d`.  A utilização de `lib://` para os caminhos dos arquivos QVD indica que eles estão armazenados na biblioteca do Qlik Sense ou QlikView. A utilização de chaves hash (Hash128) contribui para o desempenho do aplicativo QlikView.

# Documentação Técnica

**Arquivo:** `gd_headcount.qvs`  
**Última atualização:** 07/08/2025 14:33:43

# Documentação Técnica do Script QlikView: gd_headcount.qvs

**Arquivo:** `gd_headcount.qvs`

**Última atualização:** 07/08/2025 (Substituir pela data real após cada modificação)


**1. Resumo:**

O script `gd_headcount.qvs` é um script QlikView que processa dados de *headcount* (contagem de funcionários) para criar um modelo de dados destinado à análise.  Ele utiliza arquivos QVD na camada *silver* como fonte de dados, criando e populando tabelas de dimensões e fatos. O script realiza limpeza e transformação de dados, gerando tabelas auxiliares como calendário e tempo de serviço na empresa. Os dados processados são armazenados em arquivos QVD na camada *gold*.  O script utiliza a função `Hash128` para gerar chaves únicas otimizadas e `FirstSortedValue` para lidar com valores duplicados em determinadas colunas.  A utilização de `lib://` indica que os arquivos QVD são referenciados a partir da biblioteca do Qlik.


**2. Principais Etapas:**

* **2.1 Configurações Locais e de Formatação:** O script inicia definindo as configurações de idioma e formatação para português (Brasil), incluindo separadores decimais e de milhares, formatos de moeda, data e hora, nomes de dias e meses, e o primeiro dia da semana. Define variáveis para os caminhos de acesso aos arquivos de dados em diferentes camadas (*bronze*, *silver*, *gold*), fontes externas e internas, utilizando `lib://` para referenciar a biblioteca de arquivos do Qlik.

* **2.2 Criação da Tabela de Calendário (`gd_calendario_d`):**  Uma tabela de dimensão de calendário é criada, contendo informações detalhadas sobre datas, tais como ano, mês, dia da semana, semana do ano, trimestre, semestre e o status do período (histórico ou futuro).  A tabela é salva em um arquivo QVD na camada *gold*.

* **2.3 Criação da Tabela de Tempo na Companhia (`gd_tempo_companhia_d`):** Uma tabela de dimensão é gerada, categorizando o tempo de serviço dos funcionários em grupos (baseados em faixas de tempo em meses e anos, com diferenciação entre gerencial e operacional). A tabela é armazenada como um QVD na camada *gold*.

* **2.4 Carregamento de Dados Brutos:** Dados brutos de *headcount*, demissões, orçamento histórico e posições de funcionários são carregados de arquivos QVD na camada *silver*. Chaves *hash* (Hash128) são geradas a partir de várias colunas para criar chaves únicas e otimizadas, melhorando o desempenho dos relacionamentos entre as tabelas.

* **2.5 Criação de Dimensões:** Várias tabelas de dimensão são criadas a partir dos dados brutos carregados: `gd_employee_d` (funcionários), `gd_hierarquia_d` (hierarquia organizacional), `gd_funcao_d` (funções/cargos), `gd_eldorado_entity_d` (entidades Eldorado), `gd_secao_d` (seções), `gd_centro_de_custo_d` (centros de custo), `gd_situacao_d` (situação do funcionário), `gd_status_d` (status do *headcount*), `gd_tipo_funcionario_d` (tipo de funcionário), `gd_esclada_d` (jornada e escala de trabalho), `gd_idade_d` (idade e geração do funcionário), e `gd_contratacao_tipo_d` (tipo de contratação). Todas as dimensões são armazenadas em arquivos QVD na camada *gold*. A dimensão `gd_employee_d` utiliza a função `FirstSortedValue` para selecionar o valor mais recente de cada campo em caso de duplicatas para o mesmo funcionário.

* **2.6 Criação de Fatos:** Tabelas de fatos são criadas a partir dos dados brutos, consolidando informações relevantes: `gd_headcount_f` (*headcount*), `gd_termination_f` (demissões), `gd_excel_hc_orcamento_historico_f` (orçamento histórico), e `gd_posicoes_f` (posições). Campos desnecessários são removidos para otimização.  As tabelas de fatos são armazenadas em arquivos QVD na camada *gold*.

* **2.7 Concatenação de Dimensões de Demissão:** As dimensões `gd_situacao_d`, `gd_status_d`, e `gd_tipo_funcionario_d` são concatenadas com informações específicas de demissão utilizando a instrução `Concatenate`.

* **2.8 Limpeza de Dados:** As tabelas temporárias e dados brutos não mais necessários são removidos usando a instrução `Drop Table`.

* **2.9 Armazenamento dos Resultados:** Todas as tabelas (dimensões e fatos) são armazenadas em arquivos QVD na camada *gold*.

* **2.10 Finalização:** O script termina com a instrução `Exit Script`.


**Observação:** Esta documentação descreve o funcionamento do script sem propor alterações ou melhorias. A escolha da ordem de carregamento (`-load_date`) na função `FirstSortedValue`  é crucial para a consistência dos dados na tabela `gd_employee_d`.

# Documentação Técnica

**Arquivo:** `gd_headcount.qvs`  
**Última atualização:** 07/08/2025 14:30:29

## Documentação Técnica do Script QlikView: gd_headcount.qvs

**Última Atualização:** 07/08/2025 14:26:08 (Atualize esta data após cada modificação)

**1. Resumo:**

O script `gd_headcount.qvs` é um script QlikView que processa dados de *headcount* (contagem de funcionários) para construir um modelo de dados para análise. Ele utiliza arquivos QVD na camada *silver* como fonte de dados, criando e populando tabelas de dimensões e fatos.  O script realiza limpeza e transformação de dados, gerando tabelas auxiliares como calendário e tempo de serviço na empresa. Os dados processados são armazenados em arquivos QVD na camada *gold*.

**2. Principais Etapas:**

* **2.1 Configurações Locais e de Formatação:**  O script inicia definindo as configurações de idioma e formatação para português (Brasil), incluindo separadores decimais e de milhares, formatos de moeda, data e hora, nomes de dias e meses, e o primeiro dia da semana. Define também variáveis para os caminhos de acesso aos arquivos de dados em diferentes camadas (*bronze*, *silver*, *gold*), fontes externas e internas, utilizando `lib://` para referenciar a biblioteca de arquivos do Qlik.

* **2.2 Criação da Tabela de Calendário (`gd_calendario_d`):** Uma tabela de dimensão de calendário é criada, contendo informações detalhadas sobre datas, tais como ano, mês, dia da semana, semana do ano, trimestre, semestre e o status do período (histórico ou futuro).  A tabela é salva em um arquivo QVD na camada *gold*.

* **2.3 Criação da Tabela de Tempo na Companhia (`gd_tempo_companhia_d`):** Uma tabela de dimensão é gerada, categorizando o tempo de serviço dos funcionários em grupos (baseados em faixas de tempo em meses e anos, com diferenciação entre gerencial e operacional). A tabela é armazenada como um QVD na camada *gold*.

* **2.4 Carregamento de Dados Brutos:** Dados brutos de *headcount*, demissões, orçamento histórico e posições de funcionários são carregados de arquivos QVD na camada *silver*.  Chaves *hash* (Hash128) são geradas a partir de várias colunas para criar chaves únicas e otimizadas, melhorando o desempenho dos relacionamentos entre as tabelas.

* **2.5 Criação de Dimensões:** Várias tabelas de dimensão são criadas a partir dos dados brutos carregados, incluindo: `gd_employee_d` (funcionários), `gd_hierarquia_d` (hierarquia organizacional), `gd_funcao_d` (funções/cargos), `gd_eldorado_entity_d` (entidades Eldorado), `gd_secao_d` (seções), `gd_centro_de_custo_d` (centros de custo), `gd_situacao_d` (situação do funcionário), `gd_status_d` (status do *headcount*), `gd_tipo_funcionario_d` (tipo de funcionário), `gd_esclada_d` (jornada e escala de trabalho), `gd_idade_d` (idade e geração do funcionário), e `gd_contratacao_tipo_d` (tipo de contratação).  Todas as dimensões são armazenadas em arquivos QVD na camada *gold*. A dimensão `gd_employee_d` utiliza a função `FirstSortedValue` para selecionar o valor mais recente de cada campo em caso de duplicatas para o mesmo funcionário.

* **2.6 Criação de Fatos:** Tabelas de fatos são criadas a partir dos dados brutos, consolidando informações relevantes: `gd_headcount_f` (*headcount*), `gd_termination_f` (demissões), `gd_excel_hc_orcamento_historico_f` (orçamento histórico), e `gd_posicoes_f` (posições). Campos desnecessários são removidos para otimização.  As tabelas de fatos são armazenadas em arquivos QVD na camada *gold*.

* **2.7 Concatenação de Dimensões de Demissão:** As dimensões `gd_situacao_d`, `gd_status_d`, e `gd_tipo_funcionario_d` são concatenadas com informações específicas de demissão utilizando a instrução `Concatenate`.

* **2.8 Limpeza de Dados:** As tabelas temporárias e dados brutos não mais necessários são removidos usando a instrução `Drop Table`.

* **2.9 Armazenamento dos Resultados:** Todas as tabelas (dimensões e fatos) são armazenadas em arquivos QVD na camada *gold*.

* **2.10 Finalização:** O script termina com a instrução `Exit Script`.


**Observação:** Esta documentação descreve o funcionamento do script sem propor alterações ou melhorias.  A utilização de `lib://` indica que os arquivos QVD são armazenados na biblioteca do Qlik, otimizando a gestão e reutilização dos dados. A utilização de chaves *hash* (Hash128) melhora a performance. O uso de `FirstSortedValue` em `gd_employee_d` garante a consistência dos dados, mas depende da ordem de carregamento (`-load_date`) para definir qual valor será priorizado em caso de duplicatas.

# Documentação Técnica

**Arquivo:** `gd_headcount.qvs`  
**Última atualização:** 07/08/2025 14:26:08

## Documentação Técnica do Script QlikView: gd_headcount.qvs

**Última Atualização:** 06/08/2025 13:05:25

**1. Resumo:**

O script `gd_headcount.qvs` processa dados de *headcount* (contagem de funcionários) para criar um modelo de dados para análise em QlikView. Ele extrai dados de arquivos QVD na camada *silver*, cria e popula tabelas de dimensões e fatos, realiza a limpeza e transformação dos dados, e armazena os resultados em arquivos QVD na camada *gold*. O processo inclui a geração de tabelas auxiliares para calendário e tempo de serviço na empresa.


**2. Principais Etapas:**

* **2.1 Configurações:** Define as configurações regionais e de formatação para português (Brasil), incluindo separadores decimais e de milhares, formatos de moeda, data e hora, nomes de dias e meses, e o primeiro dia da semana. Define variáveis para os caminhos de acesso aos arquivos de dados em diferentes camadas (bronze, silver, gold), fontes externas e internas, utilizando `lib://` para indicar armazenamento na biblioteca de arquivos do Qlik.

* **2.2 Criação da Tabela de Calendário:** Cria uma tabela de dimensão (`gd_calendario_d`) contendo informações detalhadas sobre datas, como ano, mês, dia da semana, semana do ano, trimestre, semestre, e o status do período (histórico ou futuro).  A tabela é armazenada em um arquivo QVD na camada *gold*.

* **2.3 Criação da Tabela de Tempo na Companhia:** Cria uma tabela de dimensão (`gd_tempo_companhia_d`) categorizando o tempo de serviço dos funcionários em grupos (baseados em faixas de tempo em meses e anos, com diferenciação entre gerencial e operacional). A tabela é salva como um QVD na camada *gold*.

* **2.4 Carregamento de Dados Brutos:** Carrega dados brutos de *headcount*, demissões, orçamento histórico e posições de funcionários a partir de arquivos QVD na camada *silver*. Chaves *hash* (Hash128) são geradas para otimizar os relacionamentos entre as tabelas, utilizando diversas colunas para gerar uma chave única e otimizada para cada tabela.

* **2.5 Criação de Dimensões:** Cria diversas tabelas de dimensão a partir dos dados brutos, incluindo: `gd_employee_d` (funcionários), `gd_hierarquia_d` (hierarquia organizacional), `gd_funcao_d` (funções/cargos), `gd_eldorado_entity_d` (entidades Eldorado), `gd_secao_d` (seções), `gd_centro_de_custo_d` (centros de custo), `gd_situacao_d` (situação do funcionário), `gd_status_d` (status do *headcount*), `gd_tipo_funcionario_d` (tipo de funcionário), `gd_esclada_d` (jornada e escala de trabalho), `gd_idade_d` (idade e geração do funcionário), e `gd_contratacao_tipo_d` (tipo de contratação). Todas são armazenadas em arquivos QVD na camada *gold*. A dimensão `gd_employee_d` utiliza `FirstSortedValue` para selecionar o valor mais recente de cada campo em caso de duplicatas para uma mesma pessoa.

* **2.6 Criação de Fatos:** Cria tabelas de fatos consolidando informações relevantes: `gd_headcount_f` (*headcount*), `gd_termination_f` (demissões), `gd_excel_hc_orcamento_historico_f` (orçamento histórico), e `gd_posicoes_f` (posições). Campos desnecessários são removidos para otimização. As tabelas de fatos são armazenadas em arquivos QVD na camada *gold*.

* **2.7 Criação de Dimensões de Demissão:** As dimensões `gd_situacao_d`, `gd_status_d` e `gd_tipo_funcionario_d` são atualizadas/concatenadas com dados específicos de demissão utilizando a instrução `Concatenate`.

* **2.8 Limpeza de Dados:** Tabelas temporárias e dados brutos não mais necessários são removidos utilizando `Drop Table`.

* **2.9 Armazenamento dos Resultados:** Todas as tabelas (dimensões e fatos) são armazenadas em arquivos QVD na camada *gold*.

* **2.10 Finalização:** O script termina com `Exit Script`.

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

Documentação Técnica
Arquivo: gd_headcount.qvs
Última atualização: 07/08/2025 13:24:57
# Documentação Técnica do Script QlikView: gd_headcount.qvs

**Última Atualização:** 06/08/2025 13:05:25 (Esta data precisa ser atualizada se o script for modificado)

**1. Resumo:**

O script `gd_headcount.qvs` processa e transforma dados de *headcount* (contagem de funcionários) de uma organização, preparando-os para análise em QlikView.  Ele carrega dados brutos de arquivos QVD na camada *silver*, cria e popula tabelas de dimensões e fatos, realiza a limpeza de dados e armazena os resultados em arquivos QVD na camada *gold*.  O processo inclui a geração de tabelas auxiliares de calendário e tempo de serviço na empresa.

**2. Principais Etapas:**

* **2.1 Configurações:** O script inicia definindo as configurações de idioma e formatação para português (Brasil), incluindo separadores decimais e de milhares, formatos de moeda, data e hora, nomes de dias e meses, e o primeiro dia da semana.  Define variáveis para os caminhos de acesso aos arquivos de dados em diferentes camadas (bronze, silver, gold), fontes externas e internas, utilizando `lib://` indicando armazenamento em biblioteca de arquivos do Qlik.

* **2.2 Criação da Tabela de Calendário:** Uma tabela de dimensão (`gd_calendario_d`) é criada contendo informações detalhadas sobre datas, como ano, mês, dia da semana, semana do ano, trimestre, semestre, e o status do período (histórico ou futuro).  Esta tabela é armazenada em um arquivo QVD na camada *gold*.

* **2.3 Criação da Tabela de Tempo na Companhia:** Uma tabela de dimensão (`gd_tempo_companhia_d`) é gerada, categorizando o tempo de serviço dos funcionários em grupos (baseados em faixas de tempo em meses e anos, com diferenciação entre gerencial e operacional). Esta tabela também é salva como um QVD na camada *gold*.

* **2.4 Carregamento de Dados Brutos:** Dados brutos de *headcount*, demissões, orçamento histórico e posições de funcionários são carregados a partir de arquivos QVD na camada *silver*. Chaves *hash* (Hash128) são geradas para otimizar os relacionamentos entre as tabelas, utilizando diversas colunas para gerar uma chave única e otimizada para cada tabela.

* **2.5 Criação de Dimensões:** Várias tabelas de dimensão são criadas a partir dos dados brutos, incluindo:
    * `gd_employee_d` (funcionários)
    * `gd_hierarquia_d` (hierarquia organizacional)
    * `gd_funcao_d` (funções/cargos)
    * `gd_eldorado_entity_d` (entidades Eldorado)
    * `gd_secao_d` (seções)
    * `gd_centro_de_custo_d` (centros de custo)
    * `gd_situacao_d` (situação do funcionário)
    * `gd_status_d` (status do *headcount*)
    * `gd_tipo_funcionario_d` (tipo de funcionário)
    * `gd_esclada_d` (jornada e escala de trabalho)
    * `gd_idade_d` (idade e geração do funcionário)
    * `gd_contratacao_tipo_d` (tipo de contratação).
    Todas são armazenadas em arquivos QVD na camada *gold*. A dimensão `gd_employee_d` utiliza `FirstSortedValue` para selecionar o valor mais recente de cada campo em caso de duplicatas para uma mesma pessoa.

* **2.6 Criação de Fatos:** Tabelas de fatos são criadas, consolidando informações relevantes:
    * `gd_headcount_f` (*headcount*)
    * `gd_termination_f` (demissões)
    * `gd_excel_hc_orcamento_historico_f` (orçamento histórico)
    * `gd_posicoes_f` (posições).
Campos desnecessários são removidos para otimização. As tabelas de fatos são armazenadas em arquivos QVD na camada *gold*.

* **2.7 Criação de Dimensões de Demissão:** As dimensões `gd_situacao_d`, `gd_status_d` e `gd_tipo_funcionario_d` são atualizadas/concatenadas com dados específicos de demissão utilizando a instrução `Concatenate`.

* **2.8 Limpeza de Dados:** Tabelas temporárias e dados brutos não mais necessários são removidos utilizando `Drop Table`.

* **2.9 Armazenamento dos Resultados:** Todas as tabelas (dimensões e fatos) são armazenadas em arquivos QVD na camada *gold*.

* **2.10 Finalização:** O script termina com `Exit Script`.


**Observação:** Esta documentação descreve o funcionamento do script sem fornecer sugestões ou melhorias de código. A utilização de `lib://` sugere a localização dos arquivos em um repositório centralizado do Qlik Sense ou QlikView.  As chaves Hash128 contribuem para a performance do aplicativo QlikView, especialmente em grandes volumes de dados.  A utilização de `FirstSortedValue` na criação da dimensão `gd_employee_d` garante a consistência dos dados, mas precisa de atenção quanto a ordenação utilizada `-load_date` (data decrescente) na definição de qual valor prevalecerá.

Documentação Técnica
Arquivo: gd_headcount.qvs
Última atualização: 07/08/2025 13:11:57
# Documentação Técnica do Script QlikView: gd_headcount.qvs

**Última Atualização:** 06/08/2025 13:05:25

**1. Resumo:**

O script `gd_headcount.qvs` processa dados de *headcount* (contagem de funcionários) de uma organização, transformando-os em um modelo de dados para análise. Ele carrega dados brutos de arquivos QVD na camada *silver*, cria e popula tabelas de dimensões e fatos, limpa os dados e armazena os resultados em arquivos QVD na camada *gold*. O processo inclui a geração de tabelas auxiliares de calendário e tempo de serviço na empresa.

**2. Principais Etapas:**

* **2.1 Configurações:** O script inicia definindo as configurações de idioma e formatação para português (Brasil), incluindo separadores decimais e de milhares, formatos de moeda, data e hora, nomes de dias e meses, e o primeiro dia da semana. Define também variáveis para os caminhos de acesso aos arquivos de dados em diferentes camadas (bronze, silver, gold), fontes externas e internas.

* **2.2 Criação da Tabela de Calendário:**  Uma tabela de dimensão (`gd_calendario_d`) é criada contendo informações detalhadas sobre datas, como ano, mês, dia da semana, semana do ano, trimestre, semestre, e o status do período (histórico ou futuro).  Esta tabela é armazenada em um arquivo QVD na camada *gold*.

* **2.3 Criação da Tabela de Tempo na Companhia:** Uma tabela de dimensão (`gd_tempo_companhia_d`) é gerada, categorizando o tempo de serviço dos funcionários em grupos (gerencial e operacional) com base em faixas de tempo (meses, anos). Esta tabela também é salva como um QVD na camada *gold*.

* **2.4 Carregamento de Dados Brutos:** Dados brutos de *headcount*, demissões, orçamento histórico e posições de funcionários são carregados a partir de arquivos QVD na camada *silver*. Chaves *hash* são geradas para otimizar os relacionamentos entre as tabelas.

* **2.5 Criação de Dimensões:** Várias tabelas de dimensão são criadas a partir dos dados brutos:  `gd_employee_d` (funcionários), `gd_hierarquia_d` (hierarquia organizacional), `gd_funcao_d` (funções/cargos), `gd_eldorado_entity_d` (entidades Eldorado), `gd_secao_d` (seções), `gd_centro_de_custo_d` (centros de custo), `gd_situacao_d` (situação do funcionário), `gd_status_d` (status do *headcount*), `gd_tipo_funcionario_d` (tipo de funcionário), `gd_esclada_d` (jornada e escala de trabalho), `gd_idade_d` (idade e geração do funcionário), e `gd_contratacao_tipo_d` (tipo de contratação). Todas são armazenadas em arquivos QVD na camada *gold*.

* **2.6 Criação de Fatos:** Tabelas de fatos são criadas, consolidando informações relevantes: `gd_headcount_f` (*headcount*), `gd_termination_f` (demissões), `gd_excel_hc_orcamento_historico_f` (orçamento histórico), e `gd_posicoes_f` (posições). Campos desnecessários são removidos para otimização. As tabelas de fatos são armazenadas em arquivos QVD na camada *gold*.

* **2.7 Criação de Dimensões de Demissão:** As dimensões `gd_situacao_d`, `gd_status_d` e `gd_tipo_funcionario_d` são atualizadas com dados específicos de demissão.

* **2.8 Limpeza de Dados:** Tabelas temporárias e dados brutos não mais necessários são removidos.

* **2.9 Armazenamento dos Resultados:** Todas as tabelas (dimensões e fatos) são armazenadas em arquivos QVD na camada *gold*.

* **2.10 Finalização:** O script termina com `Exit Script`.

Documentação Técnica
Arquivo: gd_headcount.qvs
Última atualização: 07/08/2025 13:00:01
# Documentação Técnica do Script QlikView: gd_headcount.qvs

**Última Atualização:** 06/08/2025 13:05:25

**1. Resumo:**

O script `gd_headcount.qvs` processa e transforma dados de headcount (contagem de funcionários) de uma organização. Ele carrega dados brutos de diversas fontes (arquivos QVD na camada *silver*), cria e popula tabelas de dimensões e fatos, realiza a limpeza de dados e armazena os resultados em arquivos QVD na camada *gold*.  O processo inclui a geração de tabelas auxiliares de calendário e tempo na empresa.

**2. Principais Etapas:**

* **2.1 Configurações:** Define as configurações regionais e de formatação do script, incluindo separadores decimais e de milhares, formatos de moeda, data e hora, nomes de dias e meses em português (Brasil), primeiro dia da semana, e formato de abreviação numérica. Define também variáveis para os caminhos dos arquivos de dados nas camadas bronze, silver, gold, fontes externas e internas.

* **2.2 Criação da Tabela de Calendário:** Cria uma tabela de dimensão (`gd_calendario_d`) contendo informações detalhadas de datas (ano, mês, dia da semana, semana do ano, trimestre, semestre, status do período – histórico ou futuro).  A tabela é armazenada em um arquivo QVD na camada *gold*.

* **2.3 Criação da Tabela de Tempo na Companhia:** Gera uma tabela de dimensão (`gd_tempo_companhia_d`) que categoriza o tempo de serviço dos funcionários em grupos (gerencial e operacional), baseado em faixas de tempo (meses, anos). A tabela é armazenada em um arquivo QVD na camada *gold*.

* **2.4 Carregamento de Dados Brutos:** Carrega dados brutos de headcount, demissões, orçamento histórico e posições de funcionários a partir de arquivos QVD na camada *silver*.  Gera chaves hash para otimizar relacionamentos entre tabelas.

* **2.5 Criação de Dimensões:** Cria diversas tabelas de dimensão a partir dos dados brutos: `gd_employee_d` (funcionários), `gd_hierarquia_d` (hierarquia organizacional), `gd_funcao_d` (funções/cargos), `gd_eldorado_entity_d` (entidades Eldorado), `gd_secao_d` (seções), `gd_centro_de_custo_d` (centros de custo), `gd_situacao_d` (situação do funcionário), `gd_status_d` (status do headcount), `gd_tipo_funcionario_d` (tipo de funcionário), `gd_esclada_d` (jornada e escala de trabalho), `gd_idade_d` (idade e geração do funcionário), e `gd_contratacao_tipo_d` (tipo de contratação). Todas as dimensões são armazenadas em arquivos QVD na camada *gold*.

* **2.6 Criação de Fatos:** Cria tabelas de fatos consolidando informações relevantes: `gd_headcount_f` (headcount), `gd_termination_f` (demissões), `gd_excel_hc_orcamento_historico_f` (orçamento histórico), e `gd_posicoes_f` (posições).  Campos desnecessários são removidos para otimizar o tamanho.  As tabelas de fatos são armazenadas em arquivos QVD na camada *gold*.

* **2.7 Criação de Dimensões de Demissão:** As dimensões `gd_situacao_d`, `gd_status_d` e `gd_tipo_funcionario_d` são atualizadas com dados específicos de demissão.

* **2.8 Limpeza de Dados:** Remove tabelas temporárias e dados brutos não mais necessários após o processamento.

* **2.9 Armazenamento dos Resultados:** Armazena todas as tabelas (dimensões e fatos) em arquivos QVD na camada *gold*.

* **2.10 Finalização:** Encerra a execução do script usando `Exit Script`.


**Observação:** A documentação descreve o funcionamento do script, sem fornecer sugestões ou melhorias de código.

Documentação Técnica
Arquivo: gd_headcount.qvs
Última atualização: 07/08/2025 12:50:55
## Documentação Técnica do Script QlikView: gd_headcount.qvs

**Última Atualização:** 06/08/2025 13:05:25

**1. Resumo:**

O script `gd_headcount.qvs` é um script QlikView que processa e transforma dados de headcount (contagem de funcionários) de uma organização.  Ele carrega dados brutos de diversas fontes, cria dimensões e tabelas de fatos, realiza a limpeza dos dados e armazena os resultados em arquivos QVD para uso posterior em análises e relatórios de recursos humanos.  O processo inclui a geração de tabelas de calendário e tempo na empresa.


**2. Principais Etapas:**

* **2.1 Configurações Regionais e de Formatação:** Define as configurações de separadores decimais e de milhares, formatos de moeda, data e hora, e nomes de dias e meses para o idioma português (Brasil).  Define também outras configurações como o primeiro dia da semana e o formato de abreviação numérica.

* **2.2 Definição de Caminhos de Dados:** Define variáveis para especificar os caminhos de acesso aos arquivos de dados em diferentes camadas (bronze, silver, gold), bem como para fontes externas e internas.

* **2.3 Criação do Calendário:** Cria uma tabela de dimensão (`gd_calendario_d`) contendo informações detalhadas de datas, incluindo ano, mês, dia da semana, semana do ano, trimestre, semestre e status do período (histórico ou futuro). Esta tabela é armazenada em um arquivo QVD.

* **2.4 Criação do Tempo na Companhia:** Gera uma tabela de dimensão (`gd_tempo_companhia_d`) que categoriza o tempo de serviço dos funcionários em grupos gerenciais e operacionais,  baseado em faixas de tempo (meses, anos). Esta tabela também é armazenada em um arquivo QVD.

* **2.5 Carregamento de Dados Brutos:** Carrega dados brutos de headcount, demissões, orçamento histórico e posições de funcionários a partir de arquivos QVD existentes (localizados nas camadas *silver*).  Gera chaves hash para otimizar o relacionamento entre as tabelas.

* **2.6 Criação de Dimensões:** Cria várias tabelas de dimensão a partir dos dados brutos, incluindo:
    * `gd_employee_d`: Dimensão de funcionários, com informações demográficas e de contato.
    * `gd_hierarquia_d`: Dimensão de hierarquia organizacional.
    * `gd_funcao_d`: Dimensão de funções/cargos.
    * `gd_eldorado_entity_d`: Dimensão de entidades Eldorado.
    * `gd_secao_d`: Dimensão de seções.
    * `gd_centro_de_custo_d`: Dimensão de centros de custo.
    * `gd_situacao_d`: Dimensão de situação do funcionário.
    * `gd_status_d`: Dimensão de status do headcount.
    * `gd_tipo_funcionario_d`: Dimensão de tipo de funcionário.
    * `gd_esclada_d`: Dimensão de jornada e escala de trabalho.
    * `gd_idade_d`: Dimensão de idade e geração do funcionário.
    * `gd_contratacao_tipo_d`: Dimensão de tipo de contratação.
    Todas as tabelas de dimensão são armazenadas em arquivos QVD.

* **2.7 Criação de Fatos:** Cria tabelas de fatos a partir dos dados brutos, consolidando as informações relevantes e removendo campos desnecessários para otimizar o tamanho do arquivo. As tabelas criadas são:
    * `gd_headcount_f`: Tabela de fatos de headcount.
    * `gd_termination_f`: Tabela de fatos de demissões.
    * `gd_excel_hc_orcamento_historico_f`: Tabela de fatos de orçamento histórico.
    * `gd_posicoes_f`: Tabela de fatos de posições.
    Todas as tabelas de fatos são armazenadas em arquivos QVD.

* **2.8 Criação de Dimensões de Demissão:**  As dimensões `gd_situacao_d`, `gd_status_d` e `gd_tipo_funcionário_d` são concatenadas com dados específicos de demissão.

* **2.9 Limpeza de Dados:** Remove tabelas temporárias e dados brutos que não são mais necessários após o processamento.

* **2.10 Armazenamento dos Resultados:** Armazena todas as tabelas geradas (dimensões e fatos) em arquivos QVD, localizados na camada *gold*, para utilização posterior em aplicativos QlikView.

* **2.11 Finalização do Script:** Encerra a execução do script utilizando `Exit Script`.

Documentação Técnica
Arquivo: gd_headcount.qvs
Última atualização: 07/08/2025 12:48:35


Documentação Técnica
Arquivo: gd_headcount.qvs
Última atualização: 07/08/2025 12:39:45


Documentação Técnica
Arquivo: gd_headcount.qvs
Última atualização: 07/08/2025 12:33:30






// Documentação Técnica
// Arquivo: gd_headcount.qvs
// Última atualização: 07/08/2025 10:18:43
// Erro: nenhuma resposta gerada pela API.




Documentação Técnica do Script QlikView

## Nome do Arquivo
**gd_headcount.qvs**

## Data e Hora da Última Atualização
**06/08/2025 13:05:25**

## Descrição do que o Script Faz
O script `gd_headcount.qvs` é responsável por processar e transformar dados relacionados ao headcount (contagem de funcionários) de uma organização. Ele gera tabelas de calendário, tempo de empresa, e carrega dados brutos de headcount e demissões, além de criar dimensões e fatos que serão utilizados em análises de recursos humanos. O script também realiza a limpeza e a organização dos dados, armazenando os resultados em arquivos QVD para uso posterior.

## Lista Resumida dos Principais Componentes e Etapas

1. **Configurações Regionais e de Formatação**
   - Define separadores numéricos, formatos de moeda, data e hora, além de nomes de meses e dias em português.

2. **Definição de Caminhos de Dados**
   - Estabelece variáveis para os caminhos de acesso aos diferentes níveis de dados (bronze, silver, gold, etc.).

3. **Criação do Calendário**
   - Gera uma tabela de calendário (`gd_calendario_d`) com informações sobre datas, meses, anos, semanas e status de períodos (histórico ou futuro).

4. **Criação do Tempo na Companhia**
   - Gera uma tabela (`gd_tempo_companhia_d`) que categoriza o tempo de permanência dos funcionários na empresa em grupos gerenciais e operacionais.

5. **Carregamento de Dados Brutos**
   - Carrega dados de headcount, demissões, histórico de orçamento e posições a partir de arquivos QVD existentes, criando chaves de hierarquia e outras chaves de referência.

6. **Criação de Dimensões**
   - Cria várias dimensões (ex: `gd_employee_d`, `gd_hierarquia_d`, `gd_funcao_d`, etc.) a partir dos dados brutos, armazenando informações relevantes sobre funcionários, hierarquias, funções, seções e centros de custo.

7. **Criação de Fatos**
   - Gera tabelas de fatos (`gd_headcount_f`, `gd_termination_f`, etc.) que contêm dados consolidados sobre headcount e demissões, removendo campos desnecessários para otimizar o armazenamento.

8. **Criação de Dimensões de Demissão**
   - Cria dimensões específicas para demissões, incluindo status e tipo de funcionário.

9. **Limpeza de Dados**
   - Remove tabelas temporárias e dados brutos que não são mais necessários após a criação das tabelas finais.

10. **Armazenamento dos Resultados**
    - Armazena todas as tabelas geradas em arquivos QVD para uso futuro em análises e relatórios.

## Conclusão
O script `gd_headcount.qvs` é uma parte fundamental do processo de análise de dados de recursos humanos, permitindo a visualização e interpretação de informações críticas sobre a força de trabalho da organização. Através de sua estrutura organizada e eficiente, ele facilita a tomada de decisões informadas com base em dados atualizados e bem formatados.

TextBlock(citations=None, text='Documentação Técnica do Script QlikView\n\n## Nome do Arquivo\n**gd_headcount.qvs**\n\n## Data e Hora da Última Atualização\n**06/08/2025 13:05:25**\n\n## Descrição do que o Script Faz\nO script `gd_headcount.qvs` é responsável por processar e transformar dados relacionados ao headcount (contagem de funcionários) de uma organização. Ele gera tabelas de calendário, tempo de empresa, e carrega dados brutos de headcount e demissões, além de criar dimensões e fatos que serão utilizados em análises de recursos humanos. O script também realiza a limpeza e a organização dos dados, armazenando os resultados em arquivos QVD para uso posterior.\n\n## Lista Resumida dos Principais Componentes e Etapas\n\n1. **Configurações Regionais e de Formatação**\n   - Define separadores numéricos, formatos de moeda, data e hora, além de nomes de meses e dias em português.\n\n2. **Definição de Caminhos de Dados**\n   - Estabelece variáveis para os caminhos de acesso aos diferentes níveis de dados (bronze, silver, gold, etc.).\n\n3. **Criação do Calendário**\n   - Gera uma tabela de calendário (`gd_calendario_d`) com informações sobre datas, meses, anos, semanas e status de períodos (histórico ou futuro).\n\n4. **Criação do Tempo na Companhia**\n   - Gera uma tabela (`gd_tempo_companhia_d`) que categoriza o tempo de permanência dos funcionários na empresa em grupos gerenciais e operacionais.\n\n5. **Carregamento de Dados Brutos**\n   - Carrega dados de headcount, demissões, histórico de orçamento e posições a partir de arquivos QVD existentes, criando chaves de hierarquia e outras chaves de referência.\n\n6. **Criação de Dimensões**\n   - Cria várias dimensões (ex: `gd_employee_d`, `gd_hierarquia_d`, `gd_funcao_d`, etc.) a partir dos dados brutos, armazenando informações relevantes sobre funcionários, hierarquias, funções, seções e centros de custo.\n\n7. **Criação de Fatos**\n   - Gera tabelas de fatos (`gd_headcount_f`, `gd_termination_f`, etc.) que contêm dados consolidados sobre headcount e demissões, removendo campos desnecessários para otimizar o armazenamento.\n\n8. **Criação de Dimensões de Demissão**\n   - Cria dimensões específicas para demissões, incluindo status e tipo de funcionário.\n\n9. **Limpeza de Dados**\n   - Remove tabelas temporárias e dados brutos que não são mais necessários após a criação das tabelas finais.\n\n10. **Armazenamento dos Resultados**\n    - Armazena todas as tabelas geradas em arquivos QVD para uso futuro em análises e relatórios.\n\n## Conclusão\nO script `gd_headcount.qvs` é uma parte fundamental do processo de análise de dados de recursos humanos, permitindo a visualização e interpretação de informações críticas sobre a força de trabalho da organização. Através de sua estrutura organizada e eficiente, ele facilita a tomada de decisões informadas com base em dados atualizados e bem formatados.', type='text')

TextBlock(citations=None, text='Documentação Técnica do Script QlikView\n\n## Nome do Arquivo\n**gd_headcount.qvs**\n\n## Data e Hora da Última Atualização\n**06/08/2025 13:05:25**\n\n## Descrição do que o Script Faz\nO script `gd_headcount.qvs` é responsável por processar e transformar dados relacionados ao headcount (contagem de funcionários) de uma organização. Ele gera tabelas de calendário, tempo de empresa, e carrega dados brutos de headcount e demissões, além de criar dimensões e fatos que serão utilizados em análises de recursos humanos. O script também realiza a limpeza e a organização dos dados, armazenando os resultados em arquivos QVD para uso posterior.\n\n## Lista Resumida dos Principais Componentes e Etapas\n\n1. **Configurações Regionais e de Formatação**\n   - Define separadores numéricos, formatos de moeda, data e hora, além de nomes de meses e dias em português.\n\n2. **Definição de Caminhos de Dados**\n   - Estabelece variáveis para os caminhos de acesso aos diferentes níveis de dados (bronze, silver, gold, etc.).\n\n3. **Criação do Calendário**\n   - Gera uma tabela de calendário (`gd_calendario_d`) com informações sobre datas, meses, anos, semanas e status de períodos (histórico ou futuro).\n\n4. **Criação do Tempo na Companhia**\n   - Gera uma tabela (`gd_tempo_companhia_d`) que categoriza o tempo de permanência dos funcionários na empresa em grupos gerenciais e operacionais.\n\n5. **Carregamento de Dados Brutos**\n   - Carrega dados de headcount, demissões, histórico de orçamento e posições a partir de arquivos QVD existentes, criando chaves de hierarquia e outras chaves de referência.\n\n6. **Criação de Dimensões**\n   - Cria várias dimensões (ex: `gd_employee_d`, `gd_hierarquia_d`, `gd_funcao_d`, etc.) a partir dos dados brutos, armazenando informações relevantes sobre funcionários, hierarquias, funções, seções e centros de custo.\n\n7. **Criação de Fatos**\n   - Gera tabelas de fatos (`gd_headcount_f`, `gd_termination_f`, etc.) que contêm dados consolidados sobre headcount e demissões, removendo campos desnecessários para otimizar o armazenamento.\n\n8. **Criação de Dimensões de Demissão**\n   - Cria dimensões específicas para demissões, incluindo status e tipo de funcionário.\n\n9. **Limpeza de Dados**\n   - Remove tabelas temporárias e dados brutos que não são mais necessários após a criação das tabelas finais.\n\n10. **Armazenamento dos Resultados**\n    - Armazena todas as tabelas geradas em arquivos QVD para uso futuro em análises e relatórios.\n\n## Conclusão\nO script `gd_headcount.qvs` é uma parte fundamental do processo de análise de dados de recursos humanos, permitindo a visualização e interpretação de informações críticas sobre a força de trabalho da organização. Através de sua estrutura organizada e eficiente, ele facilita a tomada de decisões informadas com base em dados atualizados e bem formatados.', type='text')

﻿// Documentação Técnica
// Arquivo: gd_headcount.qvs
// Última atualização: 06/08/2025 13:05:25
# Documentação Técnica do Script QlikView

## Nome do Arquivo
**gd_headcount.qvs**

## Data e Hora da Última Atualização
**06/08/2025 13:05:25**

## Descrição do que o Script Faz
O script `gd_headcount.qvs` é responsável por processar e transformar dados relacionados ao headcount (contagem de funcionários) de uma organização. Ele gera tabelas de calendário, tempo de empresa, e carrega dados brutos de headcount e demissões, além de criar dimensões e fatos que serão utilizados em análises de recursos humanos. O script também realiza a limpeza e a organização dos dados, armazenando os resultados em arquivos QVD para uso posterior.

## Lista Resumida dos Principais Componentes e Etapas

1. **Configurações Regionais e de Formatação**
   - Define separadores numéricos, formatos de moeda, data e hora, além de nomes de meses e dias em português.

2. **Definição de Caminhos de Dados**
   - Estabelece variáveis para os caminhos de acesso aos diferentes níveis de dados (bronze, silver, gold, etc.).

3. **Criação do Calendário**
   - Gera uma tabela de calendário (`gd_calendario_d`) com informações sobre datas, meses, anos, semanas e status de períodos (histórico ou futuro).

4. **Criação do Tempo na Companhia**
   - Gera uma tabela (`gd_tempo_companhia_d`) que categoriza o tempo de permanência dos funcionários na empresa em grupos gerenciais e operacionais.

5. **Carregamento de Dados Brutos**
   - Carrega dados de headcount, demissões, histórico de orçamento e posições a partir de arquivos QVD existentes, criando chaves de hierarquia e outras chaves de referência.

6. **Criação de Dimensões**
   - Cria várias dimensões (ex: `gd_employee_d`, `gd_hierarquia_d`, `gd_funcao_d`, etc.) a partir dos dados brutos, armazenando informações relevantes sobre funcionários, hierarquias, funções, seções e centros de custo.

7. **Criação de Fatos**
   - Gera tabelas de fatos (`gd_headcount_f`, `gd_termination_f`, etc.) que contêm dados consolidados sobre headcount e demissões, removendo campos desnecessários para otimizar o armazenamento.

8. **Criação de Dimensões de Demissão**
   - Cria dimensões específicas para demissões, incluindo status e tipo de funcionário.

9. **Limpeza de Dados**
   - Remove tabelas temporárias e dados brutos que não são mais necessários após a criação das tabelas finais.

10. **Armazenamento dos Resultados**
    - Armazena todas as tabelas geradas em arquivos QVD para uso futuro em análises e relatórios.

## Conclusão
O script `gd_headcount.qvs` é uma parte fundamental do processo de análise de dados de recursos humanos, permitindo a visualização e interpretação de informações críticas sobre a força de trabalho da organização. Através de sua estrutura organizada e eficiente, ele facilita a tomada de decisões informadas com base em dados atualizados e bem formatados.




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
SET LongMonthNames='janeiro;fevereiro;março;abril;maio;junho;julho;agosto;setembro;outubro;novembro;dezembro';
SET DayNames='seg;ter;qua;qui;sex;sáb;dom';
SET LongDayNames='segunda-feira;terça-feira;quarta-feira;quinta-feira;sexta-feira;sábado;domingo';
SET NumericalAbbreviation='3:k;6:M;9:G;12:T;15:P;18:E;21:Z;24:Y;-3:m;-6:μ;-9:n;-12:p;-15:f;-18:a;-21:z;-24:y';

//SET silver_layer = '\\BRSPOWVQDEV01\QlikSharedFolder\CustomData\Eldorado Brasil\3. Recursos Humanos\People Analytics\01. HR Medallion\02. Silver\';
//SET gold_layer = '\\BRSPOWVQDEV01\QlikSharedFolder\CustomData\Eldorado Brasil\3. Recursos Humanos\People Analytics\01. HR Medallion\03. Gold\';


SET bronze_layer = 'lib://Eldorado Data Folder - 3 Recursos Humanos - People Analytics/01. HR Medallion/01. Bronze/';
SET silver_layer = 'lib://Eldorado Data Folder - 3 Recursos Humanos - People Analytics/01. HR Medallion/02. Silver/';
SET gold_layer = 'lib://Eldorado Data Folder - 3 Recursos Humanos - People Analytics/01. HR Medallion/03. Gold/';
SET manual_source = 'lib://Eldorado Data Folder - 3 Recursos Humanos - People Analytics/02. Manual Source/';
SET ti_layer = 'lib://Staging Recursos Humanos/';
SET external_layer = 'lib://Eldorado Data Folder - 3 Recursos Humanos - People Analytics/04. Fontes Externas/';



///////////////////////////        CREATE CALENDARIO      //////////////////////////////////////////////


Let vDataInicio = '2014-01-01';
Let vDataFim = Date(MakeDate(Year(Today()), 12, 31), 'YYYY-MM-DD');

gd_calendario_d:
Load
    Date(TempDate, 'DD.MM.YYYY')  																						as date_key,
    Date(Floor(MonthEnd(TempDate)), 'DD.MM.YYYY') 																		as load_month,
    Year(TempDate) 																										as ano,
    Num(Month(TempDate)) 																								as mes_numero,
    Month(TempDate) 																								    as mes_nome,
    Day(TempDate) 																										as dia,
    Week(TempDate)																										as semana_ano,
    Num(Weekday(TempDate)) 																								as dia_semana_numero,
    Date(TempDate, 'WWW') 																								as dia_semana_nome,
    Month(TempDate) & ' - ' &  Year(TempDate) 																			as ano_mes,   //Date(MonthStart(TempDate), 'YYYY-MM')
    If(MonthStart(TempDate) = MonthStart(Today()), 'Sim', 'Não') 														as mes_atual,
    If(YearStart(TempDate) = YearStart(Today()), 'Sim', 'Não') 															as ano_atual,
    Date(TempDate, 'YYYY-Q') 																							as ano_trimestre,
    Dual('Sem ' & Week(TempDate) & ' ' & Year(TempDate), WeekStart(TempDate)) 											as ano_semana,
    If(TempDate <= Today(), 'Historico', 'Futuro') 																		as periodo_status,
    If(TempDate = Today(), 'Sim', 'Não') 																				as hoje,
    If(TempDate = Today() - 1, 'Sim', 'Não') 																			as ontem,
    If(TempDate = Today() + 1, 'Sim', 'Não') 																			as amanha,
    If(WeekDay(TempDate) >= 6, 'Sim', 'Não') 																			as final_semana,
    NetworkDays(TempDate, TempDate) 																					as dia_util,
    Ceil(Month(TempDate)/3) 																							as trimestre_fiscal,
    Ceil(Month(TempDate)/6)                                                                                             as semestre,
    'S' & Ceil(Month(TempDate)/6) & ' - ' & Year(TempDate)                                                              as ano_semestre

;
Load
    TempDate
Where
    TempDate >= Date('$(vDataInicio)') and TempDate <= Date('$(vDataFim)');


Load
    MakeDate(2014,1,1) + IterNo() - 1 as TempDate
AutoGenerate 1
While IterNo() <= (Date('$(vDataFim)') - Date('$(vDataInicio)') + 1); 


STORE gd_calendario_d INTO [$(gold_layer)gd_calendario_d.QVD]
(qvd);



///////////////////////////        CREATE TIME IN COMPANY      //////////////////////////////////////////////

Let vDiasMax = 365.25 * 30; // Define 30 anos como exemplo

gd_tempo_companhia_d:
Load
    RowNo() as tempo_empresa_key,
    
    // Grupo Gerencial (Anos Agrupados)
    If(
        RowNo() <= 365.25 * 3,
        'Ano ' & Ceil(RowNo() / 365.25),
        If(
            RowNo() <= 365.25 * 10,
            'Ano ' & 
            (3 + Floor((RowNo() - 365.25 * 3) / (365.25 * 2)) * 2) & '-' & 
            (3 + Ceil((RowNo() - 365.25 * 3) / (365.25 * 2)) * 2),
            If(
                RowNo() <= 365.25 * 15,
                'Ano ' & 
                (10 + Floor((RowNo() - 365.25 * 10) / (365.25 * 5)) * 5) & '-' & 
                (10 + Ceil((RowNo() - 365.25 * 10) / (365.25 * 5)) * 5),
                'Mais que 15 anos'
            )
        )
    ) as grupo_gerencial,
    
    // Grupo Operacional (Meses/Anos)
    If(
        RowNo() <= 365.25, // Primeiro ano
        If(
            RowNo() <= 365.25 / 4, '0-3 meses',
            If(
                RowNo() <= 365.25 / 2, '3-6 meses',
                //If(
                  // RowNo() <= 365.25 * 0.75, '6-9 meses',
                    '9-12 meses'
                //)
            )
        ),
        If(
            RowNo() <= 365.25 * 4, // Até 4 anos
            'Ano ' & Ceil(RowNo() / 365.25) & ' - ' &
            Num(Floor((RowNo() - 365.25) / 182.625) * 6 + 12, '#0') & '-' &
            Num(Floor((RowNo() - 365.25) / 182.625) * 6 + 18, '#0') & ' meses',
            'Mais que 4 anos' // Acima de 4 anos
        )
    ) as grupo_operacao,

    If(  RowNo() <= 365.25, 'TRUE', 'FALSE')  as new_hire,
    // Campos numéricos
    RowNo() as dias_totais,
    Div(RowNo(), 30) as meses_totais,
    Div(RowNo(), 365.25) as anos_totais
AutoGenerate Floor($(vDiasMax));

STORE gd_tempo_companhia_d INTO [$(gold_layer)gd_tempo_companhia_d.QVD] (qvd);



///////////////////////////        LOAD RAW     //////////////////////////////////////////////



NoConcatenate
sv_headcount_f_raw:

Load
*
,Hash128(
	hierarquia_nome_n1,	hierarquia_nome_n2,	hierarquia_nome_n3
   ,hierarquia_nome_n4,	hierarquia_nome_n5, hierarquia_nome_n6,
	num(hierarquia_cod_n1),	num(hierarquia_cod_n2),	num(hierarquia_cod_n3)
   ,num(hierarquia_cod_n4),	num(hierarquia_cod_n5), num(hierarquia_cod_n6)
   ,gestor_direto_nome,	num(gestor_direto_cod)) 									as hierarquia_sk
,Hash128(num(funcao_cod)) 															as funcao_sk 
,Hash128(num(secao_cod)) 													    	as secao_sk
,Hash128(num(filial_cod), num(coligada_cod))										as eldorado_entity_sk
,Hash128(num(centro_de_custo)) 														as centro_de_custo_sk																																								
,Hash128(situacao_cod)                  											as situacao_sk
,Hash128(tipo_funcionario_cod) 														as tipo_funcionario_sk
,Hash128(jornada_mensal) 															as jornada_sk
,Hash128(contratacao_tipo)															as contratacao_tipo_sk
,Hash128(headcount_status)															as status_sk
//,Hash128(new_hire_flag) 															as hire_sk
,load_date 																			as date_key
,tempo_empresa_dias 																as tempo_empresa_key



FROM [$(silver_layer)sv_headcount_f.QVD]
(qvd);


NoConcatenate
sv_termination_f_raw:

Load
*
,Hash128(
	hierarquia_nome_n1,	hierarquia_nome_n2,	hierarquia_nome_n3,
    hierarquia_nome_n4,	hierarquia_nome_n5, hierarquia_nome_n6,
	num(hierarquia_cod_n1),	num(hierarquia_cod_n2),	num(hierarquia_cod_n3)
    ,num(hierarquia_cod_n4),	num(hierarquia_cod_n5), num(hierarquia_cod_n6), 
    gestor_direto_nome,	num(gestor_direto_cod)) 												as hierarquia_sk
,Hash128(num(funcao_cod))																		as funcao_sk
,Hash128(num(secao_cod)) 													    				as secao_sk
,Hash128(num(filial_cod),num( coligada_cod))													as eldorado_entity_sk
,Hash128(num(centro_de_custo) )																	as centro_de_custo_sk																																								
,Hash128(num(situacao_cod))                  													as situacao_sk
,Hash128(num(tipo_funcionario_cod) 	)															as tipo_funcionario_sk
,Hash128(jornada_mensal) 																		as jornada_sk
,Hash128(contratacao_tipo)																		as contratacao_tipo_sk
,Hash128('Desligado')																			as status_sk
//,Hash128(new_hire_flag) 															            as hire_sk
,termination_date 																				as date_key
,tempo_empresa_dias 																			as tempo_empresa_key

FROM [$(silver_layer)sv_termination_f.QVD]
(qvd);

NoConcatenate

sv_excel_hc_orcamento_historico_raw:
LOAD
*
,Hash128(num(funcao_cod))																		as funcao_sk
,Hash128(num(filial_cod), num( coligada_cod)	)												as eldorado_entity_sk
,Hash128(num(centro_de_custo_cod) )																as centro_de_custo_sk
,load_date  																					as date_key
FROM [$(silver_layer)sv_excel_hc_orcamento_historico_f.QVD]
(qvd);


NoConcatenate

sv_posicoes_raw:
LOAD
 
 *
,Hash128(num(funcao_cod) )																		as funcao_sk
,Hash128(num(centro_de_custo)) 												   					as centro_de_custo_sk
,load_date  																					as date_key
FROM [$(silver_layer)sv_posicoes_f.QVD]
(qvd);





/////////////////////////////        CREATE DIMENSION      //////////////////////////////////////////////

NoConcatenate

gd_employee_d:
LOAD
    pessoa,
    FirstSortedValue(nome, -load_date)                  as nome,
    FirstSortedValue(nascimento_data, -load_date)       as nascimento_data,
    FirstSortedValue(raca_cod, -load_date)              as raca_cod,
    FirstSortedValue(raca_nome, -load_date)             as raca_nome,
    FirstSortedValue(genero, -load_date)                as genero,
    FirstSortedValue(cpf, -load_date)                   as cpf,
    FirstSortedValue(rg, -load_date)                    as rg,
    FirstSortedValue(cnh_cod, -load_date)               as cnh_cod,
    FirstSortedValue(cnh_tipo, -load_date)              as cnh_tipo,
    FirstSortedValue(cnh_vencimento, -load_date)        as cnh_vencimento,
    FirstSortedValue(estado, -load_date)                as estado,
    FirstSortedValue(estado_civil_cod, -load_date)      as estado_civil_cod,
    FirstSortedValue(estado_civil_nome, -load_date)     as estado_civil_nome,
    FirstSortedValue(nacionalidade, -load_date)         as nacionalidade,
    FirstSortedValue(naturalidade, -load_date)          as naturalidade,
    FirstSortedValue(rua, -load_date)                   as rua,
    FirstSortedValue(numero, -load_date)                as numero,
    FirstSortedValue(complemento, -load_date)           as complemento,
    FirstSortedValue(bairro, -load_date)                as bairro,
    FirstSortedValue(cidade, -load_date)                as cidade,
    FirstSortedValue(pais, -load_date)                  as pais,
    FirstSortedValue(cep, -load_date)                   as cep,
    FirstSortedValue(telefone, -load_date)              as telefone,
    FirstSortedValue(readimitido, -load_date)           as readimitido,
    FirstSortedValue(qtd_readimissoes, -load_date)      as qtd_readimissoes,
    FirstSortedValue(pispasep, -load_date)              as pispasep,
    FirstSortedValue(email, -load_date)                 as email,
    FirstSortedValue(dependentes, -load_date)           as dependentes,
    FirstSortedValue(sindicato, -load_date)             as sindicato,
    FirstSortedValue(sindicato_nome, -load_date)        as sindicato_nome,
    Max(load_date)                                      as ultima_data
Resident sv_headcount_f_raw
where indice_pessoa = 1
Group By pessoa;


STORE gd_employee_d INTO [$(gold_layer)gd_employee_d.QVD]
(qvd);


NoConcatenate 

gd_hierarquia_d:
load Distinct 
 hierarquia_sk
,hierarquia_nome_n1
,hierarquia_nome_n2
,hierarquia_nome_n3
,hierarquia_nome_n4
,hierarquia_nome_n5
,hierarquia_nome_n6
,hierarquia_cod_n1
,hierarquia_cod_n2
,hierarquia_cod_n3
,hierarquia_cod_n4
,hierarquia_cod_n5
,hierarquia_cod_n6
,gestor_direto_nome
,gestor_direto_cod
Resident sv_headcount_f_raw;

STORE gd_hierarquia_d INTO [$(gold_layer)gd_hierarquia_d.QVD]
(qvd);

NoConcatenate

gd_funcao_d:
Load Distinct
 Hash128(num(funcao_cod)) 						as funcao_sk
,*
From [$(silver_layer)sv_funcao_d.QVD]
(qvd);

STORE gd_funcao_d INTO [$(gold_layer)gd_funcao_d.QVD]
(qvd);



NoConcatenate

gd_eldorado_entity_d:
Load distinct
 eldorado_entity_sk
,filial_cod
,filial_nome
,coligada_cod
,coligada_nome
Resident sv_headcount_f_raw;

STORE gd_eldorado_entity_d INTO [$(gold_layer)gd_eldorado_entity_d.QVD]
(qvd);


NoConcatenate

gd_secao_d:
Load distinct
 secao_sk
,secao_cod
,secao_nome
Resident sv_headcount_f_raw;

STORE gd_secao_d INTO [$(gold_layer)gd_secao_d.QVD]
(qvd);



NoConcatenate
gd_centro_de_custo_d:
Load distinct
Hash128(num(centro_de_custo) )																	as centro_de_custo_sk
,UPPER(grupo_diretoria) 																		as GRUPO_DIRETORIA_SECTION_ACCESS
,*
FROM [$(silver_layer)sv_centro_de_custo_d.QVD]
(qvd);

STORE gd_centro_de_custo_d INTO [$(gold_layer)gd_centro_de_custo_d.QVD]
(qvd);



NoConcatenate


gd_situacao_d:
load Distinct 
 situacao_sk
,situacao_cod
,situacao_nome
Resident sv_headcount_f_raw;
// está sendo salvo na etapa de termination dimension



/* removida pois agora está dentro da dimensao de tempo na companhia

 NoConcatenate

gd_hire_d:
load Distinct 
 hire_sk
,new_hire_flag as new_hire_flag
Resident sv_headcount_f_raw;
STORE gd_hire_d INTO [$(gold_layer)gd_hire_d.QVD]
(qvd);

*/

NoConcatenate


gd_status_d:
load Distinct
status_sk
,headcount_status as status
Resident sv_headcount_f_raw;
// está sendo salvo na etapa de termination dimension


NoConcatenate

gd_tipo_funcionario_d:
load
    tipo_funcionario_sk,
    tipo_funcionario_cod,
    tipo_funcionario_nome
Resident sv_headcount_f_raw
Where Len(Trim(tipo_funcionario_nome)) > 0
  and tipo_funcionario_nome <> '-';


// está sendo salvo na etapa de termination dimension


NoConcatenate

gd_esclada_d:
Load Distinct
jornada_sk
,jornada_mensal
,escala
Resident sv_headcount_f_raw;

STORE gd_esclada_d INTO [$(gold_layer)gd_esclada_d.QVD]
(qvd);


Noconcatenate

gd_idade_d:
Load 
    RecNo() - 1 as idade,  // Gera idades de 0 a 100
    
    // Criar Grupos de Idade
    If(
        RecNo() - 1 <= 10, '0-10',
        If(RecNo() - 1 <= 20, '11-20',
        If(RecNo() - 1 <= 30, '21-30',
        If(RecNo() - 1 <= 40, '31-40',
        If(RecNo() - 1 <= 50, '41-50',
        If(RecNo() - 1 <= 60, '51-60',
        If(RecNo() - 1 <= 70, '61-70',
        '71+'))))))) as grupo_idade,
        
    // Criar Gerações com base na idade atual
If((Year(Today()) - (RecNo() - 1)) >= 2011, 'Geração Alpha (2011 - presente)',
If((Year(Today()) - (RecNo() - 1)) >= 1996, 'Geração Z (1996 - 2010)',
If((Year(Today()) - (RecNo() - 1)) >= 1981, 'Geração Y (1981 - 1995)',
If((Year(Today()) - (RecNo() - 1)) >= 1965, 'Geração X (1965 - 1980)',
If((Year(Today()) - (RecNo() - 1)) >= 1946, 'Boomers (1946 - 1964)',
'Geração Silenciosa (Antes de 1946)'))))) as geracao

    // Criar Gerações com base na idade atual
,If((Year(Today()) - (RecNo() - 1)) >= 2011, 'A',
If((Year(Today()) - (RecNo() - 1)) >= 1996, 'Z',
If((Year(Today()) - (RecNo() - 1)) >= 1981, 'Y',
If((Year(Today()) - (RecNo() - 1)) >= 1965, 'X',
If((Year(Today()) - (RecNo() - 1)) >= 1946, 'Boomers',
'S'))))) as geracao_cod

Autogenerate 101;

STORE gd_idade_d INTO [$(gold_layer)gd_idade_d.QVD]
(qvd);

NoConcatenate

gd_contratacao_tipo_d:
Load Distinct
contratacao_tipo_sk
,contratacao_tipo
Resident sv_headcount_f_raw;

STORE gd_contratacao_tipo_d INTO [$(gold_layer)gd_contratacao_tipo_d.QVD]
(qvd);




///////////////////////////        CREATE HEADCOUNT FACT     //////////////////////////////////////////////


NoConcatenate

gd_headcount_f:
Load
*
Resident sv_headcount_f_raw;


Drop Field

// EMPLOYEE
 nome
,nascimento_data
,raca_cod
,raca_nome
,genero
,cpf
,rg
,cnh_cod
,cnh_tipo
,cnh_vencimento
,estado
,estado_civil_cod
,estado_civil_nome
,nacionalidade                                                                                                                                                                
,naturalidade                                                                                                         
,rua
,numero
,complemento
,bairro
,cidade
,pais
,cep
,telefone
,readimitido
,qtd_readimissoes
,pispasep
,email
,dependentes
,sindicato
,sindicato_nome

// HIERARQUIA
,hierarquia_nome_n1
,hierarquia_nome_n2
,hierarquia_nome_n3
,hierarquia_nome_n4
,hierarquia_nome_n5
,hierarquia_nome_n6
,hierarquia_cod_n1
,hierarquia_cod_n2
,hierarquia_cod_n3
,hierarquia_cod_n4
,hierarquia_cod_n5
,hierarquia_cod_n6
,gestor_direto_nome


// FUNCAO
//,funcao_cod ---- mantido para facilitar a validação
,funcao_nome
,lider_flag
,operacional_flag
,carreira
,grupo_cargo
,grupo_cargo_micro
,grupo_relatorio
,gs
,cargo_salarial_tipo
,cbo_2002
,cbo_descricao


//CENTRO DE CUSTO
// ,centro_de_custo -----------------mantido para facilitar a validação
,secao_cod
,secao_nome
,coligada_cod
,coligada_nome
,filial_cod
,filial_nome
,grupo_diretoria
,diretoria
,area

//secao
,secao_cod
,secao_nome
,coligada_cod
,coligada_nome
,filial_cod
,filial_nome
,grupo_diretoria
,diretoria
,area

//SITUACAO
,situacao_cod
,situacao_nome
,headcount_status

//TIPO FUNCIONARIO
,tipo_funcionario_cod
,tipo_funcionario_nome

// ESCALA
,jornada_mensal
,escala

//RANGE SALARIO
,range_salario_key
,[80]
,[90]
,[100]
,[110]
,[120]

//ADVERTENCIAS - REVISAR O PROCESSO NAO ESTÁ CORRETO
// ,advertencias
// ,advertencias_total
// ,advertencias_motivo
// ,advertencias_punicao
// ,advertencias_tipo
// ,advertencias_data

// NEW HIRE
,contratacao_tipo


From gd_headcount_f;

STORE gd_headcount_f INTO [$(gold_layer)gd_headcount_f.QVD]
(qvd);



///////////////////////////        CREATE TERMINATION FACT      //////////////////////////////////////////////



NoConcatenate

gd_termination_f:
Load
*
Resident sv_termination_f_raw;

Drop Field

// EMPLOYEE
 nome
,nascimento_data
,raca_cod
,raca_nome
,genero
,cpf
,rg
,cnh_cod
,cnh_tipo
,cnh_vencimento
,estado
,estado_civil_cod
,estado_civil_nome
,nacionalidade                                                                                                                                                                
,naturalidade                                                                                                         
,rua
,numero
,complemento
,bairro
,cidade
,pais
,cep
,telefone
,readimitido
,qtd_readimissoes
,pispasep
,email
,dependentes
,sindicato
,sindicato_nome

// HIERARQUIA
,hierarquia_nome_n1
,hierarquia_nome_n2
,hierarquia_nome_n3
,hierarquia_nome_n4
,hierarquia_nome_n5
,hierarquia_nome_n6
,hierarquia_cod_n1
,hierarquia_cod_n2
,hierarquia_cod_n3
,hierarquia_cod_n4
,hierarquia_cod_n5
,hierarquia_cod_n6
,gestor_direto_nome


// FUNCAO
,funcao_cod
,funcao_nome
,lider_flag
,operacional_flag
,carreira
,grupo_cargo
,grupo_cargo_micro
,grupo_relatorio
,gs
,cargo_salarial_tipo
,cbo_2002
,cbo_descricao

// entity

,centro_de_custo
,secao_cod
,secao_nome
,coligada_cod
,coligada_nome
,filial_cod
,filial_nome
,grupo_diretoria
,diretoria
,area

//secao
,secao_cod
,secao_nome
,coligada_cod
,coligada_nome
,filial_cod
,filial_nome
,grupo_diretoria
,diretoria
,area

//SITUACAO
,situacao_cod
,situacao_nome
// ,headcount_status

//TIPO FUNCIONARIO
,tipo_funcionario_cod
,tipo_funcionario_nome

// ESCALA
,jornada_mensal
,escala

//RANGE SALARIO
,range_salario_key
,[80]
,[90]
,[100]
,[110]
,[120]

//ADVERTENCIAS - REVISAR O PROCESSO NAO ESTÁ CORRETO
// ,advertencias
// ,advertencias_total
// ,advertencias_motivo
// ,advertencias_punicao
// ,advertencias_tipo
// ,advertencias_data

// NEW HIRE
,contratacao_tipo




From gd_termination_f;


STORE gd_termination_f INTO [$(gold_layer)gd_termination_f.QVD]
(qvd);






///////////////////////////        CREATE ORCAMENTO FACT      //////////////////////////////////////////////


NoConcatenate

gd_excel_hc_orcamento_historico_f:
Load
*
Resident sv_excel_hc_orcamento_historico_raw;

Drop Field 

centro_de_custo_cod
,load_date
,funcao_cod
,coligada_cod
From gd_excel_hc_orcamento_historico_f;


STORE gd_excel_hc_orcamento_historico_f INTO [$(gold_layer)gd_excel_hc_orcamento_historico_f.QVD]
(qvd);






///////////////////////////        CREATE POSITION FACT      //////////////////////////////////////////////






NoConcatenate

gd_posicoes_f:
Load
*
Resident sv_posicoes_raw;

Drop Field 
 centro_de_custo
,load_date
,funcao_cod
,funcao_nome
// ,area
// ,cidade
// ,diretoria
// ,genero
// ,grupo_diretoria
// ,nome
// ,secao_cod
// ,filial_cod
// ,coligada_cod


From gd_posicoes_f;
;


STORE gd_posicoes_f INTO [$(gold_layer)gd_posicoes_f.QVD]
(qvd);






///////////////////////////        CREATE TERMINATION DIMENSION      //////////////////////////////////////////////



Concatenate (gd_situacao_d)

gd_situacao_termination_d:
load Distinct 
situacao_sk
,situacao_cod
,situacao_nome

Resident sv_termination_f_raw;




STORE gd_situacao_d INTO [$(gold_layer)gd_situacao_d.QVD]
(qvd);


Concatenate(gd_status_d)
load distinct
status_sk
,'Desligado' as status
Resident sv_termination_f_raw;

STORE gd_status_d INTO [$(gold_layer)gd_status_d.QVD]
(qvd);



Concatenate(gd_tipo_funcionario_d)
LOAD Distinct
    tipo_funcionario_sk,
    tipo_funcionario_cod,
    tipo_funcionario_nome
Resident sv_termination_f_raw
Where Len(Trim(tipo_funcionario_nome)) > 0
  and tipo_funcionario_nome <> '-';



STORE gd_tipo_funcionario_d INTO [$(gold_layer)gd_tipo_funcionario_d.QVD]
(qvd);






///////////////////////////        DROP      //////////////////////////////////////////////






Drop Table
 sv_headcount_f_raw
,sv_termination_f_raw
,gd_headcount_f
,gd_termination_f
,sv_excel_hc_orcamento_historico_raw
,gd_excel_hc_orcamento_historico_f
,gd_posicoes_f
,sv_posicoes_raw




, gd_employee_d
, gd_hierarquia_d
// , gd_funcao_d
, gd_eldorado_entity_d
, gd_secao_d
, gd_centro_de_custo_d
, gd_situacao_d
, gd_tipo_funcionario_d
, gd_esclada_d
, gd_idade_d
, gd_contratacao_tipo_d
, gd_status_d

;
Exit script