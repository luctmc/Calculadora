# 🧮 Calculadora Moderna

Uma calculadora moderna e interativa desenvolvida em Python com interface gráfica clean e intuitiva, otimizada para proporções de tablet/mobile. Apresenta separação clara entre front-end e back-end, suportando operações matemáticas básicas, funções científicas avançadas e cálculos geométricos.

## 👥 Projeto Desenvolvido pelo Grupo

**Disciplina:** Programação Funcional

**Integrantes:**
- Gabriel Luís Lopes – RA: 2300873
- Lucas Timponi Mercadante Castro – RA: 2304913  
- Pedro Alexandre Dos Santos Chaves – RA: 2301503

## ✨ Funcionalidades

### 🔢 Operações Básicas
- **Adição (+)**: Soma de dois números
- **Subtração (-)**: Diferença entre dois números  
- **Multiplicação (*)**: Produto de dois números
- **Divisão (/)**: Quociente de dois números com proteção contra divisão por zero

### 🔬 Funções Científicas
- **Raiz Quadrada (√)**: Cálculo de raiz quadrada com validação para números negativos
- **Porcentagem (%)**: Cálculo de porcentagem de um número
- **Funções Trigonométricas**: Seno, cosseno e tangente em radianos
- **Conversão de Unidades**: Entre graus e radianos

### 📐 Cálculos Geométricos
- **Área do Círculo**: Usando a fórmula A = πr²
- **Volume da Esfera**: Usando a fórmula V = (4/3)πr³
- **Validação**: Apenas valores positivos para raios

### 🔍 Funções Especiais
- **Verificação Par/Ímpar**: Determina se um número inteiro é par ou ímpar
- **Histórico**: Mantém as últimas 10 operações realizadas
- **Entrada por Teclado**: Suporte completo para teclado físico

## 🚀 Como Usar

### Instalação e Execução

1. **Pré-requisitos**:
   - Python 3.7 ou superior
   - Tkinter (geralmente incluído com Python)

2. **Executar a aplicação**:
   ```bash
   python main.py
   ```

### Atalhos de Teclado

| Tecla | Função |
|-------|--------|
| `0-9` | Números |
| `+`, `-`, `*`, `/` | Operadores básicos |
| `Enter` ou `=` | Calcular resultado |
| `ESC` ou `Delete` | Limpar tudo |
| `Backspace` | Apagar último dígito |
| `.` ou `,` | Ponto decimal |
| `F1` | Raiz quadrada |
| `F2` | Seno |
| `F3` | Cosseno |
| `F4` | Tangente |
| `F5` | Área do círculo |
| `F6` | Volume da esfera |
| `F7` | Verificação par/ímpar |
| `F8` | Porcentagem |

### 📱 Interface da Calculadora

**Layout Horizontal Clean (Estilo Tablet/Mobile):**

A calculadora apresenta um design moderno e compacto com layout horizontal otimizado:

- **Lado Esquerdo**: Calculadora básica completa (números, operadores, display)
- **Lado Direito**: Funcionalidades extras organizadas por categoria
- **Topo**: Histórico compacto das últimas operações

**Características do Design:**
- 📐 **Dimensões**: 800×650 pixels (proporção tablet)
- 🎨 **Tema**: Escuro moderno com cores categorizadas
- 🔤 **Fontes**: Segoe UI (clean e legível)
- 📱 **Responsivo**: Redimensionável mantendo proporções
- ✨ **Efeitos**: Hover e feedback visual em todos os botões

**Organização Visual:**
```
┌──────────────────────────────────────────────────────────────────┐
│  🧮 Calculadora Moderna                              [_][□][X]    │
├──────────────────────────────────────────────────────────────────┤
│  📊 Histórico: [15:30:25] 2 + 3 = 5  [15:30:30] √16 = 4        │
├─────────────────────────────────┬────────────────────────────────┤
│                                 │        Extras                  │
│           0                     │  🔬 Científicas                │
│                                 │  [√ Raiz] [% Porcent]         │
│  Calculadora Básica             │  [sin F2] [cos F3]             │
│  [C] [±] [⌫] [÷]               │                                │
│  [7] [8] [9] [×]               │  📐 Geométricas                │
│  [4] [5] [6] [−]               │  [🔵 Área] [⚫ Vol]            │
│  [1] [2] [3] [+]               │  [🔢 Par/Ímpar] [tan F4]       │
│  [0]     [.] [=]               │                                │
│                                 │  ⌨️ Atalhos                   │
│                                 │  F1:√ F2:sin F3:cos F4:tan     │
│                                 │  F5:Área F6:Vol F7:Par/Ímpar   │
│                                 │  F8:% ESC:Limpar Enter:=       │
└─────────────────────────────────┴────────────────────────────────┘
```

