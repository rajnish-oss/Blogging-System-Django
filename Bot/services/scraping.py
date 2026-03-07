# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC

# # Start the driver ONCE at the beginning of your script
# driver = webdriver.Chrome() 
# driver.get("https://11a0-49-36-191-231.ngrok-free.app")
#  # Initial jump

# # def scrape_current_state():
# #     # 1. Ask the driver where it is right now
# #     current_url = driver.current_url
    
# #     # 2. Get the HTML of exactly what is on screen
# #     html_source = driver.page_source
    
# #     print(f"Captured data from: {current_url}")
# #     return html_source


# def current_page_content():
#     # Wait up to 5 seconds for a specific element (like a <div> or <body>) to load
#     try:
#         check_input = driver.find_element(By.TAG_NAME, "button")
#         check_input.click()
#         WebDriverWait(driver, 5).until(
#             EC.presence_of_element_located((By.TAG_NAME, "body"))
#         )
#         current_url = driver.current_url

        
    
#         # 2. Get the HTML of exactly what is on screen
#         html_source = driver.page_source
        
#         print(f"Captured data from: {current_url}")
#         return html_source
#     except Exception as e:
#         return f"Timeout or Error: {e}"