1 - Crie uma classe abstrata chamada Animal com métodos falar(), comer() e mover().
    Crie subclasses Cachorro, Cavalo e Gato que herdam da classe Animal e implementam
    seus próprios métodos, printando frases diferentes.  
    Crie e trabalhe com os getters e setters para as subclasses.

2 - Crie uma classe Banco com métodos abstratos depositar(), ver_saldo() e sacar() e 
    implemente a lógica de cada método. Crie subclasses ContaCorrente e ContaPoupanca
    que herdam da classe Banco e implementam os métodos de acordo com suas regras específicas.
    Por exemplo, a subclasse ContaPoupanca pode nao deter o método sacar().
    Crie atributos privados e publicos nas subclasses ContaCorrente e ContaPoupanca
    como self.nome, self.saldo, e self.numero_conta por exemplo. Crie objetos dessas
    classes com informações distintas, invoque os métodos e printe o resultado das
    operações. 

3 - Crie uma classe base Veiculo com atributos como marca, modelo e métodos como ligar()
    e desligar(), entre outros. Crie as subclasses Carro e Moto que herdam de Veiculo e
    implementam seus próprios métodos beaseando-se na abstratação de Veiculo. Em seguida,
    crie uma classe Garagem que aceita veículos e gerencia o estacionamento usando herança.
    Crie e trabalhe com os getters e setters para a classe Garagem.

4 - Crie uma classe abstrata Animal com um método emitir_som(). Crie subclasses Cachorro,
    Gato, Cavalo e Vaca que herdam de Animal e implementam seus próprios sons. Crie uma função
    que aceita uma lista de animais e faça-os emitir sons usando polimorfismo.
    Em seguida, crie contrutores para as subclasses dando um atributo nome e cor, e crie
    objetos dessas subclasses com cores e nomes distintos.

5 - Crie uma classe Alimento com atributos como nome e calorias. Crie subclasses Fruta, Legume
    e Carne que herdam de Alimento e implementam seus próprios atributos. Crie uma função que aceita 
    uma lista de alimentos e calcula o total de calorias usando polimorfismo. Para mais precisão no
    exercício, é ideal pesquisar as calorias dos alimentos e criar objetos das subclasses com seus 
    respectivos construtores e atributos.