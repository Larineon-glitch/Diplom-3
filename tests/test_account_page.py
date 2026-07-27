from page_objects.account_page import AccountPage
from page_objects.main_page import MainPage
from conftest import *
import allure


class TestAccountPage:

    @allure.title('Проверка перехода в личный кабинет')
    @allure.description('Проверка доступа к личному кабинету после авторизации')
    def test_navigate_to_personal_account_success(self, driver, create_new_user_and_delete):
        main_page = MainPage(driver)
        account_page = AccountPage(driver)
        
        # Авторизация
        user_credentials = create_new_user_and_delete[0]
        main_page.login(user_credentials['email'], user_credentials['password'])
        
        main_page.click_on_personal_account_in_header()
        
        # Проверка: кнопка "Выйти" отображается
        assert account_page.check_logout_button_displayed()
        

    @allure.title('Проверка выполнения логаута по кнопке "Выйти"')
    @allure.description('Проверка выхода из учетной записи через личный кабине')
    def test_logout_from_profile_page_success(self, driver, create_new_user_and_delete):
        main_page = MainPage(driver)
        account_page = AccountPage(driver)
        
        # Авторизация
        user_credentials = create_new_user_and_delete[0]
        main_page.login(user_credentials['email'], user_credentials['password'])
        
        # Переход в личный кабинет 
        main_page.click_on_personal_account_in_header()
        
        # Выход из учетной записи
        account_page.click_on_logout_button()
        
        # Проверка: появилась кнопка регистрации
        account_page.wait_visibility_of_button_register()
        assert account_page.check_displaying_of_button_register()