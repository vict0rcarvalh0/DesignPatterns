# Design Patterns
Repositório para registrar meus estudos de POO e Design Patterns

## Conceitos da POO
- Classes
  - Representam entidades do mundo real
  - Definem os objetos com atributos e métodos
  - Possuem construtores(método especial) que proporcionam o estado inicial para os objetos
  - São um "template" facilmente reutilizável

- Objetos
  - Representam entidades no contexto da aplicação em desenvolvimento
  - Interagem entre si para resolver problemas reais

- Métodos
  - Representam o comportamento dos objetos, ou seja, as ações que podem praticar
  - Atuam nos atributos além de implementar a funcionalidade desejada para o objeto
  
- Atributos
  - Definem as características que ajudam a modelar/mapear o objeto através da classe
  - São as características dos objetos

## Componentes da POO
- Encapsulamento
  - O encapsulamento é um conceito que se refere à proteção dos detalhes internos de um objeto
  - Ele envolve o uso de modificadores de acesso, como público, privado e protegido, para controlar o acesso aos membros (métodos e atributos) de uma classe
  - O encapsulamento ajuda a manter o estado interno de um objeto consistente e a prevenir o acesso não autorizado ou a modificação direta dos seus dados

- Polimorfismo
  - O polimorfismo permite que objetos de diferentes classes sejam tratados como objetos de uma classe comum
  - Existem dois tipos de polimorfismo: **sobrecarga** (métodos com o mesmo nome em uma classe, mas com diferentes parâmetros) e **sobreposição** (métodos em classes diferentes que têm o mesmo nome e assinatura)
  - O polimorfismo torna o código mais flexível e reutilizável, permitindo a chamada de métodos sem a necessidade de saber o tipo exato do objeto

- Herança
  - A herança é um mecanismo que permite criar uma nova classe baseada em uma classe existente (classe pai ou superclasse)
  - A classe recém-criada (classe filha ou subclasse) herda os atributos e métodos da classe pai e pode adicionar ou substituir comportamentos
  - A herança promove a reutilização de código e estabelece uma hierarquia de classes

- Abstração
  - A abstração é o processo de identificar os aspectos essenciais de um objeto ou conceito, enquanto ignoramos os detalhes não essenciais
  - Na POO, a abstração envolve a criação de classes e objetos que representam entidades do mundo real, enfatizando seus atributos e comportamentos mais importantes
  - A abstração permite modelar problemas de forma mais eficaz, simplificando a complexidade

- Composição
  - A composição é um princípio de design de software que envolve a construção de classes complexas a partir de objetos de classes mais simples
  - Em vez de herdar características de uma classe pai, a composição permite que uma classe contenha outras classes como atributos
  - Isso promove a reutilização de código e evita os problemas de acoplamento excessivo que podem surgir com herança

## Princípios do Design de Software Orientado a Objetos - SOLID
1. Princípio da responsabilidade única(**S**ingle Responsability Principle)
  - Determina que uma classe deve ter apenas um motivo para mudar, logo, se uma classe estiver tratando de mais de uma funcionalidade, é melhor dividí-la
  - Ou seja, quando desenvolvemos uma classe, ela deve tomar conta apenas de sua funcionalidade em particular
  - Por se referir à funcionalidade como motivo para mudança, traz a vantagem de tornar as classes mais objetivas
  - Exemplo: Uma classe GestorDeArquivos deve ser responsável apenas pela manipulação de arquivos, não deve incluir lógica de validação ou cálculos. Se a validação for necessária, deve ser tratada por outra classe separada.

2. Princípio do aberto/fechado(**O**pen-Closed Principle)
  - Determina que classes ou métodos devem estar abertos para extensão e fechados para modificações
  - Ou seja, a escrita das classes e métodos devem ser genéricas, de modo que sempre que sentir necessidade de estender o comportamento, não precisaria alterar a classe propriamente dita
  - "Uma extensão simples da classe deverá ajudar a implementar o novo comportamento"
  - Exemplo: Suponha que você tenha uma classe Calculadora com métodos para adição e subtração. Em vez de modificar a classe Calculadora toda vez que você quiser adicionar uma nova operação, você pode criar uma nova classe que estende Calculadora e adiciona a nova operação, mantendo a classe original inalterada.
  
3. Princípio da substituição de Liskov(**L**iskov Substitution Principle)
  - Determina que as classes derivadas devem ser capazes de substituir totalmente as classes pai
  - Ou seja, sugere que a classe derivada deve estar o mais próximo possível da classepai de modo que a classe derivada possa substituir a classe-pai sem qualquer modificação no código
  - Exemplo: Se você tem uma classe base Forma e classes derivadas como Circulo e Quadrado, a instância de qualquer subclasse deve poder substituir uma instância de Forma sem causar erros lógicos. Por exemplo, você deve poder tratar todos os tipos de formas da mesma maneira ao calcular áreas.
  
4. Princípio da segregação de interface(**I**nterface Segregation Principle)
  - Determina que clientes não devem ser forçados a depender de interfaces que não o utilizam
  - Ou seja, boas interfaces são criadas escrevendo apenas métodos relacionados à funcionalidade para que não exista nenhum método não relacionado a interface, evitando que a classe dependente da interface tenha que implementá-lo desnecesariamente
  - "Força os desenvolvedores a escrever interfaces enxutas, sem métodos indesejados ou específicos demais"
  - Exemplo: uma interface Pizza não deveria ter um método chamado adiciona_frango() pois a classe PizzaVegana não deveria ser forçada a implementar este método.

5. Princípio da inversão de dependência(**D**ependency Inversion Principle)
  - Determina que módulos de alto nível não devem ser dependentes de módulos de baixo nível, pois ambos devem ser dependentes de abstrações
  - Ou seja, os módulos devem ser interdependentes, de forma que a complexidade/rigidez do sistema diminui efica mais fácil de lidar com dependências enter módulos
  - "Módulos devem ser desacoplados com uma camada de abstração entre eles"
  - Exemplo: Em vez de uma classe Motor depender diretamente de uma classe Carro, ela deve depender de uma interface Veiculo. Isso permite que diferentes tipos de veículos (carros, motos, caminhões) sejam facilmente integrados sem alterar o código do motor.

## Classificação dos Padrões de Projeto(Design Patterns)
- <a href="https://github.com/vict0rcarvalh0/DesignPatterns/blob/main/patterns/creational-patterns/CREATIONAL.md">Padrões Criacionais</a>
- <a href="https://github.com/vict0rcarvalh0/DesignPatterns/blob/main/patterns/structural-patterns/STRUCTURAL.md">Padrões Estruturais</a>
- <a href="https://github.com/vict0rcarvalh0/DesignPatterns/blob/main/patterns/behavioral-patterns/BEHAVIORAL.md">Padrões Comportamentais</a>
