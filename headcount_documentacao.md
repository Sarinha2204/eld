# Documentação Técnica

**Arquivo:** `headcount.qvs`  
**Última atualização:** 15/08/2025 09:42:43

# **Documentação do Script QVS – Processamento de Dados de Recursos Humanos**
*Explicação detalhada e organizada para compreensão clara do funcionamento do script.*

---

## **1. Introdução**
Este script é responsável por **processar e transformar dados de Recursos Humanos (RH)**, organizando informações sobre funcionários, demissões, cargos, centros de custo e outras dimensões relevantes para análise. Seu objetivo é **preparar os dados em um formato estruturado**, facilitando relatórios e dashboards no Qlik Sense.

O script segue uma **arquitetura em camadas** (Bronze, Silver e Gold), onde:
- **Bronze**: Dados brutos (originais, sem tratamento).
- **Silver**: Dados limpos e enriquecidos (prontos para análise).
- **Gold**: Dados consolidados para visualização (não abordado neste script).

---

## **2. Configurações Iniciais**
Antes de processar os dados, o script define **formatações padrão** para garantir consistência na exibição de números, datas, moedas e textos. Exemplos:

| Configuração               | Descrição                                                                 | Exemplo de Saída       |
|----------------------------|---------------------------------------------------------------------------|------------------------|
| `ThousandSep='.'`          | Separador de milhar (ponto).                                              | `1.000`                |
| `DecimalSep=','`          | Separador decimal (vírgula).                                             | `3,14`                 |
| `MoneyFormat`              | Formato de moeda (Real brasileiro).                                      | `R$ 1.234,56`          |
| `DateFormat='DD.MM.YYYY'`  | Formato de data (dia/mês/ano).                                           | `15.05.2023`           |
| `CollationLocale='pt-BR'`  | Idioma para ordenação de textos (português do Brasil).                   | Ordena "ç" corretamente. |

---
### **2.1. Caminhos dos Arquivos (Variáveis)**
O script define **onde os dados estão armazenados** usando variáveis como:
- `bronze_layer`: Pasta com dados brutos (ex: `bz_headcount_f.QVD`).
- `silver_layer`: Pasta para salvar dados processados (ex: `sv_headcount_f.QVD`).
- `gold_layer`: Pasta para dados finais (não usada neste script).
- `manual_source`, `ti_layer`, `external_layer`: Pastas para outras fontes de dados.

> **Observação**: Os caminhos usam `lib://`, que é uma referência a uma **conexão de biblioteca** no Qlik (similar a um atalho para uma pasta de rede).

---

## **3. Carregamento dos Dados Brutos (Bronze)**
Nesta seção, o script **lê os arquivos brutos** (no formato `.QVD`, um tipo de arquivo otimizado do Qlik) e os armazena em tabelas temporárias. Exemplos de tabelas carregadas:

| Tabela                                      | Descrição                                                                 |
|---------------------------------------------|---------------------------------------------------------------------------|
| `bz_headcount_f`                            | Lista de funcionários ativos e seus dados (matrícula, cargo, salário, etc.). |
| `bz_headcount_hist_f`                       | Histórico de movimentações de funcionários (admissões, demissões).       |
| `bz_posicoes_f`                             | Posições (vagas) abertas na empresa.                                      |
| `bz_pessoa_d`                               | Dados pessoais dos funcionários (CPF, endereço, etc.).                   |
| `bz_hierarquia_d`                           | Hierarquia organizacional (quem reporta a quem).                         |
| `bz_excel_funcao_d`                         | Detalhes dos cargos (nome, código, carreira, etc.).                       |

> **Nota**: Algumas tabelas estão comentadas (ex: `bz_salario_f`), ou seja, **não são carregadas** neste script.

---

## **4. Tabelas de Mapeamento (Dicionários)**
São **tabelas de referência** que traduzem códigos em nomes legíveis. Exemplos:

### **4.1. `coligada_d`**
Mapeia códigos de empresas ("coligadas") para seus nomes:

| Código | Empresa                          |
|--------|----------------------------------|
| 1      | Eldorado                         |
| 2      | Florestal                        |
| 3      | OffShore                         |
| 30     | Cellulose Eldorado Austria GmbH  |

### **4.2. `CLASSIFICAÇÃO_MAP`**
Classifica o tipo de demissão (voluntária ou involuntária):

| Código/Tipo | Classificação   |
|-------------|------------------|
| 2, 8, N, T  | Involuntário     |
| 4, V        | Voluntário       |

### **4.3. `MAP_EVENTOS`**
Traduz códigos de eventos (ex: horas extras, férias) para categorias:

| Código | Tipo                     |
|--------|--------------------------|
| 2      | Salário Base (SB)        |
| 5      | Salário Família (SF)     |
| 255    | Faltas                   |
| 167    | Férias                   |
| 80     | PLR (Participação nos Lucros) |

