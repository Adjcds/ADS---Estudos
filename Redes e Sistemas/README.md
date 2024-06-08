# Guia de Redes e Infraestrutura

Bem-vindo ao Guia de Redes e Infraestrutura! Este repositório contém informações essenciais sobre redes de computadores, infraestrutura de redes e tópicos relacionados. Se você é novo nesse assunto ou quer aprimorar seus conhecimentos, você está no lugar certo.

## Conteúdo

1. [Redes](#redes)
2. [Infraestrutura de Redes e Principais Equipamentos](#infraestrutura-de-redes)
3. [Cabeamento Estruturado](#cabeamento-estruturado)
4. [Modelo OSI e TCP/IP](#modelo-osi-e-tcp-ip)
5. [IPv4 e IPv6](#ipv4-e-ipv6)
6. [Cálculos de Sub-Rede](#cálculos-de-sub-rede)
7. [Domínios e DNS](#domínios-e-dns)
8. [Latência](#latência)
9. [Principais Comandos de Configuração](#principais-comandos-de-configuração)
10. [Segurança](#segurança)
11. [Wireless](#wireless)

Claro! Vou expandir as explicações e adicionar alguns diagramas simples para ilustrar os conceitos de forma mais clara.

### Redes

Uma rede de computadores é um conjunto de dispositivos interconectados que compartilham recursos e informações. As redes podem ser locais (LAN), abrangendo uma área geográfica limitada, ou estendidas (WAN), cobrindo distâncias maiores.

Exemplo de diagrama:

```
     Dispositivo A       Dispositivo B
        (PC)               (Impressora)
          |                     |
          |---------------------|
                  LAN
```

### Infraestrutura de Redes e Principais Equipamentos

A infraestrutura de redes é composta por equipamentos como switches, roteadores, firewalls e access points. Esses dispositivos desempenham funções específicas na rede, como direcionar o tráfego, filtrar pacotes e fornecer conectividade sem fio.

Exemplo de diagrama:

```
        Dispositivos de Rede
   [Switch] ---- [Router] ---- [Firewall] ---- [Access Point]
```

### Cabeamento Estruturado

O cabeamento estruturado é um sistema padronizado de cabos e conectores usado para conectar dispositivos de rede. Ele facilita a organização e o gerenciamento dos cabos, tornando a manutenção e a expansão da rede mais simples.

Exemplo de diagrama:

```
        Patch Panel
           |  |  |
           |  |  |
   [Switch] [Switch] [Switch]
      |         |         |
Computador  Computador  Impressora
```

### Modelo OSI e TCP/IP

O modelo OSI (Open Systems Interconnection) e o modelo TCP/IP (Transmission Control Protocol/Internet Protocol) são estruturas conceituais que descrevem como os dados são transmitidos em uma rede. Ambos os modelos dividem o processo de comunicação em camadas, cada uma com funções específicas.

Exemplo de diagrama do modelo OSI:

```
    7. Aplicação
    6. Apresentação
    5. Sessão
    4. Transporte
    3. Rede
    2. Enlace de Dados
    1. Física
```

Exemplo de diagrama do modelo TCP/IP:

```
         Aplicação
         Transporte
           Internet
        Interface de Rede
```

### IPv4 e IPv6

O IPv4 e o IPv6 são protocolos de comunicação usados para identificar dispositivos em uma rede. O IPv4 utiliza endereços de 32 bits, enquanto o IPv6 utiliza endereços de 128 bits, oferecendo um espaço de endereçamento muito maior.

Exemplo de endereço IPv4: `192.168.0.1`

Exemplo de endereço IPv6: `2001:0db8:85a3:0000:0000:8a2e:0370:7334`

### Cálculos de Sub-Rede

Os cálculos de sub-rede são usados para dividir uma rede em sub-redes menores, permitindo uma melhor gestão dos endereços IP disponíveis e otimizando o tráfego na rede.

Exemplo de cálculo de sub-rede:

Para uma rede com prefixo IPv4 /24 (máscara de sub-rede padrão), podemos dividir em várias sub-redes com base nos requisitos de endereçamento.

Suponha que tenhamos uma rede com o endereço IP `192.168.0.0` e máscara de sub-rede `/30` (ou `255.255.255.252` em formato decimal). Queremos dividir essa rede em sub-redes menores.

1. **Identificar o Endereço de Rede Original**:
   - Endereço IP: `192.168.0.0`
   - Máscara de Sub-Rede: `/30` (ou `255.255.255.252`)

```
Rede Original:     192.168.0.0
Máscara de Sub-Rede: 255.255.255.252 (/30)
```

2. **Determinar o Número de Bits para a Sub-Rede**:
   - Queremos criar 4 sub-redes, então precisamos de pelo menos 2 bits para a sub-rede (2^2 = 4 sub-redes).

3. **Calcular a Nova Máscara de Sub-Rede**:
   - Com 2 bits para a sub-rede, teremos 30 bits para hosts (32 - 2 = 30).
   - Isso resulta em uma máscara de sub-rede `/30` (ou `255.255.255.252`).

```
Nova Máscara de Sub-Rede: 255.255.255.252 (/30)
```

4. **Determinar o Número de Hosts por Sub-Rede**:
   - Com uma máscara de sub-rede `/30`, temos 2^2 - 2 = 2 hosts disponíveis em cada sub-rede (menos 2 para o endereço de rede e o endereço de broadcast).

5. **Identificar os Limites de Cada Sub-Rede**:
   - Cada sub-rede terá 4 endereços IP:
     - Endereço de Rede
     - Primeiro Host
     - Último Host
     - Endereço de Broadcast

```
Sub-Rede 1:
  Endereço de Rede:      192.168.0.0
  Primeiro Host:         192.168.0.1
  Último Host:           192.168.0.2
  Endereço de Broadcast: 192.168.0.3

Sub-Rede 2:
  Endereço de Rede:      192.168.0.4
  Primeiro Host:         192.168.0.5
  Último Host:           192.168.0.6
  Endereço de Broadcast: 192.168.0.7

Sub-Rede 3:
  Endereço de Rede:      192.168.0.8
  Primeiro Host:         192.168.0.9
  Último Host:           192.168.0.10
  Endereço de Broadcast: 192.168.0.11

Sub-Rede 4:
  Endereço de Rede:      192.168.0.12
  Primeiro Host:         192.168.0.13
  Último Host:           192.168.0.14
  Endereço de Broadcast: 192.168.0.15
```

Essa divisão resulta em 4 sub-redes dentro da rede original `192.168.0.0`, cada uma com 2 endereços disponíveis para hosts. Isso permite uma alocação eficiente de endereços IP e segmentação lógica da rede conforme necessário.

### Domínios e DNS

Um domínio é um nome exclusivo que identifica uma entidade na internet. O DNS (Domain Name System) é um sistema que traduz nomes de domínio em endereços IP, facilitando a navegação na web.

Exemplo de diagrama:

```
              DNS
          /          \
   example.com   192.0.2.1
```

### Latência

A latência é o atraso experimentado durante a transmissão de dados em uma rede. Pode ser causada por vários fatores, como a distância física entre os dispositivos e a congestão da rede.

Exemplo de latência em uma videochamada:

A latência pode resultar em atrasos na transmissão de áudio e vídeo, fazendo com que as pessoas na chamada não se ouçam em tempo real.

### Principais Comandos de Configuração

Existem diversos comandos de configuração utilizados para configurar e gerenciar dispositivos de rede. Esses comandos variam de acordo com o fabricante e o tipo de dispositivo.

Exemplo de comando de configuração:

No Cisco IOS, o comando `show ip interface brief` exibe informações sobre interfaces de rede em um roteador Cisco.

### Segurança

A segurança da rede é crucial para proteger os dados e os recursos contra acessos não autorizados e ataques cibernéticos. Isso inclui medidas como firewalls, criptografia e políticas de acesso.

Exemplo de firewall de próxima geração:

Um firewall de próxima geração pode inspecionar o tráfego de rede em tempo real e bloquear ameaças conhecidas, protegendo a rede contra ataques.

### Wireless

Redes sem fio permitem a conexão de dispositivos à rede sem a necessidade de cabos físicos. Elas são amplamente utilizadas em ambientes empresariais e domésticos.

Exemplo de diagrama de rede sem fio:

```
               Access Point
                  |
        [Dispositivos sem Fio]
```

Espero que esses diagramas e explicações adicionais ajudem a elucidar os conceitos de redes e infraestrutura de forma mais clara. Se precisar de mais informações ou tiver dúvidas específicas, fique à vontade para perguntar!