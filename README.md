
## SEARCH HEURISTICS - Introdução a IA

Nessa implementação, são propostas duas formas de encontrar um melhor caminho (com menor custo) baseada em uma matriz
pré determinada. São elas: 

- Blind Search Uniform Cost - BFS
- Manhattan Distance


### Base
Baseada na implementação padrão, onde é selecionado um nó que posteriormente é expandido e seus filhos passam a compor uma __Fronteira__ para que possa ser expandida, selecionando um nó e a exapandindo.

### Blind Search with Uniform Cost - BFS

Baseando-se no método de custo uniforme, a fronteira dita acima é sempre ordenada pelo menor custo, o que proporciona que quando o nó de origem apareça na fornteira, esse seja já o melhor caminho

<p align="center">
    <img src="./img-docs/img4.png"> <br>Exemplo de Fronteira
</p>

<p align="center">
    <img src="./img-docs/img3.png"> <br>Exemplo de Resposta
</p>

 ### Manhattan Distance

    
Utiliza da implementação e lógica do BFS, entrentanto o cálculo de custo de um nó não é mais o correspondete na matriz, mas agora, seguindo o seguinte cálculo:

__COLOCAR O CALCULO DO MANHATTAN__ 

<p align="center">
    <img src="./img-docs/img5.png"> <br>Exemplo de Fronteira
</p>

<p align="center">
    <img src="./img-docs/img6.png"> <br>Exemplo de Resposta
</p>

__Pontos importantes para ambas as implementações:__

    - Em ambas as implementações, é realizada uma poda na Fronteira, onde não permitida a repetição de nós já visitados, sendo assim evitando *loops*


## Execução

- Para execução do projeto, basta executar o *app.py*.
- Alteração da matriz de entrada, altere o arquivo *index.txt*
    -   Em correspondencia ao arquivo setado como matriz de entrar, altere em ./properties/config.json as definições da Matriz inserida, como: Custo dos valores e dimensões da mesma; além de dimensões da tela e quadrados para melhor visualização.
- As duas primeiras linhas do arquivo da matriz, indicam *Origem* e *Destino* seguindo o padrão (X, Y)

<p align="center">
    <img src="./img-docs/img1.png">
</p>


Para o exemplo acima, temos a seguinte configuração: 

    0,0
    41,41
    2,1,1,1,1,2,1,3,1,1,1,1,1,1,1,1,2,2,2,2,2,2,2,1,1,1,2,2,2,2,2,1,1,1,1,2,2,2,1,1,1,1,
    [...]

Sendo o ponto marcado como preto a origem (0,0) e (41,41) o destino.
- No rodapé temos os resultados obtidos na busca.

- Como exemplo de *Fronteira/Borda* da busca temos a seguinte exeibição

<p align="center">
    <img src="./img-docs/img2.png">
</p>


- Rosa: Posições visitadas e já expandida
- Cinza: Posições na fronteira, que devem ser visitadas





