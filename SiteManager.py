

class SiteManager:
    """Клас для управління списком сайтів."""
    def __init__(self):
        self.sites = []

    def add_site(self, site_url):
        """Додає сайт у список."""
        if site_url not in self.sites:
            self.sites.append(site_url)
            print(f"Сайт {site_url} додано.")
        else:
            print(f"Сайт {site_url} вже існує в списку.")

    def get_sites(self):
        """Повертає список сайтів."""
        return self.sites
