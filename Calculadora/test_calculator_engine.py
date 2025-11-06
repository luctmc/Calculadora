"""
Testes básicos para verificar o funcionamento do CalculatorEngine
"""

from calculator_engine import CalculatorEngine

def test_basic_operations():
    """Testa operações básicas do motor de cálculo"""
    engine = CalculatorEngine()
    
    # Teste de adição
    result = engine.basic_operation(2, 3, '+')
    print(f"2 + 3 = {result}")
    assert result['success'] == True
    assert result['result'] == 5
    
    # Teste de subtração
    result = engine.basic_operation(10, 4, '-')
    print(f"10 - 4 = {result}")
    assert result['success'] == True
    assert result['result'] == 6
    
    # Teste de multiplicação
    result = engine.basic_operation(3, 7, '*')
    print(f"3 * 7 = {result}")
    assert result['success'] == True
    assert result['result'] == 21
    
    # Teste de divisão
    result = engine.basic_operation(15, 3, '/')
    print(f"15 / 3 = {result}")
    assert result['success'] == True
    assert result['result'] == 5
    
    # Teste de divisão por zero
    result = engine.basic_operation(10, 0, '/')
    print(f"10 / 0 = {result}")
    assert result['success'] == False
    assert "Divisão por zero" in result['error_message']
    
    print("✓ Testes de operações básicas passaram!")

def test_advanced_functions():
    """Testa funções matemáticas avançadas"""
    engine = CalculatorEngine()
    
    # Teste de porcentagem
    result = engine.percentage(100, 25)
    print(f"25% de 100 = {result}")
    assert result['success'] == True
    assert result['result'] == 25
    
    # Teste de raiz quadrada
    result = engine.square_root(16)
    print(f"√16 = {result}")
    assert result['success'] == True
    assert result['result'] == 4
    
    # Teste de raiz quadrada de número negativo
    result = engine.square_root(-4)
    print(f"√(-4) = {result}")
    assert result['success'] == False
    assert "número negativo" in result['error_message']
    
    # Teste de função trigonométrica
    result = engine.trigonometric(0, 'sin', 'radians')
    print(f"sin(0) = {result}")
    assert result['success'] == True
    assert result['result'] == 0
    
    print("✓ Testes de funções avançadas passaram!")

if __name__ == "__main__":
    test_basic_operations()
    test_advanced_functions()
    print("\n✓ Todos os testes passaram! Motor de cálculo funcionando corretamente.")