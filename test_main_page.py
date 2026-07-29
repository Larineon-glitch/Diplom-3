from page_objects.feed_page import FeedPage
from page_objects.main_page import MainPage
from conftest import *
import allure


@allure.feature('Главная страница')
class TestMainPage:
    
    @allure.story('Навигация')
    @allure.title('Переход в ленту заказов по клику на кнопку')
    def test_click_order_feed_button(self, main_page, feed_page):
        "переход в ленту заказов"
        main_page.click_header_feed_button()
        
        assert feed_page.get_text_on_title_of_orders_list() == 'Лента заказов'
    
    @allure.story('Навигация')
    @allure.title('Переход в конструктор по клику на кнопку')
    def test_click_constructor_button(self, main_page):
        "переход в конструктор"
        main_page.click_on_button_constructor()
        
        assert main_page.check_constructor_page_displayed()
    
    @allure.story('Корзина')
    @allure.title('Корзина отображается на главной странице')
    def test_basket_displayed(self, main_page):
        "отображение корзины"
        assert main_page.check_basket_displayed()
    
    @allure.story('Счетчик ингредиентов')
    @allure.title('Счетчик ингредиента увеличивается при добавлении')
    def test_ingredient_counter_increases(self, main_page):
        "увеличение счетчика"
        initial_count = main_page.get_ingredient_count()
        main_page.drag_and_drop_ingredient_to_order()
        
        new_count = main_page.get_ingredient_count()
        assert new_count > initial_count