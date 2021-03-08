# getupix_test

Algumas decisões importantes a serem notadas:

Todos os IPs estão válidos para acessarem o banco de dados na nuvem.
Para rodar, basta instalar os requirements no arquivo de texto, rodar o setup.py e então o app.py.
Está configurado para ficar em desenvolvimento.

> Eu não utilizei MongoDB na minha máquina local, e sim a versão Cloud.
O motivo é simples na verdade - eu realmente quis utilizar o MongoDB Atlas, a opção cloud do mongo.
Gosto bastante, mais prático, mais rápido, sem custo pra testar, e é mais performático para projetos quando se tem um computador fraco.
O código pode ser facilmente adaptado pra uma versão local do mongo somente alterando o IP para local e rodando o script de configuração localmente.

> Não utilizei docker. 
Mesma razão do motivo acima, meu computador não é dos melhores, e mesmo eu utilizando um Fedora 33 e sabendo utilizar bem o sistema, ainda sou limitado por hardware. 

> Evitei utilizar coisas das quais não tenho muita noção.
Por exemplo, Django é um bom framework, mas sinceramente, não curto. Flask pra mim é mais interessante e prático, e combina melhor com aplicações voltadas a ciência de dados e machine learning.
