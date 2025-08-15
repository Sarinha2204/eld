# Documentação Técnica

**Arquivo:** `bz_headcount.qvs`  
**Última atualização:** 15/08/2025 09:40:31

# **Documentação do Script QVS – Processamento de Dados de Recursos Humanos**

## **1. Introdução**
Este documento explica, de forma clara e organizada, o funcionamento de um script utilizado para processar e organizar dados relacionados a **Recursos Humanos (RH)**. O script é escrito em uma linguagem chamada **QVS** (usada na ferramenta **QlikView/Qlik Sense**), que serve para **carregar, transformar e armazenar informações** de maneira estruturada.

O objetivo principal deste script é **coletar dados brutos de diferentes fontes** (como planilhas e arquivos de banco de dados) e **prepará-los para análise**, facilitando relatórios e tomadas de decisão na área de RH.

---

## **2. Configurações Iniciais**
Antes de carregar os dados, o script define **regras de formatação** para garantir que números, datas, moedas e textos sejam exibidos de maneira padronizada e compreensível.

### **2.1. Formatação de Números, Moedas e Datas**
| Configuração | Descrição | Exemplo |
|--------------|-----------|---------|
| **ThousandSep='.'** | Separador de milhar (ponto) | `1.000` (mil) |
| **DecimalSep=','** | Separador decimal (vírgula) | `10,50` (dez vírgula cinquenta) |
| **MoneyFormat='R$#.##0,00'** | Formato de moeda (Real brasileiro) | `R$1.250,00` |
| **DateFormat='DD.MM.YYYY'** | Formato de data (dia.mês.ano) | `15.05.2024` |
| **TimestampFormat** | Formato de data e hora | `15/05/2024 14:30:00` |
| **CollationLocale='pt-BR'** | Idioma para ordenação (português do Brasil) | Ordena palavras como "ç" e acentos corretamente |

### **2.2. Configuração de Caminhos (Pastas de Origem e Destino)**
O script define **onde os dados serão buscados e salvos**, utilizando **variáveis** (como "endereços" para pastas). Essas pastas são organizadas em **camadas** (Bronze, Silver, Gold), que representam diferentes estágios de tratamento dos dados:

| Variável | Descrição | Exemplo de Conteúdo |
|----------|-----------|---------------------|
| **bronze_layer** | Local onde os dados **brutos** (sem tratamento) são armazenados. | Arquivos QVD com informações diretas de sistemas. |
| **silver_layer** | Local para dados **parcialmente tratados** (limpos e organizados). | Tabelas com dados validados e padronizados. |
| **gold_layer** | Local para dados **prontos para análise** (modelados para relatórios). | Informações consolidadas para dashboards. |
| **manual_source** | Pasta com dados **manualmente inseridos** (planilhas Excel). | Tabelas de cargos, filiais, salários. |
| **ti_layer** | Dados vindos de **sistemas corporativos** (como SAP). | Informações de funcionários, hierarquia, salários. |
| **external_layer** | Dados de **fontes externas** (fora do RH). | Centros de custo de outros departamentos. |

---
## **3. Processamento dos Dados**
O script é dividido em **blocos**, cada um responsável por **carregar um tipo específico de informação** e salvá-la na camada **Bronze** (dados brutos). Abaixo, explicamos cada bloco:

---

### **3.1. Headcount (Contagem de Funcionários)**
**Objetivo:** Registrar o número de funcionários ativos em diferentes períodos.

| Tabela | Origem | Descrição | Exemplo de Uso |
|--------|--------|-----------|----------------|
| **bz_headcount_f** | Sistema corporativo (SAP) | Dados atuais de funcionários. | Quantos funcionários existem hoje? |
| **bz_headcount_hist_f** | Planilha Excel (`hc_historica_f.xlsx`) | Dados históricos (2014 a 2018). | Como o número de funcionários mudou ao longo dos anos? |
| **bz_headcount_latest_f** | Sistema corporativo (SAP) | Informações mais recentes, incluindo salários. | Qual o salário médio por cargo? |

**Como funciona:**
1. O script **carrega** os dados da origem (SAP ou Excel).
2. **Armazena** uma cópia na pasta **Bronze** (para backup e auditoria).
3. **Descarta** a tabela temporária da memória (para liberar espaço).

---

### **3.2. Dados de Pessoas e Hierarquia**
**Objetivo:** Armazenar informações pessoais e organizacionais dos funcionários.

| Tabela | Origem | Descrição | Exemplo de Uso |
|--------|--------|-----------|----------------|
| **bz_pessoa_d** | Sistema corporativo (SAP) | Dados pessoais (nome, CPF, data de nascimento). | Qual a distribuição de idade dos funcionários? |
| **bz_hierarquia_d** | Sistema corporativo (SAP) | Estrutura organizacional (quem reporta a quem). | Qual o organograma da empresa? |

---

### **3.3. Dados de Cargos, Filiais e Salários (Planilhas Manuais)**
**Objetivo:** Complementar informações do SAP com dados gerenciados manualmente (como descrições de cargos e tabelas salariais).