## 🏗️ Arquitetura

A aplicação segue uma arquitetura em camadas bem definida:

### Estrutura de Arquivos

```
calculadora-moderna/
├── main.py                    # Ponto de entrada da aplicação
├── calculator_gui.py          # Interface gráfica (Front-end)
├── calculator_controller.py   # Controlador (Middleware)
├── calculator_engine.py       # Motor de cálculo (Back-end)
├── test_calculator_engine.py  # Testes unitários
├── README.md                  # Documentação
```

### Camadas da Aplicação

```
┌─────────────────────────────────────┐
│           Interface Gráfica         │
│            (Front-end)              │
│         - Tkinter GUI               │
│         - Event Handlers            │
│         - Display Management        │
└─────────────────┬───────────────────┘
                  │ API Calls
┌─────────────────▼───────────────────┐
│          Controlador                │
│        - Input Validation           │
│        - Command Processing         │
│        - Error Handling             │
└─────────────────┬───────────────────┘
                  │ Method Calls
┌─────────────────▼───────────────────┐
│         Motor de Cálculo            │
│           (Back-end)                │
│      - Mathematical Operations      │
│      - Geometric Calculations       │
│      - Trigonometric Functions      │
└─────────────────────────────────────┘
```

## 🎨 Design Moderno Clean

### Esquema de Cores Atualizado

**Tema Escuro Moderno:**
- **Fundo Principal**: `#1e1e1e` (preto moderno)
- **Display**: `#2c3e50` (azul escuro) com texto `#ecf0f1` (branco/cinza claro)
- **Botões Numéricos**: `#57606f` (cinza escuro) com texto branco
- **Botões Operadores**: `#ff6b35` (laranja moderno) com texto branco
- **Botões Científicos**: `#9b59b6` (roxo elegante) com texto branco
- **Botões Geométricos**: `#e67e22` (laranja escuro) com texto branco
- **Botão Igual**: `#2ed573` (verde moderno) com texto branco
- **Botão Limpar**: `#ff4757` (vermelho moderno) com texto branco

### Características Visuais Atualizadas

- **Layout Horizontal**: Calculadora básica à esquerda, extras à direita
- **Proporções Tablet**: 800×650 pixels (clean e compacto)
- **Fonte Moderna**: Segoe UI com tamanhos otimizados (10pt-24pt)
- **Efeitos Modernos**: Hover suave, feedback visual e animações
- **Design Flat**: Bordas limpas com efeitos de profundidade sutis
- **Categorização Visual**: Cores específicas por tipo de função
- **Responsividade**: Layout adaptável mantendo proporções
- **Feedback Inteligente**: Indicadores visuais para todas as interações
- **Histórico Integrado**: Painel compacto na parte superior
- **Atalhos Visíveis**: Lista sempre disponível no painel lateral

## 🧪 Testes

### Executar Testes

```bash
python -m pytest test_calculator_engine.py -v
```

### Cobertura de Testes

Os testes cobrem:
- ✅ Operações matemáticas básicas
- ✅ Funções científicas e trigonométricas
- ✅ Cálculos geométricos
- ✅ Validação de entrada
- ✅ Tratamento de erros
- ✅ Casos extremos

## 📋 Requisitos do Sistema

### Funcionais

1. **Operações Básicas**: Suporte a +, -, ×, ÷ com validação completa
2. **Funções Científicas**: √ (raiz quadrada), % (porcentagem), sin, cos, tan
3. **Cálculos Geométricos**: Área do círculo, volume da esfera
4. **Função Especial**: Verificação par/ímpar para números inteiros
5. **Interface Horizontal**: Layout clean otimizado para tablet/mobile
6. **Entrada Flexível**: Mouse, teclado e atalhos F1-F8
7. **Histórico Inteligente**: Últimas 10 operações com timestamps
8. **Feedback Visual**: Indicadores de sucesso, erro e operações

### Não Funcionais

