# Documentação Técnica

**Arquivo:** `gd_headcount.qvs`  
**Última atualização:** 15/08/2025 09:41:33

# **Documentação do Script QVS – Estrutura de Dados para Análise de Recursos Humanos**

---

## **1. Introdução**
Este documento explica um script utilizado para organizar e preparar dados relacionados a **Recursos Humanos (RH)** de uma empresa. O objetivo é transformar informações brutas em tabelas estruturadas, facilitando a análise de funcionários, hierarquias, desligamentos, orçamentos e outras métricas importantes para a gestão de pessoas.

O script segue uma abordagem chamada **"Medallion Architecture"**, que divide os dados em três camadas principais:
- **Bronze**: Dados brutos (não processados).
- **Silver**: Dados limpos e padronizados.
- **Gold**: Dados prontos para análise, organizados em **fatos** (informações quantitativas) e **dimensões** (informações descritivas).

---

## **2. Configurações Iniciais**
Antes de processar os dados, o script define padrões de formatação para garantir que datas, números e moedas sejam exibidos de maneira consistente.

### **2.1. Formatação de Números, Moedas e Datas**
| Configuração               | Descrição                                                                 | Exemplo               |
|----------------------------|---------------------------------------------------------------------------|-----------------------|
| **ThousandSep**            | Separador de milhares (ponto).                                            | `1.000`               |
| **DecimalSep**             | Separador decimal (vírgula).                                              | `3,14`                |
| **MoneyFormat**            | Formato de moeda (Real Brasileiro).                                       | `R$1.000,00`          |
| **DateFormat**             | Formato de data (dia.mês.ano).                                            | `31.12.2023`          |
| **MonthNames**             | Nomes abreviados dos meses.                                               | `jan`, `fev`, `mar`   |
| **FirstWeekDay**           | Primeiro dia da semana (6 = domingo).                                    |                       |
| **CollationLocale**        | Idioma para ordenação de textos (Português do Brasil).                    |                       |

### **2.2. Caminhos dos Arquivos (Pastas)**
O script define onde os dados serão salvos ou lidos, usando **variáveis** para facilitar a manutenção. Exemplo:
- `bronze_layer`: Pasta com dados brutos.
- `silver_layer`: Pasta com dados limpos.
- `gold_layer`: Pasta com dados prontos para análise.

---
## **3. Criação de Tabelas de Apoio**
Antes de processar os dados de funcionários, o script cria duas tabelas essenciais para análises temporais.

### **3.1. Tabela de Calendário (`gd_calendario_d`)**
**Objetivo**: Criar um calendário com todas as datas de **2014 até o final do ano atual**, incluindo informações como:
- Dia da semana.
- Mês e ano.
- Se é feriado ou final de semana.
- Se a data é passada (`Histórico`) ou futura (`Futuro`).

**Exemplo de campos gerados**:
| Campo               | Descrição                                                                 | Exemplo          |
|---------------------|---------------------------------------------------------------------------|------------------|
| `date_key`          | Data no formato `DD.MM.AAAA`.                                             | `01.01.2024`     |
| `ano_mes`           | Mês e ano (ex: "janeiro - 2024").                                        | `jan - 2024`     |
| `dia_semana_nome`   | Nome do dia da semana.                                                   | `seg`            |
| `final_semana`      | Indica se é sábado ou domingo (`Sim`/`Não`).                             | `Sim`            |
| `hoje`              | Indica se é a data atual (`Sim`/`Não`).                                   | `Não`            |

**Para que serve?**
- Permite analisar tendências ao longo do tempo (ex: contratações por mês).
- Filtra dados por períodos específicos (ex: "mostrar apenas dados de 2023").

---

### **3.2. Tabela de Tempo na Empresa (`gd_tempo_companhia_d`)**
**Objetivo**: Classificar o tempo que um funcionário trabalha na empresa em grupos, como:
- **Grupos gerenciais** (ex: "Ano 1-2", "Ano 3-5").
- **Grupos operacionais** (ex: "0-3 meses", "9-12 meses").
- **Indicador de novo funcionário** (`new_hire`).