---
## **5. Processamento dos Dados (Silver)**
Nesta etapa, os dados brutos são **limpos, enriquecidos e salvos** em novas tabelas na camada Silver.

### **5.1. Pré-Processamento de Centro de Custo (`centro_de_custo`)**
- **Filtra centros de custo inválidos** (ex: vazios ou com `#`).
- **Classifica diretorias** em grupos (ex: "Corporativo", "Industrial").
- **Salva o resultado** em `sv_centro_de_custo_d.QVD`.

**Exemplo de lógica**:
```qlik
If(
    Match(Diretoria, 'Financeiro', 'RH, Sustent e Com', 'Presidência'),
    'Corporativo',
    Diretoria
) as grupo_diretoria
```
> *Se a diretoria for "Financeiro", classifica como "Corporativo"; caso contrário, mantém o nome original.*

---

### **5.2. Pré-Processamento de Funções (`funcao`)**
- **Extrai o código da função** (ex: `00123` de um texto como `123 - Analista`).
- **Classifica cargos** como "Líder" ou "Não Líder".
- **Identifica funções operacionais** (ex: "Técnico", "Operacional").
- **Salva em** `sv_funcao_d.QVD`.

**Exemplo de extração de código**:
```qlik
RIGHT('00000' & KEEPCHAR([Cargo], '0123456789'), 5) as funcao_cod
```
> *Pega apenas os números do campo "Cargo" e completa com zeros à esquerda (ex: `123` vira `00123`).*

---

### **5.3. Pré-Processamento de Headcount (`headcount_temp_1`)**
Esta é a **tabela principal de funcionários**, que combina dados de:
- Funcionários ativos (`bz_headcount_f`).
- Histórico de movimentações (`bz_headcount_hist_f`).
- Funcionários offshore (contratados no exterior).

#### **Regras Aplicadas**:
1. **Funcionários admitidos e demitidos no mesmo mês**:
   - Identifica casos onde um funcionário foi contratado e demitido rapidamente.
   - Marca esses registros com `short_tenure = 1` (curta permanência).

2. **Classificação de status**:
   - `new_hire_flag`: `TRUE` se o funcionário tem menos de 1 ano na empresa.
   - `admitido_flag`: `TRUE` se foi admitido no mês atual.
   - `headcount_flag_new`: `TRUE` se está ativo e não é estagiário.

3. **Filtros aplicados**:
   - Exclui registros com:
     - Situação `Z` (admissões futuras) ou vazia.
     - Tipo de funcionário `U` ou `S` (outros/estagiários).
     - Cargos específicos (ex: "Conselheiro Adm").
     - Matrículas de testes (ex: `999999937`).

4. **Cálculos**:
   - `tempo_empresa_dias`: Dias desde a admissão.
   - `idade`: Calculada a partir da data de nascimento.

#### **Juntando Dados (Joins)**:
O script **enriquece a tabela** com informações de:
- **Centro de custo** (diretoria, área).
- **Hierarquia** (quem é o gestor direto).
- **Pessoa** (CPF, endereço, estado civil).
- **Função** (detalhes do cargo).
- **Range salarial** (faixas de salário por cargo).

---
### **5.4. Tabela Final de Headcount (`sv_headcount_f`)**
Após o processamento, a tabela é salva com **todos os campos necessários para análise**, como:
- `chapa`: Matrícula do funcionário.
- `nome`: Nome completo.
- `funcao_cod`/`funcao_nome`: Cargo.
- `data_admissao`: Data de entrada na empresa.
- `salario`: Valor do salário (formatado).
- `gestor_direto_nome`: Nome do chefe imediato.
- `idade_grupo`: Faixa etária ("Até 30 anos", "31 a 50 anos", etc.).
- `readimitido`: Se já foi demitido e recontratado (`Sim`/`Não`).

**Exemplo de cálculo de faixa salarial (`agrup_fs`)**:
```qlik
IF(NUM(salario / [100]) < 0.8, 'Menor 80%',
  IF(NUM(salario / [100]) < 0.9, 'Entre 80% e 90%',
    ...
  )
) as agrup_fs
```
> *Classifica o salário em faixas (ex: "Entre 90% e 100%" da média do cargo).*

---
### **5.5. Tabela de Demissões (`sv_termination_f`)**
Processa dados de **funcionários demitidos**, aplicando regras como:
- **Classificação da demissão** (`demissao_classificacao`):
  - `Voluntário`: Pedido pelo funcionário (ex: código `1`, `4`).
  - `Involuntário`: Decisão da empresa (ex: código `2`, `8`).
- **Turnover flag**: `TRUE` se a demissão é considerada "turnover" (exclui aposentadorias, transferências).
- **Tempo na empresa**: Calculado em dias (`tempo_empresa_dias`).

