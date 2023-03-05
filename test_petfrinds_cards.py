import pytest
from selenium import webdriver

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC



def test_show_my_pets():
    # неявное ожидание 5 сек. при каждом шаге

    pytest.driver = webdriver.Chrome()
    pytest.driver.implicitly_wait(5)





    # Нажимаем на кнопку для перехода к списку своих питомцев
    pytest.driver.find_element_by_xpath('//*[@href="/my_pets"]').click()

    # явное ожидание 10 сек.
    WebDriverWait(pytest.driver, 10).until(EC.presence_of_element_located((By.ID, 'all_my_pets')))

    # Проверяем, что мы оказались на странице со списком своих питомцев
    assert pytest.driver.find_element_by_tag_name('h2').text == "Bobik"

    # объявляем 4 переменные, в которых записываем все найденные элементы на странице:
    # в images — все картинки питомцев,
    # в names — все их имена,
    # в breeds — все породы животных,
    # в years - все возрасты
    images = pytest.driver.find_elements_by_xpath('//*[@id="all_my_pets"]//img')
    names = pytest.driver.find_elements_by_xpath('//*[@id="all_my_pets"]/table/tbody/tr/td[1]')
    breeds = pytest.driver.find_elements_by_xpath('//*[@id="all_my_pets"]/table/tbody/tr/td[2]')
    years = pytest.driver.find_elements_by_xpath('//*[@id="all_my_pets"]/table/tbody/tr/td[3]')

    # объявляем переменную, в которую записываем текстовое значение элемента на странице,
    # в котором содержится информация об общем количестве питомцев пользователя
    my_pets = pytest.driver.find_element_by_xpath('/html/body/div[1]/div/div[1]').text
    # строку преобразуем в список
    list_my_pets = my_pets.split()

    # Проверяем, что на странице присутствуют все питомцы пользователя
    # общее количество питомцев пользователя равно длине списка имен
    assert int(list_my_pets[2]) == len(names)

    images1 = []
    for i in range(len(images)):
        if images[i].get_attribute('src') != '':
            images1.append(images[i])

    # Проверяем, что хотя бы у половины питомцев есть фото
    assert len(images1) >= int(list_my_pets[2]) / 2

