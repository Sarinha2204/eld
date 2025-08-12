# Documentação Técnica

**Arquivo:** `headcount.qvs`  
**Última atualização:** 12/08/2025 08:54:18

## Documentação do Script QVS: `headcount.qvs`

**Data da última atualização:** 07/08/2025 (A hora varia nas diferentes versões da documentação fornecida)


**1. Resumo:**

O script QVS `headcount.qvs` importa dados de um arquivo CSV externo, contendo informações sobre funcionários, departamentos e cargos de uma organização.  Ele processa esses dados, realizando limpeza e transformações, e os carrega em três tabelas do aplicativo QlikView: "Funcionários", "Departamentos" e "Cargos".  O script utiliza variáveis para definir caminhos de arquivos, facilitando a configuração e manutenção.


**2. Principais Etapas:**

**2.1. Definição de Variáveis:**

*   A variável `$(vDataPath)` armazena o caminho do arquivo CSV de entrada contendo os dados brutos dos funcionários.
*   A variável `$(vOutputPath)` armazena um caminho de saída (a descrição fornecida não detalha seu uso no script).

**2.2. Importação e Carregamento de Dados:**

*   O script importa os dados do arquivo CSV especificado pela variável `$(vDataPath)`.
*   Durante a importação, são definidos os nomes e tipos de dados de cada coluna.

**2.3. Transformação e Limpeza de Dados:**

*   O script remove linhas em branco do conjunto de dados.
*   Realiza o tratamento de caracteres especiais presentes nos dados, visando garantir a integridade e consistência dos mesmos.
*   Converte dados de data para um formato consistente e padronizado.
*   Calcula e adiciona uma nova coluna, "Idade", baseada na data de nascimento dos funcionários.

**2.4. Criação e Carregamento de Tabelas:**

*   O script cria e carrega a tabela "Funcionários", contendo informações detalhadas de cada funcionário.
*   O script cria e carrega a tabela "Departamentos", listando os departamentos da organização.
*   O script cria e carrega a tabela "Cargos", listando os cargos ocupados pelos funcionários.

**2.5. Comentários e Finalização:**

*   O script inclui comentários para documentar as diferentes seções e etapas.
*   O script finaliza o processo de carregamento e transformação dos dados.


**Observação:**  Esta documentação é baseada nas informações fornecidas nos resumos do script. A ausência do código-fonte impede uma análise mais detalhada e precisa das funcionalidades e comandos específicos utilizados. Uma análise completa exigiria o acesso ao script original.

# Documentação Técnica

**Arquivo:** `headcount.qvs`  
**Última atualização:** 07/08/2025 14:39:54

## Documentação do Script QVS: `headcount.qvs`

**Data da última atualização:** 07/08/2025 14:34:01


**1. Resumo:**

O script QVS `headcount.qvs` importa dados de um arquivo CSV externo, contendo informações sobre funcionários de uma organização.  O script realiza o processamento desses dados, incluindo limpeza e transformações, e os carrega em três tabelas dentro do aplicativo QlikView: "Funcionários", "Departamentos" e "Cargos".


**2. Principais Etapas:**

**2.1 Definição de Variáveis:**

* O script define a variável `$(vDataPath)` para especificar o caminho do arquivo CSV de origem que contém os dados dos funcionários.
* O script define a variável `$(vOutputPath)`, embora a descrição fornecida não indique o seu uso explícito no script.

**2.2 Importação e Carregamento de Dados:**

* O script carrega os dados do arquivo CSV especificado pela variável `$(vDataPath)`.
* Durante o carregamento, são definidos os nomes e os tipos de dados para cada coluna do arquivo CSV.

**2.3 Transformação e Limpeza de Dados:**

* O script processa os dados carregados, removendo linhas em branco.
*  O script realiza o tratamento de caracteres especiais presentes nos dados.
*  O script converte dados de data para um formato consistente e padronizado.
*  O script calcula e adiciona uma nova coluna denominada "Idade", derivada da data de nascimento dos funcionários.

**2.4 Criação e Carregamento de Tabelas:**

* O script cria a tabela "Funcionários", contendo os dados detalhados de cada funcionário.
* O script cria a tabela "Departamentos", listando os departamentos da organização.
* O script cria a tabela "Cargos", listando os cargos ocupados pelos funcionários.
* As tabelas "Funcionários", "Departamentos" e "Cargos" são carregadas no aplicativo QlikView.

**2.5 Comentários e Finalização:**

* O script inclui comentários para documentar as diferentes seções e etapas do processo.
* O script finaliza o processo de carregamento e transformação dos dados.


**Observação:** Esta documentação se baseia exclusivamente nas informações fornecidas. A ausência do código-fonte impede uma análise mais detalhada e precisa.  Uma análise completa requer acesso ao script original.

# Documentação Técnica

**Arquivo:** `headcount.qvs`  
**Última atualização:** 07/08/2025 14:34:01

## Documentação Técnica - Script QVS: `headcount.qvs`

**Data da última atualização:** 07/08/2025 14:26:22

**1. Resumo:**

O script QVS `headcount.qvs` importa dados de um arquivo CSV contendo informações de funcionários, processa esses dados realizando limpeza e transformações, e finalmente carrega os dados estruturados em três tabelas QlikView: "Funcionários", "Departamentos" e "Cargos".

**2. Principais Etapas:**

**2.1 Definição de Variáveis e Caminhos de Arquivo:**

* O script define a variável `$(vDataPath)` para especificar o caminho do arquivo CSV de origem.
* Define a variável `$(vOutputPath)` para especificar o caminho de saída (embora não seja utilizada explicitamente no resumo fornecido do script).

**2.2 Carregamento do Arquivo CSV:**

* O script carrega os dados do arquivo CSV especificado em `$(vDataPath)`.
* Durante o carregamento, são definidos os nomes e tipos de dados de cada coluna do arquivo CSV.

**2.3 Transformação e Limpeza de Dados:**

* O script remove linhas em branco do conjunto de dados.
* Processa e trata caracteres especiais presentes nos dados.
* Converte datas para um formato consistente.
* Calcula e adiciona uma nova coluna chamada "Idade" baseada na data de nascimento dos funcionários.

**2.4 Criação de Tabelas:**

* O script cria a tabela "Funcionários" contendo informações detalhadas de cada funcionário.
* Cria a tabela "Departamentos", listando os departamentos da empresa.
* Cria a tabela "Cargos", listando os cargos ocupados pelos funcionários.

**2.5 Carregamento das Tabelas no QlikView:**

* As tabelas "Funcionários", "Departamentos" e "Cargos" são carregadas no aplicativo QlikView.


**2.6 Comentários e Finalização:**

* O script inclui comentários para documentar as diferentes seções e etapas.
* O script finaliza o processo de carregamento e transformação dos dados.


---

**Observação:** Esta documentação é baseada exclusivamente nas informações fornecidas no resumo do script.  A ausência do código-fonte do script `headcount.qvs` impede uma análise mais detalhada e precisa das suas funcionalidades e comandos específicos.  Uma análise completa exigiria o acesso ao script original.

# Documentação Técnica

**Arquivo:** `headcount.qvs`  
**Última atualização:** 07/08/2025 14:26:22

## Documentação do Script QVS: headcount.qvs

**Data e hora da última atualização:** 07/08/2025 10:04:08

**Resumo:**

O script `headcount.qvs` carrega dados de um arquivo CSV contendo informações sobre funcionários de uma empresa, realiza a limpeza e transformação desses dados, e então carrega as informações estruturadas em três tabelas no aplicativo QlikView: "Funcionários", "Departamentos" e "Cargos".

**Principais Etapas:**

1. **Definição de Variáveis e Caminhos de Arquivo:**
    * A variável `$(vDataPath)` especifica o caminho do arquivo CSV de entrada contendo os dados brutos dos funcionários.
    * A variável `$(vOutputPath)` especifica o caminho de saída para as tabelas processadas.

2. **Carregamento do Arquivo CSV:**
    * O script carrega o arquivo CSV especificado pela variável `$(vDataPath)`.
    * Define-se o nome e o tipo de dados de cada coluna do arquivo CSV durante o processo de carregamento.

3. **Transformação e Limpeza de Dados:**
    *  Linhas em branco são removidas do conjunto de dados.
    *  Caracteres especiais são removidos ou tratados.
    *  Datas são convertidas para um formato consistente.
    *  Uma nova coluna, "Idade", é calculada com base na data de nascimento dos funcionários.

4. **Criação de Tabelas:**
    * Uma tabela denominada "Funcionários" é criada, contendo informações detalhadas sobre cada funcionário.
    * Uma tabela denominada "Departamentos" é criada, listando os departamentos da empresa.
    * Uma tabela denominada "Cargos" é criada, listando os cargos ocupados pelos funcionários.

5. **Carregamento das Tabelas no QlikView:**
    * As tabelas "Funcionários", "Departamentos" e "Cargos" são carregadas no aplicativo QlikView para análise e visualização.

6. **Comentários e Finalização:**
    * O script inclui comentários para explicar as diferentes seções e etapas.
    * O script termina, concluindo o processo de carregamento e transformação dos dados.




# Documentação do Script QVS: headcount.qvs

**Data e hora da última atualização:** 07/08/2025 10:04:08

## Descrição do Script

