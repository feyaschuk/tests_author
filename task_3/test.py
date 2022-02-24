import sys, pytest
import subprocess

''' раскомментировать для проверки precode.py, сейчас проверяет author.py '''
#from precode import time_check, cache_args, long_heavy 
from author import time_check, cache_args, long_heavy     

#cmd= "python precode.py"
cmd = 'python author.py'
p = subprocess.Popen(cmd, stdout = open('output.txt', 'w'))


@pytest.mark.xfail
def test_wrong_type():
    """ Должно возникнуть исключение при недостающих параметрах."""
    with pytest.raises(TypeError):
        from precode import time_check, cache_args, long_heavy

@pytest.mark.xfail
def test_errors_raises():
    """Убедитесь, что файл precode.py импортируется без ошибок."""
    try: 
        from precode import time_check, cache_args, long_heavy
    except: 
        e = sys.exc_info()[1]
        assert e.args[0] == None

@time_check
@cache_args
def some_view(mocker):
    pass

@pytest.mark.parametrize("x", [1,1])
def test_some_view_1(mocker, x):
    """ Проверка №1 результата функции long_heavy и декораторов."""
    """ Для проверки работы студента нужно раскомментировать"""
    '''строку precode.long_heavy и закомментировать -author.long_heavy'''

    mocker.patch(
    ### 'precode.long_heavy', 
        'author.long_heavy',      
        return_value=2)          
    excpected = 2
    actual = long_heavy(x)        
    assert excpected == actual 
      
@pytest.mark.parametrize("x", [2,2,2])
def test_some_view_2(mocker,x):
    """ Проверка №2 результата функции long_heavy и декораторов."""
    mocker.patch(
        ### 'precode.long_heavy',   
        'author.long_heavy',  
        return_value=4)        
    excpected = 4
    actual = long_heavy(x)        
    assert excpected == actual 

def test_print_result():    
    """ Проверка корректного вывода функции print """
    """ Для проверки работы студента нужно раскомментировать"""
    '''строку cmd = python precode.py и закомментировать - cmd = python author.py'''

    ###cmd = 'python precode.py'    
    cmd = 'python author.py'                
    p = subprocess.Popen(cmd, stdout=subprocess.PIPE) 
    output = p.stdout.read().decode()    
    
    assert output == (
    "Время выполнения функции: 1.0 с.\r\n"
    "2\r\n"
    "Время выполнения функции: 0.0 с.\r\n"
    "2\r\n"
    "Время выполнения функции: 1.0 с.\r\n"
    "4\r\n"
    "Время выполнения функции: 0.0 с.\r\n"
    "4\r\n"
    "Время выполнения функции: 0.0 с.\r\n"
    "4\r\n")
    
        
        