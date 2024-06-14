# Guia sobre Redes e Sistemas

## Sumário
1. [O que são redes?](#o-que-são-redes)
2. [Infraestrutura de redes e os principais equipamentos](#infraestrutura-de-redes-e-os-principais-equipamentos)
3. [Cabeamento Estruturado](#cabeamento-estruturado)
4. [Modelo OSI e TCP/IP](#modelo-osi-e-tcpip)
5. [IPv4 e IPv6](#ipv4-e-ipv6)
6. [Cálculo de sub-rede](#cálculo-de-sub-rede)
7. [Domínios, DNS e latência](#domínios-dns-e-latência)
8. [Principais comandos de configuração](#principais-comandos-de-configuração)
9. [Segurança](#segurança)
10. [Wireless](#wireless)

## O que são redes?

Redes são sistemas que conectam vários dispositivos, permitindo a troca de dados e recursos entre eles. As redes podem variar em tamanho e complexidade, desde uma simples rede doméstica até redes corporativas e a própria Internet.

## Infraestrutura de redes e os principais equipamentos

### Infraestrutura de redes

A infraestrutura de redes envolve todos os componentes físicos e lógicos necessários para a comunicação entre dispositivos. Isso inclui cabeamento, hardware, software, e protocolos.

### Principais equipamentos

- **Roteadores (Routers)**: Direcionam o tráfego entre diferentes redes.
- **Switches**: Conectam dispositivos dentro de uma mesma rede, encaminhando dados para o destino correto.
- **Pontos de Acesso (Access Points)**: Permitem a conexão de dispositivos sem fio a uma rede cabeada.
- **Modems**: Convertem sinais digitais em analógicos e vice-versa, permitindo a conexão com a Internet.
- **Firewalls**: Protegem a rede contra acessos não autorizados e ataques.

## Cabeamento Estruturado

Cabeamento estruturado é uma metodologia padronizada para instalar o cabeamento de rede. Ele organiza e padroniza a infraestrutura de cabeamento para maximizar o desempenho e facilitar a manutenção. Os principais componentes incluem:

- **Cabos de par trançado (UTP/STP)**: Utilizados em redes Ethernet.
- **Cabos de fibra óptica**: Utilizados para longas distâncias e altas velocidades.
- **Painéis de conexão (Patch Panels)**: Centralizam as conexões de cabos.
- **Racks e gabinetes**: Organizam e protegem os equipamentos de rede.

## Modelo OSI e TCP/IP

### Modelo OSI

O Modelo OSI (Open Systems Interconnection) é um modelo de referência que descreve como os dados são transmitidos através de uma rede. Ele possui 7 camadas:

1. **Física**: Transmissão de bits através de meios físicos.
2. **Enlace de Dados**: Controle de acesso ao meio e detecção de erros.
3. **Rede**: Roteamento de pacotes entre redes.
4. **Transporte**: Transferência confiável de dados.
5. **Sessão**: Gerenciamento de sessões de comunicação.
6. **Apresentação**: Tradução de dados entre formatos.
7. **Aplicação**: Serviços de rede para aplicativos.

### Modelo TCP/IP

O modelo TCP/IP é um conjunto de protocolos que permite a comunicação na Internet. Ele possui 4 camadas:

1. **Camada de Interface de Rede**: Equivalente às camadas Física e Enlace de Dados do OSI.
2. **Camada de Internet**: Equivalente à camada de Rede do OSI.
3. **Camada de Transporte**: Equivalente à camada de Transporte do OSI.
4. **Camada de Aplicação**: Equivalente às camadas de Sessão, Apresentação e Aplicação do OSI.

## IPv4 e IPv6

### IPv4

O IPv4 (Internet Protocol version 4) é a quarta versão do IP e utiliza endereços de 32 bits, permitindo aproximadamente 4,3 bilhões de endereços únicos.

### IPv6

O IPv6 (Internet Protocol version 6) é a sexta versão do IP e utiliza endereços de 128 bits, permitindo uma quantidade quase ilimitada de endereços únicos. Ele foi desenvolvido para substituir o IPv4 devido à escassez de endereços.

## Cálculo de sub-rede

O cálculo de sub-rede envolve dividir uma rede maior em sub-redes menores, otimizando o uso de endereços IP.

### Exemplo

Dada a rede 192.168.1.0/24, podemos dividir em duas sub-redes usando uma máscara de sub-rede /25:

- **Sub-rede 1**: 192.168.1.0/25 (192.168.1.0 - 192.168.1.127)
- **Sub-rede 2**: 192.168.1.128/25 (192.168.1.128 - 192.168.1.255)

## Domínios, DNS e latência

### Domínios

Um domínio é um nome amigável utilizado para identificar um recurso na Internet, como um site (e.g., exemplo.com).

### DNS (Domain Name System)

O DNS é o sistema que traduz nomes de domínio em endereços IP. Ele permite que usuários acessem sites usando nomes em vez de números.

### Latência

Latência é o tempo que um pacote de dados leva para ir de um ponto a outro na rede. Baixa latência é crucial para aplicações em tempo real, como jogos online e videoconferências.

## Principais comandos de configuração

### Windows

- **ipconfig**: Exibe configurações de IP.
- **ping**: Verifica a conectividade com um host.
- **tracert**: Exibe o caminho até um host.

### Linux

- **ifconfig/ip**: Exibe e configura interfaces de rede.
- **ping**: Verifica a conectividade com um host.
- **traceroute**: Exibe o caminho até um host.

### Comandos universais

- **nslookup**: Consulta o DNS.
- **netstat**: Exibe conexões de rede.

## Segurança

A segurança de rede envolve medidas para proteger a integridade, confidencialidade e disponibilidade dos dados e sistemas. Algumas práticas incluem:

- **Firewalls**: Filtram o tráfego de rede.
- **Criptografia**: Protege os dados durante a transmissão.
- **Autenticação**: Verifica a identidade dos usuários.

## Wireless

Redes wireless utilizam ondas de rádio para comunicação entre dispositivos. Componentes principais incluem:

- **Roteadores Wireless**: Fornecem acesso à Internet sem fio.
- **Pontos de Acesso**: Estendem a cobertura de redes sem fio.
- **Segurança Wireless**: WPA3 é o padrão atual para proteger redes wireless.

---

Este guia é parte do curso de DevOps do Santander Coders 2024 em parceria com a Ada Tech. Para mais informações, consulte a documentação oficial e os recursos de aprendizado disponíveis.

**Autor:** [AdrielleJcds](https://github.com/Adjcds)  
**E-mail:** adrielle.dev@gmail.com  
**Última Atualização:** [14/06/2024]