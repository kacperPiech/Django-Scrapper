from bs4 import BeautifulSoup
from playwright.sync_api import sync_playwright
from htmldate import find_date
import requests
import trafilatura
import dateparser
from datetime import datetime
from website_scrapper.models import Website_Content
    

class WebsiteScraperBuilder():
    def __init__(self, url : str) -> None:
        with sync_playwright() as p:
            browser = p.firefox.launch(headless=True)
            page = browser.new_page()
            page.goto(url)
            html = page.content()
            browser.close()
        self.url = url
        self.html = html
        self.soup = BeautifulSoup(html, 'html.parser')
    
    def extract_website_title(self):
        website_title = self.soup.find('title').get_text()
        return website_title
    
    def extract_website_html_content(self):
        website_html_content = trafilatura.extract(self.html, output_format='html')
        return website_html_content
    
    def extract_website_plain_content(self):
        website_plain_content = trafilatura.extract(self.html)
        return website_plain_content
    
    def extract_url(self):
        return self.url
    
    def extract_publication_date(self):
        try:
            date = find_date(self.url, outputformat="%d-%m-%Y %H:%M:%S")
            if date:
                return date
        except Exception:
            pass 
        
        considered_languages=["pl", "en"]
        html_tags_to_consider = ["meta", "time", "p", "span", "div"]
        
        for all_html_values in self.soup.find_all(html_tags_to_consider):
            
            if all_html_values.name == "time":
                date = all_html_values.get("datetime") or all_html_values.text
                
            elif all_html_values.name == "meta" and all_html_values.get("property") == "article:published_time":
                date = all_html_values.get("content")
                
            else:
                date = all_html_values.get_text(strip=True)

            if not date or not any(potential_number.isdigit() for potential_number in date):
                continue
            date = date.strip(' .:\n\t')
            
            final_date = dateparser.parse(
                date,
                languages=considered_languages,
                settings={
                    "DATE_ORDER": "DMY",
                    "PREFER_DAY_OF_MONTH": "first",
                    "RELATIVE_BASE": datetime.now(),
                },
            )
            if final_date:
                return final_date.strftime("%d-%m-%Y %H:%M:%S")
            

    def save(self):
        return Website_Content.objects.get_or_create(
            title = self.extract_website_title(),
            website_html_content = self.extract_website_html_content(),
            website_plain_content = self.extract_website_plain_content(),
            url = self.extract_url(),
            publication_date = self.extract_publication_date()
        )
        


        
            
    
        
        
        
        