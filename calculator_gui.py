import tkinter as tk
from tkinter import ttk
from calculator_controller import CalculatorController


class CalculatorGUI:
    def __init__(self):
        self.controller = CalculatorController()
        self.root = tk.Tk()
        self.setup_window()
        self.create_main_layout()
        self.create_display()
        self.create_button_frame()
        self.create_history_panel()
        
    def setup_window(self):
        """Configurar janela principal da calculadora"""
        self.root.title("Calculadora - Todas as Funcionalidades")
        self.root.geometry("800x650")  # Tamanho de tablet/celular grande
        self.root.minsize(750, 600)  # Tamanho mínimo compacto
        self.root.resizable(True, True)
        
        # Cor de fundo escura moderna
        self.root.configure(bg="#1e1e1e")
        
        # Configurar ícone da janela (se disponível)
        try:
            self.root.iconbitmap(default="calculator.ico")
        except:
            pass
        
        # Centralizar janela na tela
        self.root.update_idletasks()
        width = self.root.winfo_width()
        height = self.root.winfo_height()
        x = (self.root.winfo_screenwidth() // 2) - (width // 2)
        y = (self.root.winfo_screenheight() // 2) - (height // 2)
        self.root.geometry(f"{width}x{height}+{x}+{y}")
        
        # Configurar captura de eventos de teclado
        self.root.focus_set()
        self.root.bind('<Key>', self.on_key_press)
        
        # Configurar responsividade da janela
        self.root.grid_rowconfigure(0, weight=1)
        self.root.grid_columnconfigure(0, weight=1)
    
    def create_main_layout(self):
        """Criar layout principal com design moderno horizontal"""
        # Frame principal com padding elegante
        self.main_frame = tk.Frame(self.root, bg="#1e1e1e")
        self.main_frame.pack(fill=tk.BOTH, expand=True, padx=12, pady=12)
        
        # Título da calculadora mais compacto
        title_label = tk.Label(
            self.main_frame,
            text="Calculadora",
            font=("Segoe UI", 14, "bold"),
            bg="#1e1e1e",
            fg="#ecf0f1"
        )
        title_label.pack(pady=(0, 8))
        
        # Frame do histórico compacto
        self.history_frame = tk.Frame(self.main_frame, bg="#2d2d2d", height=70)
        self.history_frame.pack(fill=tk.X, pady=(0, 12))
        self.history_frame.pack_propagate(False)
        
        # Frame horizontal para calculadora básica e funcionalidades extras
        self.horizontal_frame = tk.Frame(self.main_frame, bg="#1e1e1e")
        self.horizontal_frame.pack(fill=tk.BOTH, expand=True)
        
        # Frame esquerdo para calculadora básica
        self.calculator_frame = tk.Frame(self.horizontal_frame, bg="#1e1e1e")
        self.calculator_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=(0, 15))
        
        # Frame direito para funcionalidades extras
        self.extras_frame = tk.Frame(self.horizontal_frame, bg="#1e1e1e", width=280)
        self.extras_frame.pack(side=tk.RIGHT, fill=tk.Y)
        self.extras_frame.pack_propagate(False)
        
    def create_display(self):
        """Criar display principal para mostrar números e resultados"""
        # Frame para o display com design elegante
        display_frame = tk.Frame(
            self.calculator_frame, 
            bg="#1e1e1e", 
            pady=20
        )
        display_frame.pack(fill=tk.X)
        
        # Display principal com melhor visibilidade
        self.display_var = tk.StringVar(value="0")
        self.display = tk.Entry(
            display_frame,
            textvariable=self.display_var,
            font=("Segoe UI", 24, "bold"),  # Fonte compacta
            justify="right",
            state="readonly",
            bg="#000000",  # Fundo preto para máximo contraste
            fg="#00ff00",  # Texto verde brilhante (estilo calculadora)
            bd=2,
            relief="sunken",
            highlightthickness=2,
            highlightcolor="#00ff00",
            highlightbackground="#333333",
            insertbackground="#00ff00",
            readonlybackground="#000000"  # Garantir fundo preto mesmo em readonly
        )
        self.display.pack(fill=tk.X, ipady=15, padx=5)
        
        # Borda do display com efeito de profundidade
        border_frame = tk.Frame(
            display_frame,
            height=3,
            bg="#34495e"
        )
        border_frame.pack(fill=tk.X, pady=(3, 0))
        
        # Sombra inferior para dar profundidade
        shadow_frame = tk.Frame(
            display_frame,
            height=1,
            bg="#1a252f"
        )
        shadow_frame.pack(fill=tk.X)
        
        # Indicador de status discreto
        self.status_label = tk.Label(
            display_frame,
            text="",
            font=("Segoe UI", 10),
            bg="#1e1e1e",
            fg="#888888",
            height=1,
            anchor="w"
        )
        self.status_label.pack(fill=tk.X, pady=(10, 0))
        
    def create_button_frame(self):
        """Criar frame para organização dos botões em grid"""
        # === CALCULADORA BÁSICA (LADO ESQUERDO) ===
        basic_label = tk.Label(
            self.calculator_frame,
            text="Calculadora Básica",
            font=("Segoe UI", 12, "bold"),
            bg="#1e1e1e",
            fg="#3498db"
        )
        basic_label.pack(pady=(5, 8))
        
        self.basic_frame = tk.Frame(
            self.calculator_frame, 
            bg="#1e1e1e",
            padx=5,
            pady=5
        )
        self.basic_frame.pack(fill=tk.BOTH, expand=True)
        
        # === FUNCIONALIDADES EXTRAS (LADO DIREITO) ===
        extras_label = tk.Label(
            self.extras_frame,
            text="Extras",
            font=("Segoe UI", 12, "bold"),
            bg="#1e1e1e",
            fg="#e74c3c"
        )
        extras_label.pack(pady=(5, 10))
        
        # Seção de funções científicas
        scientific_label = tk.Label(
            self.extras_frame,
            text="🔬 Científicas",
            font=("Segoe UI", 10, "bold"),
            bg="#1e1e1e",
            fg="#9b59b6"
        )
        scientific_label.pack(pady=(0, 5))
        
        self.scientific_frame = tk.Frame(
            self.extras_frame, 
            bg="#1e1e1e",
            padx=5,
            pady=5
        )
        self.scientific_frame.pack(fill=tk.X, padx=10)
        
        # Seção de funções geométricas
        geometric_label = tk.Label(
            self.extras_frame,
            text="📐 Geométricas",
            font=("Segoe UI", 10, "bold"),
            bg="#1e1e1e",
            fg="#e67e22"
        )
        geometric_label.pack(pady=(12, 5))
        
        self.geometric_frame = tk.Frame(
            self.extras_frame, 
            bg="#1e1e1e",
            padx=5,
            pady=5
        )
        self.geometric_frame.pack(fill=tk.X, padx=10)
        
        # Seção de atalhos
        shortcuts_label = tk.Label(
            self.extras_frame,
            text="⌨️ Atalhos",
            font=("Segoe UI", 10, "bold"),
            bg="#1e1e1e",
            fg="#f39c12"
        )
        shortcuts_label.pack(pady=(12, 5))
        
        # Texto com atalhos compacto
        shortcuts_text = tk.Label(
            self.extras_frame,
            text="F1:√ F2:sen F3:cos F4:tan\nF5:Área F6:Vol F7:Par/Ímpar\nF8:% ESC:Limpar Enter:=",
            font=("Segoe UI", 8),
            bg="#1e1e1e",
            fg="#bdc3c7",
            justify=tk.LEFT
        )
        shortcuts_text.pack(padx=10, pady=(0, 8))
        
        # Configurar grids para cada seção
        self.setup_grids()
        
        # Criar todos os botões organizados por seção
        self.create_buttons()
    
    def setup_grids(self):
        """Configurar grids para cada seção - Tamanho tablet/mobile"""
        # Grid para calculadora básica (5 linhas x 4 colunas) - Compacto
        for i in range(5):
            self.basic_frame.grid_rowconfigure(i, weight=1, minsize=55)
        for i in range(4):
            self.basic_frame.grid_columnconfigure(i, weight=1, minsize=85)
        
        # Grid para funções científicas (2 linhas x 2 colunas) - Compacto
        for i in range(2):
            self.scientific_frame.grid_rowconfigure(i, weight=1, minsize=45)
        for i in range(2):
            self.scientific_frame.grid_columnconfigure(i, weight=1, minsize=130)
        
        # Grid para funções geométricas (2 linhas x 2 colunas) - Compacto
        for i in range(2):
            self.geometric_frame.grid_rowconfigure(i, weight=1, minsize=45)
        for i in range(2):
            self.geometric_frame.grid_columnconfigure(i, weight=1, minsize=130)

    def create_buttons(self):
        """Criar botões organizados por seções"""
        
        # === SEÇÃO: OPERAÇÕES BÁSICAS ===
        # Primeira linha: funções especiais
        self.create_button_in_frame(self.basic_frame, "C", 0, 0, self.clear_all, "#ff4757", "#ffffff")
        self.create_button_in_frame(self.basic_frame, "±", 0, 1, self.toggle_sign, "#747d8c", "#ffffff")
        self.create_button_in_frame(self.basic_frame, "⌫", 0, 2, self.backspace, "#747d8c", "#ffffff")
        self.create_button_in_frame(self.basic_frame, "÷", 0, 3, lambda: self.operator_click("/"), "#ff6b35", "#ffffff")
        
        # Segunda linha: números 7-9 e multiplicação
        self.create_button_in_frame(self.basic_frame, "7", 1, 0, lambda: self.number_click("7"), "#57606f", "#ffffff")
        self.create_button_in_frame(self.basic_frame, "8", 1, 1, lambda: self.number_click("8"), "#57606f", "#ffffff")
        self.create_button_in_frame(self.basic_frame, "9", 1, 2, lambda: self.number_click("9"), "#57606f", "#ffffff")
        self.create_button_in_frame(self.basic_frame, "×", 1, 3, lambda: self.operator_click("*"), "#ff6b35", "#ffffff")
        
        # Terceira linha: números 4-6 e subtração
        self.create_button_in_frame(self.basic_frame, "4", 2, 0, lambda: self.number_click("4"), "#57606f", "#ffffff")
        self.create_button_in_frame(self.basic_frame, "5", 2, 1, lambda: self.number_click("5"), "#57606f", "#ffffff")
        self.create_button_in_frame(self.basic_frame, "6", 2, 2, lambda: self.number_click("6"), "#57606f", "#ffffff")
        self.create_button_in_frame(self.basic_frame, "−", 2, 3, lambda: self.operator_click("-"), "#ff6b35", "#ffffff")
        
        # Quarta linha: números 1-3 e adição
        self.create_button_in_frame(self.basic_frame, "1", 3, 0, lambda: self.number_click("1"), "#57606f", "#ffffff")
        self.create_button_in_frame(self.basic_frame, "2", 3, 1, lambda: self.number_click("2"), "#57606f", "#ffffff")
        self.create_button_in_frame(self.basic_frame, "3", 3, 2, lambda: self.number_click("3"), "#57606f", "#ffffff")
        self.create_button_in_frame(self.basic_frame, "+", 3, 3, lambda: self.operator_click("+"), "#ff6b35", "#ffffff")
        
        # Quinta linha: zero, decimal e igual
        self.create_button_in_frame(self.basic_frame, "0", 4, 0, lambda: self.number_click("0"), "#57606f", "#ffffff", columnspan=2)
        self.create_button_in_frame(self.basic_frame, ".", 4, 2, lambda: self.number_click("."), "#57606f", "#ffffff")
        self.create_button_in_frame(self.basic_frame, "=", 4, 3, self.equals_click, "#2ed573", "#ffffff")
        
        # === FUNCIONALIDADES EXTRAS (LADO DIREITO) ===
        # Funções científicas
        self.create_button_in_frame(self.scientific_frame, "√ Raiz\n(F1)", 0, 0, self.square_root_click, "#9b59b6", "#ffffff")
        self.create_button_in_frame(self.scientific_frame, "% Porcentagem\n(F8)", 0, 1, self.percentage_click, "#9b59b6", "#ffffff")
        self.create_button_in_frame(self.scientific_frame, "sen (F2)", 1, 0, lambda: self.trigonometric_click("sin"), "#9b59b6", "#ffffff")
        self.create_button_in_frame(self.scientific_frame, "cos (F3)", 1, 1, lambda: self.trigonometric_click("cos"), "#9b59b6", "#ffffff")
        
        # Funções geométricas
        self.create_button_in_frame(self.geometric_frame, "🔵 Área Círculo\n(F5)", 0, 0, self.circle_area_click, "#e67e22", "#ffffff")
        self.create_button_in_frame(self.geometric_frame, "⚫ Volume Esfera\n(F6)", 0, 1, self.sphere_volume_click, "#e67e22", "#ffffff")
        self.create_button_in_frame(self.geometric_frame, "🔢 Par/Ímpar\n(F7)", 1, 0, self.even_odd_click, "#e67e22", "#ffffff")
        self.create_button_in_frame(self.geometric_frame, "tan (F4)", 1, 1, lambda: self.trigonometric_click("tan"), "#9b59b6", "#ffffff")
        
    def create_button_in_frame(self, parent_frame, text, row, col, command, bg_color="#57606f", text_color="#ffffff", columnspan=1):
        """Criar um botão individual em um frame específico"""
        
        # Determinar tamanho da fonte baseado no texto - Mobile friendly
        font_size = 10 if len(text) > 8 else 14
        
        button = tk.Button(
            parent_frame,
            text=text,
            font=("Segoe UI", font_size, "bold"),
            bg=bg_color,
            fg=text_color,
            activebackground=self.get_hover_color(bg_color),
            activeforeground=text_color,
            bd=0,
            relief="flat",
            cursor="hand2",
            command=command,
            wraplength=120  # Quebrar texto longo
        )
        
        # Grid com espaçamento compacto
        button.grid(
            row=row, 
            column=col, 
            columnspan=columnspan,
            sticky="nsew", 
            padx=3, 
            pady=3,
            ipadx=5,
            ipady=8
        )
        
        # Adicionar efeitos visuais modernos
        self._add_modern_button_effects(button, bg_color)
        
    def get_hover_color(self, original_color):
        """Obter cor mais clara para efeito hover"""
        hover_colors = {
            "#57606f": "#6c7a89",  # Números - cinza mais claro
            "#ff6b35": "#ff7f50",  # Operadores - laranja mais claro
            "#ff4757": "#ff6b7a",  # Clear - vermelho mais claro
            "#2ed573": "#55e68a",  # Igual - verde mais claro
            "#9b59b6": "#bb6bd9",  # Científicas - roxo mais claro
            "#e67e22": "#f39c12",  # Geométricas - laranja mais claro
            "#747d8c": "#8395a7"   # Funções - cinza mais claro
        }
        return hover_colors.get(original_color, "#6c7a89")
    
    def _add_modern_button_effects(self, button, original_color):
        """Adicionar efeitos visuais modernos aos botões"""
        def on_enter(e):
            button.config(
                bg=self.get_hover_color(original_color),
                relief="flat"
            )
        
        def on_leave(e):
            button.config(
                bg=original_color,
                relief="flat"
            )
        
        def on_press(e):
            # Efeito de pressionar - cor mais escura
            press_color = self._darken_color(original_color)
            button.config(
                bg=press_color,
                relief="flat"
            )
        
        def on_release(e):
            # Voltar para cor hover se mouse ainda estiver sobre o botão
            button.config(
                bg=self.get_hover_color(original_color),
                relief="flat"
            )
        
        # Vincular eventos
        button.bind("<Enter>", on_enter)
        button.bind("<Leave>", on_leave)
        button.bind("<Button-1>", on_press)
        button.bind("<ButtonRelease-1>", on_release)
    
    def _darken_color(self, color):
        """Escurecer uma cor para efeito de pressionar"""
        darken_colors = {
            "#57606f": "#4a525e",
            "#ff6b35": "#e55a2b",
            "#ff4757": "#e53e4d",
            "#2ed573": "#29c065",
            "#9b59b6": "#8e44ad",
            "#e67e22": "#d35400",
            "#747d8c": "#636b78"
        }
        return darken_colors.get(color, "#4a525e")
    

        
    def number_click(self, number):
        """Processar clique em número ou decimal"""
        # Processar entrada através do controlador para manter estado consistente
        result = self.controller.process_input(number)
        # Temporariamente habilitar para atualizar, depois desabilitar
        self.display.config(state="normal")
        self.display_var.set(str(result))
        self.display.config(state="readonly")
            
    def operator_click(self, operator):
        """Processar clique em operador"""
        # Processar operador através do controlador
        result = self.controller.process_input(operator)
        self.display.config(state="normal")
        self.display_var.set(str(result))
        self.display.config(state="readonly")
        
        # Mostrar indicador visual de que operador foi selecionado
        operator_names = {'+': 'adição', '-': 'subtração', '*': 'multiplicação', '/': 'divisão'}
        operation_name = operator_names.get(operator, 'operação')
        self._show_status_message(f"Operador {operation_name} selecionado", "info")
        
    def equals_click(self):
        """Processar clique no botão igual"""
        # Processar igual através do controlador
        result = self.controller.process_input('=')
        
        if result == "Erro":
            self._show_error_feedback("Operação inválida")
        else:
            self._show_success_feedback("cálculo")
        
        self.display.config(state="normal")
        self.display_var.set(str(result))
        self.display.config(state="readonly")
        # Atualizar histórico após operação
        self.update_history_display()
        
    def clear_all(self):
        """Limpar display e resetar calculadora"""
        self.controller.clear_all()
        self.display.config(state="normal")
        self.display_var.set("0")
        self.display.config(state="readonly")
        self._clear_status_message()
        
    def backspace(self):
        """Remover último caractere do display"""
        result = self.controller.process_input('←')
        self.display.config(state="normal")
        self.display_var.set(str(result))
        self.display.config(state="readonly")
    
    def square_root_click(self):
        """Processar clique no botão de raiz quadrada"""
        current_value = self.display_var.get()
        try:
            result = self.controller.execute_operation("square_root", number=float(current_value))
            if result.startswith("Erro"):
                self._show_error_feedback(result)
                self.update_display("Erro")
            else:
                self.update_display(result)
                self._show_success_feedback("raiz quadrada")
            self.update_history_display()
        except ValueError:
            self._show_error_feedback("Valor inválido para raiz quadrada")
            self.update_display("Erro")
    
    def trigonometric_click(self, function):
        """Processar clique nos botões trigonométricos"""
        current_value = self.display_var.get()
        try:
            # Por padrão, usar radianos
            result = self.controller.execute_operation(
                "trigonometric", 
                number=float(current_value), 
                function=function, 
                unit="radians"
            )
            if result.startswith("Erro"):
                self._show_error_feedback(result)
                self.update_display("Erro")
            else:
                self.update_display(result)
                self._show_success_feedback(f"função {function}")
            self.update_history_display()
        except ValueError:
            self._show_error_feedback("Valor inválido para função trigonométrica")
            self.update_display("Erro")
    
    def percentage_click(self):
        """Processar clique no botão de porcentagem"""
        current_value = self.display_var.get()
        try:
            # Para porcentagem simples, calcular X% (X/100)
            result = self.controller.execute_operation("percentage", number=100, percent=float(current_value))
            if result.startswith("Erro"):
                self._show_error_feedback(result)
                self.update_display("Erro")
            else:
                self.update_display(result)
                self._show_success_feedback("porcentagem")
            self.update_history_display()
        except ValueError:
            self._show_error_feedback("Valor inválido para porcentagem")
            self.display_var.set("Erro")
    
    def circle_area_click(self):
        """Processar clique no botão de área do círculo"""
        current_value = self.display_var.get()
        try:
            result = self.controller.execute_operation("circle_area", radius=float(current_value))
            if result.startswith("Erro"):
                self._show_error_feedback(result)
                self.display_var.set("Erro")
            else:
                self.display_var.set(result)
                self._show_success_feedback("área do círculo")
            self.update_history_display()
        except ValueError:
            self._show_error_feedback("Valor inválido para raio do círculo")
            self.display_var.set("Erro")
    
    def sphere_volume_click(self):
        """Processar clique no botão de volume da esfera"""
        current_value = self.display_var.get()
        try:
            result = self.controller.execute_operation("sphere_volume", radius=float(current_value))
            if result.startswith("Erro"):
                self._show_error_feedback(result)
                self.display_var.set("Erro")
            else:
                self.display_var.set(result)
                self._show_success_feedback("volume da esfera")
            self.update_history_display()
        except ValueError:
            self._show_error_feedback("Valor inválido para raio da esfera")
            self.display_var.set("Erro")
    
    def even_odd_click(self):
        """Processar clique no botão de verificação par/ímpar"""
        current_value = self.display_var.get()
        try:
            result = self.controller.execute_operation("is_even_odd", number=int(float(current_value)))
            if result.startswith("Erro"):
                self._show_error_feedback(result)
                self.display_var.set("Erro")
            else:
                self.display_var.set(result)
                self._show_success_feedback("verificação par/ímpar")
            self.update_history_display()
        except ValueError:
            self._show_error_feedback("Valor inválido para verificação par/ímpar")
            self.display_var.set("Erro")
    
    def toggle_sign(self):
        """Alternar sinal do número atual (positivo/negativo)"""
        current_value = self.display_var.get()
        try:
            if current_value != "0" and current_value != "Erro":
                if current_value.startswith("-"):
                    new_value = current_value[1:]
                else:
                    new_value = "-" + current_value
                self.display_var.set(new_value)
                # Atualizar o controlador com o novo valor
                self.controller.state.current_value = new_value
                self.controller.state.display_value = new_value
        except:
            pass  # Ignorar erros silenciosamente

    def on_key_press(self, event):
        """
        Processar eventos de teclado e mapear para funções da calculadora.
        
        Args:
            event: Evento de teclado do Tkinter
        """
        key = event.keysym
        char = event.char
        
        # Mapear teclas numéricas (0-9)
        if char.isdigit():
            self.number_click(char)
            return
        
        # Mapear operadores básicos
        key_mappings = {
            'plus': '+',
            'minus': '-',
            'asterisk': '*',
            'slash': '/',
            'Return': '=',
            'KP_Enter': '=',
            'equal': '=',
            'period': '.',
            'comma': '.',  # Aceitar vírgula como ponto decimal
            'Escape': 'C',
            'Delete': 'C',
            'BackSpace': '←'
        }
        
        # Verificar mapeamentos diretos
        if key in key_mappings:
            mapped_key = key_mappings[key]
            if mapped_key in ['+', '-', '*', '/']:
                self.operator_click(mapped_key)
            elif mapped_key == '=':
                self.equals_click()
            elif mapped_key == '.':
                self.number_click('.')
            elif mapped_key == 'C':
                self.clear_all()
            elif mapped_key == '←':
                self.backspace()
            return
        
        # Mapear caracteres especiais diretamente
        if char in ['+', '-', '*', '/', '=']:
            if char in ['+', '-', '*', '/']:
                self.operator_click(char)
            elif char == '=':
                self.equals_click()
            return
        
        # Mapear teclas de função para operações avançadas
        function_mappings = {
            'F1': self.square_root_click,  # F1 para raiz quadrada
            'F2': lambda: self.trigonometric_click('sen'),  # F2 para seno
            'F3': lambda: self.trigonometric_click('cos'),  # F3 para cosseno
            'F4': lambda: self.trigonometric_click('tan'),  # F4 para tangente
            'F5': self.circle_area_click,  # F5 para área do círculo
            'F6': self.sphere_volume_click,  # F6 para volume da esfera
            'F7': self.even_odd_click,  # F7 para par/ímpar
            'F8': self.percentage_click  # F8 para porcentagem
        }
        
        if key in function_mappings:
            function_mappings[key]()
            return
        
        # Validar entrada - ignorar teclas não mapeadas
        self._validate_keyboard_input(key, char)
    
    def _validate_keyboard_input(self, key, char):
        """
        Validar entrada por teclado e fornecer feedback visual se necessário.
        
        Args:
            key: Tecla pressionada (keysym)
            char: Caractere da tecla (char)
        """
        # Lista de teclas válidas que são aceitas
        valid_keys = [
            '0', '1', '2', '3', '4', '5', '6', '7', '8', '9',
            '+', '-', '*', '/', '=', '.', ',',
            'plus', 'minus', 'asterisk', 'slash', 'Return', 'KP_Enter',
            'equal', 'period', 'comma', 'Escape', 'Delete', 'BackSpace',
            'F1', 'F2', 'F3', 'F4', 'F5', 'F6', 'F7', 'F8'
        ]
        
        # Teclas de controle que devem ser ignoradas silenciosamente
        control_keys = [
            'Shift_L', 'Shift_R', 'Control_L', 'Control_R',
            'Alt_L', 'Alt_R', 'Tab', 'Caps_Lock', 'Num_Lock',
            'Scroll_Lock', 'Up', 'Down', 'Left', 'Right',
            'Home', 'End', 'Page_Up', 'Page_Down', 'Insert'
        ]
        
        # Se não é uma tecla válida nem uma tecla de controle, mostrar feedback
        if key not in valid_keys and key not in control_keys and char not in valid_keys:
            self._show_invalid_key_feedback()
    
    def _show_invalid_key_feedback(self):
        """
        Mostrar feedback visual para tecla inválida.
        """
        # Mostrar mensagem de status
        self._show_status_message("Tecla não reconhecida", "warning")
        
        # Piscar o display brevemente para indicar tecla inválida
        original_bg = self.display.cget('bg')
        self.display.config(bg='#2d2d1b')  # Cor amarela escura para warning
        self.root.after(150, lambda: self.display.config(bg=original_bg))
    
    def create_history_panel(self):
        """Criar painel de histórico compacto e moderno"""
        # Título do histórico discreto
        history_title = tk.Label(
            self.history_frame,
            text="Histórico",
            font=("Segoe UI", 12, "bold"),
            bg="#2d2d2d",
            fg="#ffffff"
        )
        history_title.pack(pady=(8, 5))
        
        # Frame para a lista de histórico
        history_list_frame = tk.Frame(
            self.history_frame, 
            bg="#1a1a1a", 
            relief="flat", 
            bd=0
        )
        history_list_frame.pack(fill=tk.BOTH, expand=True, padx=8, pady=(0, 8))
        
        # Scrollbar discreta
        self.history_scrollbar = tk.Scrollbar(
            history_list_frame,
            bg="#404040",
            troughcolor="#2d2d2d",
            activebackground="#666666",
            width=12
        )
        self.history_scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        
        # Listbox para exibir o histórico
        self.history_listbox = tk.Listbox(
            history_list_frame,
            yscrollcommand=self.history_scrollbar.set,
            font=("Consolas", 9),
            bg="#1a1a1a",
            fg="#cccccc",
            selectbackground="#404040",
            selectforeground="#ffffff",
            bd=0,
            highlightthickness=0,
            activestyle="none",
            height=4
        )
        self.history_listbox.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        
        # Configurar scrollbar
        self.history_scrollbar.config(command=self.history_listbox.yview)
        
        # Botão compacto para limpar histórico
        clear_history_btn = tk.Button(
            self.history_frame,
            text="Limpar",
            font=("Segoe UI", 9),
            bg="#ff4757",
            fg="#ffffff",
            activebackground="#ff6b7a",
            activeforeground="#ffffff",
            bd=0,
            relief="flat",
            cursor="hand2",
            command=self.clear_history,
            pady=4
        )
        clear_history_btn.pack(fill=tk.X, padx=8, pady=(0, 8))
        
        # Adicionar efeitos modernos ao botão
        self._add_modern_button_effects(clear_history_btn, "#ff4757")
        
        # Inicializar histórico vazio
        self.update_history_display()
    
    def update_history_display(self):
        """Atualizar a exibição do histórico com as últimas operações"""
        # Limpar listbox atual
        self.history_listbox.delete(0, tk.END)
        
        # Obter histórico formatado do controlador
        formatted_history = self.controller.get_formatted_history()
        
        # Adicionar cada entrada do histórico à listbox
        for entry in formatted_history:
            self.history_listbox.insert(tk.END, entry)
        
        # Rolar para o final (última operação)
        if formatted_history:
            self.history_listbox.see(tk.END)
    
    def clear_history(self):
        """Limpar todo o histórico de operações"""
        self.controller.clear_history()
        self.update_history_display()
        self._show_status_message("Histórico limpo", "success")
    
    def _show_status_message(self, message, message_type="info"):
        """
        Exibir mensagem de status na interface.
        
        Args:
            message: Mensagem a ser exibida
            message_type: Tipo da mensagem (info, success, warning, error)
        """
        colors = {
            "info": "#74b9ff",
            "success": "#00b894", 
            "warning": "#fdcb6e",
            "error": "#e17055"
        }
        
        self.status_label.config(
            text=message,
            fg=colors.get(message_type, "#888888")
        )
        
        # Limpar mensagem após 3 segundos
        self.root.after(3000, self._clear_status_message)
    
    def _clear_status_message(self):
        """Limpar mensagem de status"""
        self.status_label.config(text="", fg="#888888")
    
    def _show_error_feedback(self, error_message):
        """
        Mostrar feedback visual para erros.
        
        Args:
            error_message: Mensagem de erro a ser exibida
        """
        # Mostrar mensagem de erro no status
        self._show_status_message(f"Erro: {error_message}", "error")
        
        # Piscar o display em vermelho escuro
        original_bg = self.display.cget('bg')
        self.display.config(bg='#2d1b1b')
        self.root.after(200, lambda: self.display.config(bg=original_bg))
    
    def _show_success_feedback(self, operation_type=""):
        """
        Mostrar feedback visual para operações bem-sucedidas.
        
        Args:
            operation_type: Tipo da operação realizada
        """
        if operation_type:
            self._show_status_message(f"Operação {operation_type} realizada", "success")
        
        # Piscar o display em verde escuro
        original_bg = self.display.cget('bg')
        self.display.config(bg='#1b2d1b')
        self.root.after(200, lambda: self.display.config(bg=original_bg))

    def update_display(self, value):
        """Atualizar o display com novo valor"""
        self.display.config(state="normal")
        self.display_var.set(str(value))
        self.display.config(
            state="readonly",
            bg="#000000",  # Garantir fundo preto
            fg="#00ff00",  # Garantir texto verde
            readonlybackground="#000000"
        )
        
    def show_welcome_screen(self):
        """Mostrar tela de boas-vindas com todas as funcionalidades"""
        # Criar janela de boas-vindas
        welcome_window = tk.Toplevel(self.root)
        welcome_window.title("Calculadora - Funcionalidades")
        welcome_window.geometry("500x600")
        welcome_window.configure(bg="#1e1e1e")
        welcome_window.resizable(False, False)
        
        # Centralizar janela de boas-vindas
        welcome_window.update_idletasks()
        x = (welcome_window.winfo_screenwidth() // 2) - (250)
        y = (welcome_window.winfo_screenheight() // 2) - (300)
        welcome_window.geometry(f"500x600+{x}+{y}")
        
        # Fazer a janela ficar sempre no topo
        welcome_window.transient(self.root)
        welcome_window.grab_set()
        
        # Frame principal
        main_frame = tk.Frame(welcome_window, bg="#1e1e1e", padx=30, pady=20)
        main_frame.pack(fill=tk.BOTH, expand=True)
        
        # Título
        title_label = tk.Label(
            main_frame,
            text="🧮 Calculadora",
            font=("Segoe UI", 24, "bold"),
            bg="#1e1e1e",
            fg="#ecf0f1"
        )
        title_label.pack(pady=(0, 20))
        
        # Subtítulo
        subtitle_label = tk.Label(
            main_frame,
            text="Todas as Funcionalidades Disponíveis",
            font=("Segoe UI", 14),
            bg="#1e1e1e",
            fg="#bdc3c7"
        )
        subtitle_label.pack(pady=(0, 25))
        
        # Frame para as funcionalidades
        features_frame = tk.Frame(main_frame, bg="#1e1e1e")
        features_frame.pack(fill=tk.BOTH, expand=True)
        
        # Lista de funcionalidades
        features = [
            ("🔢 Operações Básicas", [
                "• Adição (+), Subtração (−), Multiplicação (×), Divisão (÷)",
                "• Números decimais e negativos",
                "• Função limpar (C) e backspace (←)"
            ]),
            ("🔬 Funções Científicas", [
                "• Raiz quadrada (√) - Tecla F1",
                "• Porcentagem (%) - Tecla F8", 
                "• Seno, Cosseno, Tangente - Teclas F2, F3, F4"
            ]),
            ("📐 Cálculos Geométricos", [
                "• Área do círculo - Tecla F5",
                "• Volume da esfera - Tecla F6",
                "• Verificação par/ímpar - Tecla F7"
            ]),
            ("⌨️ Atalhos de Teclado", [
                "• Números: 0-9, Operadores: +, -, *, /",
                "• Enter ou = para calcular",
                "• ESC ou Delete para limpar tudo",
                "• Backspace para apagar último dígito"
            ]),
            ("📊 Recursos Extras", [
                "• Histórico das últimas operações",
                "• Feedback visual para todas as ações",
                "• Interface responsiva e moderna"
            ])
        ]
        
        # Criar seções para cada categoria
        for category, items in features:
            # Título da categoria
            category_label = tk.Label(
                features_frame,
                text=category,
                font=("Segoe UI", 12, "bold"),
                bg="#1e1e1e",
                fg="#3498db",
                anchor="w"
            )
            category_label.pack(fill=tk.X, pady=(10, 5))
            
            # Items da categoria
            for item in items:
                item_label = tk.Label(
                    features_frame,
                    text=item,
                    font=("Segoe UI", 10),
                    bg="#1e1e1e",
                    fg="#ecf0f1",
                    anchor="w",
                    wraplength=440
                )
                item_label.pack(fill=tk.X, padx=(15, 0), pady=1)
        
        # Frame para botões
        button_frame = tk.Frame(main_frame, bg="#1e1e1e")
        button_frame.pack(fill=tk.X, pady=(20, 0))
        
        # Botão para começar
        start_button = tk.Button(
            button_frame,
            text="Começar a Usar",
            font=("Segoe UI", 12, "bold"),
            bg="#2ed573",
            fg="#ffffff",
            activebackground="#55e68a",
            activeforeground="#ffffff",
            bd=0,
            relief="flat",
            cursor="hand2",
            command=welcome_window.destroy,
            padx=30,
            pady=10
        )
        start_button.pack(side=tk.RIGHT)
        
        # Botão para mostrar novamente
        show_again_button = tk.Button(
            button_frame,
            text="Mostrar Novamente",
            font=("Segoe UI", 10),
            bg="#747d8c",
            fg="#ffffff",
            activebackground="#8395a7",
            activeforeground="#ffffff",
            bd=0,
            relief="flat",
            cursor="hand2",
            command=lambda: self.show_welcome_screen(),
            padx=20,
            pady=8
        )
        show_again_button.pack(side=tk.LEFT)
        
        # Adicionar efeitos aos botões
        self._add_welcome_button_effects(start_button, "#2ed573")
        self._add_welcome_button_effects(show_again_button, "#747d8c")
        
        # Focar na janela de boas-vindas
        welcome_window.focus_set()
    
    def _add_welcome_button_effects(self, button, original_color):
        """Adicionar efeitos aos botões da tela de boas-vindas"""
        hover_colors = {
            "#2ed573": "#55e68a",
            "#747d8c": "#8395a7"
        }
        
        def on_enter(e):
            button.config(bg=hover_colors.get(original_color, "#55e68a"))
        
        def on_leave(e):
            button.config(bg=original_color)
        
        button.bind("<Enter>", on_enter)
        button.bind("<Leave>", on_leave)
    
    def run(self):
        """Executar a aplicação"""
        self.root.mainloop()


if __name__ == "__main__":
    app = CalculatorGUI()
    app.run()