O script "headcount.qvs" tem como objetivo principal carregar e transformar dados de um arquivo CSV que contém informações sobre o quadro de funcionários de uma empresa. Ele realiza a limpeza e a estruturação dos dados, criando tabelas que são posteriormente carregadas no aplicativo QlikView. O script é essencial para garantir que as informações estejam organizadas e prontas para análise, permitindo uma visualização clara e precisa dos dados dos funcionários.

## Principais Componentes e Etapas

### 1. Definição de Variáveis e Caminhos de Arquivo
- **Variável `$(vDataPath)`**: Define o caminho do arquivo CSV de entrada, onde estão armazenadas as informações dos funcionários.
- **Variável `$(vOutputPath)`**: Define o caminho de saída onde as tabelas processadas serão armazenadas.

### 2. Carregamento do Arquivo CSV
- O script carrega o arquivo CSV que contém os dados dos funcionários.
- As colunas do arquivo são definidas, especificando os tipos de dados correspondentes a cada uma.

### 3. Transformação e Limpeza dos Dados
- **Remoção de Linhas em Branco**: O script elimina quaisquer linhas que não contenham dados relevantes.
- **Tratamento de Caracteres Especiais**: Caracteres indesejados são removidos para garantir a integridade dos dados.
- **Conversão de Datas**: As datas são convertidas para o formato correto, assegurando que estejam em um padrão uniforme.
- **Criação da Coluna "Idade"**: Uma nova coluna é gerada com a idade dos funcionários, calculada com base na data de nascimento.

### 4. Criação de Tabelas
- **Tabela "Funcionários"**: Contém todas as informações relevantes sobre os funcionários, como nome, cargo, departamento, entre outros.
- **Tabela "Departamentos"**: Lista todos os departamentos da empresa, permitindo uma organização clara dos dados.
- **Tabela "Cargos"**: Inclui a lista de cargos ocupados pelos funcionários, facilitando a análise de funções dentro da empresa.

### 5. Carregamento das Tabelas no Aplicativo QlikView
- As tabelas "Funcionários", "Departamentos" e "Cargos" são carregadas no aplicativo QlikView, tornando os dados disponíveis para visualização e análise.

### 6. Comentários e Finalização
- O script inclui comentários que explicam o propósito de cada seção e as principais etapas do processo.
- A finalização do script garante que todas as operações sejam concluídas corretamente e que os dados estejam prontos para uso.

---

Esta documentação fornece uma visão geral clara e detalhada do funcionamento do script "headcount.qvs", facilitando a compreensão e a manutenção do código por outros desenvolvedores e analistas que possam trabalhar com ele no futuro.

Documentação do Script QVS: headcount.qvs

Data da última atualização: 07/08/2025 09:56:15

Resumo:
O script "headcount.qvs" é responsável por carregar e transformar dados de um arquivo CSV contendo informações sobre o quadro de funcionários de uma empresa. O script realiza a limpeza e a estruturação dos dados, criando tabelas e carregando-as no aplicativo QlikView.

Principais Etapas:

1. Definição de variáveis e caminhos de arquivo:
   - Definição da variável `$(vDataPath)` para o caminho do arquivo CSV de entrada.
   - Definição da variável `$(vOutputPath)` para o caminho de saída das tabelas.

2. Carregamento do arquivo CSV:
   - Carregamento do arquivo CSV contendo as informações sobre o quadro de funcionários.
   - Definição das colunas e seus respectivos tipos de dados.

3. Transformação e limpeza dos dados:
   - Remoção de linhas em branco e caracteres especiais.
   - Conversão de datas no formato correto.
   - Criação de uma nova coluna "Idade" com base na data de nascimento.

4. Criação de tabelas:
   - Criação da tabela "Funcionários" contendo as informações sobre os funcionários.
   - Criação da tabela "Departamentos" contendo a lista de departamentos da empresa.
   - Criação da tabela "Cargos" contendo a lista de cargos ocupados pelos funcionários.

5. Carregamento das tabelas no aplicativo QlikView:
   - Carregamento das tabelas "Funcionários", "Departamentos" e "Cargos" no aplicativo QlikView.

6. Comentários e finalização:
   - Comentários explicando o propósito do script e suas principais etapas.
   - Finalização do script.

Documentação do Script QVS: headcount.qvs

Data da última atualização: 07/08/2025 09:56:15

Resumo:
O script "headcount.qvs" é responsável por carregar e transformar dados de um arquivo CSV contendo informações sobre o quadro de funcionários de uma empresa. O script realiza a limpeza e a estruturação dos dados, criando tabelas e carregando-as no aplicativo QlikView.

Principais Etapas:

1. Definição de variáveis e caminhos de arquivo:
   - Definição da variável `$(vDataPath)` para o caminho do arquivo CSV de entrada.
   - Definição da variável `$(vOutputPath)` para o caminho de saída das tabelas.

2. Carregamento do arquivo CSV:
   - Carregamento do arquivo CSV contendo as informações sobre o quadro de funcionários.
   - Definição das colunas e seus respectivos tipos de dados.

3. Transformação e limpeza dos dados:
   - Remoção de linhas em branco e caracteres especiais.
   - Conversão de datas no formato correto.
   - Criação de uma nova coluna "Idade" com base na data de nascimento.

4. Criação de tabelas:
   - Criação da tabela "Funcionários" contendo as informações sobre os funcionários.
   - Criação da tabela "Departamentos" contendo a lista de departamentos da empresa.
   - Criação da tabela "Cargos" contendo a lista de cargos ocupados pelos funcionários.

5. Carregamento das tabelas no aplicativo QlikView:
   - Carregamento das tabelas "Funcionários", "Departamentos" e "Cargos" no aplicativo QlikView.

6. Comentários e finalização:
   - Comentários explicando o propósito do script e suas principais etapas.
   - Finalização do script.

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

//SET bronze_layer = '\\BRSPOWVQDEV01\QlikSharedFolder\CustomData\Eldorado Brasil\3. Recursos Humanos\People Analytics\01. HR Medallion\01. Bronze\';

//SET silver_layer = '\\BRSPOWVQDEV01\QlikSharedFolder\CustomData\Eldorado Brasil\3. Recursos Humanos\People Analytics\01. HR Medallion\02. Silver\';


SET bronze_layer = 'lib://Eldorado Data Folder - 3 Recursos Humanos - People Analytics/01. HR Medallion/01. Bronze/';
SET silver_layer = 'lib://Eldorado Data Folder - 3 Recursos Humanos - People Analytics/01. HR Medallion/02. Silver/';
SET gold_layer = 'lib://Eldorado Data Folder - 3 Recursos Humanos - People Analytics/01. HR Medallion/03. Gold/';
SET manual_source = 'lib://Eldorado Data Folder - 3 Recursos Humanos - People Analytics/02. Manual Source/';
SET ti_layer = 'lib://Staging Recursos Humanos/';
SET external_layer = 'lib://Eldorado Data Folder - 3 Recursos Humanos - People Analytics/04. Fontes Externas/';


///////////////////////////        LOAD RAW      //////////////////////////////////////////////


bz_headcount_f:
Load
*
FROM [$(bronze_layer)bz_headcount_f.QVD]
(qvd);


bz_headcount_hist_f:
Load
*
FROM [$(bronze_layer)bz_headcount_hist_f.QVD]
(qvd);



bz_headcount_latest_f:
Load
*
FROM [$(bronze_layer)bz_headcount_latest_f.QVD](qvd);
// bz_salario_f:
// Load
// *
// FROM [$(bronze_layer)bz_salario_f.QVD]
// (qvd);


// bz_eventos_f:
// Load
// *
// FROM [$(bronze_layer)bz_eventos_f.QVD]
// (qvd);

bz_posicoes_f:
Load
*
FROM [$(bronze_layer)bz_posicoes_f.QVD]
(qvd);

bz_excel_hc_orcamento_historico_f:
Load
*
FROM [$(bronze_layer)bz_excel_hc_orcamento_historico_f.QVD]
(qvd);

bz_headcount_offshore_f:
Load
*
FROM [$(bronze_layer)bz_headcount_offshore_f.QVD]
(qvd);


bz_excel_posicoes_f:
Load
*
FROM [$(bronze_layer)bz_excel_posicoes_f.QVD]
(qvd);



bz_excel_estrutura_cc_d:
Load
*
FROM [$(bronze_layer)bz_excel_estrutura_cc_d.QVD]
(qvd);



bz_pessoa_d:
Load
*
FROM [$(bronze_layer)bz_pessoa_d.QVD]
(qvd);



bz_hierarquia_d:
Load
*
FROM [$(bronze_layer)bz_hierarquia_d.QVD]
(qvd);


bz_excel_funcao_d:
Load
*
FROM [$(bronze_layer)bz_excel_funcao_d.QVD]
(qvd);


bz_excel_range_salario_d:
Load
*
FROM [$(bronze_layer)bz_excel_range_salario_d.QVD]
(qvd);

bz_excel_filial_d:
Load
*
FROM [$(bronze_layer)bz_excel_filial_d.QVD]
(qvd);

bz_externo_centro_custo_d:
Load
*
FROM [$(bronze_layer)bz_externo_centro_custo_d.QVD]
(qvd);



///////////////////////////        DIMENSION TEMP      //////////////////////////////////////////////



coligada_d:
MAPPING LOAD * Inline
[
CODCOLIGADA,   	COLIGADA,
1,				Eldorado,
2, 				Florestal,
3,				OffShore,
4,          	Rishis,
5,				EBlog,
30,             Cellulose Eldorado Austria GmbH
31, 			Eldorado USA, Inc.
32, 			Cellulose Eldorado Asia
];





