## Getting Started

Welcome to the VS Code Java world. Here is a guideline to help you get started to write Java code in Visual Studio Code.

## Folder Structure

The workspace contains two folders by default, where:

- `src`: the folder to maintain sources
- `lib`: the folder to maintain dependencies

Meanwhile, the compiled output files will be generated in the `bin` folder by default.

> If you want to customize the folder structure, open `.vscode/settings.json` and update the related settings there.

## Dependency Management

The `JAVA PROJECTS` view allows you to manage your dependencies. More details can be found [here](https://github.com/microsoft/vscode-java-dependency#manage-dependencies).

## Questão

Nesta questão, você deverá implementar classes Java que atendam ao cenário do problema descrito abaixo. Os quesitos avaliados serão a aplicação adequada de (i) abstração, (ii) encapsulamento, (iii) herança e (iv) polimorfismo. Indique no código fonte, na forma de comentário, onde cada um desses princípios foi empregado na solução entregue.
Descrição do Cenário:
A venda de computadores e componentes de informática pode ser feita por lojas considerando que os itens são vendidos de forma avulsa ou agregada. Por exemplo, é possível comprar placas de vídeo, processadores e pentes de memória individualmente ou na forma de um computador montado.
Seu trabalho nesta questão é modelar e implementar este cenário de vendas, onde todos os itens disponíveis têm um código sequencial que os identifica de forma inequívoca. Qualquer item, independente de ser um item avulso ou um item montado, deve ser capaz de informar qual o seu preço. O preço de um item de compra é calculado da seguinte forma:

* Todos os itens avulsos possuem preço próprio.

* Um item montado tem o seu preço calculado pela soma dos preços de suas partes. Nesta questão, projeto classes para os seguintes itens de compra:

* Processadores: são itens avulsos que se diferenciam um dos outros apenas pela descrição (string) e pelo preço (double).

* Pentes de Memória: são itens avulsos que se diferenciam uns dos outros pela descrição (string), capacidade em gigabyte (integer) e preço (double).

* Monitores de Vídeo: são itens avulsos que se diferenciam uns dos outros pela descrição (string), resolução em polegadas (double) e preço (double).

* Teclado: são itens avulsos que se diferenciam uns dos outros pela descrição (string) e preço (double).

* Gabinetes: são itens que o usuário pode montar pela inclusão de processadores e pentes de memória.

* Computadores: são itens que o usuário pode montar pela inclusão de gabinetes, monitores e teclados.
