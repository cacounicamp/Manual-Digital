# Manual de ingressante Digital

O objetivo desse projeto é ter o manual de ingressante de forma virtual, para acessarmos pelos dispositivos móveis!


## Organização
O projeto contém somente uma página HTML (index.html) simples com todo o texto do manual. No momento só existem dois arquivos de css, o primeiro root.css é referente ao css principal. O segundo arquivo print.css foi criado, mas ainda não possui nenhum conteúdo, com o objetivo de personalizarmos um css afim de utilizar essa versão para impressão também. Com css é possível formatarmos nosso manual para que fique adequado e como é atualmente impresso.

Além disso, existe a pasta images, que possui subpastas de cada seção do manual.

No momento, as seções que temos são as listadas abaixo. Note que as seções principais só existem no menu lateral, não colocamos elas no texto, porque deixaria mais complexo. Só apresentamos o que está dentro delas:

* Olá Mundo - não aparece no texto
    * Prefácio - aparece como seção no texto
* Sobrevivendo na Unicamp - não aparece no texto
    * ...
* Convivendo na Unicamp - não aparece no texto
    * ...
* Vida acadêmica - não aparece no texto
    * ...
* Campine-se - não aparece no texto
    * ...
* Além da graduação - não aparece no texto
    * ...

Além disso, o arquivo index.php é necessário para o deploy no Heroku.

## Orientações / Dicas para editar o HTML
Para facilitar, separamos em alguns tipos de conteúdos recorrentes que queremos colocar como: Título, texto, imagens e legendas, listas e links e damos umas dicas.


### Âncora
Para começar, é importante entender que o manual tem as seções, que são só títulos, porque não possuem nenhum texto, e possui subseções. Ao clicar em uma subseção temos uma âncora que desce a página até o texto referente à ela.

Para isso acontecer, ao criar uma seção colocamos um ```id``` nela, e no menu, colocamos um ```a href``` apontando pro id. 

Use as seções existentes como exemplo (=


### Título
Colocar ```<h1>titulo aqui</h1>``` nos títulos principais, que estão no sumário, exemplo: Prefácio na seção Olá mundo, e Dinheiro na seção Sobrevivendo na Unicamp.

Colocar ```<h2>sub titulo</h2>``` nos subtítulos que podem existir, por exemplo na seção sobre Saúde tem subtítulo que é Hemocentro e CECOM


### Imagens
Circundar com uma div, e colocar o nome da imagem. Eu to criando pastinha, então coloca tipo ```imagens/<nome-da-sua-secao>/nome-da-imagem>``` . Pode inventar o nome da seção e o nome da imagem. Pra colocar legenda, usa um <span> legenda aqui </span>

```
<div>
    <img  src="images/sobrevivendo-unicamp/caco-reflexivo.jpeg"/>
    <span> Facul é difícil </span>
</div>
```

### Listas
Usar as tags ```<ul>``` e ```<li>```. Se quiser que o inicio do texto seja negrito, tem que colocar a tag de negrito, que é ```<b>texto</b>```:

```
<ul>
<li><b>Ensino:</b> lalala </li>
<li><b>Extensão:</b> lalala </li>
</ul>
```


### Links
Temos que usar a tag ```<a>```, coloca no href o link em si, e entre as tags o texto bonitinho
```
<a href="https://www.facebook.com/SAPPE-Unicamp-112906617163477" > Facebook SAPPE</a>
```

## Como editar
Para editar, você precisa clonar esse repo, e ter um conhecimento básico de git, html e css! Pergunta pra galera, alguém vai conseguir te ajudar!


## Deploy no Heroku
Após commitar e deixar no repositório suas alterações, você deve subir elas as alterações no site, fazendo um deploy no Heroku. Não se assuste, é simples.

No Heroku (https://dashboard.heroku.com/), você deve ter acesso a conta do CACo. Lá foi criado o projeto caco-manual-ingressante-2021.

A primeira coisa é instalar o Heroku CLI no seu computador: https://devcenter.heroku.com/articles/heroku-cli

Agora você precisa pelo terminal entrar no seu projeto e executar os seguintes comandos:

```$ heroku login```

```$ git add .```

```$ git commit -am "make it better"```

```$ git push heroku main```


## Script filter.py

Na pasta ```utils``` foi criado o script filter.py para passarmos os textos do Manual de Ingressante para o formato html.

TODO: Explicar como usar 

## Coisas para fazer no Manual
1. Imagens
* Imagens em preto e branco: Todas as nossas imagens estão em preto e branco, poderíamos atualizar para imagens com cor

2. CSS
* Imagem das entidades: No momento as imagens de todas as entidades estão comentadas, porque o css padrão das imagens não ficou legal. Precisamos fazer um css legal pra elas.

* class=box: Criamos uma class "box" que seriam para divs de destaque ou específicos da pandemia, mas ainda não foi feito um css pra ela.

3. E se a gente for imprimir o manual novamente?

Isso é bem provável que vai rolar, porque a pandemia vai ter um fim (esperamos..... o.o). Os textos da versão atual (2021) não estão em outro lugar senão esse repositório. O modo dos anos anteriores, de diagramação, não foi atualizado.

Portanto, precisamos atualizar o modo de diagramação.

Outra ideia, seria criar um css específico voltado para a impressão do manual. Isso é possível... personalizar o modo de impressão da página HTML, aí teríamos somente esse repositório com dois css, um que vamos ver no computador/celular; e outro que vamos ver no momento da impressão, dá pra checar isso clicando com o botão direito no site e clicando em "print". 

Achei bem maneira essa ideia... mas dá um trabalho kkkk Pensando nisso, foi criado um css "print.css" para que possamos experimentar isso, e quem sabe em algum momento dê certo e a gente use oficialmente só esse repositório. 

De qualquer forma, é legal pensar se isso é acessível para todos: o manual ser em HTML/CSS. É mais acessível ter as duas versões, diagramar e tals, ou só deixar esse? Coisas para nós pensarmos! (=

4. Completar o README
* Script utils/filter.py: Esse script converte nosso texto em HTML. Temos que adicionar como utilizá-lo e com exemplos.

## Sucesso!
Sinta-se a vontade para sugerir melhorias e executá-las. Lembre-se de manter o html e css simples, para que todos se sintam confortáveis para editar (=




