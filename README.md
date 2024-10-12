<h1>Super App</h1>

<p>Super App é uma aplicação web, desenvolvida utilizando o framework Flask com integração a um banco de dados, que pode ser tanto SQLite quanto MySQL, e implementada com Docker para facilitar o deploy e o gerenciamento de ambientes.</p>

<p>A estrutura do projeto foi redesenhada para seguir o padrão de camadas, permitindo uma separação clara entre as responsabilidades do código. 
  A aplicação conta com uma interface de administração, autenticação de usuários e um sistema de persistência de dados.</p>

<h2>Sumário</h2>
<ul>
    <li><a href="#recursos">Recursos</a></li>
    <li><a href="#tecnologias-utilizadas">Tecnologias Utilizadas</a></li>
    <li><a href="#requisitos">Requisitos</a></li>
    <li><a href="#como-rodar-a-aplicação-localmente">Como Rodar a Aplicação Localmente</a></li>
    <li><a href="#como-rodar-a-aplicação-com-docker">Como Rodar a Aplicação com Docker</a></li>
    <li><a href="#publicação-no-docker-hub">Publicação no Docker Hub</a></li>
</ul>

<h2 id="recursos">Recursos</h2>
<ul>
    <li>Autenticação de usuários</li>
    <li>Painel administrativo utilizando Flask-Admin</li>
    <li>Suporte a bancos de dados SQLite e MySQL</li>
    <li>Containerização com Docker</li>
    <li>Facilidade de deploy utilizando Docker Hub</li>
</ul>

<h2 id="tecnologias-utilizadas">Tecnologias Utilizadas</h2>
<ul>
    <li>Python</li>
    <li>Flask</li>
    <li>SQLAlchemy</li>
    <li>SQLite / MySQL</li>
    <li>Docker</li>
    <li>Docker Compose</li>
</ul>

<h2 id="requisitos">Requisitos</h2>
<p>Antes de rodar a aplicação, você vai precisar ter instalado:</p>
<ul>
    <li>Python</li>
    <li>Docker</li>
    <li>Docker Compose</li>
</ul>

<h2 id="como-rodar-a-aplicação-localmente">Como Rodar a Aplicação Localmente</h2>
<ol>
    <li>Clone este repositório:
        <pre><code>git clone https://github.com/Super-App.git
        </code></pre>
    </li>
    <li>Instale as dependências:
        <pre><code>pip install -r requirements.txt
        </code></pre>
    </li>
    <li>Execute a aplicação:
        <pre><code>python app.py
        </code></pre>
    </li>
    <li>Acesse a aplicação em seu navegador:
        <pre><code>http://localhost:8080/admin
        </code></pre>
    </li>
</ol>

<h2 id="como-rodar-a-aplicação-com-docker">Como Rodar a Aplicação com Docker</h2>
<ol>
    <li>Certifique-se de que o Docker está instalado e em execução.</li>
    <li>Construa a imagem Docker:
        <pre><code>docker build -t super-app .
        </code></pre>
    </li>
    <li>Execute a aplicação com Docker Compose:
        <pre><code>docker-compose up -d
        </code></pre>
    </li>
    <li>Acesse a aplicação em seu navegador:
        <pre><code>http://localhost:8080/admin
        </code></pre>
    </li>
</ol>

<p>A aplicação estará rodando no contêiner <code>web</code>, e o banco de dados no contêiner <code>db</code>. O arquivo <code>docker-compose.yml</code> define a configuração de rede e persistência.</p>

<h2 id="publicação-no-docker-hub">Publicação no Docker Hub</h2>
<ol>
    <li>Faça login no Docker Hub:
        <pre><code>docker login
        </code></pre>
    </li>
    <li>Construa a imagem com a tag do seu usuário Docker Hub:
        <pre><code>docker build -t seu-usuario/super-app .
        </code></pre>
    </li>
    <li>Faça o push da imagem para o Docker Hub:
        <pre><code>docker push seu-usuario/super-app
        </code></pre>
    </li>
    <li>Agora a imagem está disponível publicamente. Para rodá-la em outro ambiente:
        <pre><code>docker run -p 8080:8080 seu-usuario/super-app
        </code></pre>
    </li>
</ol>