// DIRETORIA_MAP:
// MAPPING LOAD * Inline
// [
// DIRETORIA,   					GRUPO DIRETORIA,
// 'Dir. Industrial', 				'Industrial',
// 'Dir. Florestal', 				'Florestal',
// 'TI', 							'Corporativo',
// 'Dir. Transportadora', 			'Transportadora',
// 'Dir. Comercial e Logística', 	'Comercial e Logística',
// 'Presidência', 					'Corporativo',
// 'Dir. RH, Sustent. e Comun.', 	'Corporativo',
// 'Dir. Financeira', 				'Corporativo',
// 'Dir. Jurídica', 				'Corporativo',
// '#N/D', 						'Corporativo'
// ];


CLASSIFICAÇÃO_MAP:
MAPPING LOAD * INLINE
[
Tipo de Demissão, Classificação Demissão
2,Involuntário
8,Involuntário
N,Involuntário
T,Involuntário
4,Voluntário
V,Voluntário
1,Involuntário   // Involuntário - JC
];


MAP_EVENTOS:
MAPPING LOAD * INLINE [
CODEVENTO, 	TIPO
2, 			SB
5,			SF
6,			SM
7,			AD Comp.
14,			Insuf. Saldo
21,			Insuf. Saldo
24, 		HE ESPORÁDICA
25, 		HE ESPORÁDICA
27, 		HE ESPORÁDICA
28, 		HE RECORRENTE
31, 		HE ESPORÁDICA
35, 		HE ESPORÁDICA
36, 		HE ESPORÁDICA
37, 		HE ESPORÁDICA
58, 		HE RECORRENTE
62,			ADICIONAL
65,			ADICIONAL
66,			ADICIONAL
68,			ADICIONAL
69,			ADICIONAL
72,			ADICIONAL
73,			ADICIONAL
77,			AUXÍLIO
80,			PLR
99,			AUXÍLIO
108,		DSR
110,		DSR
111,		DSR
121,		Dev Falta
167,		FÉRIAS
170,		FÉRIAS
211,		SB
213, 		FÉRIAS
214,		FÉRIAS
255,		FALTAS
256,		ATRASO
257,		DSR Faltas
271,		DESC. INTERODONTO
277,		DESC. SEGURO VIDA
364, 		FGTS SB
490,		HE RECORRENTE
514,		HE ESPORÁDICA
506,		HE ESPORÁDICA
695,		HE ESPORÁDICA
696,		HE ESPORÁDICA
698,		HE ESPORÁDICA
700,		HE RECORRENTE
755,		FALTAS
800,		HE RECORRENTE
8006, 		HE ESPORÁDICA
8007, 		HE ESPORÁDICA
8009, 		HE ESPORÁDICA
801,  		HE RECORRENTE
530,  		HE ESPORÁDICA
1025, 		FÉRIAS
1030, 		REEMBOLSO MENSALIDADE UNIMED
1031, 		REEMBOLSO COPART UNIMED
1033, 		MENSALIDADE DEPENDENTES UNIMED
1034, 		MENSALIDADE TITULAR UNIMED
];



Map_funcao:
MAPPING LOAD
	Trim( Capitalize(funcao_nome)),
    funcao_cod
    
    
FROM [$(silver_layer)sv_funcao_d.QVD]
(qvd);


///////////////////////////        PRE CENTRO DE CUSTO      //////////////////////////////////////////////



centro_de_custo:
Load
[Centro Custo] 																as centro_de_custo
,[Descrição]                                                                as centro_de_custo_nome
,[Diretoria]																as diretoria
,[Área]																		as area
,If(
    Match(Diretoria, 'Financeiro', 'RH, Sustent e Com', 'Presidência', 'Jurídico', 'TI'), 
        'Corporativo', 
         Diretoria
    ) as grupo_diretoria,
If(
  Match(Diretoria, 'Financeiro', 'RH, Sustent e Com' , 'Presidência', 'Jurídico', 'TI'), 
        'CORP',  
 If(Match(Diretoria, 'Industrial'),
        'IND',
 If(Match(Diretoria, 'Comercial'),
        'COM',
 If(Match(Diretoria, 'Logística'),
        'LOG',
 If(Match(Diretoria, 'Florestal'),
        'FLO',
 If(Match(Diretoria, 'Transportadora', 'Transportadora Madeira'),
        'TRP'))))))  as grupo_diretoria_micro

, [Centro de lucro]    													    as centro_lucro_cod
, [Descrição CL] 															as centro_lucro_nome

resident bz_externo_centro_custo_d

//remove linhas com centro de custo nulo ou igual a '#'
WHERE Len(Trim([Centro Custo])) > 0 AND [Centro Custo] <> '#';


STORE centro_de_custo INTO [$(silver_layer)sv_centro_de_custo_d.QVD]
(qvd);




///////////////////////////        PRE FUNCAO      //////////////////////////////////////////////



funcao:
Load Distinct
     RIGHT('00000' & KEEPCHAR([Cargo], '0123456789'), 5) 																as funcao_cod
    ,SubField([Cargo], ' - ', 2) 																						as funcao_nome
    ,IF([Carreira] = '1-Gestão' OR [Grupo Relatório] = '5 - Especialista', 'Líder', 'Não Líder')						as lider_flag
    ,IF(Match(SubField(Capitalize([Grupo de Cargo 2]), ' - ', 2), 'Operacional','Técnico')
    , 'Operacional', 'Não Operacional')																					as operacional_flag
    ,[Carreira]												                                                			as carreira
    ,SubField(Capitalize([Grupo de Cargo]), ' - ', 2)																	as grupo_cargo
    ,SubField(Capitalize([Grupo de Cargo 2]), ' - ', 2) 																as grupo_cargo_micro
    ,[Grupo Relatório]																									as grupo_relatorio
    ,GS																										    		as gs
    ,UPPER("Tabela Salarial")																							as cargo_salarial_tipo    
    ,[CBO 
2002]																													as cbo_2002
    ,[Descrição CBO]																						    		as cbo_descricao

resident bz_excel_funcao_d;

STORE funcao INTO [$(silver_layer)sv_funcao_d.QVD]
(qvd);



///////////////////////////        PRE HEADCOUNT      //////////////////////////////////////////////




// Passo 1: Carregar funcionários admitidos que foram demitidos antes do fim do mês de admissão


bz_admitidos_demitidos_temp:

