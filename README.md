# Projeto Cadastro de EPI

 Passo : 1 
 Executar um git clone desse projeto.

 Copie a URL do código. Exemplo :
 https://github.com/usuario/nome-do-repositorio.git

 Passo 2 :

 Abra o terminal do seu computador e realize o GIT CLONE. Exemplo :
 git clone https://github.com/usuario/nome-do-repositorio.git
 
 Substitua pelo link que você quer realizar o git, no caso o nosso projeto acima.

 Passo 3 : 
 
 Abrindo o link no VS CODE : 

 Primeiro, use o comando cd para entrar na pasta do repositório que você acabou de clonar. O nome da pasta será o mesmo nome do repositório.

    Bash

    cd nome-do-repositorio// Troque pelo repositório clonado!//

  Em seguida, execute o seguinte comando. O ponto . significa "a pasta atual".

    Bash

    code .

  Passo 4 :
  No vs code com os códigos em mãos, criamos um ambiente virtual com :
  
    python -m venv venv

  Em seguida, ativamos o mesmo para validação : 

  WINDOWS :
        
        .\venv\Scripts\activate

  MAC\LINUX :

        source venv/bin/activate

  Passo 5 : 

  Instalação do Django : 
  Comando :

        pip isntall django 

  Passo 6 : 

  Feito isso, agora podemos rodar o servidor! Está tudo Pronto! 

          python manage.py runserver 

  Pronto, agora o servidor está no ar pronto para cadastrar os EPI`s.

 

 

