# Behavioral Patterns(Padrões Comportamentais)

## Observer

**Resumo**

O padrão Observer é um dos padrões comportamentais mais utilizados em engenharia de software. Ele define uma relação de dependência entre objetos de modo que, quando um objeto muda de estado, todos os seus dependentes são notificados e atualizados automaticamente. Isso é alcançado através de um mecanismo de assinatura e notificação, onde os observadores registram interesse em receber notificações sobre mudanças de estado em um objeto observado.

**Propósito**

O objetivo principal do padrão Observer é permitir a comunicação entre objetos em um sistema de forma desacoplada, de modo que as mudanças em um objeto possam notificar e atualizar automaticamente outros objetos que dependem dele. Isso promove a modularidade, reutilização e extensibilidade do código.

**Caso de uso**

Imagine um sistema de monitoramento meteorológico, onde várias telas exibem informações sobre o clima atual. O padrão Observer pode ser aplicado aqui, onde o objeto responsável por coletar dados meteorológicos seria o "objeto observado". As telas de exibição seriam os "observadores". Quando os dados meteorológicos são atualizados, todas as telas registradas como observadores são notificadas e atualizadas automaticamente para refletir as mudanças.

## Command

**Resumo**

O padrão Command é um padrão comportamental que encapsula uma solicitação como um objeto, permitindo que você parametrize clientes com operações, enfileire solicitações e suporte à operações que podem ser desfeitas. Ele separa o emissor de uma solicitação de seu receptor, permitindo assim maior flexibilidade na manipulação de comandos.

**Propósito**

O propósito do padrão Command é desacoplar o objeto que invoca uma operação de objetos que realmente realizam a operação. Isso permite que você manipule solicitações como objetos, parametrize os clientes com operações, enfileire solicitações e suporte à operações que podem ser desfeitas.

**Caso de uso**

Considere um editor de texto onde você pode realizar várias operações, como copiar, colar, desfazer e refazer. Cada uma dessas operações pode ser encapsulada como um comando. Por exemplo, a ação de copiar texto pode ser representada por um objeto de comando de copiar, a ação de colar texto pode ser representada por um objeto de comando de colar. Isso permite que o editor de texto gerencie esses comandos de forma independente de quem os executa, permitindo também a possibilidade de desfazer e refazer operações.

## Template Method

**Resumo**

O padrão Template Method é um padrão comportamental que define o esqueleto de um algoritmo em uma operação, adiando alguns passos para subclasses. Ele permite que as subclasses redefinam certos passos de um algoritmo sem alterar sua estrutura geral.

**Propósito**

O propósito do padrão Template Method é permitir a definição de uma estrutura algorítmica em uma classe base, enquanto alguns passos específicos do algoritmo podem ser implementados por subclasses. Isso promove a reutilização de código e permite a variação de partes específicas de um algoritmo sem modificar sua estrutura geral.

**Caso de uso**

Um exemplo comum de uso do padrão Template Method é encontrado em frameworks de desenvolvimento de jogos, onde uma classe base pode definir o esqueleto de um método de renderização de cena, enquanto subclasses podem fornecer implementações específicas para diferentes tipos de renderização, como renderização em 2D ou 3D.

## State

**Resumo**

O padrão State é um padrão comportamental que permite que um objeto altere seu comportamento quando seu estado interno muda. Ele encapsula estados diferentes em objetos separados e delega responsabilidades associadas a cada estado a esses objetos.

**Propósito**
O propósito do padrão State é permitir que um objeto altere seu comportamento quando seu estado interno muda. Isso é alcançado através da encapsulação de cada estado possível em um objeto separado e delegando a responsabilidade pelas operações associadas a esse estado ao próprio objeto de estado.

**Caso de uso**

Considere um player de música que pode estar em diferentes estados, como "reproduzindo", "pausado" ou "parado". Cada estado pode ser representado por um objeto de estado correspondente. Quando o player muda de estado, as operações associadas a esse estado (como reproduzir, pausar ou parar) são tratadas pelo objeto de estado atual. Isso permite que o player se adapte dinamicamente ao seu estado interno sem alterar sua interface externa.