| Tabela | Origem | Descrição | Exemplo de Uso |
|--------|--------|-----------|----------------|
| **bz_excel_funcao_d** | Excel (`funcoes_d.xlsx`) | Detalhes sobre cargos (CBO, formação requerida, salário-base). | Quais cargos exigem curso superior? |
| **bz_excel_filial_d** | Excel (`filial_d.xlsx`) | Lista de filiais (código e nome). | Em quais cidades a empresa tem unidades? |
| **bz_excel_salario_d** | Excel (`tabela_salarial_d.xlsx`) | Faixas salariais por cargo. | Qual a faixa salarial para um analista júnior? |

**Exemplo de dados carregados (bz_excel_funcao_d):**
| Cargo | CBO 2002 | Descrição CBO | Formação |
|-------|----------|----------------|----------|
| Analista de TI | 3171-10 | Analista de sistemas | Superior em TI |

---

### **3.4. Orçamentos e Projeções**
**Objetivo:** Armazenar dados de planejamento financeiro e projeções de headcount.

| Tabela | Origem | Descrição | Exemplo de Uso |
|--------|--------|-----------|----------------|
| **bz_excel_hc_orcamento_historico_f** | Excel (`hc_orcamento_historico.xlsx`) | Orçamento previsto vs. realizado de funcionários. | A empresa está dentro do planejado de contratações? |
| **bz_excel_estrutura_cc_d** | Excel (`centro_de_custo_d.xlsx`) | Estrutura de centros de custo (áreas da empresa). | Quais áreas têm mais funcionários? |

---

### **3.5. Movimentações e Posições**
**Objetivo:** Registrar mudanças na força de trabalho (admissões, demissões, transferências).

| Tabela | Origem | Descrição | Exemplo de Uso |
|--------|--------|-----------|----------------|
| **bz_movimentos_f** | Sistema corporativo (SAP) | Histórico de movimentações (contratações, demissões). | Qual a taxa de turnover (rotatividade) anual? |
| **bz_posicoes_f** | Sistema corporativo (SAP) | Posições ativas na empresa. | Quantas vagas estão abertas por área? |
| **bz_headcount_offshore_f** | Sistema corporativo (SAP) | Funcionários em unidades no exterior. | Quantos funcionários trabalham fora do Brasil? |
| **bz_excel_posicoes_f** | Excel (`posicoes_abertas.xlsx`) | Posições em aberto (vagas a serem preenchidas). | Quais cargos estão com vagas disponíveis? |

---

### **3.6. Dados Externos (Centros de Custo)**
**Objetivo:** Integrar informações de outros departamentos (como Finanças) para cruzamento com dados de RH.

| Tabela | Origem | Descrição | Exemplo de Uso |
|--------|--------|-----------|----------------|
| **bz_externo_centro_custo_d** | Arquivo QVD externo | Centros de custo de outras áreas. | Qual o custo de pessoal por departamento? |

---

## **4. Fluxo de Execução do Script**
1. **Configurações iniciais:**
   - Define formatos de data, moeda e separadores.
   - Indica pastas de origem e destino.

2. **Carregamento dos dados:**
   - Para cada tabela, o script:
     - **Lê** os dados da origem (SAP, Excel ou QVD).
     - **Armazena** uma cópia na camada **Bronze**.
     - **Remove** a tabela temporária da memória.

3. **Fim do processo:**
   - O comando `EXIT Script;` encerra a execução.

---

## **5. Exemplo Prático: Como os Dados São Usados**
Imagine que a empresa queira saber:
**"Quantos funcionários do cargo 'Analista de TI' foram contratados em 2024?"**

1. O script carrega:
   - **bz_headcount_f** (funcionários ativos).
   - **bz_excel_funcao_d** (detalhes do cargo "Analista de TI").
   - **bz_movimentos_f** (histórico de contratações).

2. Um relatório no Qlik Sense poderia **cruzar essas informações** e mostrar:
   - Total de analistas de TI.
   - Quantos foram admitidos em 2024.
   - Comparação com outros cargos.

---

## **6. Resumo dos Arquivos Gerados**
Todos os dados carregados são salvos na pasta **Bronze** com o formato **QVD** (um tipo de arquivo otimizado para o Qlik). Exemplos:

| Arquivo Gerado | Descrição |
|----------------|-----------|
| `bz_headcount_f.QVD` | Funcionários ativos (dados do SAP). |
| `bz_excel_funcao_d.QVD` | Descrição de cargos (dados manuais). |
| `bz_movimentos_f.QVD` | Histórico de movimentações (admissões/demissões). |

---
## **7. Considerações Finais**
- Este script **não altera os dados originais**, apenas os **copia e organiza** para uso posterior.
- As informações na camada **Bronze** são **brutas** e serão tratadas em etapas seguintes (Silver e Gold).
- O processo é **automatizado**, ou seja, pode ser executado periodicamente para atualizar os dados.

---
**Fim da Documentação.**
