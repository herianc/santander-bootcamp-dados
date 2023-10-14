
Banco de Dados é uma coleção organizada de informações ou dados e é estruturada.

## Tipos de Bancos de Dados 
- Relacionais / SQL
- Não Relacionais / No SQL (Not OnlySQL)
- Orientado a Objetos
- Hierárquico 

## SGBD 
Sistema de Gerenciamento de Banco de Dados. Permitem criar, manipular e consultar os bancos de dados de forma mais intuitiva e prática.

__Funcionalidades Básicas de um SGBD__: CRUD (Create, Read, Update and Delete) 

## Característica de um BD Relacional
- Relacionamento entre tabelas
- SQL
- Integridade referencial
- Normalização de dados
- Segurança 
- Flexibilidade e extensibilidade 
- Suporte a transações ACID ( Atomicidade, Consistência, Isolamento e Durabilidade)

## SQL - Structured Query Language 
Linguagem de consulta padronizada
## Organização da SQL 
- DQL - Linguagem de Consulta de Dados (SELECT)
- DML - Linguagem de Manipulação de Dados (INSERT, UPDATE e DELETE)
- DDL - Linguagem de Definição de Dados (CREATE, ALTER, DROP)
- DCL - Linguagem de Controle de Dados (GRANT, REVOKE)
- DTL - Linguagem de Transação de Dados (BEGIN, COMMIT, ROLLBACK)

## Sintaxe Básica: Nomenclatura 
- Os nomes devem começar com uma letra ou com um underline.
- *** Os nomes podem conter letras, números e caracteres de sublinhado
- Sensibilidade a maiúsculas e minúsculas. 


## MER e DER: Modelagem de Bancos de Dados
Modelo Entidade-Relacionamento (MER) é representado através de diagramas chamados Diagramas Entidade-Relacionamento (DER)

## Entidades 
As entidades são nomeadas com substantivos concretos ou abstratos que representem de forma clara sua função dentro do domínio.

## Atributos 
São características ou propriedades das entidades. Eles descrevem informações específicas sobre uma entidade

## Relacionamentos
Os relacionamentos representam as associações entre entidades.

## Cardinalidade 
Forma como as entidades se relacionam e indicam o número máximo de instâncias ou ocorrências que podem ocorrer.

- Relacionamento 1..1 (um para um)
- Relacionamento 1..n ou 1..* (um para muitos)
- Relacionamento n..n (muitos para muitos)


# SQL Analytics - utilização do SQL para manipulação, transformação e análise de dados com foco em BI

## ETL - Extract, Transform and Load: 
A **Extração** pode ser feita de diversas formas, formulários, web scraping, etc..

A **Transformação** diz respeito a mudança da estrutura do dado de acordo com o sistema que será inserido. EX: JSON -> DATA WAREHOUSE, CSV -> Python dict

A limpeza do dados também uma parte da transformação. 

O **Carregamento** (load) é a integração dos dados para um repositório centralizado.


## ELT - Extract, Load and Transform:
Os dados são armazenados (Carregamento) brutos. Os dados são transformados após, dando uma maior independência ao analista de dados. 

Vantagens do ELT:
- Tempo de carregamento 
- Tempo de transformação
- Tempo de manutenção
- Complexidade de implementação

Quando estiver trabalhando com Big Data o ELT torna as coisas mais ágeis.  Quando o contexto tem um volume de dados menor, o ETL é mais interessante tendo em vista que o custo do armazenamento dos dados é bem menor, já que os foram selecionados e limpos. 


## Processos da Análise Exploratória
- Análise Descritiva - O que aconteceu?
- Diagnóstica - Por que aconteceu?
- Preditiva - O que vai acontecer?
- Prescritivo - O que fazer? 

## Visualização de dados 
- Gráfico de linha: tendência ao longo do tempo
- Gráfico de Área: magnitude 
- Mapas: Relacionando os dados com a Geografia 
- Mapa de Árvore: Consegue trabalhar com um grande número de elementos e os ordena por dimensão 
- Gráfico de Dispersão: utilizado quando queremos ver a força entre duas variáveis 


