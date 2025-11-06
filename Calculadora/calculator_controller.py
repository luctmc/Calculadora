"""
Controlador da Calculadora Moderna

Este módulo contém a classe CalculatorController que atua como intermediário
entre a interface gráfica e o motor de cálculo, gerenciando o estado da
aplicação e processando comandos de entrada.
"""

from datetime import datetime
from typing import List, Dict, Any, Union
from calculator_engine import CalculatorEngine


class CalculatorState:
    """
    Classe para gerenciar o estado atual da calculadora.
    """
    
    def __init__(self):
        """Inicializa o estado da calculadora."""
        self.current_value: str = "0"
        self.previous_value: str = ""
        self.operator: str = ""
        self.waiting_for_operand: bool = True
        self.last_operation: str = ""
        self.display_value: str = "0"
    
    def reset(self):
        """Reseta o estado da calculadora."""
        self.current_value = "0"
        self.previous_value = ""
        self.operator = ""
        self.waiting_for_operand = True
        self.last_operation = ""
        self.display_value = "0"


class CalculatorController:
    """
    Controlador principal da calculadora que gerencia a comunicação entre
    a interface gráfica e o motor de cálculo.
    """
    
    def __init__(self):
        """Inicializa o controlador da calculadora."""
        self.engine = CalculatorEngine()
        self.state = CalculatorState()
        self.history: List[Dict[str, Any]] = []
        self.max_history_size = 10
    
    def _add_to_history(self, operation: str, result: str, success: bool):
        """
        Adiciona uma operação ao histórico.
        
        Args:
            operation: Descrição da operação realizada
            result: Resultado da operação
            success: Se a operação foi bem-sucedida
        """
        history_entry = {
            "timestamp": datetime.now(),
            "operation": operation,
            "result": result,
            "success": success
        }
        
        self.history.append(history_entry)
        
        # Manter apenas as últimas 10 operações
        if len(self.history) > self.max_history_size:
            self.history.pop(0)
    
    def _format_result(self, result: Union[float, int, str]) -> str:
        """
        Formata o resultado para exibição.
        
        Args:
            result: Resultado a ser formatado
            
        Returns:
            str: Resultado formatado para exibição
        """
        if isinstance(result, (int, float)):
            # Se for um número inteiro, exibir sem casas decimais
            if isinstance(result, float) and result.is_integer():
                return str(int(result))
            # Caso contrário, formatar com até 10 casas decimais, removendo zeros desnecessários
            elif isinstance(result, float):
                formatted = f"{result:.10f}".rstrip('0').rstrip('.')
                return formatted if formatted else "0"
            else:
                return str(result)
        else:
            return str(result)
    
    def _validate_input(self, input_data: str) -> bool:
        """
        Valida a entrada do usuário.
        
        Args:
            input_data: Dados de entrada a serem validados
            
        Returns:
            bool: True se a entrada for válida, False caso contrário
        """
        if not input_data or not isinstance(input_data, str):
            return False
        
        # Verificar se é um número válido
        try:
            float(input_data.replace(',', '.'))
            return True
        except ValueError:
            # Verificar se é um operador válido
            return input_data in ['+', '-', '*', '/', '=', 'C', '←', '.']
    
    def process_input(self, input_data: str) -> str:
        """
        Processa entrada do usuário (números, operadores, comandos).
        
        Args:
            input_data: Entrada do usuário
            
        Returns:
            str: Valor a ser exibido no display
        """
        if not self._validate_input(input_data):
            return self.state.display_value
        
        # Processar comandos especiais
        if input_data == 'C':
            return self.clear_all()
        elif input_data == '←':
            return self._backspace()
        elif input_data == '=':
            return self._calculate()
        elif input_data in ['+', '-', '*', '/']:
            return self._set_operator(input_data)
        elif input_data == '.':
            return self._add_decimal()
        else:
            # É um número
            return self._add_digit(input_data)
    
    def _add_digit(self, digit: str) -> str:
        """
        Adiciona um dígito ao valor atual.
        
        Args:
            digit: Dígito a ser adicionado
            
        Returns:
            str: Novo valor do display
        """
        if self.state.waiting_for_operand:
            self.state.current_value = digit
            self.state.waiting_for_operand = False
        else:
            if self.state.current_value == "0":
                self.state.current_value = digit
            else:
                self.state.current_value += digit
        
        self.state.display_value = self.state.current_value
        return self.state.display_value
    
    def _add_decimal(self) -> str:
        """
        Adiciona ponto decimal ao valor atual.
        
        Returns:
            str: Novo valor do display
        """
        if self.state.waiting_for_operand:
            self.state.current_value = "0."
            self.state.waiting_for_operand = False
        elif '.' not in self.state.current_value:
            self.state.current_value += '.'
        
        self.state.display_value = self.state.current_value
        return self.state.display_value
    
    def _backspace(self) -> str:
        """
        Remove o último dígito do valor atual.
        
        Returns:
            str: Novo valor do display
        """
        if not self.state.waiting_for_operand and len(self.state.current_value) > 1:
            self.state.current_value = self.state.current_value[:-1]
        else:
            self.state.current_value = "0"
            self.state.waiting_for_operand = True
        
        self.state.display_value = self.state.current_value
        return self.state.display_value
    
    def _set_operator(self, operator: str) -> str:
        """
        Define o operador para a próxima operação.
        
        Args:
            operator: Operador matemático
            
        Returns:
            str: Valor do display
        """
        if not self.state.waiting_for_operand:
            if self.state.operator and self.state.previous_value:
                # Calcular operação pendente
                self._calculate()
            
            self.state.previous_value = self.state.current_value
        
        self.state.operator = operator
        self.state.waiting_for_operand = True
        
        return self.state.display_value
    
    def _calculate(self) -> str:
        """
        Executa o cálculo da operação atual.
        
        Returns:
            str: Resultado do cálculo ou mensagem de erro
        """
        if not self.state.operator or not self.state.previous_value:
            return self.state.display_value
        
        try:
            result = self.engine.basic_operation(
                self.state.previous_value,
                self.state.current_value,
                self.state.operator
            )
            
            operation_str = f"{self.state.previous_value} {self.state.operator} {self.state.current_value}"
            
            if result["success"]:
                formatted_result = self._format_result(result["result"])
                self.state.current_value = str(result["result"])
                self.state.display_value = formatted_result
                self.state.last_operation = f"{operation_str} = {formatted_result}"
                
                # Adicionar ao histórico
                self._add_to_history(operation_str, formatted_result, True)
            else:
                self.state.display_value = "Erro"
                self.state.last_operation = f"{operation_str} = Erro: {result['error_message']}"
                
                # Adicionar erro ao histórico
                self._add_to_history(operation_str, result["error_message"], False)
            
            # Resetar estado para próxima operação
            self.state.operator = ""
            self.state.previous_value = ""
            self.state.waiting_for_operand = True
            
            return self.state.display_value
            
        except Exception as e:
            self.state.display_value = "Erro"
            self._add_to_history(
                f"{self.state.previous_value} {self.state.operator} {self.state.current_value}",
                f"Erro interno: {str(e)}",
                False
            )
            return self.state.display_value
    
    def execute_operation(self, operation_type: str, **kwargs) -> str:
        """
        Executa uma operação específica do motor de cálculo.
        
        Args:
            operation_type: Tipo da operação a ser executada
            **kwargs: Argumentos específicos da operação
            
        Returns:
            str: Resultado formatado da operação
        """
        try:
            result = None
            operation_str = ""
            
            if operation_type == "percentage":
                number = kwargs.get("number", self.state.current_value)
                percent = kwargs.get("percent", "")
                result = self.engine.percentage(number, percent)
                operation_str = f"{percent}% de {number}"
                
            elif operation_type == "square_root":
                number = kwargs.get("number", self.state.current_value)
                result = self.engine.square_root(number)
                operation_str = f"√{number}"
                
            elif operation_type == "trigonometric":
                number = kwargs.get("number", self.state.current_value)
                function = kwargs.get("function", "sin")
                unit = kwargs.get("unit", "radians")
                result = self.engine.trigonometric(number, function, unit)
                unit_symbol = "°" if unit == "degrees" else "rad"
                operation_str = f"{function}({number}{unit_symbol})"
                
            elif operation_type == "circle_area":
                radius = kwargs.get("radius", self.state.current_value)
                result = self.engine.circle_area(radius)
                operation_str = f"Área círculo (r={radius})"
                
            elif operation_type == "sphere_volume":
                radius = kwargs.get("radius", self.state.current_value)
                result = self.engine.sphere_volume(radius)
                operation_str = f"Volume esfera (r={radius})"
                
            elif operation_type == "is_even_odd":
                number = kwargs.get("number", self.state.current_value)
                result = self.engine.is_even_odd(number)
                operation_str = f"{number} é par/ímpar?"
                
            elif operation_type == "degrees_to_radians":
                degrees = kwargs.get("degrees", self.state.current_value)
                result = self.engine.degrees_to_radians(degrees)
                operation_str = f"{degrees}° → rad"
                
            elif operation_type == "radians_to_degrees":
                radians = kwargs.get("radians", self.state.current_value)
                result = self.engine.radians_to_degrees(radians)
                operation_str = f"{radians}rad → °"
            
            if result:
                if result["success"]:
                    formatted_result = self._format_result(result["result"])
                    self.state.current_value = str(result["result"])
                    self.state.display_value = formatted_result
                    self.state.waiting_for_operand = True
                    
                    # Adicionar ao histórico
                    self._add_to_history(operation_str, formatted_result, True)
                    
                    return formatted_result
                else:
                    self.state.display_value = "Erro"
                    
                    # Adicionar erro ao histórico
                    self._add_to_history(operation_str, result["error_message"], False)
                    
                    return result["error_message"]
            
            return "Operação não reconhecida"
            
        except Exception as e:
            error_msg = f"Erro interno: {str(e)}"
            self.state.display_value = "Erro"
            self._add_to_history(operation_type, error_msg, False)
            return error_msg
    
    def get_history(self) -> List[Dict[str, Any]]:
        """
        Retorna o histórico de operações.
        
        Returns:
            List: Lista com as últimas operações realizadas
        """
        return self.history.copy()
    
    def get_formatted_history(self) -> List[str]:
        """
        Retorna o histórico formatado para exibição na interface.
        
        Returns:
            List[str]: Lista de strings formatadas com as operações
        """
        formatted_history = []
        
        for entry in self.history:
            timestamp = entry["timestamp"].strftime("%H:%M:%S")
            operation = entry["operation"]
            result = entry["result"]
            
            if entry["success"]:
                formatted_entry = f"[{timestamp}] {operation} = {result}"
            else:
                formatted_entry = f"[{timestamp}] {operation} = Erro: {result}"
            
            formatted_history.append(formatted_entry)
        
        return formatted_history
    
    def clear_history(self):
        """
        Limpa todo o histórico de operações.
        """
        self.history.clear()
    
    def get_history_summary(self) -> Dict[str, Any]:
        """
        Retorna um resumo do histórico de operações.
        
        Returns:
            Dict: Resumo com estatísticas do histórico
        """
        total_operations = len(self.history)
        successful_operations = sum(1 for entry in self.history if entry["success"])
        failed_operations = total_operations - successful_operations
        
        last_operation_time = None
        if self.history:
            last_operation_time = self.history[-1]["timestamp"]
        
        return {
            "total_operations": total_operations,
            "successful_operations": successful_operations,
            "failed_operations": failed_operations,
            "last_operation_time": last_operation_time,
            "max_history_size": self.max_history_size
        }
    
    def clear_all(self) -> str:
        """
        Limpa todos os valores e reseta a calculadora.
        
        Returns:
            str: Valor do display após limpeza (sempre "0")
        """
        self.state.reset()
        return self.state.display_value
    
    def get_current_display(self) -> str:
        """
        Retorna o valor atual do display.
        
        Returns:
            str: Valor atual do display
        """
        return self.state.display_value
    
    def get_last_operation(self) -> str:
        """
        Retorna a última operação realizada.
        
        Returns:
            str: Descrição da última operação
        """
        return self.state.last_operation