**Exemplo de lógica de turnover**:
```qlik
IF(
    NOT Match([Tipo Funcionário], 'C', 'S', 'T', 'U', 'Z')  // Exclui conselheiros, estagiários, etc.
    AND NOT Match([Tipo de Demissão], '5', 'A', 'D', 'E', 'F', 'I', 'J', 'P', 'R', 'S', 'U'),
    'TRUE',  // É turnover
    'FALSE'  // Não é turnover
) as turnover_flag
```

---
### **5.6. Outras Tabelas Processadas**
| Tabela                              | Descrição                                                                 |
|-------------------------------------|---------------------------------------------------------------------------|
| `sv_excel_hc_orcamento_historico_f` | Histórico de orçamento de headcount (quantidade planejada de funcionários). |
| `sv_posicoes_f`                     | Posições (vagas) abertas, com status ("Em Andamento", "Substituição").     |

---
## **6. Limpeza Final**
Ao final, o script **exclui as tabelas brutas** para liberar memória:
```qlik
Drop Table bz_headcount_f, bz_headcount_hist_f, bz_pessoa_d, ...;
```
E encerra a execução:
```qlik
Exit Script;
```

---
## **7. Fluxo Resumido do Script**
1. **Configurações**: Define formatações e caminhos dos arquivos.
2. **Carregamento Bronze**: Lê dados brutos (.QVD).
3. **Mapeamentos**: Cria dicionários para traduzir códigos.
4. **Pré-Processamento**:
   - Limpa e estrutura dados de centro de custo, funções e headcount.
   - Aplica regras de negócio (ex: classificação de demissões).
5. **Joins**: Combina tabelas para enriquecer informações.
6. **Tabelas Finais (Silver)**:
   - `sv_headcount_f`: Funcionários ativos e históricos.
   - `sv_termination_f`: Demissões.
   - `sv_posicoes_f`: Vagas abertas.
7. **Limpeza**: Remove tabelas temporárias e encerra.

---
## **8. Exemplos Práticos**
### **8.1. Como um Funcionário é Classificado como "Novo Contratado"?**
- **Regra**: Se o tempo na empresa for **menor que 1 ano** (`tempo_empresa_dias < 365`).
- **Campos gerados**:
  - `contratacao_tipo = "Novo Contratado"`
  - `new_hire_flag = "TRUE"`

### **8.2. Como Identificar um Gestor Direto?**
O script percorre a hierarquia do funcionário (níveis 1 a 6) e busca o **primeiro gestor válido**:
```qlik
IF(
    [hierarquia_cod_n6] <> [chapa] AND [hierarquia_cod_n6] <> '#',
    [hierarquia_nome_n6],  // Se o nível 6 é um gestor, usa seu nome.
    IF(
        [hierarquia_cod_n5] <> [chapa] AND [hierarquia_cod_n5] <> '#',
        [hierarquia_nome_n5],  // Senão, verifica o nível 5.
        ...
    )
) as gestor_direto_nome
```

### **8.3. Como um Salário é Comparado à Faixa do Cargo?**
- O script calcula a **posição do salário** (`posic_fs`) em relação à média do cargo:
  - `salario / 100`: Normaliza o valor (ex: `R$ 3.000,00` vira `30`).
  - Compara com faixas pré-definidas (80%, 90%, 100%, etc.).
- **Resultado**: Campos como `agrup_fs = "Entre 90% e 100%"`.

---
## **9. Glossário de Termos**
| Termo               | Significado                                                                 |
|---------------------|---------------------------------------------------------------------------|
| **Headcount**       | Contagem de funcionários (ativos, demitidos, etc.).                      |
| **Turnover**        | Rotatividade de funcionários (demissões não planejadas).                 |
| **Coligada**        | Empresa do mesmo grupo (ex: Eldorado, Florestal).                         |
| **GS**              | Grau Salarial (nível do cargo na tabela salarial).                       |
| **CBO**             | Classificação Brasileira de Ocupações (código padrão para cargos).      |
| **QVD**             | Formato de arquivo do Qlik (otimizado para carregamento rápido).        |
| **Join**            | Combinação de tabelas usando campos em comum (ex: matrícula do funcionário). |

---
## **10. Considerações Finais**
- **Objetivo do Script**: Preparar dados de RH para análise, garantindo **consistência, clareza e riqueza de informações**.
- **Flexibilidade**: As regras podem ser ajustadas (ex: adicionar novos filtros) sem alterar a estrutura principal.
- **Desempenho**: O uso de `.QVD` e joins otimizados torna o processamento **rápido mesmo com grandes volumes de dados**.

> **Importante**: Este script **não gera visualizações** (gráficos, tabelas). Seu papel é **preparar os dados** para que sejam usados em dashboards no Qlik Sense.
