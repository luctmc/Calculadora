"""
Motor de Cálculo da Calculadora Moderna

Este módulo contém a classe CalculatorEngine que implementa todas as operações
matemáticas da calculadora, incluindo operações básicas, funções avançadas,
cálculos geométricos e trigonométricos.
"""

import math
from typing import Dict, Union, Any


class CalculatorEngine:
    """
    Motor de cálculo responsável por todas as operações matemáticas.
    
    Esta classe implementa operações básicas (+, -, *, /), funções matemáticas
    avançadas, cálculos geométricos e validação de entrada.
    """
    
    def __init__(self):
        """Inicializa o motor de cálculo."""
        pass
    
    def _validate_number(self, value: Any) -> bool:
        """
        Valida se o valor é um número válido.
        
        Args:
            value: Valor a ser validado
            
        Returns:
            bool: True se for um número válido, False caso contrário
        """
        try:
            float(value)
            return True
        except (ValueError, TypeError):
            return False
    
    def _create_response(self, success: bool, result: Union[float, str] = None, 
                        error_message: str = None, formula_used: str = None,
                        operation_type: str = "") -> Dict[str, Any]:
        """
        Cria uma resposta padronizada para as operações.
        
        Args:
            success: Se a operação foi bem-sucedida
            result: Resultado da operação
            error_message: Mensagem de erro, se houver
            formula_used: Fórmula utilizada no cálculo
            operation_type: Tipo da operação realizada
            
        Returns:
            Dict: Resposta padronizada
        """
        return {
            "success": success,
            "result": result,
            "error_message": error_message,
            "formula_used": formula_used,
            "operation_type": operation_type
        }
    
    def basic_operation(self, num1: Union[float, str], num2: Union[float, str], 
                       operator: str) -> Dict[str, Any]:
        """
        Executa operações matemáticas básicas (+, -, *, /).
        
        Args:
            num1: Primeiro número
            num2: Segundo número
            operator: Operador (+, -, *, /)
            
        Returns:
            Dict: Resultado da operação ou erro
        """
        # Validar entradas
        if not self._validate_number(num1):
            return self._create_response(
                False, 
                error_message="Primeiro número inválido",
                operation_type="basic_operation"
            )
        
        if not self._validate_number(num2):
            return self._create_response(
                False,
                error_message="Segundo número inválido", 
                operation_type="basic_operation"
            )
        
        if operator not in ['+', '-', '*', '/']:
            return self._create_response(
                False,
                error_message="Operador inválido. Use +, -, * ou /",
                operation_type="basic_operation"
            )
        
        try:
            n1 = float(num1)
            n2 = float(num2)
            
            if operator == '+':
                result = n1 + n2
            elif operator == '-':
                result = n1 - n2
            elif operator == '*':
                result = n1 * n2
            elif operator == '/':
                if n2 == 0:
                    return self._create_response(
                        False,
                        error_message="Erro: Divisão por zero não é permitida",
                        operation_type="basic_operation"
                    )
                result = n1 / n2
            
            # Formatar resultado para até 10 casas decimais
            if result == int(result):
                result = int(result)
            else:
                result = round(result, 10)
            
            return self._create_response(
                True,
                result=result,
                formula_used=f"{n1} {operator} {n2}",
                operation_type="basic_operation"
            )
            
        except (ValueError, OverflowError) as e:
            return self._create_response(
                False,
                error_message=f"Erro no cálculo: {str(e)}",
                operation_type="basic_operation"
            )
    
    def percentage(self, number: Union[float, str], percent: Union[float, str]) -> Dict[str, Any]:
        """
        Calcula a porcentagem de um número.
        
        Args:
            number: Número base
            percent: Porcentagem a ser calculada
            
        Returns:
            Dict: Resultado do cálculo de porcentagem
        """
        if not self._validate_number(number) or not self._validate_number(percent):
            return self._create_response(
                False,
                error_message="Valores inválidos para cálculo de porcentagem",
                operation_type="percentage"
            )
        
        try:
            n = float(number)
            p = float(percent)
            result = (n * p) / 100
            
            if result == int(result):
                result = int(result)
            else:
                result = round(result, 10)
            
            return self._create_response(
                True,
                result=result,
                formula_used=f"{p}% de {n}",
                operation_type="percentage"
            )
            
        except (ValueError, OverflowError) as e:
            return self._create_response(
                False,
                error_message=f"Erro no cálculo de porcentagem: {str(e)}",
                operation_type="percentage"
            )
    
    def square_root(self, number: Union[float, str]) -> Dict[str, Any]:
        """
        Calcula a raiz quadrada de um número.
        
        Args:
            number: Número para calcular a raiz quadrada
            
        Returns:
            Dict: Resultado da raiz quadrada ou erro
        """
        if not self._validate_number(number):
            return self._create_response(
                False,
                error_message="Valor inválido para raiz quadrada",
                operation_type="square_root"
            )
        
        try:
            n = float(number)
            
            if n < 0:
                return self._create_response(
                    False,
                    error_message="Erro: Raiz quadrada de número negativo não é permitida",
                    operation_type="square_root"
                )
            
            result = math.sqrt(n)
            
            if result == int(result):
                result = int(result)
            else:
                result = round(result, 10)
            
            return self._create_response(
                True,
                result=result,
                formula_used=f"√{n}",
                operation_type="square_root"
            )
            
        except (ValueError, OverflowError) as e:
            return self._create_response(
                False,
                error_message=f"Erro no cálculo da raiz quadrada: {str(e)}",
                operation_type="square_root"
            )
    
    def trigonometric(self, number: Union[float, str], function: str,
                     unit: str = "degrees") -> Dict[str, Any]:
        """
        Calcula funções trigonométricas (seno, cosseno, tangente).
        
        Args:
            number: Ângulo para o cálculo
            function: Função trigonométrica (sin, cos, tan)
            unit: Unidade do ângulo (radians ou degrees)
            
        Returns:
            Dict: Resultado da função trigonométrica
        """
        if not self._validate_number(number):
            return self._create_response(
                False,
                error_message="Valor inválido para função trigonométrica",
                operation_type="trigonometric"
            )
        
        if function not in ['sin', 'cos', 'tan']:
            return self._create_response(
                False,
                error_message="Função trigonométrica inválida. Use sin, cos ou tan",
                operation_type="trigonometric"
            )
        
        if unit not in ['radians', 'degrees']:
            return self._create_response(
                False,
                error_message="Unidade inválida. Use 'radians' ou 'degrees'",
                operation_type="trigonometric"
            )

        try:
            n = float(number)

            # Converter graus para radianos se necessário
            if unit == "degrees":
                n = math.radians(n)

            if function == 'sin':
                result = math.sin(n)
            elif function == 'cos':
                result = math.cos(n)
            elif function == 'tan':
                result = math.tan(n)

            # Arredondar para evitar problemas de precisão
            result = round(result, 10)

            unit_symbol = "°" if unit == "degrees" else "rad"
            return self._create_response(
                True,
                result=result,
                formula_used=f"{function}({float(number)}{unit_symbol})",
                operation_type="trigonometric"
            )
            
        except (ValueError, OverflowError) as e:
            return self._create_response(
                False,
                error_message=f"Erro no cálculo trigonométrico: {str(e)}",
                operation_type="trigonometric"
            )
    
    def degrees_to_radians(self, degrees: Union[float, str]) -> Dict[str, Any]:
        """
        Converte graus para radianos.
        
        Args:
            degrees: Ângulo em graus
            
        Returns:
            Dict: Ângulo convertido para radianos
        """
        if not self._validate_number(degrees):
            return self._create_response(
                False,
                error_message="Valor inválido para conversão",
                operation_type="degrees_to_radians"
            )
        
        try:
            d = float(degrees)
            result = math.radians(d)
            result = round(result, 10)
            
            return self._create_response(
                True,
                result=result,
                formula_used=f"{d}° → rad",
                operation_type="degrees_to_radians"
            )
            
        except (ValueError, OverflowError) as e:
            return self._create_response(
                False,
                error_message=f"Erro na conversão: {str(e)}",
                operation_type="degrees_to_radians"
            )
    
    def radians_to_degrees(self, radians: Union[float, str]) -> Dict[str, Any]:
        """
        Converte radianos para graus.
        
        Args:
            radians: Ângulo em radianos
            
        Returns:
            Dict: Ângulo convertido para graus
        """
        if not self._validate_number(radians):
            return self._create_response(
                False,
                error_message="Valor inválido para conversão",
                operation_type="radians_to_degrees"
            )
        
        try:
            r = float(radians)
            result = math.degrees(r)
            result = round(result, 10)
            
            return self._create_response(
                True,
                result=result,
                formula_used=f"{r}rad → °",
                operation_type="radians_to_degrees"
            )
            
        except (ValueError, OverflowError) as e:
            return self._create_response(
                False,
                error_message=f"Erro na conversão: {str(e)}",
                operation_type="radians_to_degrees"
            )
    
    def circle_area(self, radius: Union[float, str]) -> Dict[str, Any]:
        """
        Calcula a área do círculo usando a fórmula A = πr².
        
        Args:
            radius: Raio do círculo
            
        Returns:
            Dict: Resultado do cálculo da área ou erro
        """
        if not self._validate_number(radius):
            return self._create_response(
                False,
                error_message="Valor inválido para o raio",
                operation_type="circle_area"
            )
        
        try:
            r = float(radius)
            
            if r < 0:
                return self._create_response(
                    False,
                    error_message="Erro: O raio deve ser um valor positivo",
                    operation_type="circle_area"
                )
            
            result = math.pi * r * r
            result = round(result, 10)
            
            return self._create_response(
                True,
                result=result,
                formula_used=f"A = πr² = π × {r}²",
                operation_type="circle_area"
            )
            
        except (ValueError, OverflowError) as e:
            return self._create_response(
                False,
                error_message=f"Erro no cálculo da área do círculo: {str(e)}",
                operation_type="circle_area"
            )
    
    def sphere_volume(self, radius: Union[float, str]) -> Dict[str, Any]:
        """
        Calcula o volume da esfera usando a fórmula V = (4/3)πr³.
        
        Args:
            radius: Raio da esfera
            
        Returns:
            Dict: Resultado do cálculo do volume ou erro
        """
        if not self._validate_number(radius):
            return self._create_response(
                False,
                error_message="Valor inválido para o raio",
                operation_type="sphere_volume"
            )
        
        try:
            r = float(radius)
            
            if r < 0:
                return self._create_response(
                    False,
                    error_message="Erro: O raio deve ser um valor positivo",
                    operation_type="sphere_volume"
                )
            
            result = (4/3) * math.pi * r * r * r
            result = round(result, 10)
            
            return self._create_response(
                True,
                result=result,
                formula_used=f"V = (4/3)πr³ = (4/3)π × {r}³",
                operation_type="sphere_volume"
            )
            
        except (ValueError, OverflowError) as e:
            return self._create_response(
                False,
                error_message=f"Erro no cálculo do volume da esfera: {str(e)}",
                operation_type="sphere_volume"
            )
    
    def is_even_odd(self, number: Union[int, str]) -> Dict[str, Any]:
        """
        Verifica se um número é par ou ímpar.
        
        Args:
            number: Número inteiro para verificação
            
        Returns:
            Dict: Resultado da verificação (par ou ímpar) ou erro
        """
        if not self._validate_number(number):
            return self._create_response(
                False,
                error_message="Valor inválido para verificação par/ímpar",
                operation_type="is_even_odd"
            )
        
        try:
            n = float(number)
            
            # Verificar se é um número inteiro
            if n != int(n):
                return self._create_response(
                    False,
                    error_message="Erro: Apenas números inteiros são aceitos para verificação par/ímpar",
                    operation_type="is_even_odd"
                )
            
            n = int(n)
            
            # Determinar se é par ou ímpar
            if n % 2 == 0:
                result = "par"
            else:
                result = "ímpar"
            
            return self._create_response(
                True,
                result=result,
                formula_used=f"{n} é {result}",
                operation_type="is_even_odd"
            )
            
        except (ValueError, OverflowError) as e:
            return self._create_response(
                False,
                error_message=f"Erro na verificação par/ímpar: {str(e)}",
                operation_type="is_even_odd"
            )