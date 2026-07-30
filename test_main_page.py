import allure
import pytest


@allure.feature('Главная страница')
class TestMainPage:
    
    @allure.story('Навигация')
    @allure.title('Переход в ленту заказов по клику на кнопку')
    def test_click_order_feed_button(self, main_page, feed_page):
        "Проверяет только переход в ленту заказов"
        # клик на кнопку "Лента заказов"
        main_page.click_header_feed_button()
        
        # открылась страница ленты заказов
        assert feed_page.get_text_on_title_of_orders_list() == 'Лента заказов'
    
    @allure.story('Навигация')
    @allure.title('Переход в конструктор по клику на кнопку')
    def test_click_constructor_button(self, main_page):
        "Проверяет только переход в конструктор"
        # клик на кнопку "Конструктор"
        main_page.click_on_button_constructor()
        
        # открылась страница конструктора
        assert main_page.check_constructor_page_displayed()
    
    @allure.story('Корзина')
    @allure.title('Корзина отображается на главной странице')
    def test_basket_displayed(self, main_page):
        "Проверяет отображение корзины"
        assert main_page.check_basket_displayed()
    
    @allure.story('Модальное окно')
    @allure.title('Клик на ингредиент открывает модальное окно с деталями')
    def test_ingredient_modal_appears(self, main_page):
        "Проверяет открытие модального окна"
        main_page.click_on_ingredient()
        
        # модальное окно отображается
        assert main_page.check_modal_displayed()
    
    @allure.story('Модальное окно')
    @allure.title('Модальное окно закрывается по клику на крестик')
    def test_ingredient_modal_closes(self, main_page):
        "Проверяет закрытие модального окна"
        main_page.click_on_ingredient()
        
        main_page.click_close_modal_button()
        
        # модальное окно закрылось
        assert main_page.check_modal_closed()
    
    @allure.story('Счетчик ингредиентов')
    @allure.title('Счетчик ингредиента увеличивается при добавлении')
    def test_ingredient_counter_increases(self, main_page):
        "Проверяет увеличение счетчика."
        initial_count = main_page.get_ingredient_count()
        
        main_page.drag_and_drop_ingredient_to_order()
        
        # счетчик увеличился
        new_count = main_page.get_ingredient_count()
        assert new_count > initial_count