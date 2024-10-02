class InventoryPage:
    def __init__(self, page):
        self.page = page
        self.add_backpack = page.locator("[data-test=\"add-to-cart-sauce-labs-backpack\"]")
        self.product_sort_container = page.locator("[data-test=\"product-sort-container\"]")
        self.inventory_item_name = page.locator("[data-test=\"inventory-item\"]")

    def sort_by_name_az(self):
        self.product_sort_container.select_option('az')

    def get_inventory_item_names(self):
        return self.inventory_item_name.all_inner_texts()
