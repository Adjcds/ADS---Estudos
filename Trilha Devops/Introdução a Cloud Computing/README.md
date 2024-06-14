# README: Guia sobre Introdução a Cloud Computing

## Sumário
1. [Apresentação e histórico](#apresentação-e-histórico)
2. [Cloud pública x privada e principais provedores](#cloud-pública-x-privada-e-principais-provedores)
3. [Modelos IaaS, PaaS, SaaS e Serverless](#modelos-iaas-paas-saas-e-serverless)
4. [Principais serviços - Parte 1](#principais-serviços---parte-1)
5. [Principais serviços - Parte 2](#principais-serviços---parte-2)
6. [Arquitetura para Cloud](#arquitetura-para-cloud)
7. [Introdução à infraestrutura como código](#introdução-à-infraestrutura-como-código)
8. [Introdução ao deployment em Cloud e esteiras de CI/CD](#introdução-ao-deployment-em-cloud-e-esteiras-de-cicd)
9. [Introdução à segurança em Cloud](#introdução-à-segurança-em-cloud)
10. [Revisão geral e conclusão](#revisão-geral-e-conclusão)

## Apresentação e histórico

### O que é Cloud Computing?

Cloud Computing, ou computação em nuvem, refere-se à entrega de serviços de computação—como servidores, armazenamento, bancos de dados, rede, software, análise e inteligência—pela Internet ("a nuvem"). Ela permite que as empresas acessem recursos sob demanda, paguem conforme o uso e escalem facilmente seus serviços.

### Histórico

A ideia de Cloud Computing remonta aos anos 1960, com a visão de John McCarthy de que a computação seria fornecida como um serviço público. No entanto, foi apenas no início dos anos 2000 que a computação em nuvem se tornou prática com o lançamento de serviços como Amazon Web Services (AWS) em 2006.

## Cloud pública x privada e principais provedores

### Cloud Pública

Cloud pública é um ambiente de nuvem onde os recursos são disponibilizados ao público pela Internet por um provedor de serviços. Exemplos incluem AWS, Microsoft Azure e Google Cloud Platform (GCP).

### Cloud Privada

Cloud privada é um ambiente de nuvem dedicado a uma única organização, oferecendo maior controle e segurança. Pode ser hospedada no data center da organização ou em uma nuvem privada gerenciada por terceiros.

### Principais Provedores

1. **Amazon Web Services (AWS):** Oferece uma vasta gama de serviços em nuvem, incluindo IaaS, PaaS e SaaS.
2. **Microsoft Azure:** Integra-se bem com produtos Microsoft e oferece serviços abrangentes de nuvem.
3. **Google Cloud Platform (GCP):** Conhecido por seus serviços de análise e machine learning.

## Modelos IaaS, PaaS, SaaS e Serverless

### IaaS (Infrastructure as a Service)

Proporciona infraestrutura virtualizada, como servidores, armazenamento e rede. Exemplos: Amazon EC2, Google Compute Engine.

### PaaS (Platform as a Service)

Oferece uma plataforma que permite aos desenvolvedores criar, testar e implantar aplicações sem gerenciar a infraestrutura subjacente. Exemplos: Google App Engine, Heroku.

### SaaS (Software as a Service)

Entrega aplicações pela Internet como um serviço. Exemplos: Google Workspace, Microsoft Office 365.

### Serverless

Permite aos desenvolvedores construir e executar aplicações sem gerenciar servidores. Exemplos: AWS Lambda, Google Cloud Functions.

## Principais serviços - Parte 1

### Computação

- **AWS EC2:** Instâncias de máquinas virtuais escaláveis.
- **Azure Virtual Machines:** Máquinas virtuais na nuvem.
- **Google Compute Engine:** Instâncias de VMs com desempenho personalizado.

### Armazenamento

- **Amazon S3:** Armazenamento de objetos com alta durabilidade.
- **Azure Blob Storage:** Armazenamento de objetos para grandes quantidades de dados não estruturados.
- **Google Cloud Storage:** Armazenamento de objetos unificado.

### Bancos de Dados

- **Amazon RDS:** Serviço de banco de dados relacional gerenciado.
- **Azure SQL Database:** Banco de dados SQL como serviço.
- **Google Cloud SQL:** Banco de dados relacional gerenciado.

## Principais serviços - Parte 2

### Redes

- **Amazon VPC:** Serviço de rede privada virtual.
- **Azure Virtual Network:** Redes virtuais isoladas.
- **Google Virtual Private Cloud (VPC):** Redes virtuais globais.

### Análise de Dados

- **Amazon Redshift:** Data warehouse em nuvem.
- **Azure Synapse Analytics:** Análise de dados em larga escala.
- **Google BigQuery:** Armazenamento e análise de dados.

### Machine Learning

- **Amazon SageMaker:** Construção, treinamento e implantação de modelos de machine learning.
- **Azure Machine Learning:** Plataforma para machine learning.
- **Google AI Platform:** Serviços de machine learning.

## Arquitetura para Cloud

### Principais Considerações

- **Escalabilidade:** Habilidade de aumentar ou diminuir recursos conforme a demanda.
- **Resiliência:** Capacidade de se recuperar de falhas.
- **Segurança:** Implementação de práticas e ferramentas para proteger dados e recursos.

### Exemplos de Arquiteturas

- **Microservices:** Divisão de aplicações em pequenos serviços independentes.
- **Serverless:** Uso de funções como serviço (FaaS) para construir aplicações sem gerenciar servidores.

## Introdução à infraestrutura como código

### O que é Infraestrutura como Código (IaC)?

IaC é o processo de gerenciar e provisionar recursos de TI por meio de scripts de configuração em vez de processos manuais. Ferramentas populares incluem Terraform e AWS CloudFormation.

### Benefícios

- **Automatização:** Reduz o erro humano e aumenta a consistência.
- **Versionamento:** Facilita o controle de versões da infraestrutura.
- **Reprodutibilidade:** Garante que o ambiente de desenvolvimento, teste e produção sejam idênticos.

## Introdução ao deployment em Cloud e esteiras de CI/CD

### Deployment em Cloud

Implantar aplicações em ambientes de nuvem envolve o uso de ferramentas e serviços que facilitam a entrega contínua de software. Exemplos incluem AWS CodeDeploy, Azure DevOps, e Google Cloud Deployment Manager.

### CI/CD (Continuous Integration/Continuous Deployment)

CI/CD é uma prática de desenvolvimento que envolve a integração contínua de código e a entrega contínua de software. Ferramentas populares incluem Jenkins, GitLab CI, e CircleCI.

### Benefícios

- **Automação:** Reduz a necessidade de intervenções manuais.
- **Velocidade:** Acelera o processo de entrega de software.
- **Qualidade:** Melhora a qualidade do código por meio de testes automatizados.

## Introdução à segurança em Cloud

### Principais Aspectos

- **Controle de Acesso:** Implementação de políticas de controle de acesso rígidas.
- **Criptografia:** Uso de criptografia para proteger dados em trânsito e em repouso.
- **Monitoramento:** Monitoramento contínuo para detectar e responder a incidentes de segurança.

### Ferramentas e Serviços

- **AWS Identity and Access Management (IAM):** Gerenciamento de usuários e permissões.
- **Azure Security Center:** Central de segurança para gerenciamento de ameaças.
- **Google Cloud Security Command Center:** Ferramenta de monitoramento de segurança.

## Revisão geral e conclusão

### Revisão

Este guia cobriu os seguintes tópicos:

- **Histórico e tipos de cloud computing (pública e privada).**
- **Modelos de serviço em nuvem (IaaS, PaaS, SaaS, Serverless).**
- **Principais serviços oferecidos por AWS, Azure e GCP.**
- **Arquitetura de cloud computing, infraestrutura como código, e deployment em nuvem.**
- **Segurança na nuvem e melhores práticas.**

### Conclusão

A computação em nuvem revolucionou a forma como as empresas gerenciam e escalam suas operações de TI. Compreender os diferentes modelos de serviço, ferramentas e práticas é essencial para aproveitar ao máximo as vantagens da nuvem. Este guia serve como uma introdução aos conceitos básicos, mas recomenda-se aprofundar o conhecimento por meio de cursos e certificações específicas de cada provedor de nuvem.

Este guia é parte do curso de DevOps do Santander Coders 2024 em parceria com a Ada Tech. Para mais informações, consulte a documentação oficial e os recursos de aprendizado disponíveis.

**Autor:** [AdrielleJcds](https://github.com/Adjcds)  
**E-mail:** adrielle.dev@gmail.com  
**Última Atualização:** [14/06/2024]