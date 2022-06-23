

def print_func_name(func):
    print('Function name:\n ' + func.__name__.capitalize().replace('_', ' '))
    if func.__code__.co_varnames:
        print('arguments:')
    else:
        print('no arguments')
    for arg in func.__code__.co_varnames:
        print(' - ' + arg)
    else:
        print('-------------')



def open_browser(browser='chrome'):
    pass


def go_to_companyname_homepage(company_name, region):
    pass


def find_registration_button_on_login_page():
    pass

l = [open_browser, go_to_companyname_homepage, find_registration_button_on_login_page]

for i in l:
    print_func_name(i)
