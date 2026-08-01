from page_objects.feed_page import FeedPage
from page_objects.main_page import MainPage
from conftest import *
import allure


class TestFeedPage:

    @allure.title('Проверка увеличения числа на счетчике количества выполненных за всё время заказов')
    @allure.description('Проверка обновления счетчика заказов за все время')
    def test_changes_counter_for_quantity_of_orders_success(self, driver, create_new_user_and_delete):
        main_page = MainPage(driver)
        feed_page = FeedPage(driver)
        
        # Авторизация 
        user_credentials = create_new_user_and_delete[0]
        main_page.login(user_credentials['email'], user_credentials['password'])
        
        # Получение начального значения счетчика заказов за все время
        main_page.click_header_feed_button()
        orders_count_1 = feed_page.get_quantity_of_orders()
        
        # Создание нового заказа через конструктор
        main_page.click_on_button_constructor()
        main_page.drag_and_drop_ingredient_to_order()
        main_page.click_on_button_make_order()
        
        # Ожидание обработки заказа и появления номера в модальном окне
        main_page.wait_for_order_processing(timeout=30)
        main_page.click_on_button_close_confirmation_modal()
        
        # Проверка обновленного значения счетчика заказов
        main_page.click_header_feed_button()
        orders_count_2 = feed_page.get_quantity_of_orders()
        
        # Преобразуем значения в числа и сравниваем
        count_1 = int(orders_count_1)
        count_2 = int(orders_count_2)
        # Проверка: счетчик увеличился после создания заказа
        assert count_2 > count_1, f"Счетчик не увеличился: было {count_1}, стало {count_2}"

    @allure.title('Проверка увеличения числа на счетчике выполненных за Сегодня заказов')
    @allure.description('Проверка обновления счетчика заказов за текущий день')
    def test_changes_counter_for_daily_quantity_of_orders_success(self, driver, create_new_user_and_delete):
        main_page = MainPage(driver)
        feed_page = FeedPage(driver)
        
        # Авторизация
        user_credentials = create_new_user_and_delete[0]
        main_page.login(user_credentials['email'], user_credentials['password'])
        
        main_page.click_header_feed_button()
        orders_count_1 = feed_page.get_daily_quantity_of_orders()
        
        main_page.click_on_button_constructor()
        main_page.drag_and_drop_ingredient_to_order()
        main_page.click_on_button_make_order()
        
        main_page.wait_for_order_processing(timeout=30)
        main_page.click_on_button_close_confirmation_modal()
        
        # Проверка обновленного значения дневного счетчика
        main_page.click_header_feed_button()
        orders_count_2 = feed_page.get_daily_quantity_of_orders()
        
        # Проверка: счетчик увеличился после создания заказа
        count_1 = int(orders_count_1)
        count_2 = int(orders_count_2)
        
        assert count_2 > count_1, f"Счетчик не увеличился: было {count_1}, стало {count_2}"
        
    @allure.title('Проверка появления нового заказа в разделе "В работе"')
    @allure.description('Проверка отображения нового заказа в ленте заказов')
    def test_displaying_new_order_in_progress_feed_success(self, driver, create_new_user_and_delete):
        main_page = MainPage(driver)
        feed_page = FeedPage(driver)
        
        # Авторизация
        user_credentials = create_new_user_and_delete[0]
        main_page.login(user_credentials['email'], user_credentials['password'])
        
        main_page.drag_and_drop_ingredient_to_order()
        main_page.click_on_button_make_order()
        
        main_page.wait_for_order_processing(timeout=30)
        main_page.get_number_of_order_in_modal_confirmation()
        main_page.click_on_button_close_confirmation_modal()
        
        main_page.click_header_feed_button()
        
        order_in_progress = feed_page.get_order_number_in_feed_progress_section()
        assert order_in_progress is not None