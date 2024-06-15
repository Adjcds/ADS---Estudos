# Introdução ao Terraform

Bem-vindo(a) ao guia de introdução ao **Terraform**, uma ferramenta de Infraestrutura como Código (IaC) desenvolvida pela HashiCorp. Este repositório contém explicações sobre os principais conceitos e exercícios de fixação para ajudá-lo a entender e aplicar os fundamentos do Terraform.

## Sumário

1. [Introdução ao Terraform](#introdução-ao-terraform)
2. [Workflow e Lifecycle do Terraform](#workflow-e-lifecycle-do-terraform)
3. [Providers](#providers)
4. [Block Types do Terraform](#block-types-do-terraform)
5. [Funções](#funções)
6. [Statefile](#statefile)
7. [Módulos](#módulos)
8. [Boas Práticas](#boas-práticas)
9. [Edições Terraform](#edições-terraform)
10. [Encerramento](#encerramento)

---

## Introdução ao Terraform

### O que é Terraform?

Terraform é uma ferramenta de IaC (Infrastructure as Code) que permite definir e provisionar infraestrutura por meio de arquivos de configuração legíveis e versionáveis. Com o Terraform, você pode gerenciar qualquer coisa, desde serviços de baixo nível, como instâncias de computação, armazenamento e rede, até componentes de nível superior, como DNS, funcionalidades de monitoramento e provedores de serviços.

### Exercícios de Fixação I

**Questão 1: O que é Terraform?**  
Resposta: Ferramenta de IaC (Infraestrutura como Código).

**Explicação:** Terraform permite a definição de infraestrutura usando código, o que facilita a automação e versionamento, garantindo consistência e reprodutibilidade nos ambientes de TI.

**Questão 2: O Terraform foi escrito em qual linguagem?**  
Resposta: Go.

**Explicação:** A escolha da linguagem Go permite que o Terraform tenha alta performance e seja facilmente portável para diferentes sistemas operacionais, aproveitando as vantagens de compilação nativa e concorrência eficiente.

**Questão 3: Qual é a empresa mantenedora do Terraform?**  
Resposta: HashiCorp.

**Explicação:** HashiCorp é conhecida por desenvolver várias ferramentas de gerenciamento de infraestrutura, e o Terraform é uma de suas principais soluções para IaC, sendo amplamente adotado em diversas indústrias.

## Workflow e Lifecycle do Terraform

### Workflow do Terraform

O fluxo de trabalho básico do Terraform consiste em três fases principais:

1. **Write**: Escreva a configuração de infraestrutura em arquivos .tf usando a linguagem HCL (HashiCorp Configuration Language).
2. **Plan**: Gere e reveja um plano de execução para alinhar o estado desejado da infraestrutura com o estado atual.
3. **Apply**: Aplique as mudanças necessárias para atingir o estado desejado da infraestrutura.

### Lifecycle do Terraform

O ciclo de vida dos recursos gerenciados pelo Terraform envolve criação, atualização e destruição de infraestrutura com comandos como `terraform apply` e `terraform destroy`.

### Exercícios de Fixação II

**Questão 1: Como é realizada a comunicação do Terraform com o Provider?**  
Resposta: Via API Rest.

**Explicação:** Os providers utilizam APIs REST para interagir com os serviços dos provedores de nuvem ou outras plataformas, permitindo que o Terraform gerencie os recursos de forma programática.

**Questão 2: Quais são as fases que compõem o Workflow do Terraform?**  
Resposta: Write, Plan e Apply.

**Explicação:** Essas fases estruturam o processo de definição e aplicação da infraestrutura, garantindo que as mudanças sejam planejadas e executadas de forma controlada.

**Questão 3: Qual é o comando que apaga os recursos criados com o Terraform?**  
Resposta: `terraform destroy`.

**Explicação:** O comando `terraform destroy` remove todos os recursos gerenciados pelo Terraform, garantindo uma limpeza completa do ambiente conforme a configuração especificada.

## Providers

### O que são Providers?

Providers são plugins que o Terraform utiliza para interagir com APIs de provedores de serviços, como AWS, Azure, Google Cloud, entre outros. Cada provider tem seu próprio conjunto de recursos que pode ser gerenciado pelo Terraform.

### Exercícios de Fixação III

**Questão 1: O que são os Providers do Terraform?**  
Resposta: São plugins que o Terraform utiliza para gerenciar as chamadas para a API do provedor de recursos.

**Explicação:** Os providers são essenciais para que o Terraform possa gerenciar recursos de diferentes plataformas, abstraindo as chamadas de API necessárias para criar, atualizar ou deletar infraestrutura.

**Questão 2: Onde é possível encontrar os plugins disponíveis do Terraform?**  
Resposta: No site do [Terraform Registry](https://registry.terraform.io/).

**Explicação:** O Terraform Registry é o repositório central para todos os providers e módulos disponíveis, facilitando a descoberta e utilização desses componentes nas configurações do Terraform.

**Questão 3: Quem garante a segurança dos recursos disponibilizados pelo Terraform Registry?**  
Resposta: A segurança dos recursos é regulada e homologada pela HashiCorp, que faz um rígido controle junto aos provedores.

**Explicação:** A HashiCorp realiza verificações de segurança e conformidade para garantir que os providers disponíveis no Terraform Registry atendam aos padrões exigidos.

## Block Types do Terraform

### O que são Block Types?

Os Block Types no Terraform são estruturas de configuração usadas para definir os elementos que compõem a infraestrutura. Os principais tipos de blocos incluem:

- **provider**: Define os provedores a serem usados.
- **resource**: Define os recursos a serem gerenciados.
- **data**: Consulta dados existentes.
- **output**: Define as saídas que devem ser exibidas.
- **module**: Reutiliza configurações.
- **variable**: Define variáveis de entrada.
- **locals**: Define variáveis locais.

### Exercícios de Fixação IV

**Questão 1: Qual é a extensão de um arquivo Terraform?**  
Resposta: .tf.

**Explicação:** Arquivos Terraform têm a extensão `.tf`, o que facilita a identificação e manipulação das configurações de infraestrutura.

**Questão 2: Quais são os BlockTypes do Terraform?**  
Resposta: provider, resource, data, input, output, modules e settings.

**Explicação:** Esses blocos estruturam a configuração do Terraform, permitindo definir provedores, recursos, variáveis, módulos, entre outros elementos necessários para gerenciar a infraestrutura.

**Questão 3: O que é esperado no BlockType Settings?**  
Resposta: Configurações que o Terraform utilizará, como configurações do Terraform Cloud e as versões e origem dos Providers.

**Explicação:** O bloco `settings` especifica configurações gerais do Terraform, como a utilização do Terraform Cloud e os requisitos de versão dos providers.

## Funções

### O que são Funções Built-in?

As funções built-in do Terraform são funções prontas que podem ser utilizadas para transformar e combinar valores. Elas ajudam a manipular strings, listas e outras estruturas de dados dentro dos arquivos de configuração do Terraform.

### Exercícios de Fixação V

**Questão 1: O que são as funções Built-in do Terraform?**  
Resposta: São funções prontas do Terraform que são utilizadas para transformar e combinar valores.

**Explicação:** Essas funções facilitam a manipulação de dados dentro dos arquivos de configuração, tornando as configurações mais flexíveis e poderosas.

**Questão 2: Qual desses não é um grupo que contempla funções Built-in do Terraform?**  
Resposta: Transform Functions.

**Explicação:** Embora existam várias funções built-in no Terraform, "Transform Functions" não é um grupo reconhecido de funções. Em vez disso, as funções são categorizadas de outras maneiras, como String Functions, Numeric Functions, entre outras.

**Questão 3: Qual é o objetivo da função Join?**  
Resposta: A função join recebe um separador e uma lista como parâmetro e produz uma string concatenando o valor dos elementos com o separador informado.

**Explicação:** A função `join` é usada para combinar elementos de uma lista em uma única string, separando os elementos com um delimitador especificado, o que é útil para formatar listas de valores.

## Statefile

### O que é o Statefile?

O Statefile (`terraform.tfstate`) é um arquivo utilizado pelo Terraform para armazenar o estado atual da infraestrutura gerenciada. Ele é essencial para o funcionamento correto do Terraform, pois mantém um mapeamento dos recursos criados, modificados ou destruídos.

### Exercícios de Fixação VI

**Questão 1: Qual é o arquivo que o Terraform utiliza para gerenciar o estado dos recursos?**  
Resposta: `terraform.tfstate`.

**Explicação:** O arquivo `terraform.tfstate` armazena o estado da infraestrutura gerenciada, permitindo ao Terraform saber quais recursos existem e como estão configurados.

**Questão 2: É recomendado alterar o arquivo `terraform.tfstate` do Terraform?**  
Resposta: Não. Esse arquivo é o responsável pelo gerenciamento de estado do Terraform, qualquer alteração manual pode quebrar o gerenciamento de estado.

**Explicação:** Alterar manualmente o arquivo `terraform.tfstate` pode causar inconsistências e problemas no gerenciamento de infraestrutura, pois o Terraform pode perder a referência correta dos recursos.

**Questão 3: O arquivo de gerenciamento de estado do Terraform utiliza qual extensão?**  
Resposta: `.tfstate`.

**Explicação:** A extensão `.tfstate` identifica o arquivo de estado do Terraform, diferenciando-o dos arquivos de configuração (`.tf`).

## Módulos

### O que são Módulos no Terraform?

Os módulos no Terraform são blocos reutilizáveis

 de configuração que permitem a criação de infraestrutura de forma modular. Eles ajudam a organizar e estruturar o código, facilitando a reutilização e a manutenção.

### Exercícios de Fixação VII

**Questão 1: O que é o módulo no Terraform e como ele funciona?**  
Resposta: O Módulo é um bloco reutilizável de configuração do Terraform. Ele permite a criação de infraestrutura de forma modular.

**Explicação:** Módulos encapsulam a configuração do Terraform, permitindo reutilização e organização do código, o que facilita a manutenção e padronização da infraestrutura.

**Questão 2: Quais são os benefícios na utilização de módulos no Terraform?**  
Resposta: Reutilização de configuração, padronização de código e fácil compartilhamento.

**Explicação:** Módulos promovem boas práticas de desenvolvimento, facilitando a reutilização, padronização e compartilhamento de configurações, o que aumenta a eficiência e consistência na gestão de infraestrutura.

**Questão 3: Como funciona a relação entre módulos no Terraform?**  
Resposta: A utilização de módulos no Terraform permite que um módulo utilize o outro para realizar a criação de recursos estabelecendo uma relação de root e child.

**Explicação:** Módulos podem ser aninhados, permitindo a composição de módulos menores em módulos maiores, criando uma hierarquia que facilita a organização e reutilização de recursos.

## Boas Práticas

### Exercícios de Fixação VIII

**Questão 1: Quais são as edições disponíveis do Terraform?**  
Resposta: Terraform Free, Cloud e Enterprise.

**Explicação:** O Terraform está disponível em várias edições para atender diferentes necessidades, desde a versão gratuita para uso local até as versões Cloud e Enterprise para soluções mais avançadas e gerenciadas.

**Questão 2: Sobre o Terraform Cloud é correto afirmar que:**  
Resposta: A edição Cloud do Terraform comporta todas as vantagens do Open Source e inclui uma interface gráfica muito prática e intuitiva que ajuda no desenvolvimento do Terraform.

**Explicação:** O Terraform Cloud oferece uma interface web intuitiva e adiciona funcionalidades como colaboração em equipe, gestão de estados remotos e execução de planos automatizados.

**Questão 3: Qual a diferença das edições Cloud e Enterprise?**  
Resposta: A Edição Enterprise do Terraform é uma implantação autogerenciada pelo próprio cliente, enquanto a Edição Cloud é hospedada e mantida pela HashiCorp.

**Explicação:** A versão Enterprise é gerenciada pelo próprio cliente, oferecendo maior controle sobre a infraestrutura, enquanto a versão Cloud é gerenciada pela HashiCorp, proporcionando facilidade de uso e manutenção.

## Edições Terraform

### Exercícios de Fixação IX

**Questão 1: Entre as boas práticas do Terraform, é recomendado segmentar os arquivos na seguinte estrutura:**  
Resposta: É uma boa prática segmentar os arquivos em: Modules, Variables, Resources e Outputs.

**Explicação:** Segmentar os arquivos de configuração em módulos, variáveis, recursos e saídas facilita a organização, manutenção e reutilização do código, promovendo boas práticas de desenvolvimento.

**Questão 2: Você recebe códigos Terraform de um colega e precisa incrementar a sua parte do projeto para subir em produção, no entanto o arquivo não está seguindo a formatação correta. Qual comando Terraform auxilia na formatação dos arquivos?**  
Resposta: `terraform fmt`.

**Explicação:** O comando `terraform fmt` formata automaticamente os arquivos de configuração do Terraform de acordo com os padrões recomendados, garantindo consistência e legibilidade no código.

**Questão 3: Após realizar code review de um código Terraform você encontra uma senha hard coded nas configurações do Terraform, qual é a boa prática para resolver esse problema?**  
Resposta: A recomendação é aplicar arquivos de senhas num cofre de senhas ou então como variáveis de ambiente.

**Explicação:** Armazenar senhas e outras informações sensíveis em um cofre de senhas ou como variáveis de ambiente aumenta a segurança e evita exposição acidental de credenciais.

## Encerramento

### Exercícios de Fixação X

**Questão 1: Em resumo, quais são os benefícios na utilização do Terraform?**  
Resposta: Utilizar infraestrutura como código, automação de serviços, reaproveitamento e padronização de código.

**Explicação:** Terraform oferece benefícios como automação da infraestrutura, reutilização e padronização de configurações, e gerenciamento eficiente de recursos através de código versionável.

**Questão 2: Sua empresa está adotando a estratégia de utilizar multicloud. Por que deveria utilizar Terraform e não os respectivos IaC’s dos provedores Cloud?**  
Resposta: Porque o Terraform é multicloud e agnóstico ao provedor.

**Explicação:** Terraform pode gerenciar recursos em múltiplos provedores de nuvem de maneira unificada, permitindo maior flexibilidade e evitando dependência de um único fornecedor.

**Questão 3: Sua equipe está iniciando o desenvolvimento de um novo projeto com Kubernetes, como o Terraform pode auxiliar nesse processo?**  
Resposta: O Terraform disponibiliza um provider exclusivo para projetos Kubernetes.

**Explicação:** O provider Kubernetes do Terraform permite gerenciar recursos de Kubernetes através de configurações de Terraform, facilitando a integração e automação de infraestrutura em ambientes de contêineres.

Este guia é parte do curso de DevOps do Santander Coders 2024 em parceria com a Ada Tech. Para mais informações, consulte a documentação oficial e os recursos de aprendizado disponíveis.

**Autor:** [AdrielleJcds](https://github.com/Adjcds)  
**E-mail:** adrielle.dev@gmail.com  
**Última Atualização:** [14/06/2024]