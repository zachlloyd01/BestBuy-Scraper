import time
from selenium import webdriver
from selenium.webdriver.support.ui import Select



'''
    Make sure Chrome version 88
    FILL OUT VARIABLES BELOW, PLEASE!
'''

first_name = ''
last_name = ''

email_address = ''
phone_number = '' # Must be real number!

street_address = ''
zip_code = ''
city = ''
state = '' # Preset to Georgia

# Payment info goes here!
credit_card = '' #Make sure!
exp_month = ''
exp_year = ''
sec_code = ''

options = webdriver.ChromeOptions()
options.add_argument('--ignore-certificate-errors')
options.add_argument('--ignore-certificate-errors-spki-list')
options.add_argument("--log-level=3");

options.add_argument('--ignore-ssl-errors')

browser = webdriver.Chrome(chrome_options=options, executable_path='chromedriver') # Web driver to open

item_url = 'https://www.bestbuy.com/site/sony-playstation-5-console/6426149.p?skuId=6426149' # Go to this page

browser.get(item_url)

buy_button = False # Flag for loop

def auto_checkout():

    '''
        Checkout using given CC info
    '''

    time.sleep(2)
    browser.find_element_by_class_name('go-to-cart-button').find_element_by_tag_name('a').click()
    print('in cart page')

    time.sleep(1)

    time.sleep(1)
    browser.find_element_by_class_name('btn-primary').click()

    time.sleep(5)
    browser.find_element_by_class_name('cia-secondary-content-v2').find_element_by_class_name('button-wrap').find_element_by_tag_name('button').click()

    time.sleep(2)
    browser.find_element_by_class_name('ispu-card__switch').click()

    time.sleep(6) #Ensure page laods, slow under load...

    browser.find_element_by_id('consolidatedAddresses.ui_address_5.firstName').send_keys(first_name)

    time.sleep(1)
    browser.find_element_by_id('consolidatedAddresses.ui_address_5.lastName').send_keys(last_name)

    time.sleep(1)
    browser.find_element_by_id('consolidatedAddresses.ui_address_5.street').send_keys(street_address)

    time.sleep(1)
    browser.find_element_by_id('consolidatedAddresses.ui_address_5.city').send_keys(city)

    time.sleep(1)
    Select(browser.find_element_by_id('consolidatedAddresses.ui_address_5.state')).select_by_visible_text(state)

    time.sleep(1)
    browser.find_element_by_id('consolidatedAddresses.ui_address_5.zipcode').send_keys(zip_code)

    time.sleep(1)
    browser.find_element_by_id('user.emailAddress').send_keys(email_address)

    time.sleep(1)
    browser.find_element_by_id('user.phone').send_keys(phone_number)

    time.sleep(1)
    browser.find_element_by_class_name('button--continue').find_element_by_tag_name('button').click()

    time.sleep(3)

    try:
        '''
            If this works, then checkout is address-checking
        '''
        browser.find_element_by_class_name('modal-body').find_element_by_class_name('btn-secondary').click()

    except:
        '''
            Do not need to confirm address
        '''
        pass

    time.sleep(2)
    browser.find_element_by_id('optimized-cc-card-number').send_keys(credit_card)

    time.sleep(1)
    Select(browser.find_element_by_name('expiration-month')).select_by_visible_text(exp_month)

    time.sleep(1)
    Select(browser.find_element_by_name('expiration-year')).select_by_visible_text(exp_year)

    time.sleep(1)
    browser.find_element_by_id('credit-card-cvv').send_keys(sec_code)

    time.sleep(2)
    browser.find_element_by_class_name('btn-primary').click() # Done!

    time.sleep(10)
    quit() # End the program

while not buy_button:
    try:
        '''
            If this works, then item is not in stock
        '''
        add_to_cart = browser.find_element_by_class_name("btn-disabled")

        print("Item not in stock!")

        '''
            Refresh page after small delay
        '''
        time.sleep(1)
        browser.refresh()
    except:
        add_to_cart = browser.find_element_by_class_name("btn-primary")

        #Click the button
        add_to_cart.click()
        print("Button was clicked.")
        buy_button = True

        time.sleep(2)
        auto_checkout()
