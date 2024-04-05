# Structural Patterns(Padrões Estruturais)

## Façade

**Resumo**

O padrão Façade é um padrão estrutural que fornece uma interface simplificada para um conjunto de interfaces mais complexas em um subsistema. Ele oculta a complexidade do subsistema e fornece um ponto de entrada único para interagir com ele.

**Propósito**

O propósito do padrão Façade é fornecer uma interface unificada e simplificada para um subsistema complexo, ocultando sua complexidade subjacente. Isso promove a modularidade, o desacoplamento e a reutilização de código, tornando mais fácil para os clientes interagirem com o subsistema sem precisar conhecer todos os detalhes internos.

**Caso de uso**

Um exemplo comum de uso do padrão Façade é em sistemas de bibliotecas gráficas, onde uma única interface simples pode ser fornecida para realizar operações gráficas complexas, como desenhar formas, adicionar texto ou aplicar efeitos visuais. A Façade encapsularia as chamadas de métodos e a lógica necessária para interagir com o subsistema gráfico subjacente, tornando mais fácil para os desenvolvedores usarem a biblioteca gráfica sem precisar entender todos os detalhes de implementação.

## Proxy

**Resumo**

O padrão Proxy é um padrão estrutural que fornece um substituto ou placeholder para outro objeto, controlando o acesso a esse objeto. Ele é usado quando precisamos controlar ou gerenciar o acesso a um objeto de forma transparente para o cliente.

**Propósito**

O propósito do padrão Proxy é fornecer um substituto ou placeholder para outro objeto para controlar o acesso a ele. Isso pode ser útil para adicionar funcionalidades adicionais, como controle de acesso, lazy loading, cache ou registro de chamadas, sem modificar o código do objeto real.

**Caso de uso**

Um exemplo de uso do padrão Proxy é em um sistema de cache para acesso a dados remotos. O proxy pode ser responsável por verificar se os dados solicitados já estão em cache e, em caso afirmativo, retornar os dados do cache em vez de fazer uma chamada de rede para obter os dados reais. Isso ajuda a reduzir a sobrecarga de rede e melhorar o desempenho do sistema, enquanto mantém a interface de acesso aos dados transparente para o cliente.