**Exemplo de classificações**:
| Dias na empresa | Grupo Gerencial       | Grupo Operacional   | New Hire |
|-----------------|-----------------------|---------------------|----------|
| 90              | Ano 1                 | 3-6 meses           | TRUE     |
| 730             | Ano 2                 | Ano 2 - 12-18 meses | FALSE    |
| 5.475           | Ano 15-20             | Mais que 4 anos     | FALSE    |

**Para que serve?**
- Analisar rotatividade (`turnover`) por tempo de empresa.
- Identificar padrões de desligamento (ex: "funcionários com menos de 6 meses saem mais").

---
## **4. Carregamento dos Dados Brutos**
O script lê arquivos `.QVD` (formato do Qlik) da camada **Silver** e os prepara para transformação.

### **4.1. Tabelas Carregadas**
| Tabela                          | Descrição                                                                 |
|---------------------------------|---------------------------------------------------------------------------|
| `sv_headcount_f_raw`            | Dados de funcionários ativos (nome, cargo, salário, hierarquia, etc.).   |
| `sv_termination_f_raw`          | Dados de funcionários desligados (data de saída, motivo, etc.).           |
| `sv_excel_hc_orcamento_historico_raw` | Histórico de orçamento de pessoal.                  |
| `sv_posicoes_raw`               | Informações sobre posições/cargos disponíveis na empresa.                 |

**O que acontece aqui?**
- O script **adiciona chaves únicas** (`hierarquia_sk`, `funcao_sk`) para ligar as tabelas.
- Define a `date_key` (data de referência) e `tempo_empresa_key` (tempo na empresa).

---
## **5. Criação das Dimensões (Tabelas Descritivas)**
Dimensões são tabelas que **descrevem** os dados (ex: quem é o funcionário, qual seu cargo). Elas são usadas para filtrar e agrupar informações.

### **5.1. Dimensão de Funcionários (`gd_employee_d`)**
**Campos principais**:
- Nome, CPF, data de nascimento, gênero, endereço, e-mail.
- **`ultima_data`**: Data mais recente de atualização do registro.

**Exemplo**:
| pessoa | nome          | genero | ultima_data  |
|--------|---------------|--------|--------------|
| 1001   | Ana Silva     | F      | 15.05.2024   |

---

### **5.2. Dimensão de Hierarquia (`gd_hierarquia_d`)**
**Campos principais**:
- Níveis hierárquicos (ex: Diretor → Gerente → Supervisor).
- Código e nome do gestor direto.

**Exemplo**:
| hierarquia_sk | hierarquia_nome_n1 | hierarquia_nome_n2 | gestor_direto_nome |
|---------------|--------------------|--------------------|--------------------|
| ABC123        | Diretoria X        | Gerência Y         | Carlos Souza       |

---

### **5.3. Outras Dimensões Criadas**
| Dimensão               | Descrição                                                                 |
|------------------------|---------------------------------------------------------------------------|
| `gd_funcao_d`          | Cargos (ex: "Analista", "Coordenador").                                   |
| `gd_eldorado_entity_d` | Filiais e coligadas da empresa.                                          |
| `gd_secao_d`           | Seções/departamentos.                                                    |
| `gd_centro_de_custo_d` | Centros de custo (áreas de alocação de despesas).                         |
| `gd_idade_d`           | Faixas etárias e gerações (ex: "Geração Y", "Boomers").                  |
| `gd_contratacao_tipo_d`| Tipo de contratação (ex: "CLT", "Temporário").                           |

---
## **6. Criação das Tabelas de Fatos (Dados Quantitativos)**
Fatos são tabelas com **métricas numéricas** (ex: quantidade de funcionários, salários).

### **6.1. Tabela de Headcount (`gd_headcount_f`)**
**Objetivo**: Registrar o número de funcionários ativos por data, cargo, departamento, etc.