1. **Performance**: Cálculos instantâneos com precisão de 10 casas decimais
2. **Usabilidade**: Interface clean tipo tablet (800×650px)
3. **Acessibilidade**: Atalhos de teclado e feedback visual
4. **Confiabilidade**: Tratamento robusto de erros e validação
5. **Manutenibilidade**: Arquitetura MVC bem documentada
6. **Portabilidade**: Funciona em Windows, macOS e Linux
7. **Responsividade**: Layout adaptável mantendo proporções
8. **Experiência do Usuário**: Design moderno com tema escuro

## 🔧 Desenvolvimento

### Estrutura do Código

- **Separação de Responsabilidades**: MVC pattern
- **Validação Robusta**: Entrada e cálculos validados
- **Tratamento de Erros**: Mensagens claras e recuperação
- **Documentação**: Docstrings completas em todos os métodos
- **Testes**: Cobertura abrangente de funcionalidades

### Padrões Utilizados

- **MVC (Model-View-Controller)**: Separação clara de camadas
- **Factory Pattern**: Criação de respostas padronizadas
- **Observer Pattern**: Eventos de interface
- **Strategy Pattern**: Diferentes tipos de operações

## 🚀 Melhorias e Otimizações Implementadas

### Design e Interface
- ✅ **Layout Horizontal Clean**: Calculadora básica + painel de extras
- ✅ **Tema Escuro Moderno**: Cores categorizadas e elegantes
- ✅ **Proporções Tablet**: 800×650px otimizado para dispositivos móveis
- ✅ **Tipografia Moderna**: Segoe UI com tamanhos responsivos
- ✅ **Efeitos Visuais**: Hover, feedback e animações suaves

### Funcionalidades Avançadas
- ✅ **Funções Científicas**: Raiz quadrada, trigonometria, porcentagem
- ✅ **Cálculos Geométricos**: Área círculo, volume esfera
- ✅ **Verificação Par/Ímpar**: Para números inteiros
- ✅ **Histórico Inteligente**: 10 últimas operações com timestamps
- ✅ **Atalhos de Teclado**: F1-F8 para funções especiais

### Experiência do Usuário
- ✅ **Interface Intuitiva**: Todas as funcionalidades visíveis
- ✅ **Feedback Visual**: Indicadores de sucesso/erro
- ✅ **Entrada Flexível**: Mouse + teclado + atalhos
- ✅ **Design Responsivo**: Redimensionável mantendo proporções
- ✅ **Organização Clara**: Seções categorizadas por tipo de função

### Arquitetura e Código
- ✅ **Padrão MVC**: Separação clara de responsabilidades
- ✅ **Validação Robusta**: Tratamento completo de erros
- ✅ **Documentação Completa**: Docstrings em todos os métodos
- ✅ **Testes Abrangentes**: Cobertura de todas as funcionalidades
- ✅ **Código Limpo**: Estrutura organizada e manutenível

## 🤝 Contribuição

Para contribuir com o projeto:

1. Fork o repositório
2. Crie uma branch para sua feature (`git checkout -b feature/nova-funcionalidade`)
3. Commit suas mudanças (`git commit -am 'Adiciona nova funcionalidade'`)
4. Push para a branch (`git push origin feature/nova-funcionalidade`)
5. Abra um Pull Request

## 📄 Licença

Este projeto está sob a licença MIT. Veja o arquivo `LICENSE` para mais detalhes.

## 🆘 Suporte

Se encontrar problemas ou tiver sugestões:

1. Verifique se todas as dependências estão instaladas
2. Consulte a documentação dos requisitos
3. Execute os testes para verificar a integridade
4. Abra uma issue no repositório com detalhes do problema

---

## 🎓 Informações Acadêmicas

**Disciplina:** Programação Funcional  
**Instituição:** [Nome da Instituição]  
**Período:** [Período Letivo]

**Equipe de Desenvolvimento:**
- **Gabriel Luís Lopes** – RA: 2300873
- **Lucas Timponi Mercadante Castro** – RA: 2304913  
- **Pedro Alexandre Dos Santos Chaves** – RA: 2301503

## 🏆 Características do Projeto

Este projeto demonstra a aplicação de conceitos de programação funcional e orientada a objetos em Python, incluindo:

- **Arquitetura MVC** bem estruturada
- **Interface gráfica moderna** com Tkinter
- **Tratamento robusto de erros** e validação
- **Testes unitários** abrangentes
- **Documentação completa** do código
- **Design responsivo** e acessível
- **Experiência do usuário** otimizada

---

**Desenvolvido com ❤️ usando Python e Tkinter**  
**Projeto Acadêmico - Programação Funcional - 2024**