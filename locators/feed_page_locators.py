from selenium.webdriver.common.by import By


class FeedPageLocators:
    total_orders_counter = (By.XPATH, "//div[@class='undefined mb-15']/p[@class='OrderFeed_number__2MbrQ text text_type_digits-large']")
    today_orders_counter = (By.XPATH, "(//p[@class='OrderFeed_number__2MbrQ text text_type_digits-large'])[2]")
    in_progress_order = (By.XPATH, "//ul[@class='OrderFeed_orderListReady__1YFem OrderFeed_orderList__cBvyi']/li[@class='text text_type_digits-default mb-2']")
    orders_number = (By.XPATH, "(//div[@class = 'OrderHistory_textBox__3lgbs mb-6'])[1]")
    current_order_number = (By.XPATH, "//p[@class = 'text text_type_digits-default mb-10 mt-5']")