**Campos removidos**:
- Dados pessoais (CPF, RG, endereço) são excluídos para proteger a privacidade.
- Mantém apenas **chaves** (`pessoa`, `funcao_sk`) e métricas relevantes.

**Exemplo**:
| pessoa | date_key   | funcao_sk | centro_de_custo_sk | salario |
|--------|------------|-----------|--------------------|---------|
| 1001   | 01.01.2024 | CARG001   | CUSTO001           | 5.000   |

---

### **6.2. Tabela de Desligamentos (`gd_termination_f`)**
**Objetivo**: Registrar funcionários que saíram da empresa.

**Campos importantes**:
- `termination_date`: Data de desligamento.
- `tempo_empresa_key`: Tempo que o funcionário trabalhou.

---

### **6.3. Tabelas de Orçamento e Posições**
| Tabela                          | Descrição                                                                 |
|---------------------------------|---------------------------------------------------------------------------|
| `gd_excel_hc_orcamento_historico_f` | Histórico de orçamento planejado vs. real.                          |
| `gd_posicoes_f`                 | Posições/cargos disponíveis na empresa (vagas abertas ou ocupadas).      |

---
## **7. Salvamento e Limpeza**
Após processar os dados, o script:
1. **Salva** as tabelas na camada **Gold** (prontas para análise).
2. **Exclui** tabelas temporárias para liberar memória.

---
## **8. Resumo do Fluxo de Dados**
1. **Configurações**: Define formatos e caminhos.
2. **Tabelas de apoio**: Cria calendário e tempo na empresa.
3. **Carregamento**: Lê dados da camada **Silver**.
4. **Dimensões**: Organiza informações descritivas (funcionários, cargos, hierarquias).
5. **Fatos**: Prepara dados numéricos (headcount, desligamentos, orçamento).
6. **Salvamento**: Armazena tudo na camada **Gold**.
7. **Limpeza**: Remove tabelas temporárias.

---
## **9. Exemplo Prático: Como Esses Dados São Usados?**
### **Cenário 1: Análise de Rotatividade**
- **Pergunta**: "Quantos funcionários com menos de 1 ano saíram em 2023?"
- **Como responder**:
  1. Filtrar `gd_termination_f` por `ano = 2023`.
  2. Cruzar com `gd_tempo_companhia_d` para identificar `grupo_operacional = "0-12 meses"`.
  3. Contar os registros.

### **Cenário 2: Distribuição por Faixa Etária**
- **Pergunta**: "Qual a porcentagem de funcionários da Geração Y?"
- **Como responder**:
  1. Usar `gd_employee_d` para obter datas de nascimento.
  2. Cruzar com `gd_idade_d` para classificar em `geracao = "Y"`.
  3. Calcular a porcentagem sobre o total.

---
## **10. Glossário de Termos**
| Termo               | Significado                                                                 |
|---------------------|---------------------------------------------------------------------------|
| **Fato**            | Tabela com dados numéricos (ex: salários, quantidade de funcionários).    |
| **Dimensão**        | Tabela com dados descritivos (ex: nomes, cargos, departamentos).          |
| **Chave (SK)**      | Código único que liga tabelas (ex: `funcao_sk`).                         |
| **Headcount**       | Contagem de funcionários ativos.                                           |
| **QVD**            | Formato de arquivo do Qlik (semelhante a um Excel otimizado).              |
| **Hash128**         | Função que gera um código único para evitar duplicidades.                 |

---
## **11. Considerações Finais**
Este script é uma **base estruturada** para análises de RH, permitindo:
- **Relatórios personalizados** (ex: diversidade, rotatividade, custos).
- **Integração com ferramentas de visualização** (como Qlik Sense ou Power BI).
- **Tomada de decisão baseada em dados** (ex: identificar áreas com alta rotatividade).

**Importante**: Os dados são tratados para garantir **privacidade** (ex: CPFs não são armazenados nas tabelas finais).
