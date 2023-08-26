__O que é versionamento de código?__
É o gerenciamento de mudanças em códigos e scripts. Facilitando alterações e retorno a versões antigas de um mesmo código. 

**Sistemas de Controle de Versão**: Controlam as versões de um arquivo ao longo do tempo.

- Registra o histórico de atualizações de um arquivo 
- Gerencia quais foram as alterações, data, autor, etc.
- Organização, controle e segurança. 

**Tipos de Sistemas de Controle de Versão (VCS**):
- VCS Centralizado: Um servidor centralizado que contem o banco de versões do código

- VCS Distribuído: Neste tipo de VCS o banco de versões é duplicado para cada membro da equipe que trabalha no mesmo código, evitando perca por corrompimento do servidor central. 

Clona o repositório completo, o que inclui o histórico de versões. Cada clone é como um backup; Possibilita um fluxo de trabalho flexível e também trabalhar sem conexão à rede. 

__O que é GIT?__
É um DVCS gratuito e Open Source, usa o sistema de ramificações (branching) e fusões (merging) eficientes, além de ser leve e rápido.

__Fluxo Básico do GIT__ 
`git clone` - Clona um repositório Git existente para um novo diretório (pasta) local. 

`git commit` - Grava alterações no repositório.

`git pull` - "Puxa" as alterações do repositório remoto para o local (busca e mescla).

`git push` - "Empurra" as alterações do repositório local para o remoto. 


__O que é GitHub?__ 
Plataforma de hospedagem de código para controle de versão com Git e colaboração. 


## __Comandos de Configuração no Git Bash__

`git config` - mostra todas os comandos para configuração do git

`git config --global user.name "nome do usuario"` - configura o nome do usuário que faz as alterações no código. 

`git config --global user.email mail@mail.com` - configura o e-mail do usuário que fez as alterações 

`git config --global init.defaultBranch main` - configura o nome da ramificação principal 

`git init` - Inicia um novo repositório git dentro da pasta em questão.

`git remote add origin /URL/`  para a criação de repositório remoto a partir de uma pasta local

`git status` mostra o status da versão atual. Pastas vazias não são reconhecidas 

`git add arquivo.py` adiciona um arquivo novo para a lista de commit

`git commit` salva uma nova versão dos arquivos no repositório 

`git commit -m"mensagem para identificação do commit"`

`git log` verifica os registros de commit do projeto

`echo diretorio/ > .gitignore` coloca um arquivo ou diretório no git ignore

`.gitkeep` uma forma de adicionar um diretório vazio ao repositório via git

## Como desfazer uma alteração no Repositório Local

Caso o commit tenha sido feito em uma pasta errada, basta usar `rm -rf .git` 

Caso uma alteração tenha sido feita, salva, mas não comitada. É possível restaurar o arquivo com `git restore nome_do_arquivo` 

Para alterar a mensagem do último commit, basta usar `git commit --amend -m"mensagem"` 

Para desfazer um commit usa-se `git reset --soft AS12783678216ASDA`. A versão volta para a versão anterior do reset feito há também `--mixed e --hard`. O reset também pode ser usado para remover um arquivo específico `git resert main.py` 

## Enviando e Baixando Alterações com o Repositório Remoto

Após ter criado o repositório no GitHub, é preciso conectar os dois repositórios (Local e Remoto)

`git remote add origin https://github.com/usuario/meu-repositorio` 
`git branch -M main` 
`git push -u origin main` - "empurra" as alterações do repositório local para o repositório remoto 

`git pull` - "puxa" a versão do projeto salva no repositório remoto para o local 

## Branches

São ramificações do projeto. É um ponteiro móvel para um commit no histórico do repositório. Ao criar uma nova Branch a partir de outra existente, a nova se inicia apontando para o mesmo commit da Branch que estava quando foi criada. 

`git checkout -b nome_da_ramificação` 

`git branch -v` - lista todas as ramificações de um projeto e os seu último commit

`git merge nome_da_ramificacao` - mescla uma ramificação à branch principal

`git branch -d nome_da_ramificacao` - deleta uma ramificação 



