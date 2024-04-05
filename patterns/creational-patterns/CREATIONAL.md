# Creational Patterns(Padrões Criacionais)

## Singleton

**Resumo**

O padrão Singleton é um padrão de criação que garante que uma classe tenha apenas uma instância e fornece um ponto de acesso global para essa instância. Ele é amplamente utilizado em situações onde uma única instância de uma classe é necessária para coordenar ações em todo o sistema.

**Propósito**

O propósito do padrão Singleton é garantir que uma classe tenha apenas uma instância e fornecer um ponto de acesso global para essa instância. Isso é útil em situações onde há a necessidade de coordenar recursos compartilhados ou controlar ações que devem ser realizadas apenas uma vez.

**Caso de uso**

Um exemplo comum de uso do padrão Singleton é em uma aplicação que faz uso de um gerenciador de logs. O gerenciador de logs pode ser implementado como um Singleton, garantindo que todas as partes da aplicação usem a mesma instância para registrar mensagens de log. Isso evita a sobrecarga de criar múltiplas instâncias do gerenciador de logs e garante a consistência nos registros.

## Simple Factory

**Resumo**

O padrão Simple Factory é um padrão de criação que encapsula a criação de objetos em uma única classe, conhecida como a fábrica. A fábrica decide qual subclasse deve ser instanciada com base em um parâmetro fornecido e retorna uma instância da subclasse apropriada.

**Propósito**

O propósito do padrão Simple Factory é encapsular a criação de objetos e ocultar a lógica de criação das partes do código que consomem esses objetos. Isso promove o desacoplamento entre o código que usa os objetos e as classes específicas dos objetos, facilitando a manutenção e extensão do código.

**Caso de uso**

Um exemplo de uso do padrão Simple Factory pode ser encontrado em um sistema de gerenciamento de formas geométricas. A fábrica pode ser responsável por criar instâncias de diferentes formas geométricas, como círculos, quadrados ou triângulos, com base no tipo de forma solicitado. Isso permite que o código cliente crie formas sem precisar saber sobre as complexidades da criação de cada tipo de forma.

## Factory Method

**Resumo**

O padrão Factory Method é um padrão de criação que define uma interface para criar um objeto, mas permite que as subclasses alterem o tipo de objetos que serão criados. Ele encapsula a lógica de criação em uma classe base, delegando a responsabilidade de criar objetos concretos para suas subclasses.

**Propósito**

O propósito do padrão Factory Method é fornecer uma interface para criar objetos em uma classe base, permitindo que subclasses alterem o tipo de objetos que serão criados. Isso promove o princípio do polimorfismo e permite que o código cliente trabalhe com objetos abstratos em vez de classes concretas.

**Caso de uso**

Um exemplo comum de uso do padrão Factory Method é em jogos, onde diferentes tipos de inimigos precisam ser criados durante o jogo. A classe base pode definir um método de fábrica para criar inimigos, enquanto subclasses podem fornecer implementações específicas para criar diferentes tipos de inimigos, como inimigos terrestres, aéreos ou chefes.

## Abstract Factory

**Resumo**

O padrão Abstract Factory é um padrão de criação que fornece uma interface para criar famílias de objetos relacionados ou dependentes sem especificar suas classes concretas. Ele encapsula a criação de objetos de diferentes tipos, mas relacionados, em uma única interface de fábrica.

**Propósito**

O propósito do padrão Abstract Factory é fornecer uma interface para criar famílias de objetos relacionados sem especificar suas classes concretas. Isso permite que o código cliente trabalhe com famílias de objetos de forma independente de suas implementações específicas, promovendo assim o princípio do encapsulamento.

**Caso de uso**

Um exemplo de uso do padrão Abstract Factory pode ser encontrado em um sistema de UI (User Interface) onde diferentes elementos de interface do usuário, como botões, campos de texto e caixas de seleção, precisam ser criados para diferentes plataformas, como desktop e mobile. Uma fábrica abstrata pode fornecer métodos para criar esses elementos de UI, enquanto fábricas concretas fornecem implementações específicas para cada plataforma. Isso permite que o código cliente crie elementos de UI sem se preocupar com detalhes de implementação específicos de plataforma.