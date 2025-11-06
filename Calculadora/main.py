#!/usr/bin/env python3
"""
Calculadora Moderna - Arquivo Principal

Este arquivo serve como ponto de entrada para a aplicação da calculadora moderna.
Executa a interface gráfica completa com todas as funcionalidades implementadas.

Autor: Sistema de Desenvolvimento
Versão: 1.0.0
Data: 2024

Funcionalidades principais:
- Operações matemáticas básicas (+, -, *, /)
- Funções científicas (√, %, sin, cos, tan)
- Cálculos geométricos (área do círculo, volume da esfera)
- Verificação par/ímpar
- Entrada por teclado e mouse
- Histórico de operações com timestamps
- Feedback visual e tratamento robusto de erros
- Interface moderna e responsiva
"""

import sys
import os
import tkinter as tk
from tkinter import messagebox

# Adicionar o diretório atual ao path para importações
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

try:
    from calculator_gui import CalculatorGUI
except ImportError as e:
    print(f"Erro ao importar módulos da calculadora: {e}")
    print("Verifique se todos os arquivos estão no diretório correto:")
    print("- calculator_gui.py")
    print("- calculator_controller.py") 
    print("- calculator_engine.py")
    sys.exit(1)


def check_dependencies():
    """
    Verifica se todas as dependências necessárias estão disponíveis.
    
    Returns:
        bool: True se todas as dependências estão OK, False caso contrário
    """
    try:
        # Verificar se Tkinter está disponível
        root = tk.Tk()
        root.withdraw()  # Esconder janela temporária
        root.destroy()
        
        # Verificar módulos matemáticos
        import math
        
        return True
        
    except ImportError as e:
        print(f"Dependência não encontrada: {e}")
        return False
    except Exception as e:
        print(f"Erro ao verificar dependências: {e}")
        return False


def show_startup_info():
    """
    Exibe informações de inicialização da aplicação.
    """
    print("=" * 60)
    print("🧮 CALCULADORA MODERNA v1.0.0")
    print("=" * 60)
    print("\n📋 Funcionalidades disponíveis:")
    print("   • Operações básicas: +, -, *, /")
    print("   • Funções científicas: √ (F1), sin (F2), cos (F3), tan (F4)")
    print("   • Cálculos geométricos: Área círculo (F5), Volume esfera (F6)")
    print("   • Verificação par/ímpar (F7), Porcentagem (F8)")
    print("   • Entrada por teclado e mouse")
    print("   • Histórico das últimas 10 operações")
    print("   • Feedback visual para todas as interações")
    
    print("\n⌨️  Atalhos de teclado:")
    print("   • ESC ou Delete: Limpar tudo")
    print("   • Backspace: Apagar último dígito")
    print("   • Enter ou =: Calcular resultado")
    print("   • F1-F8: Funções especiais")
    
    print("\n🎨 Interface moderna com:")
    print("   • Design responsivo e intuitivo")
    print("   • Efeitos visuais e hover")
    print("   • Tratamento robusto de erros")
    print("   • Histórico com timestamps")
    
    print("\n🚀 Iniciando aplicação...")
    print("-" * 60)


def main():
    """
    Função principal para executar a Calculadora Moderna.
    
    Realiza verificações de dependências, inicializa a interface gráfica
    e executa a aplicação com tratamento completo de erros.
    
    Returns:
        int: Código de saída (0 = sucesso, 1 = erro)
    """
    try:
        # Verificar dependências
        if not check_dependencies():
            print("\n❌ Erro: Dependências não encontradas.")
            print("Instale o Python 3.7+ com Tkinter incluído.")
            return 1
        
        # Mostrar informações de inicialização
        show_startup_info()
        
        # Criar e executar a aplicação
        app = CalculatorGUI()
        
        print("✅ Calculadora iniciada com sucesso!")
        print("   Janela da aplicação aberta. Use Ctrl+C para encerrar.\n")
        
        # Executar loop principal da interface
        app.run()
        
        print("\n👋 Calculadora encerrada. Obrigado por usar!")
        return 0
        
    except KeyboardInterrupt:
        print("\n\n⚠️  Aplicação interrompida pelo usuário (Ctrl+C)")
        print("👋 Calculadora encerrada. Obrigado por usar!")
        return 0
        
    except ImportError as e:
        print(f"\n❌ Erro de importação: {e}")
        print("Verifique se todos os arquivos da calculadora estão presentes:")
        print("- calculator_gui.py")
        print("- calculator_controller.py")
        print("- calculator_engine.py")
        return 1
        
    except tk.TclError as e:
        print(f"\n❌ Erro na interface gráfica: {e}")
        print("Possíveis causas:")
        print("- Tkinter não está instalado corretamente")
        print("- Sistema não suporta interface gráfica")
        print("- Problemas com o servidor X (Linux)")
        return 1
        
    except Exception as e:
        print(f"\n❌ Erro inesperado ao executar a calculadora: {e}")
        print("Detalhes técnicos:")
        print(f"   Tipo do erro: {type(e).__name__}")
        print(f"   Mensagem: {str(e)}")
        print("\n🔧 Sugestões:")
        print("- Verifique se o Python 3.7+ está instalado")
        print("- Confirme que o Tkinter está disponível")
        print("- Execute 'python -m tkinter' para testar o Tkinter")
        print("- Verifique as permissões dos arquivos")
        return 1


def show_help():
    """
    Exibe informações de ajuda sobre como usar a aplicação.
    """
    help_text = """
🧮 Calculadora Moderna - Ajuda

USO:
    python main.py              # Executar a calculadora
    python main.py --help       # Mostrar esta ajuda
    python main.py --version    # Mostrar versão

REQUISITOS:
    - Python 3.7 ou superior
    - Tkinter (geralmente incluído com Python)
    - Módulos: math, datetime, typing

ARQUIVOS NECESSÁRIOS:
    - main.py                   # Este arquivo
    - calculator_gui.py         # Interface gráfica
    - calculator_controller.py  # Controlador
    - calculator_engine.py      # Motor de cálculo

FUNCIONALIDADES:
    - Operações básicas: +, -, *, /
    - Funções científicas: √, %, sin, cos, tan
    - Cálculos geométricos: área círculo, volume esfera
    - Verificação par/ímpar
    - Histórico de operações
    - Entrada por teclado e mouse

ATALHOS DE TECLADO:
    0-9         Números
    +,-,*,/     Operadores
    Enter, =    Calcular
    ESC, Del    Limpar
    Backspace   Apagar
    F1-F8       Funções especiais

Para mais informações, consulte o arquivo README.md
"""
    print(help_text)


if __name__ == "__main__":
    # Verificar argumentos da linha de comando
    if len(sys.argv) > 1:
        arg = sys.argv[1].lower()
        if arg in ['--help', '-h', 'help']:
            show_help()
            sys.exit(0)
        elif arg in ['--version', '-v', 'version']:
            print("Calculadora Moderna v1.0.0")
            sys.exit(0)
        else:
            print(f"Argumento desconhecido: {sys.argv[1]}")
            print("Use --help para ver as opções disponíveis.")
            sys.exit(1)
    
    # Executar aplicação principal
    exit_code = main()
    sys.exit(exit_code)