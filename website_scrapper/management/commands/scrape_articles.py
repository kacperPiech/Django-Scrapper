from django.core.management.base import BaseCommand
from website_scrapper.services.scrapper import WebsiteScraperBuilder
from tqdm import tqdm 

class Command(BaseCommand):
    help = "Scrapes a list of articles and saves them to the database."

    def handle(self, *args, **kwargs):
        urls_to_scrape = [
            "https://galicjaexpress.pl/ford-c-max-jaki-silnik-benzynowy-wybrac-aby-zaoszczedzic-na-paliwie",
            "https://galicjaexpress.pl/bmw-e9-30-cs-szczegolowe-informacje-o-osiagach-i-historii-modelu",
            "https://take-group.github.io/example-blog-without-ssr/jak-kroic-piers-z-kurczaka-aby-uniknac-suchych-kawalkow-miesa",
            "https://take-group.github.io/example-blog-without-ssr/co-mozna-zrobic-ze-schabu-oprocz-kotletow-5-zaskakujacych-przepisow",
        ]
        
        for url in tqdm(urls_to_scrape, desc="Scraping articles", unit="url"):
            try:
                scraper = WebsiteScraperBuilder(url)
                scrapper, obtained  = scraper.save()
            except Exception as e:
                self.stdout.write(self.style.ERROR(f"Failed {url}: {e}"))

