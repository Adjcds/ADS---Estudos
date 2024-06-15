# Conhecendo sobre Infraestrutura AWS

Bem-vindo(a) ao guia de introdução à **Infraestrutura AWS**. Este repositório contém explicações sobre os principais conceitos e exercícios de fixação para ajudá-lo a entender e aplicar os fundamentos da infraestrutura AWS.

## Sumário

1. [Computação em Nuvem](#computação-em-nuvem)
2. [Infraestrutura Global AWS](#infraestrutura-global-aws)
3. [Alta Disponibilidade e outros conceitos](#alta-disponibilidade-e-outros-conceitos)
4. [Overview AWS](#overview-aws)
5. [Provisionando um Servidor na AWS](#provisionando-um-servidor-na-aws)
6. [Balanceamento de Carga / Elastic Load Balancing](#balanceamento-de-carga--elastic-load-balancing)
7. [Combinando Balanceamento de Carga com Escalabilidade na AWS](#combinando-balanceamento-de-carga-com-escalabilidade-na-aws)
8. [AWS Well-Architected Framework](#aws-well-architected-framework)
9. [Serviço DNS / Amazon Route 53](#serviço-dns--amazon-route-53)

---

## Computação em Nuvem

### Descrição

A computação em nuvem permite acesso a recursos de computação pela internet, eliminando a necessidade de gerenciamento físico direto de hardware. Isso inclui servidores, armazenamento, bancos de dados, redes, software e muito mais.

### Links para Estudo

- [O que é a computação em nuvem?](https://aws.amazon.com/pt/what-is-cloud-computing/)
- [Resumo dos benefícios](https://aws.amazon.com/pt/application-hosting/benefits/)
- [Modelo de responsabilidade compartilhada](https://aws.amazon.com/pt/compliance/shared-responsibility-model/)
- [Preços da AWS](https://aws.amazon.com/pt/pricing/)
- [AWS Named as a Leader for the 11th Consecutive Year in 2021 Gartner Magic Quadrant](https://aws.amazon.com/pt/blogs/aws/aws-named-as-a-leader-for-the-11th-consecutive-year-in-2021-gartner-magic-quadrant-for-cloud-infrastructure-platform-services-cips/)

### Exercícios de Fixação I

**Questão 1: O que é a computação em nuvem?**  
Resposta: Computação em nuvem é a entrega de serviços de computação sob demanda pela internet, oferecendo armazenamento, processamento e recursos de TI sem a necessidade de gerenciamento direto.

**Explicação:** A computação em nuvem permite que usuários e empresas acessem recursos de TI conforme necessário, sem a necessidade de possuir e manter a infraestrutura física, oferecendo escalabilidade e flexibilidade.

**Questão 2: Quais são alguns dos benefícios da computação em nuvem listados pela AWS?**  
Resposta: Escalabilidade, custo-benefício, flexibilidade, segurança, e inovação.

**Explicação:** A computação em nuvem oferece vários benefícios como a capacidade de escalar recursos rapidamente, pagar apenas pelo que é utilizado, flexibilidade para se adaptar às necessidades do negócio, segurança robusta, e acesso a tecnologias inovadoras.

## Infraestrutura Global AWS

### Descrição

A infraestrutura global da AWS é composta por regiões e zonas de disponibilidade distribuídas ao redor do mundo, oferecendo alta disponibilidade, escalabilidade e segurança.

### Links para Estudo

- [Infraestrutura global da AWS](https://aws.amazon.com/pt/about-aws/global-infrastructure/)
- [Regiões e zonas de disponibilidade](https://aws.amazon.com/pt/about-aws/global-infrastructure/regions_az/)
- [AWS Local Zones](https://aws.amazon.com/pt/about-aws/global-infrastructure/localzones/)
- [Perguntas frequentes sobre o AWS Local Zones](https://aws.amazon.com/pt/about-aws/global-infrastructure/localzones/faqs/)

### Exercícios de Fixação II

**Questão 1: O que são regiões e zonas de disponibilidade na AWS?**  
Resposta: Regiões são áreas geográficas separadas que contêm múltiplas zonas de disponibilidade. As zonas de disponibilidade são locais físicos discretos dentro de uma região que são isolados umas das outras para garantir resiliência.

**Explicação:** As regiões e zonas de disponibilidade da AWS garantem que os serviços e dados estejam disponíveis e seguros, mesmo em caso de falhas em uma única zona, proporcionando alta disponibilidade e tolerância a falhas.

**Questão 2: O que são AWS Local Zones?**  
Resposta: AWS Local Zones são locais físicos onde a AWS implanta infraestruturas de computação, armazenamento e outros serviços para fornecer latência ultrabaixa para aplicações específicas.

**Explicação:** AWS Local Zones ajudam a trazer serviços de computação e armazenamento mais próximos dos usuários finais, reduzindo a latência e melhorando o desempenho de aplicações sensíveis ao tempo.

## Alta Disponibilidade e outros conceitos

### Descrição

Alta disponibilidade e resiliência são essenciais para garantir a continuidade de negócios. A AWS oferece diversas ferramentas e práticas para alcançar esses objetivos.

### Links para Estudo

- [Continuidade de negócios na AWS: Disponibilidade e resiliência](https://aws.amazon.com/pt/blogs/aws-brasil/continuidade-de-negocios-na-aws-disponibilidade-e-resiliencia/)
- [Regiões e zonas de disponibilidade](https://aws.amazon.com/pt/about-aws/global-infrastructure/regions_az/)

### Exercícios de Fixação III

**Questão 1: O que é alta disponibilidade na AWS?**  
Resposta: Alta disponibilidade é a capacidade de um sistema permanecer operacional e acessível por um longo período de tempo, minimizando o tempo de inatividade.

**Explicação:** Alta disponibilidade é alcançada através do uso de múltiplas zonas de disponibilidade e regiões, permitindo que serviços continuem operando mesmo em caso de falhas de infraestrutura.

**Questão 2: Como a AWS garante a resiliência dos seus serviços?**  
Resposta: Através do uso de múltiplas zonas de disponibilidade, replicação de dados, e práticas robustas de recuperação de desastres.

**Explicação:** A resiliência na AWS é garantida pela distribuição dos serviços e dados em várias zonas de disponibilidade, o que permite a continuidade dos serviços mesmo em caso de falhas significativas.

## Overview AWS

### Descrição

A AWS oferece uma vasta gama de serviços e ferramentas para gerenciamento de recursos em nuvem, desde a interface de linha de comando (CLI) até consoles de gerenciamento e SDKs.

### Links para Estudo

- [Boas-vindas à documentação do AWS](https://docs.aws.amazon.com/pt_br/)
- [AWS Command Line Interface](https://aws.amazon.com/pt/cli/)
- [Explorador de Custos da AWS](https://aws.amazon.com/pt/aws-cost-management/aws-cost-explorer/)
- [Console de gerenciamento da AWS](https://aws.amazon.com/pt/console/)
- [O que é um SDK?](https://aws.amazon.com/pt/what-is/sdk/)

### Exercícios de Fixação IV

**Questão 1: O que é a AWS CLI?**  
Resposta: AWS Command Line Interface (CLI) é uma ferramenta que permite gerenciar serviços AWS a partir da linha de comando.

**Explicação:** A AWS CLI facilita a interação com os serviços AWS diretamente do terminal, permitindo a automação e script de tarefas rotineiras de gerenciamento de infraestrutura.

**Questão 2: O que é o AWS Cost Explorer?**  
Resposta: O AWS Cost Explorer é uma ferramenta que permite visualizar e analisar os custos e uso da AWS.

**Explicação:** O AWS Cost Explorer ajuda a entender onde e como os recursos da AWS estão sendo utilizados, fornecendo insights para otimizar custos e gerenciar o orçamento de forma eficaz.

## Provisionando um Servidor na AWS

### Descrição

Provisionar um servidor na AWS envolve a escolha do tipo de instância EC2 adequado às suas necessidades e configurar os recursos através do AWS Marketplace.

### Links para Estudo

- [Amazon EC2](https://aws.amazon.com/pt/ec2/instance-types/)
- [AWS Marketplace](https://aws.amazon.com/pt/partners/aws-marketplace/)
- [Preço sob demanda do Amazon EC2](https://aws.amazon.com/pt/ec2/pricing/on-demand/)

### Exercícios de Fixação V

**Questão 1: O que é uma instância EC2 na AWS?**  
Resposta: Uma instância EC2 é um servidor virtual que pode ser usado para executar aplicações na nuvem AWS.

**Explicação:** As instâncias EC2 oferecem capacidade de computação escalável na AWS, permitindo executar uma variedade de workloads, desde servidores web até aplicações empresariais complexas.

**Questão 2: O que é o AWS Marketplace?**  
Resposta: O AWS Marketplace é uma loja online onde é possível encontrar, comprar e implantar software que roda na AWS.

**Explicação:** O AWS Marketplace facilita o acesso a uma vasta gama de softwares de parceiros da AWS, permitindo a implantação rápida e eficiente de soluções de software na infraestrutura AWS.

## Balanceamento de Carga / Elastic Load Balancing

### Descrição

O balanceamento de carga distribui o tráfego de rede ou aplicação entre várias instâncias para garantir a disponibilidade e escalabilidade de aplicativos.

### Links para Estudo

- [O que é Balanceamento de carga?](https://aws.amazon.com/pt/what-is/load-balancing/)
- [Elastic Load Balancing](

https://aws.amazon.com/pt/elasticloadbalancing/)

### Exercícios de Fixação VI

**Questão 1: O que é Elastic Load Balancing (ELB) na AWS?**  
Resposta: ELB é um serviço que automaticamente distribui o tráfego de entrada de aplicações entre múltiplas instâncias EC2.

**Explicação:** O ELB melhora a tolerância a falhas e a escalabilidade de aplicações ao distribuir automaticamente o tráfego de rede para garantir a disponibilidade e desempenho.

**Questão 2: Quais são os tipos de balanceadores de carga oferecidos pela AWS?**  
Resposta: Application Load Balancer, Network Load Balancer e Classic Load Balancer.

**Explicação:** A AWS oferece diferentes tipos de balanceadores de carga para atender diversas necessidades de aplicativos, desde balanceamento de carga de rede de alto desempenho até balanceamento de carga de aplicações HTTP e HTTPS.

## Combinando Balanceamento de Carga com Escalabilidade na AWS

### Descrição

A combinação de balanceamento de carga com escalabilidade automática (Auto Scaling) permite a criação de aplicativos altamente disponíveis e resilientes.

### Links para Estudo

- [AWS Auto Scaling](https://aws.amazon.com/pt/autoscaling/)

### Exercícios de Fixação VII

**Questão 1: O que é Auto Scaling na AWS?**  
Resposta: Auto Scaling ajusta automaticamente a quantidade de recursos computacionais conforme a demanda varia, mantendo o desempenho e otimizando custos.

**Explicação:** O Auto Scaling permite que aplicações mantenham alta disponibilidade ao ajustar dinamicamente a capacidade computacional em resposta a mudanças na carga de trabalho.

**Questão 2: Como o Auto Scaling trabalha junto com o Elastic Load Balancing?**  
Resposta: Auto Scaling adiciona ou remove instâncias com base em políticas definidas e o Elastic Load Balancing distribui o tráfego para as instâncias em execução.

**Explicação:** A integração do Auto Scaling com o ELB garante que o tráfego seja distribuído eficientemente entre um número apropriado de instâncias, adaptando-se às necessidades da aplicação em tempo real.

## AWS Well-Architected Framework

### Descrição

O AWS Well-Architected Framework ajuda a construir arquiteturas seguras, resilientes, eficientes e otimizadas para o desempenho em nuvem.

### Links para Estudo

- [AWS Well-Architected Framework](https://docs.aws.amazon.com/pt_br/wellarchitected/latest/framework/welcome.html)
- [Os pilares do Framework](https://docs.aws.amazon.com/pt_br/wellarchitected/latest/framework/the-pillars-of-the-framework.html)

### Exercícios de Fixação VIII

**Questão 1: Quais são os cinco pilares do AWS Well-Architected Framework?**  
Resposta: Excelência operacional, segurança, confiabilidade, eficiência de desempenho, e otimização de custos.

**Explicação:** Esses cinco pilares fornecem uma base para criar infraestruturas na AWS que sejam robustas, seguras, eficientes e economicamente viáveis.

**Questão 2: Qual é o objetivo principal do AWS Well-Architected Framework?**  
Resposta: Auxiliar na criação de arquiteturas de nuvem que sejam seguras, resilientes, de alta performance e eficientes em termos de custo.

**Explicação:** O framework oferece orientações e melhores práticas para construir e operar cargas de trabalho confiáveis e seguras na nuvem AWS, alinhando as necessidades do negócio com a infraestrutura de TI.

## Serviço DNS / Amazon Route 53

### Descrição

O Amazon Route 53 é um serviço DNS escalável e de alta disponibilidade que ajuda a gerenciar a direção do tráfego na web.

### Links para Estudo

- [Registro de novos domínios](https://registro.br/ajuda/registro-de-novos-dominios/o-que-e-um-nome-de-dominio/)
- [Amazon Route 53](https://aws.amazon.com/pt/route53/)
- [O que é DNS?](https://tecnoblog.net/responde/o-que-e-dns/)
- [Registrar e gerenciar novos domínios com o Amazon Route 53](https://docs.aws.amazon.com/pt_br/Route53/latest/DeveloperGuide/registrar.html)

### Exercícios de Fixação IX

**Questão 1: O que é DNS?**  
Resposta: DNS (Domain Name System) é um sistema que traduz nomes de domínio legíveis por humanos em endereços IP numéricos necessários para localizar e identificar serviços de computador e dispositivos com os protocolos de rede subjacentes.

**Explicação:** O DNS facilita a navegação na internet, permitindo que usuários acessem sites através de nomes de domínio ao invés de memorizar endereços IP.

**Questão 2: O que é o Amazon Route 53?**  
Resposta: Amazon Route 53 é um serviço de DNS web escalável e de alta disponibilidade que roteia o tráfego dos usuários para aplicativos da AWS e fora da AWS.

**Explicação:** O Amazon Route 53 gerencia a tradução de nomes de domínio em endereços IP e pode ser usado para gerenciar registros DNS para aplicações em nuvem e servidores on-premises.

Este guia é parte do curso de DevOps do Santander Coders 2024 em parceria com a Ada Tech. Para mais informações, consulte a documentação oficial e os recursos de aprendizado disponíveis.

**Autor:** [AdrielleJcds](https://github.com/Adjcds)  
**E-mail:** adrielle.dev@gmail.com  
**Última Atualização:** [14/06/2024]