# 🧮 Calculadora

Uma calculadora interativa desenvolvida em Python com interface gráfica clean e intuitiva, otimizada para proporções de tablet/mobile. Apresenta separação clara entre front-end e back-end, suportando operações matemáticas básicas, funções científicas avançadas e cálculos geométricos.

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

## 🏗️ Arquitetura

A aplicação segue uma arquitetura em camadas bem definida:

### Estrutura de Arquivos

```
calculadora/
├── main.py                    # Ponto de entrada da aplicação
├── calculator_gui.py          # Interface gráfica (Front-end)
├── calculator_controller.py   # Controlador (Middleware)
├── calculator_engine.py       # Motor de cálculo (Back-end)
├── test_calculator_engine.py  # Testes unitários
├── README.md                  # Documentação
```
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