Load
*,
Date(MonthEnd(Date#([Data Admissão], 'DD.MM.YYYY'))) as [Dia do calendário]

Resident bz_headcount_latest_f

WHERE 
// regra de admitido e contratado no mesmo mes
Date(Date#([Data Demissão], 'DD.MM.YYYY')) < Date(MonthEnd(Date#([Data Admissão], 'DD.MM.YYYY')))
// remove demissões de transferência
and [Tipo de Demissão] <> 5


;
    
Drop Field Situação, [Situação TEXT] from bz_admitidos_demitidos_temp;
    
// Passo 2: Verificar quais desses funcionários ainda estão na base de headcount

Left Join (bz_admitidos_demitidos_temp)

Load
    Funcionário,
    '1' as [Existe na Headcount]

Resident bz_headcount_f;


// Passo 3: Filtrar apenas os que NÃO estão na headcount (para adicionar depois)


bz_headcount_and_short_tenure_and_offshore_f:

NoConcatenate

Load 
    * 
    ,'X'			 as Situação               // --------------------IMPORTANTE----------------------- TODOS OS ADMITIDOS E DESLIGADOS NO MESMO MES SAO CLASSIFICADOS FORÇADOS COM ESSE STATUS POIS DO CONTRARIO ENTRARIO COMO DESLIGADO NORMAL. ISSO NAO AFETA EM NADA O APARECIMENTO DELE COMO DESLIGADO NA TERMINATION.
    ,'C/Dem no mês'	 as [Situação TEXT]
    ,1 				 as short_tenure 
Resident bz_admitidos_demitidos_temp
WHERE IsNull([Existe na Headcount]);

Drop Table bz_admitidos_demitidos_temp;

Concatenate


Load
'1/'&MID([Centro de custo], 6)                                                                                    as [Centro de Custo]
,[Chapa] 																										  as [Funcionário]
//,AutoNumberHash128([Função])+90000																			  as [Funções]
// ,RIGHT('00000' & [Código Função], 5) 																		  as [Funções]
,ApplyMap('Map_funcao', Trim(capitalize([Função])))											                      as [Funções]
,Date#([Data Admissão] , 'DD.MM.YYYY')																              as [Data Admissão]
,capitalize([Função]) 																							  as [Funções TEXT]
,Left(Capitalize(Genero),1) 																					  as [Sexo]
,Capitalize([Nome])																								  as [Funcionário TEXT]
,LEFT([Situação],1)																								  as [Situação]
,Mid([Situação],5)																								  as [Situação TEXT]
,LEFT([Tipo Funcionário],1)																						  as [Tipo Funcionário]
,Mid([Tipo Funcionário],5)																						  as [Tipo Funcionário TEXT]
,Date#([Dia do calendário], 'DD.MM.YYYY')                                                                         as [Dia do calendário]
,IF(Match(Left(Mid([Centro de custo], 6), 1), '4', '5', '6'), 
    Pick(Match(Left(Mid([Centro de custo], 6), 1), '4', '5', '6'), 30, 31, 32), 
    0
) 																												  as [Coligadas]
,1  																											  as [Código Filial]
,1																												  as offshore

Resident bz_headcount_offshore_f

where [Data Demissão] = '#';

Drop Table bz_headcount_offshore_f;

Concatenate

Load
*
,1																												  as hc_hist

Resident bz_headcount_hist_f;


concatenate

// Passo 4: Concatenar com a base completa de headcount
Load * 
Resident bz_headcount_f;
// Carrega todos registros






///////////////////////////        SV HEADCOUNT      //////////////////////////////////////////////






headcount_temp_1:

Load
    Date#([Dia do calendário], 'DD.MM.YYYY') 																			as load_date  
    ,[Funcionário] 																										as chapa
    ,[Funcionário TEXT] 																								as nome
    ,RIGHT('00000' & [Funções], 5) 																						as funcao_cod
    ,[Funções TEXT] 																									as funcao_nome
    ,Date#([Data Admissão], 'DD.MM.YYYY') 																			    as data_admissao
    ,(Date#([Dia do calendário], 'DD.MM.YYYY') - Date#([Data Admissão], 'DD.MM.YYYY')) 									as tempo_empresa_dias
    


 // a regra de new hire e contratação tipo é a mesma, diferencia true or false no resultado para que seja montada a dimensao na proxima camada   
    

    ,IF(Num( (Date#([Dia do calendário], 'DD.MM.YYYY') - Date#([Data Admissão], 'DD.MM.YYYY')) / 365.25, '#,##') 
    < 1,
    'Novo Contratado', 'Não Novo Contratado')	                                                                        as contratacao_tipo

    ,IF(Num( (Date#([Dia do calendário], 'DD.MM.YYYY') - Date#([Data Admissão], 'DD.MM.YYYY')) / 365.25, '#,##') 
    < 1,
    'TRUE', 'FALSE')                        	                                                                        as new_hire_flag


// a regra de admitido é para que seja destacado os funcionarios que foram admitidos no mes


    ,IF( Date(MonthEnd(Date#([Data Admissão], 'DD.MM.YYYY'))) = Date(MonthEnd(Date#([Dia do calendário], 'DD.MM.YYYY'))),
    'TRUE', 'FALSE') 																									as admitido_flag


// a regra de admitidos até 3 meses


    ,IF(Num( (Date#([Dia do calendário], 'DD.MM.YYYY') - Date#([Data Admissão], 'DD.MM.YYYY')) / 365.25, '#,##')  <= 0.25,
    'TRUE',
    'FALSE'
) 																														as admitido_flag_3meses
                                                                                                                       

#_dias_atestado
 
Sum(
  aggr(
    sum({<tipo_evento = {'Atestado'}>} [gd_eventos_f.hora_total]) * 30
    /
    sum({<tipo_evento = {'Jornada'}>} distinct [gd_eventos_f.hora_total]),
     gd_eventos_f.chapa, (mes_nome)
  )
)

//   ,IF(
  
//   short_tenure = 1, 'FALSE',
//   IF(

//     Match(Situação, 'A', 'E', 'F', 'N', 'O','Q', 'R', 'T', 'U', 'V', 'W','Y' )  
// // A	Ativo
// // E	Licença Mater.
// // F	Férias
// // N	Mandato Sindical Ônus do Empregador
// // O	Doença Ocupacional
// // Q	Prisão / Cárcere
// // R	Licença Remun.
// // T	Af Ac. Trabalho
// // U	Outros
// // V	Aviso Prévio
// // W	Licença Mater. Compl. 180 dias
// // Y	Licença Patemidade

//     AND Match([Tipo Funcionário], 'B', 'D', 'E', 'F', 'I', 'M', 'N', 'O', 'P', 'R', 'V', 'X')
// // B	Temporário com redução de encargos
// // D	Diretor
// // E	Estatutário
// // F	Temporário/Comissionista
// // I	Cedido
// // M	Misto
// // N	Normal
// // O	Comissionista
// // P	Af.Previdência ---------Temporário REMOVIDO DO TRUE A PEDIDO DO MURILO POIS NAO TEMOS CONTROLE DE ATESTADO PARA DEFINIR CURTO E LONGO PRAZO
// // R	Rural
// // V	Contrato Verde/Amarelo
// // X	Expatriado

//             ,            
//     		'TRUE',
//     		'FALSE'
//       )	)																    											as headcount_flag_new
      
 , if(
    Len(Trim(Situação)) > 0 and
    WildMatch([Funções TEXT], '*Estagiário*') = 0 and
    Match([Tipo Funcionário],'N') and
    Match(Situação, 'A', 'E', 'F', 'V'),
    
    'TRUE',
    'FALSE'
) as headcount_flag_new // regra HR Analytics

      
      
      
      
     ,[Situação]							 																			as situacao_cod
     ,[Situação TEXT]																									as situacao_nome
//      ,IF(MATCH([Situação], 'A','E','F','V'), 'Ativo', 'Afastado')		    											as headcount_status
     ,'REVISAR!'                                                                                                        as dias_afastados
     ,[Tipo Funcionário] 																								as tipo_funcionario_cod														
     ,[Tipo Funcionário TEXT]                                                                                           as tipo_funcionario_nome
     ,MID([Centro de Custo], 3)                                                                                         as centro_de_custo
     ,[Seção]                                                                                                           as secao_cod
     ,[Coligadas]                                                                                                       as coligada_cod
     ,IF(MATCH([Coligadas], ''),NULL(), APPLYMAP('coligada_d',[Coligadas])) 			                                as coligada_nome
     ,[Código Filial]                                                                                                   as filial_cod
     ,REPLACE([Salário], '.', ',')																					    as salario
     ,FLOOR( [Jornada Mensal] / 1000 ) / 60	 																			as jornada_mensal
     ,[Horários: Escala TEXT]																							as escala
     ,[Data de Nascimento]                                                                                              as nascimento_data
     ,Floor((Date#([Dia do calendário], 'DD.MM.YYYY') - Date#([Data de Nascimento], 'DD.MM.YYYY')) / 365.25) 			as idade
     ,IF(
            Floor(( Date(Date#("Dia do calendário", 'DD.MM.YYYY'), 'DD.MM.YYYY') 
            	       - Date#("Data de Nascimento", 'DD.MM.YYYY') ) / 365.25) <= 30,  			'Até 30 anos',
            IF(
                Floor(( Date(Date#("Dia do calendário", 'DD.MM.YYYY'), 'DD.MM.YYYY') 
                		   - Date#("Data de Nascimento", 'DD.MM.YYYY') ) / 365.25) > 50,    	'Acima de 50 anos',
                																				
                                                                                                'De 31 a 50 anos')
         )																											   as idade_grupo
      ,IF([Sexo] = 'M', 'Masculino',
	   IF([Sexo] = 'F', 'Feminino',
					    'Não informado')) 																			   as genero

      ,[Grau de Instrução TEXT]                                                                                        as grau_instrucao
      ,[Cor e Raça]  																								   as raca_cod
      ,[Cor e Raça TEXT]  																							   as raca_nome 	//verificar pois nao está vindo preenchido
      ,[Cota PCD]																									   as cota_pcd  
      ,offshore
      ,hc_hist
    
Resident bz_headcount_and_short_tenure_and_offshore_f

WHERE
1=1
and
 Date# ([Data Admissão] , 'DD.MM.YYYY') <=  Date# (Today(), 'DD.MM.YYYY')  // Inclusão em acordo com o time de folha pois o cadastro do funcionário é feito antes de o trabalho efetivamente começar.

   	and NOT Match([Situação], 'Z', '') 
    and MID([Centro de Custo], 3) > 99 
    and NOT Match([Tipo Funcionário], 'U', 'S') 
    and NOT Match([Funções TEXT], 
        'Conselheiro Adm', 
        'Conselheiro Fiscal', 
        '703', 
        '704', 
        '706'
    )
    and NOT Match([Funcionário], 
        '999907338', '999007075', '999999937', '999997747', '999997704',
        '999999078', '50003102', '50003331', '50006331', '50006095',
        '50005321', '50006666', '50003263', '50002600', '990007078',
        '990007075', '4268', '50007122', '50007171', '50007177',
        '50006978', '50007427', '50007435', '990008274', '999908188',
        '990007079', '888807074', '999997075', '990007132', '990007362',
        '990007320', '999997321', '950007284', '888887267', '990007465',
        '888807465', '990007495', '999997493', '888887554', '40000009',
        '999907551', '990007508', '4269', '999907759', '990007810',
        '999008084', '999908130', '990008219', '990008497', '999007508',
        '999007079', '990008293', '990008234'
    )
    
// da bypass em contratados e admitidos do mesmo mês
// or  short_tenure = 1
// da bypass em funcionários de offshore
or  offshore=1
or  hc_hist=1


;




													//join com tabela de hierarquia de centro de custo


LEFT JOIN (headcount_temp_1)
LOAD Distinct
//     [Centro Custo]  																                                    as centro_de_custo
// //     ,IF(MATCH([Dir.], 'Dir. Planejamento Estratégico'), NULL(), [Dir.]) 												as diretoria
//     ,[Dir.]																												as diretoria

//     ,IF([Área] = '-', NULL(), [Área]) 																					as area
// //     ,IF(
// //     	MATCH(IF(MATCH([Dir.], 'Dir. Planejamento Estratégico'), NULL()
// //         , [Dir.]), '')
// //         ,NULL()
// //         , APPLYMAP('DIRETORIA_MAP',IF(MATCH([Dir.], 'Dir. Planejamento Estratégico')
// //         , NULL(), [Dir.])))																								as grupo_diretoria   
//     ,[Grupo Diretoria]																									as grupo_diretoria
*
Resident centro_de_custo;











											// headcount latest por chapa. Adiciona somente detalhes que a core nao possui
                                            
                                            
                                            
                                            
LEFT JOIN (headcount_temp_1)
LOAD 
    [Pessoas] 																											as pessoa 
   ,[Funcionário] 																			                           	as chapa 
Resident bz_headcount_latest_f;     
    





												// adiciona dados de pessoa
                                        
                                        
                                        
                                        

LEFT JOIN (headcount_temp_1)
LOAD Distinct
     [Pessoas]                                                                                                         as pessoa
    ,[CPF RM]                                                                                                          as cpf
    ,[Carteira de Identidade]                                                                                          as rg
    ,[Carteira de Motorista]                     																	   as cnh_cod
    ,[Tipo da Carteira de Habilitação]                                                                                 as cnh_tipo
    ,[Data Vencimento da CNH]                                                                                          as cnh_vencimento
    ,[Estado]																									       as estado
    ,[Estado Civil]  																								   as estado_civil_cod
    ,[Estado Civil TEXT]																							   as estado_civil_nome
    ,[Nacionalidade]  																								   as nacionalidade                                                                                                                                                                
    ,[Naturalidade] 																								   as naturalidade                                                                                                         
    ,[Rua]                                            																   as rua
    ,[Número]																										   as numero
    ,[Complemento]                                                                                                     as complemento
    ,[Bairro]																										   as bairro
    ,[Cidade]                                                                                                          as cidade
    ,[Pais] 																										   as pais
    ,[CEP]																											   as cep
    ,[Telefone 1]                                                                                                      as telefone
        
Resident bz_pessoa_d;




													// adiciona dados de hierarquia




LEFT JOIN (headcount_temp_1)

LOAD Distinct
	Funcionário																											 as chapa
    ,IF(TRIM("Endereço Internet Mail")= '', 'Nenhum Registro Encontrado', "Endereço Internet Mail") 				     as email												
    
    // Remove o texto '1/' dos campos caso esteja presente
    ,[Hierarquia Nível 1]                                                                                                as [hierarquia_cod_n1]
    ,IF(LEFT([Hierarquia Nível 1 TEXT], 2) = '1/', MID([Hierarquia Nível 1 TEXT], 3), [Hierarquia Nível 1 TEXT])		 as [hierarquia_nome_n1]
    
    ,[Hierarquia Nível 2]                                                                                                as [hierarquia_cod_n2]
    ,IF(LEFT([Hierarquia Nível 2 TEXT], 2) = '1/', MID([Hierarquia Nível 2 TEXT], 3), [Hierarquia Nível 2 TEXT]) 		 as [hierarquia_nome_n2]
    
    ,[Hierarquia Nível 3]                                                                                                as [hierarquia_cod_n3]
    ,IF(LEFT([Hierarquia Nível 3 TEXT], 2) = '1/', MID([Hierarquia Nível 3 TEXT], 3), [Hierarquia Nível 3 TEXT]) 		 as [hierarquia_nome_n3]
    
    ,[Hierarquia Nível 4]                                                                                                as [hierarquia_cod_n4]
    ,IF(LEFT([Hierarquia Nível 4 TEXT], 2) = '1/', MID([Hierarquia Nível 4 TEXT], 3), [Hierarquia Nível 4 TEXT]) 		 as [hierarquia_nome_n4]
    
    ,[Hierarquia Nível 5]                                                                                                as [hierarquia_cod_n5]
    ,IF(LEFT([Hierarquia Nível 5 TEXT], 2) = '1/', MID([Hierarquia Nível 5 TEXT], 3), [Hierarquia Nível 5 TEXT]) 		 as [hierarquia_nome_n5]
    
    ,[Hierarquia Nível 6]                                                                                                as [hierarquia_cod_n6]
    ,IF(LEFT([Hierarquia Nível 6 TEXT], 2) = '1/', MID([Hierarquia Nível 6 TEXT], 3), [Hierarquia Nível 6 TEXT]) 		 as [hierarquia_nome_n6]
Resident bz_hierarquia_d;







											// regra de rehired com base da headcount latest 
                                            


                                            
                                            

LEFT JOIN (headcount_temp_1)
LOAD 
    [Pessoas]                                                             												as pessoa
    ,if(count([Data Admissão]) > 1, count([Data Admissão]) - 1, 0) 														as qtd_readimissoes
Resident bz_headcount_latest_f

WHERE 1=1 
AND NOT Match([Situação], '0', 'Z', '9')     // Exclui '0' mudanças de matrícula, 'Z' admissões futuras e '9' matrículas apagadas
AND NOT Match([Tipo Funcionário], 'Z', 'T')  // Exclui 'Z' aprendizes e 'T' estagiários
AND NOT Match([Tipo de Admissão], 'T')       // Exclui transferências sem ônus
GROUP BY Pessoas;







											// cria tabela para abter a seção nome que so existe na latest
                                            // como a seção text vem de uma tabela onde so existe o dado mais recente, a seção pode ser inexistente se nenhum funcionário estiver associado a ela.
                                            
                                         
                                         
                                         


LEFT JOIN (headcount_temp_1)
LOAD Distinct
    [Seção] 																											as secao_cod,
    [Seção TEXT] 																										as secao_nome
Resident bz_headcount_latest_f

WHERE NOT  IsNull( [Seção TEXT] );





											// cria tabela para obter o sindicato
                                    		// esta tabela traz somente o dado o dado mais recente ( nao faz sentido ser nessa arquitetura )






LEFT JOIN (headcount_temp_1)
LOAD Distinct
     [Funcionário]                                                                                                      as chapa
    ,[Sindicato] 																										as sindicato
    ,[Sindicato TEXT] 																									as sindicato_nome
Resident bz_headcount_latest_f

WHERE NOT  IsNull( [Sindicato TEXT] );





											// cria tabela para obter o pis pasep e quantidade de dependentes
                                    		// esta tabela traz somente o dado o dado mais recente ( nao faz sentido ser nessa arquitetura )






LEFT JOIN (headcount_temp_1)
LOAD Distinct
	 [Funcionário] 											                                                           as chapa
    ,[Número PIS/PASE]																								   as pispasep
    ,[Número de Dependentes no IRRF]+[N. Depentendetes Salário Familia]												   as dependentes
        
Resident bz_headcount_latest_f

WHERE [Situação] <> '9' //matrículas apagadas da base do RM
;




	

											// cria tabela para obter funcao
                                            
                                            		
                                                    
                                    


LEFT JOIN (headcount_temp_1)
LOAD Distinct
	
     RIGHT('00000' & KEEPCHAR([Cargo], '0123456789'), 5) 																as funcao_cod
//     ,SubField([Cargo], ' - ', 2) 																						as funcao_nome
    ,IF([Carreira] = '1-Gestão' OR [Grupo Relatório] = '5 - Especialista', 'Líder', 'Não Líder')						as lider_flag
    ,IF(Match(SubField(Capitalize([Grupo de Cargo 2]), ' - ', 2), 'Operacional','Técnico')
    , 'Operacional', 'Não Operacional')																					as operacional_flag
    ,[Carreira]												                                                			as carreira
    ,SubField(Capitalize([Grupo de Cargo]), ' - ', 2)																	as grupo_cargo
    ,SubField(Capitalize([Grupo de Cargo 2]), ' - ', 2) 																as grupo_cargo_micro
    ,[Grupo Relatório]																									as grupo_relatorio
    ,GS																										    		as gs
    ,UPPER("Tabela Salarial")																							as cargo_salarial_tipo    
    ,[CBO 
2002]																													as cbo_2002
    ,[Descrição CBO]																						    		as cbo_descricao

Resident bz_excel_funcao_d;

  											



											// cria a headcount temp 2 para adicionar regras de negocio que tem dependencia de mais de uma tabela





headcount_temp_2:

Load

*

,Alt(qtd_readimissoes, 0)      																							           as qtd_readimissoes_new
,Alt(pessoa,chapa) 																												   as pessoa_new
,AutoNumberHash128(UPPER(
    	IF(
        	WILDMATCH( Num([coligada_cod]) & Num([filial_cod]) & Upper([cargo_salarial_tipo]) & num([gs])
            				, '*ALL*')
                           	, [cargo_salarial_tipo] & Num([gs])
                            , Num([coligada_cod]) & Num([filial_cod]) & Upper([cargo_salarial_tipo]) & Num([gs]))) )               as range_salario_key


RESIDENT headcount_temp_1;

Drop Field qtd_readimissoes, pessoa;

Drop Table headcount_temp_1;





												// cria tabela para obter range de salario
                                                    
                                                    
                                                    

LEFT JOIN (headcount_temp_2)
LOAD
	
	 AutoNumberHash128( Num([CÓD. FILIAL]) & Num([CÓD. EMPRESA]) & Upper([TIPO CARGO]) & Num([GS]) )                    as range_salario_key
    ,NUM([0.8], '#.##0,00')																								as 80
    ,NUM([0.9], '#.##0,00')																								as 90
    ,NUM([1], '#.##0,00')																								as 100
    ,NUM([1.1000000000000001], '#.##0,00')																				as 110
    ,NUM([1.2], '#.##0,00')																								as 120
Resident bz_excel_range_salario_d;




											// headcount KPI final


#_dias_atestado
 
Sum(
  aggr(
    sum({<tipo_evento = {'Atestado'}>} [gd_eventos_f.hora_total]) * 30
    /
    sum({<tipo_evento = {'Jornada'}>} distinct [gd_eventos_f.hora_total]),
     gd_eventos_f.chapa, (mes_nome)
  )
)
 

LEFT JOIN (headcount_temp_2)
LOAD Distinct
 coligada_cod
,filial_cod
,filial_nome
Resident bz_excel_filial_d;




sv_headcount_f:
LOAD 

*    

,NUM(salario/ [100], '#,##%')		           										       						        as posic_fs
,IF(NUM( salario / [100] ) < 0.8, 'Menor 80%',
  IF(NUM( salario / [100] ) < 0.9, 'Entre 80% e 90%',
    IF(NUM( salario / [100] ) < 1, 'Entre 90% e 100%',
      IF(NUM( salario / [100] ) < 1.1, 'Entre 100% e 110%',
        IF(NUM( salario / [100] ) <= 1.2, 'Entre 110% até 120%',
           'Acima 120%'
        )
      )
    )
  )
) 																														as agrup_fs
// ,'REMOVER' 																												as advertencias
// ,'REMOVER' 																												as advertencias_total
// ,'REMOVER' 																												as advertencias_motivo
// ,'REMOVER' 																												as advertencias_punicao
// ,'REMOVER' 																												as advertencias_tipo
// ,'REMOVER' 																												as advertencias_data
,if(qtd_readimissoes_new >= 1, 'Sim', 'Não')                                                    					    as readimitido  	
,qtd_readimissoes_new 																									as qtd_readimissoes
,pessoa_new 																											as pessoa

,IF(
        [hierarquia_cod_n6] <> [chapa] AND [hierarquia_cod_n6] <> '#',
        [hierarquia_nome_n6],
        IF(
            [hierarquia_cod_n5] <> [chapa] AND [hierarquia_cod_n5] <> '#',
            [hierarquia_nome_n5],
            IF(
                [hierarquia_cod_n4] <> [chapa] AND [hierarquia_cod_n4] <> '#',
                [hierarquia_nome_n4],
                IF(
                    [hierarquia_cod_n3] <> [chapa] AND [hierarquia_cod_n3] <> '#',
                    [hierarquia_nome_n3],
                    IF(
                        [hierarquia_cod_n2] <> [chapa] AND [hierarquia_cod_n2] <> '#',
                        [hierarquia_nome_n2],
                        IF(
                            [hierarquia_cod_n1] <> [chapa] AND [hierarquia_cod_n1] <> '#',
                            [hierarquia_nome_n1]
                        )
                    )
                )
            )
        )
    )  AS [gestor_direto_nome]
,IF(
        [hierarquia_cod_n6] <> [chapa] AND [hierarquia_cod_n6] <> '#',
        [hierarquia_cod_n6],
        IF(
            [hierarquia_cod_n5] <> [chapa] AND [hierarquia_cod_n5] <> '#',
            [hierarquia_cod_n5],
            IF(
                [hierarquia_cod_n4] <> [chapa] AND [hierarquia_cod_n4] <> '#',
                [hierarquia_cod_n4],
                IF(
                    [hierarquia_cod_n3] <> [chapa] AND [hierarquia_cod_n3] <> '#',
                    [hierarquia_cod_n3],
                    IF(
                        [hierarquia_cod_n2] <> [chapa] AND [hierarquia_cod_n2] <> '#',
                        [hierarquia_cod_n2],
                        IF(
                            [hierarquia_cod_n1] <> [chapa] AND [hierarquia_cod_n1] <> '#',
                            [hierarquia_cod_n1]
                        )
                    )
                )
            )
        )
    )  AS [gestor_direto_cod]
,IF(situacao_cod = 'A' and headcount_flag_new = 'TRUE' and Num( (Date#([load_date], 'DD.MM.YYYY') - Date#([data_admissao], 'DD.MM.YYYY')) , '#,##') > 1, 'TRUE', 'FALSE') 	as disponivel_flag  
,If(headcount_flag_new = 'TRUE','Ativo','Inativo')																															as headcount_status
// ,if(previous(pessoa_new) = pessoa_new
//     and Previous(centro_de_custo) <> centro_de_custo
//     ,'TRUE','FALSE')  																											AS mov_in
,IF(pessoa_new = PEEK('pessoa_new') and [load_date]=Peek('load_date'), PEEK('indice_pessoa') + 1, 1) 	as indice_pessoa
,IF(chapa = PEEK('chapa') and [load_date]=Peek('load_date'), PEEK('indice_pessoa') + 1, 1) 	            as indice_chapa
RESIDENT headcount_temp_2
order by pessoa_new, load_date, data_admissao desc
;
// Order by pessoa_new, load_date asc;

DROP TABLE headcount_temp_2;


// sv_headcount_f:
// Load

// *
// ,if(previous(pessoa_new) = pessoa_new
//     and Previous(centro_de_custo) <> centro_de_custo
//     ,'TRUE','FALSE')  																											AS mov_out
// RESIDENT headcount_temp_3
// Order by pessoa_new, load_date desc;


// DROP TABLE headcount_temp_3;


STORE sv_headcount_f INTO [$(silver_layer)sv_headcount_f.QVD]
(qvd);


DROP TABLE sv_headcount_f ;




///////////////////////////        SV TERMINATION      //////////////////////////////////////////////




TRACE 'sv_termination_f';

termination_temp_1:

Load
   	Date#([Data Demissão], 'DD.MM.YYYY')     																			as termination_date
   ,MonthEnd(Date#([Data Demissão], 'DD.MM.YYYY')) 																		as load_date
   ,[Pessoas] 																											as pessoa
   ,[Funcionário] 																										as chapa
   ,[Funcionário TEXT]																									as nome
   ,[Situação]								 																			as situacao_cod
   ,[Situação TEXT]																										as situacao_nome
   ,RIGHT('00000' & [Funções], 5) 																						as funcao_cod
   ,[Funções TEXT] 																										as funcao_nome
   ,DATE(DATE#("Data Admissão", 'DD.MM.YYYY'), 'DD.MM.YYYY') 															as data_admissao
   ,(Date#([Data Demissão], 'DD.MM.YYYY') - Date#([Data Admissão], 'DD.MM.YYYY')) 										as tempo_empresa_dias
   ,[Tipo de Demissão]																									as demissao_tipo_cod
   ,[Tipo de Demissão TEXT]																								as demissao_tipo_nome
   ,[Motivo Demissão]																									as demissao_motivo_cod
   ,[Motivo Demissão TEXT]																								as demissao_motivo_nome
   //,APPLYMAP('CLASSIFICAÇÃO_MAP',[Tipo de Demissão],'Outro')															as demissao_classificação
   ,If(Match([Tipo de Demissão], '1', '2', '8', 'N'), 'Voluntário', 'Involuntário')                                      as demissao_classificacao
   ,[Tipo Funcionário] 												 												    as tipo_funcionario_cod														
   ,[Tipo Funcionário TEXT]                                                                                             as tipo_funcionario_nome //a base está vindo em branco
   ,[Seção]                                                                                                             as secao_cod
   ,[Coligadas]                                                                                                         as coligada_cod
   ,IF(MATCH([Coligadas], ''),NULL(), APPLYMAP('coligada_d',[Coligadas])) 			                                    as coligada_nome
   ,[Código Filial]                                                                                                     as filial_cod
//    ,IF(MATCH([Código Filial], ''),NULL(), APPLYMAP('filial_d',[Código Filial]))                                         as filial_nome
   ,REPLACE([Salário], '.', ',')																					    as salario
   ,Num(Replace([Jornada Mensal], '.', ','), '#.##0,00')                            								    as jornada_mensal
   ,[Horários: Escala TEXT]																							    as escala
  
// a regra de new hire e contratação tipo é a mesma, diferencia true or false no resultado para que seja montada a dimensao na proxima camada

    ,IF(Num( (Date#([Data Demissão], 'DD.MM.YYYY') - Date#([Data Admissão], 'DD.MM.YYYY')) / 365.25, '#,##') 
    < 1,
    'Novo Contratado', 'Não Novo Contratado')																			as contratacao_tipo
    
    ,IF(Num( (Date#([Data Demissão], 'DD.MM.YYYY') - Date#([Data Admissão], 'DD.MM.YYYY')) / 365.25, '#,##') 
    < 1,
    'TRUE', 'FALSE')                        																			as new_hire_flag


// a regra de admitido é para que seja destacado os funcionarios que foram admitidos no mes

   ,IF( Date(MonthEnd(Date#([Data Admissão], 'DD.MM.YYYY'))) = Date(MonthEnd(Date#([Data Demissão], 'DD.MM.YYYY'))),
    'TRUE', 'FALSE') 																									as admitido_flag



// a regra de admitidos até 3 meses


   ,IF(Num( (Date#([Data Demissão], 'DD.MM.YYYY') - Date#([Data Admissão], 'DD.MM.YYYY')) / 365.25, '#,##')  <= 0.25,
    'TRUE',
    'FALSE'
) 																														as admitido_flag_3meses

   ,IF( 
   		  NOT Match([Tipo Funcionário], 'C', 'S', 'T', 'U', 'Z') 
          // C - CONSELHEIRO, 
          // S - PENSIONISTA, 
          // T - ESTAGIÁRIO, 
          // U - OUTROS, 
          // Z - APRENDIZ
          
     AND  NOT Match([Tipo de Demissão], '5'
     //, '8' removido 
     , 'A', 'D', 'E', 'F', 'I', 'J', 'P', 'R', 'S', 'U') 

 // 5	Transferência sem ônus p/ Cedente, 
 // 8	Falecimento, removido
 // A	Aposentadoria invalidez (ac. trab.), 
 // D	Aposentadoria invalidez (doenca)
 // E	Aposentadoria especial, 
 // F	Falecimento p/ acidente de trabalho, 
 // I	Apos. p/ Idade com resc. contrato, 
 // J	Apos. p/ Idade sem resc. contrato
 // P	Falecimento p/ doenca profissional, 
 // R	Apos. Tempo Serv. c/ Resc. Contrato, 
 // S	Apos tempo servico sem resc.contrato, 
 // U	Aposentadoria Compulsória
 ,'TRUE'
 ,'FALSE' )																												as turnover_flag




   

Resident bz_headcount_latest_f
WHERE 
1=1
AND [Situação] = 'D' //Demitido
AND [Tipo de Demissão] <> '5' // Recontratação
; 






LEFT JOIN (termination_temp_1)
LOAD
     Funcionário                                                        												 as chapa // Campo de ligação
    ,FirstSortedValue([Cor e Raça], -NUM(DATE(DATE#("Dia do calendário", 'DD.MM.YYYY'), 'DD.MM.YYYY') ))                 as raca_cod 
    ,FirstSortedValue([Cor e Raça TEXT], -NUM(DATE(DATE#("Dia do calendário", 'DD.MM.YYYY'), 'DD.MM.YYYY') ))            as raca_nome
    ,FirstSortedValue(DATE(DATE#("Data de Nascimento", 'DD.MM.YYYY'), 'DD.MM.YYYY'), -NUM(DATE(DATE#("Dia do calendário", 'DD.MM.YYYY'), 'DD.MM.YYYY') ))   as nascimento_data
    ,FirstSortedValue("Cota PCD", -NUM(DATE(DATE#("Dia do calendário", 'DD.MM.YYYY'), 'DD.MM.YYYY') ))                   as cota_pcd
    ,FirstSortedValue("Horários: Escala TEXT", -NUM(DATE(DATE#("Dia do calendário", 'DD.MM.YYYY'), 'DD.MM.YYYY') ))      as escala
    
Resident bz_headcount_and_short_tenure_and_offshore_f

GROUP BY Funcionário
;









												// adiciona dados de pessoa
                                        
                                        
                                        
                                        

LEFT JOIN (termination_temp_1)
LOAD Distinct
     [Pessoas]                                                                                                         as pessoa
    ,[CPF RM]                                                                                                          as cpf
    ,[Carteira de Identidade]                                                                                          as rg
    ,[Carteira de Motorista]                     																	   as cnh_cod
    ,[Tipo da Carteira de Habilitação]                                                                                 as cnh_tipo
    ,[Data Vencimento da CNH]                                                                                          as cnh_vencimento
    ,[Estado]																									       as estado
    ,[Estado Civil]  																								   as estado_civil_cod
    ,[Estado Civil TEXT]																							   as estado_civil_nome
    ,[Nacionalidade]  																								   as nacionalidade                                                                                                                                                                
    ,[Naturalidade] 																								   as naturalidade                                                                                                         
    ,[Rua]                                            																   as rua
    ,[Número]																										   as numero
    ,[Complemento]                                                                                                     as complemento
    ,[Bairro]																										   as bairro
    ,[Cidade]                                                                                                          as cidade
    ,[Pais] 																										   as pais
    ,[CEP]																											   as cep
    ,[Telefone 1]                                                                                                      as telefone
    ,IF([Sexo] = 'M', 'Masculino',
	 IF([Sexo] = 'F', 'Feminino',
					  'Não informado')) 																			   as genero
        
Resident bz_pessoa_d
;




													// adiciona dados de hierarquia




LEFT JOIN (termination_temp_1)

LOAD Distinct
	Funcionário																											 as chapa
    ,IF(TRIM("Endereço Internet Mail")= '', 'Nenhum Registro Encontrado', "Endereço Internet Mail") 				     as email												
    
    // Remove o texto '1/' dos campos caso esteja presente
    ,[Hierarquia Nível 1]                                                                                                as hierarquia_cod_n1
    ,IF(LEFT([Hierarquia Nível 1 TEXT], 2) = '1/', MID([Hierarquia Nível 1 TEXT], 3), [Hierarquia Nível 1 TEXT])		 as hierarquia_nome_n1
    
    ,[Hierarquia Nível 2]                                                                                                as hierarquia_cod_n2
    ,IF(LEFT([Hierarquia Nível 2 TEXT], 2) = '1/', MID([Hierarquia Nível 2 TEXT], 3), [Hierarquia Nível 2 TEXT]) 		 as hierarquia_nome_n2
    
    ,[Hierarquia Nível 3]                                                                                                as hierarquia_cod_n3
    ,IF(LEFT([Hierarquia Nível 3 TEXT], 2) = '1/', MID([Hierarquia Nível 3 TEXT], 3), [Hierarquia Nível 3 TEXT]) 		 as hierarquia_nome_n3
    
    ,[Hierarquia Nível 4]                                                                                                as hierarquia_cod_n4
    ,IF(LEFT([Hierarquia Nível 4 TEXT], 2) = '1/', MID([Hierarquia Nível 4 TEXT], 3), [Hierarquia Nível 4 TEXT]) 		 as hierarquia_nome_n4
    
    ,[Hierarquia Nível 5]                                                                                                as hierarquia_cod_n5
    ,IF(LEFT([Hierarquia Nível 5 TEXT], 2) = '1/', MID([Hierarquia Nível 5 TEXT], 3), [Hierarquia Nível 5 TEXT]) 		 as hierarquia_nome_n5
    
    ,[Hierarquia Nível 6]                                                                                                as hierarquia_cod_n6
    ,IF(LEFT([Hierarquia Nível 6 TEXT], 2) = '1/', MID([Hierarquia Nível 6 TEXT], 3), [Hierarquia Nível 6 TEXT]) 		 as hierarquia_nome_n6
    
Resident bz_hierarquia_d
;








								// readmitidos 



LEFT JOIN (termination_temp_1)
LOAD 
    [Pessoas]                                                             												as pessoa
    ,if(count([Data Admissão]) > 1, count([Data Admissão]) - 1, 0) 														as qtd_readimissoes
Resident bz_headcount_latest_f

WHERE 1=1 
AND NOT Match([Situação], '0', 'Z', '9')     // Exclui '0' mudanças de matrícula, 'Z' admissões futuras e '9' matrículas apagadas
AND NOT Match([Tipo Funcionário], 'Z', 'T')  // Exclui 'Z' aprendizes e 'T' estagiários
AND NOT Match([Tipo de Admissão], 'T')       // Exclui transferências sem ônus
GROUP BY Pessoas;




											// cria tabela para abter a seção nome que so existe na latest
                                            // como a seção text vem de uma tabela onde so existe o dado mais recente, a seção pode ser inexistente se nenhum funcionário estiver associado a ela.
                                            
                                         
                                         
                                         


LEFT JOIN (termination_temp_1)
LOAD Distinct
    [Seção] 																											as secao_cod,
    [Seção TEXT] 																										as secao_nome
Resident bz_headcount_latest_f

WHERE NOT  IsNull( [Seção TEXT] );


							// centro de custo



LEFT JOIN (termination_temp_1)
LOAD Distinct
	 [Funcionário] 											                                                           as chapa
    ,MID([Centro de Custo], 3)																						   as centro_de_custo
    ,MID([Centro de Custo TEXT], 3)																					   as centro_de_custo_nome
        
Resident bz_headcount_latest_f
;




							// hierarquia




LEFT JOIN (termination_temp_1)
LOAD Distinct
//     [Centro Custo]  																                                    as centro_de_custo
// //     ,IF(MATCH([Dir.], 'Dir. Planejamento Estratégico'), NULL(), [Dir.]) 												as diretoria
//     ,[Dir.]																												as diretoria

//     ,IF([Área] = '-', NULL(), [Área]) 																					as area
// //     ,IF(
// //     	MATCH(IF(MATCH([Dir.], 'Dir. Planejamento Estratégico'), NULL()
// //         , [Dir.]), '')
// //         ,NULL()
// //         , APPLYMAP('DIRETORIA_MAP',IF(MATCH([Dir.], 'Dir. Planejamento Estratégico')
// //         , NULL(), [Dir.])))																								as grupo_diretoria   
//     ,[Grupo Diretoria]																									as grupo_diretoria
*
Resident centro_de_custo;





											// cria tabela para obter funcao
                                            
                                            		
                                                    
                                    


LEFT JOIN (termination_temp_1)
LOAD Distinct
	
    RIGHT('00000' & KEEPCHAR([Cargo], '0123456789'), 5) 																as funcao_cod
    ,IF([Carreira] = '1-GESTÃO' OR [Grupo Relatório] = '5- ESPECIALISTA', 'Líder', 'Não Líder')							as lider_flag
    ,IF([Grupo Relatório] = '8 - Demais', 'Operacional', 'Não Operacional')												as operacional_flag
    ,[Carreira]												                                                			as carreira
    ,SubField(Capitalize([Grupo de Cargo]), ' - ', 2)																	as grupo_cargo
    ,SubField(Capitalize([Grupo de Cargo 2]), ' - ', 2) 																as grupo_cargo_micro
    ,[Grupo Relatório]																									as grupo_relatorio
    ,GS																										    		as gs
    ,UPPER("Tabela Salarial")																							as cargo_salarial_tipo    
    ,[CBO 
2002]																													as cbo_2002
    ,[Descrição CBO]																						    		as cbo_descricao

Resident bz_excel_funcao_d
;





											// cria a headcount temp 2 para adicionar regras de negocio que tem dependencia de mais de uma tabela





termination_temp_2:

Load

*

,Floor((Today() - Date#(nascimento_data, 'DD.MM.YYYY')) / 365.25) 											    					as idade
,IF(
            Floor(( Date(Date#(nascimento_data, 'DD.MM.YYYY'), 'DD.MM.YYYY') 
            	       - Date#(nascimento_data, 'DD.MM.YYYY') ) / 365.25) <= 30,  			'Até 30 anos',
            IF(
                Floor(( Date(Date#(nascimento_data, 'DD.MM.YYYY'), 'DD.MM.YYYY') 
                		   - Date#(nascimento_data, 'DD.MM.YYYY') ) / 365.25) > 50,    	'Acima de 50 anos',
                																				
                                                                                                'De 31 a 50 anos')
         )																											    		   as idade_grupo

,Alt(qtd_readimissoes, 0)      																							           as qtd_readimissoes_new
,AutoNumberHash128(UPPER(
    	IF(
        	WILDMATCH( Num([coligada_cod]) & Num([filial_cod]) & Upper([cargo_salarial_tipo]) & num([gs])
            				, '*ALL*')
                           	, [cargo_salarial_tipo] & Num([gs])
                            , Num([coligada_cod]) & Num([filial_cod]) & Upper([cargo_salarial_tipo]) & Num([gs]))) )               as range_salario_key


RESIDENT termination_temp_1;

Drop Field qtd_readimissoes;

Drop Table termination_temp_1;





												// cria tabela para obter range de salario
                                                    
                                                    
                                                    

LEFT JOIN (termination_temp_2)
LOAD
	
	 AutoNumberHash128( Num([CÓD. FILIAL]) & Num([CÓD. EMPRESA]) & Upper([TIPO CARGO]) & Num([GS]) )                    as range_salario_key
    ,NUM([0.8], '#.##0,00')																								as 80
    ,NUM([0.9], '#.##0,00')																								as 90
    ,NUM([1], '#.##0,00')																								as 100
    ,NUM([1.1000000000000001], '#.##0,00')																				as 110
    ,NUM([1.2], '#.##0,00')																								as 120
    
Resident bz_excel_range_salario_d
;






LEFT JOIN (termination_temp_2)
LOAD Distinct
 coligada_cod
,filial_cod
,filial_nome
Resident bz_excel_filial_d;

                                            




											// headcount KPI final




sv_termination_f:
LOAD 

*    

,NUM(salario/ [100], '#,##%')		           										       						        as posic_fs
,IF(NUM( salario / [100] ) < 0.8, 'Menor 80%',
  IF(NUM( salario / [100] ) < 0.9, 'Entre 80% e 90%',
    IF(NUM( salario / [100] ) < 1, 'Entre 90% e 100%',
      IF(NUM( salario / [100] ) < 1.1, 'Entre 100% e 110%',
        IF(NUM( salario / [100] ) <= 1.2, 'Entre 110% até 120%',
           'Acima 120%'
        )
      )
    )
  )
) 																														as agrup_fs
,if(qtd_readimissoes_new >= 1, 'Sim', 'Não')                                                    					    as readimitido  	
,qtd_readimissoes_new 																									as qtd_readimissoes
,IF(
        [hierarquia_cod_n6] <> [chapa] AND [hierarquia_cod_n6] <> '#',
        [hierarquia_nome_n6],
        IF(
            [hierarquia_cod_n5] <> [chapa] AND [hierarquia_cod_n5] <> '#',
            [hierarquia_nome_n5],
            IF(
                [hierarquia_cod_n4] <> [chapa] AND [hierarquia_cod_n4] <> '#',
                [hierarquia_nome_n4],
                IF(
                    [hierarquia_cod_n3] <> [chapa] AND [hierarquia_cod_n3] <> '#',
                    [hierarquia_nome_n3],
                    IF(
                        [hierarquia_cod_n2] <> [chapa] AND [hierarquia_cod_n2] <> '#',
                        [hierarquia_nome_n2],
                        IF(
                            [hierarquia_cod_n1] <> [chapa] AND [hierarquia_cod_n1] <> '#',
                            [hierarquia_nome_n1]
                        )
                    )
                )
            )
        )
    )  AS [gestor_direto_nome]
,IF(
        [hierarquia_cod_n6] <> [chapa] AND [hierarquia_cod_n6] <> '#',
        [hierarquia_cod_n6],
        IF(
            [hierarquia_cod_n5] <> [chapa] AND [hierarquia_cod_n5] <> '#',
            [hierarquia_cod_n5],
            IF(
                [hierarquia_cod_n4] <> [chapa] AND [hierarquia_cod_n4] <> '#',
                [hierarquia_cod_n4],
                IF(
                    [hierarquia_cod_n3] <> [chapa] AND [hierarquia_cod_n3] <> '#',
                    [hierarquia_cod_n3],
                    IF(
                        [hierarquia_cod_n2] <> [chapa] AND [hierarquia_cod_n2] <> '#',
                        [hierarquia_cod_n2],
                        IF(
                            [hierarquia_cod_n1] <> [chapa] AND [hierarquia_cod_n1] <> '#',
                            [hierarquia_cod_n1]
                        )
                    )
                )
            )
        )
    )  AS [gestor_direto_cod]
     
RESIDENT termination_temp_2;

DROP TABLE termination_temp_2;


STORE sv_termination_f INTO [$(silver_layer)sv_termination_f.QVD]
(qvd);

DROP TABLE sv_termination_f;




///////////////////////////        SV EXCEL ORCAMENTO HISTORICO      //////////////////////////////////////////////





sv_excel_hc_orcamento_historico_f:
Load
coligada_cod
,filial_cod
,centro_de_custo_cod
,funcao_cod
,Valor
,Date( load_date, 'DD.MM.YYYY') 	as load_date
resident bz_excel_hc_orcamento_historico_f;

STORE sv_excel_hc_orcamento_historico_f INTO [$(silver_layer)sv_excel_hc_orcamento_historico_f.QVD]
(qvd);

DROP TABLE sv_excel_hc_orcamento_historico_f;




///////////////////////////        SV POSICOES      //////////////////////////////////////////////




sv_posicoes_f:

Load
CCUSTO			 				as centro_de_custo
,Capitalize([STATUS]) 			as rp_status
,POSICAO						as funcao_nome
,RP                             as rp
,Date(MonthStart(Today()))      as load_date
,if( [CLASSIFICACAO] = 'SubstituiÃ§Ã£o','Substituição', Capitalize([CLASSIFICACAO])) 	as rp_classificacao
,Capitalize(EMPRESA) 																	as rp_empresa_contratado 
,if(Capitalize(TIPORP1) = null(),'Sem Classificação', Capitalize(TIPORP1) ) 			as rp_tipo 
,If(WildMatch(Upper(POSICAO), 'APRENDIZ'), 'TRUE', 'FALSE') 						as aprendiz_flag
,if( Match(Capitalize([STATUS]), 'Em Andamento', 'Em Admissão'),'TRUE','FALSE')     as andamento_flag


Resident bz_excel_posicoes_f


Where
      WildMatch(Upper(POSICAO), '*APRENDIZ*',	'*ESTAG*') = 0
and   WildMatch(Upper(RESPONSAVELVAGA), '*NAO DEFINIDO*') = 0   
    ;



Left join (sv_posicoes_f)
Load Distinct
    [Funções TEXT] as funcao_nome,
    Max(RIGHT('00000' & [Funções], 5)) as funcao_cod
Resident bz_headcount_latest_f
Group By [Funções TEXT];


STORE sv_posicoes_f INTO [$(silver_layer)sv_posicoes_f.QVD]
(qvd);



///////////////////////////        DROP RAW      //////////////////////////////////////////////


//      FATOS

Drop Table
 bz_headcount_f
,bz_headcount_latest_f
// ,bz_salario_f
// ,bz_eventos_f
,bz_excel_hc_orcamento_historico_f
,bz_posicoes_f
,bz_headcount_and_short_tenure_and_offshore_f



//       DIMENSÕES     



, bz_excel_estrutura_cc_d
,bz_pessoa_d
,bz_hierarquia_d
,bz_hierarquia_d
,bz_excel_funcao_d
,bz_excel_range_salario_d
,bz_excel_range_salario_d
,bz_excel_filial_d
,bz_externo_centro_custo_d
,centro_de_custo
,funcao
;

Exit Script;