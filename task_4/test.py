import pytest
import sys
import subprocess

from author import make_divider_of

''' раскомментировать для проверки precode.py, сейчас проверяет author.py '''
#from precode import make_divider_of

#cmd= "python precode.py"
cmd = 'python author.py'
p = subprocess.Popen(cmd, stdout = open('output.txt', 'w'))

"""Запись кода студента в файл usercode.txt"""
f_in = open('precode.py', 'r') 
data = f_in.read()
f_out = open('usercode.txt', 'w')
f_out.write(str(data))
f_out.close() 

expected = [5.0, 4.0, 2.0]   
expected_string = '5.0\n4.0\n2.0\n'

divider = 2        
divider_1 = 5   
divisible = 10
divisible_1 = 20

@pytest.fixture()
def div2():
    return make_divider_of(divider)

@pytest.fixture()
def div5():          
    return make_divider_of(divider_1)


def test_errors_raises():
    """Убедитесь, что файл precode.py импортируется без ошибок."""
    try: 
        import author  
    except: 
        e = sys.exc_info()[1]
        assert e.args[0] == None


def test_wrong_type(div2, div5):
    """ Должно возникнуть исключение с неправильным типом param."""
    with pytest.raises(TypeError):
        div2('abc')
        div5('abc')

def test_div2(div2):  
    """ Проверка результата div2 """   
    assert(div2(divisible))== expected[0], 'Проверьте результат 1 функции'

def test_div5(div5):   
    """ Проверка результата div5 """    
    assert(div5(divisible_1))== expected[1], 'Проверьте результат 2 функции'

def test_mix(div5, div2):
    """ Проверка результата div5(div2())) """       
    assert(div5(div2(divisible_1)))== expected[2], 'Проверьте результат 3 функции'

def test_new_print():
    """ Проверка вывода функции print """ 
    with open('output.txt') as f:
        text = f.read()          
        assert text  == expected_string, 'Проверьте вывод сообщения о результате'   

def test_function_name():
    """ Проверка вывода функции print """ 
    with open('usercode.txt') as f:
        text = f.read()          
        assert 'def make_divider_of(divider):' in text, 'Проверьте название основной функции'
        assert 'def division_operation(divisible):' in text, 'Проверьте название вложенной функции'
    
    
        
        
        