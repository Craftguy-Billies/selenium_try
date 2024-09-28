from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import time

def get_first_youtube_embed(query):
    # Set up Chrome options for Selenium
    chrome_options = Options()
    chrome_options.add_argument("--headless")  # Run in headless mode (no UI)
    
    # Specify the path to the ChromeDriver
    chrome_driver_path = "C:\chromedriver.exe"  # Update this with the path to your ChromeDriver
    
    # Start the browser
    service = Service(chrome_driver_path)
    driver = webdriver.Chrome(service=service, options=chrome_options)
    
    # Format the YouTube search URL
    search_url = f"https://www.youtube.com/results?search_query={query.replace(' ', '+')}"
    
    # Load the page
    driver.get(search_url)
    
    # Wait for the page to fully load
    time.sleep(3)  # You may adjust this if the page is slow
    
    # Find the first video link
    first_video = driver.find_element(By.XPATH, '//a[@href and contains(@href, "/watch?v=")]')
    print(first_video)
    
    if first_video:
        video_url = f"https://www.youtube.com{first_video.get_attribute('href')}"
        video_url = video_url.split('&')[0]
        video_id = video_url.split('v=')[1]
        embed_code = f'<iframe width="560" height="315" src="https://www.youtube.com/embed/{video_id}" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>'
        
        # Close the browser
        driver.quit()
        
        return embed_code
    
    # If no video found, return None
    driver.quit()
    return "No video found."

# Example usage
query = input("Enter your search query: ")
embed_code = get_first_youtube_embed(query)
if embed_code:
    print("Embed Code for First Video:\n", embed_code)
