from playwright.sync_api import Page, expect
from pages.LoginPage import LoginPage
from pages.InventoryPage import InventoryPage

def test_sor_inventory(page: Page) -> None:
    login_page = LoginPage(page)
    shop = InventoryPage(page)
    login_page.navigate()
    login_page.login("standard_user", "secret_sauce")
    shop.sort_by_name_az()
    sorted_names = shop.get_inventory_item_names()
    assert is_sorted_ascending(sorted_names), "Товары не отсортированы по алфавиту A-Z"

def is_sorted_ascending(items):
    return all(items[i] <= items[i + 1] for i in range(len(items) - 1))
