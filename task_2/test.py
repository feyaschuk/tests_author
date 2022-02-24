from author import Contact
''' раскомментировать для проверки precode.py, сейчас проверяет author.py '''
#from precode import Contact
import pytest
import sys
import subprocess

cmd = 'python author.py'
p = subprocess.Popen(cmd, stdout = open('output.txt', 'w'))
   
exspected_class_fields =  ['name', 'phone', 'birthday', 'address']
mike = Contact("Михаил Булгаков", "2-03-27", "15.05.1891", "Россия, Москва, Большая Пироговская, дом 35б, кв. 6")
vlad = Contact("Владимир Маяковский", "73-88", "19.07.1893", "Россия, Москва, Лубянский проезд, д. 3, кв. 12")       

@pytest.fixture()
def list_objects(): 
    """ Создание и получение объектов Contact """ 
    object_list =[mike, vlad]
    for el in object_list:        
        return el 

@pytest.fixture()
def get_fields(list_objects): 
    """ Получение списка полей объектов Contact """      
    fields_list =[]
    for key in list_objects.__dict__.keys():
        fields_list.append(key) 
    return fields_list


def test_errors_raises():
    """Убедитесь, что файл precode.py импортируется без ошибок."""
    try: 
        import precode   
    except: 
        e = sys.exc_info()[1]
        assert e.args[0] == None

def test_empty():
    """ Проверка создания пустого объекта """ 
    with pytest.raises(TypeError):
        Contact()
 
def test_create_class():  
    """ Проверка класса объекта """   
    assert isinstance(mike, Contact) == True, 'Проверьте что обьект создан и с верным именем класса'
    assert isinstance(vlad, Contact) == True, 'Проверьте что обьект создан и с верным именем класса'
    
def test_fields(get_fields): 
    """ Проверка полей объекта """           
    assert get_fields == exspected_class_fields, 'Проверьте, что поля класса совпадают с заданными в precode'      

def test_class_methods():
    """ Проверка метода объекта """ 
    test_method = "".join(map(str, [arg for arg in dir(Contact) if not arg.startswith('_')]))
    assert test_method=='show_contact', 'Проверьте что метод show_contact существует'
 
def test_print():
    """ Проверка вывода функции print """ 
    """ Для проверки работы студента нужно раскомментировать"""
    '''строку cmd = python precode.py и закомментировать - cmd = python author.py'''

    ###cmd = 'python precode.py'    
    cmd = 'python author.py'                
    p = subprocess.Popen(cmd, stdout=subprocess.PIPE)
    expected = ['Создаём новый контакт Михаил Булгаков\r\n', 'Создаём новый контакт Владимир Маяковский\r\n', 'Михаил Булгаков — адрес: Россия, Москва, Большая Пироговская, дом 35б, кв. 6, телефон: 2-03-27, день рождения: 15.05.1891\r\n', 'Владимир Маяковский — адрес: Россия, Москва, Лубянский проезд, д. 3, кв. 12, телефон: 73-88, день рождения: 19.07.1893\r\n']
    line_1 = p.stdout.readline().decode()         
    assert ("".join(line_1)) == expected[0], 'Проверьте вывод сообщения при создании контакта Булгакова'   
    line_2 = p.stdout.readline().decode()
    assert ("".join(line_2)) == expected[1], 'Проверьте вывод сообщения при создании контакта Маяковского'     
    line_3 = p.stdout.readline().decode()   
    assert ("".join(line_3)) == expected[2], 'Проверьте вывод при вызове show_contact для Булгакова'      
    line_4 = p.stdout.readline().decode()
    assert ("".join(line_4)) == expected[3], 'Проверьте вывод при вызове show_contact для Маяковского'
    