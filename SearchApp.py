
from SiteManager import SiteManager
from SiteParser import SiteParser
from UserInterface import UserInterface


class SearchApp:
    """Основний клас програми."""
    def __init__(self):
        self.site_manager = SiteManager()
        self.site_parser = SiteParser()
        self.ui = UserInterface(self.site_manager, self.site_parser)

    def run(self):
        while True:
            print("\nМеню:")
            print("1. Додати сайт")
            print("2. Показати сайти")
            print("3. Виконати пошук")
            print("4. Вийти")
            choice = input("Введіть номер дії: ")

            if choice == "1":
                site_url = input("Введіть URL сайту: ")
                self.site_manager.add_site(site_url)
            elif choice == "2":
                self.ui.display_sites()
            elif choice == "3":
                query = input("Введіть пошуковий запит: ")
                results = self.site_parser.search(self.site_manager.get_sites(), query)
                self.ui.display_results(results)
            elif choice == "4":
                print("Вихід із програми.")
                break
            else:
                print("Невірний вибір. Спробуйте ще раз.")

if __name__ == "__main__":
    app = SearchApp()
    app.run()
