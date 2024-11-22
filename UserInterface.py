

class UserInterface:
    """Клас для взаємодії з користувачем."""
    def __init__(self, site_manager, site_parser):
        self.site_manager = site_manager
        self.site_parser = site_parser

    def display_sites(self):
        """Виводить список сайтів."""
        sites = self.site_manager.get_sites()
        if sites:
            print("Список сайтів:")
            for site in sites:
                print(f"- {site}")
        else:
            print("Список сайтів порожній.")

    def display_results(self, results):
        if results:
            print("Результати пошуку:")
            for site, matches in results.items():
                print(f"{site}: {matches} збігів")
        else:
            print("Немає збігів.")
