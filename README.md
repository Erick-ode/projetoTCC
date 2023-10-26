# projetoTCC

Servidor Backend
O servidor backend é construído em Flask, um framework Python. Certifique-se de estar utilizando a versão mais atualizada do Python para garantir a compatibilidade.

Configuração do Ambiente Virtual
Para garantir um ambiente de desenvolvimento limpo e bem isolado, é recomendável utilizar um ambiente virtual. Caso você não tenha o virtualenv instalado, você pode instalá-lo com o seguinte comando:
    pip install virtualenv

Depois de instalar o virtualenv, siga estas etapas:

Windows:
Navegue até a pasta raiz do projeto.

Ative o ambiente virtual executando o comando:
    venv\Scripts\activate

Linux:
Navegue até a pasta raiz do projeto.

Ative o ambiente virtual com o comando:
    source venv/bin/activate

Instalação de Dependências
Com o ambiente virtual ativado, você pode instalar as dependências necessárias para o projeto. Isso pode ser feito usando o arquivo requirements.txt. Certifique-se de estar na pasta raiz do projeto e execute o seguinte comando:
    pip install -r requirements.txt

Isso instalará todas as dependências listadas no arquivo requirements.txt.

Inicialização do Servidor Backend
Agora que o ambiente virtual está configurado e as dependências estão instaladas, você pode iniciar o servidor backend Flask. Na pasta pasta raiz do projeto use o seguinte comando:
    python waitress_server.py

O servidor estará funcionando.


Frontend
O projeto frontend é construído com React, uma biblioteca JavaScript. Para configurar o ambiente de produção para o frontend, siga estas etapas:

Instale as dependências do projeto com o seguinte comando:
    npm install --production

Construa o projeto React para produção:
    npm run build

Servidor Web para Frontend
Usando o pacote serve:
Instale o pacote serve globalmente:
    npm install -g serve

Navegue até a pasta frontend e execute o servidor serve com o seguinte comando:
    serve -s build

Agora o projeto React deve estar acessível.