from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time


def load_driver():
    ''' Opens Chrome driver and sets the ICGEM website
    '''
    # r/Users/admin/Learn_Python2/Hashtag_Lira/Plataforma_Ensino/Automation_Python-Web/chromedriver
    # executable_path=path)
    browser = webdriver.Chrome(ChromeDriverManager().install())
    browser.get("http://icgem.gfz-potsdam.de/home")
    time.sleep(2)
    browser.find_element(By.CSS_SELECTOR, '#menu > a:nth-child(7)').click()
    time.sleep(5)
    return browser


def model_type_selection(browser):
    ''' Selects the kind of model as follows:

             1- Longtime Model \n
             2- Model from Series \n
             3- Topography related Model \n
             4- Celestial Object Model \n
             5- Topography \n

    input >
    browser:            webdriver.Chrome instance
    '''
    dic_tipo = {
        '1': 'Longtime Model',
        '2': 'Model from Series',
        '3': 'Topography related Model',
        '4': 'Celestial Object Model',
        '5': 'Topography',
    }
    type_model_window = browser.find_element(By.NAME, 'sel_type')
    type_model_window.click()
    sec = False
    while sec == False:
        tipo = input(""" \n Select the number related to the desired type of model \n
        \t \t 1- Longtime Model \n
        \t \t 2- Model from Series \n
        \t \t 3- Topography related Model \n
        \t \t 4- Celestial Object Model \n
        \t \t 5- Topography \n
        """)
        if tipo.isdigit() or int(tipo) in range(1, 6):
            sec = True
        else:
            print("Please select one of the displayed numbers!")
    for model_index in dic_tipo.keys():
        if model_index == tipo:
            tipo = dic_tipo[model_index]
    tags = type_model_window.find_elements_by_tag_name('option')
    for i, tag in enumerate(tags):
        if tag.text == tipo:
            tag.click()
    time.sleep(2)
    return tipo


def model_selection(browser, tipo):
    ''' Selects the model

    input >
    browser:            webdriver.Chrome instance
    model_name:         string of the model name
    '''
    #model_name = input('Download data from which model?')
    model_name = 'EIGEN-6C4'
    model_window = browser.find_element_by_class_name('col')
    model_window.click()
    model_window.send_keys(model_name)
    time.sleep(3)


def functional_selection(browser):
    ''' Selects the functional observable to be downloaded

    input >
    browser:            webdriver.Chrome instance
    functional:         string of the functional name
    '''
    #functional = input('Data should be from which observable?')
    functional = 'gravity_earth'
    functional_window = browser.find_element_by_name('sel_func')
    functional_window.click()
    functional_window.send_keys(functional)
    time.sleep(3)


def grid_selection(browser):
    ''' Sets the area from which the data is related to

    input >
    browser:            webdriver.Chrome instance
    '''
    # Left Latitude
    #latitude_esq = input('Enter left latitude limit of the grid...')
    latitude_esq = str(-75)
    browser.find_element_by_name('grid_left').click()
    browser.find_element_by_name('grid_left').click()
    browser.find_element_by_name('grid_left').send_keys(Keys.END)
    browser.find_element_by_name('grid_left').send_keys(Keys.BACKSPACE)
    browser.find_element_by_name('grid_left').send_keys(Keys.BACKSPACE)
    browser.find_element_by_name('grid_left').send_keys(Keys.BACKSPACE)
    browser.find_element_by_name('grid_left').send_keys(Keys.BACKSPACE)
    browser.find_element_by_name('grid_left').send_keys(latitude_esq)  # '-75'
    time.sleep(2)
    # Right Latitude
    #latitude_dir = input('Enter right latitude limit of the grid...')
    latitude_dir = str(-32)
    browser.find_element_by_name('grid_right').click()
    browser.find_element_by_name('grid_right').send_keys(Keys.END)
    browser.find_element_by_name('grid_right').send_keys(Keys.BACKSPACE)
    browser.find_element_by_name('grid_right').send_keys(Keys.BACKSPACE)
    browser.find_element_by_name('grid_right').send_keys(Keys.BACKSPACE)
    browser.find_element_by_name('grid_right').send_keys(Keys.BACKSPACE)
    browser.find_element_by_name('grid_right').send_keys('-32')  # '-32'
    time.sleep(2)
    # Upper Longitude
    #longitude_acima = input('Enter top longitude limit of the grid...')
    longitude_acima = str(6)
    browser.find_element_by_name('grid_top').click()
    browser.find_element_by_name('grid_top').send_keys(Keys.END)
    browser.find_element_by_name('grid_top').send_keys(Keys.BACKSPACE)
    browser.find_element_by_name('grid_top').send_keys(Keys.BACKSPACE)
    browser.find_element_by_name('grid_top').send_keys(Keys.BACKSPACE)
    browser.find_element_by_name('grid_top').send_keys(Keys.BACKSPACE)
    browser.find_element_by_name('grid_top').send_keys(longitude_acima)  # '6'
    time.sleep(2)
    # Lower Longitude
    #longitude_abaixo = input('Enter bottom longitude limit of the grid...')
    longitude_abaixo = str(-35)
    browser.find_element_by_name('grid_bottom').click()
    browser.find_element_by_name('grid_bottom').send_keys(Keys.END)
    browser.find_element_by_name('grid_bottom').send_keys(Keys.BACKSPACE)
    browser.find_element_by_name('grid_bottom').send_keys(Keys.BACKSPACE)
    browser.find_element_by_name('grid_bottom').send_keys(Keys.BACKSPACE)
    browser.find_element_by_name('grid_bottom').send_keys(Keys.BACKSPACE)
    browser.find_element_by_name('grid_bottom').send_keys(
        longitude_abaixo)  # '-35'
    time.sleep(2)
    # Grid Step
    espacamento = input('Enter grid spacing...')
    browser.find_element_by_name('grid_step').click()
    browser.find_element_by_name('grid_step').send_keys(Keys.END)
    browser.find_element_by_name('grid_step').send_keys(Keys.BACKSPACE)
    browser.find_element_by_name('grid_step').send_keys(Keys.BACKSPACE)
    browser.find_element_by_name('grid_step').send_keys(Keys.BACKSPACE)
    browser.find_element_by_name('grid_step').send_keys(Keys.BACKSPACE)
    browser.find_element_by_name('grid_step').send_keys(espacamento)  # '2'
    time.sleep(2)


def click_start_computation(browser):
    ''' Clicks on Start Computation button and waits until data is fully calculated
    for download on the new tab

    input >
    browser:            webdriver.Chrome instance
    '''
    submit = browser.find_elements_by_tag_name('input')[-1]
    submit.click()

    browser.switch_to.window(browser.window_handles[-1])
    print(browser.title)
    print(browser.find_element_by_link_text('Download Grid').text)
    print(browser.find_element_by_xpath(
        '/html/body/div[3]/div/div[1]/table/tbody/tr[7]/td/b[1]/a'
    ).text)
    input()
    while str(100) not in browser.find_element_by_id('progress_bar').get_attribute('style'):
        time.sleep(1)
    browser.find_element_by_link_text('Download Grid').click()
    browser.find_element_by_xpath(
        '/html/body/div[3]/div/div[1]/table/tbody/tr[7]/td/b[1]/a').click()


def download_regular_icgem():
    ''' Manages the whole process of downloading the desired gridded data from ICGEM
    '''
    browser = load_driver()
    model_type_selection(browser)
    model_selection(browser)
    functional_selection(browser)
    grid_selection(browser)
    click_start_computation(browser)
