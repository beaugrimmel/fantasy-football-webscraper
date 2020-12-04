import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait

class Player():
    def __init__(self):
        self.name = ''
        self.points = ''
        self.projection = ''
        self.position = ''

class Webscraper():
    def __init__(self, chromedriver_path):
        self.chromedriver_path = chromedriver_path
        self.driver = webdriver.Chrome(chromedriver_path)
    
    def end_scraper(self):
        self.driver.quit()

    def goto_website(self, website_url):
        self.driver.get(website_url)

    def login(self, username, password):
        try:
            user_box = WebDriverWait(self.driver, 25).until(EC.presence_of_element_located((By.XPATH, '//*[@id="landing"]/div/div/div[2]/div/div[2]/div[2]/div[1]/div[1]/input')))
            user_box.send_keys(username)
            user_box.send_keys(Keys.RETURN)
        except TimeoutException:
            print ("Loading took too much time for user box!")
        try:
            password_box = WebDriverWait(self.driver, 25).until(EC.presence_of_element_located((By.XPATH, '//*[@id="landing"]/div/div/div[2]/div/div[2]/div[2]/div[2]/div[1]/input')))
            password_box.send_keys(password)
            password_box.send_keys(Keys.RETURN)
        except TimeoutException:
            print ("Loading took too much time for password box!")

    def select_leaders_tab(self):
        try:
            leaders_box = WebDriverWait(self.driver, 25).until(EC.presence_of_element_located((By.XPATH, '//*[@id="root"]/div/div[1]/div[1]/div[3]/div/div[1]/a[3]')))
            leaders_box.click()
        except:
            print ("Loading took too much time for leaders tab!")

    def select_league(self):
        pass # TODO Implement function to select leagueDO 

    def select_week(self, week):
        # TODO This just doesnt work well
        try:
            week_dropdown = WebDriverWait(self.driver, 3).until(EC.presence_of_element_located((By.XPATH, '//*[@id="root"]/div/div[1]/div[1]/div[3]/div/div[2]/div/div[3]/div[2]/div[2]/div[2]')))
        except TimeoutException:
            print ("Loading took too much time for week dropdown!")
            return
        week_dropdown.click()
        try:
            week_number = WebDriverWait(self.driver, 3).until(EC.presence_of_element_located((By.XPATH, '//*[@id="root"]/div/div[1]/div[1]/div[3]/div/div[2]/div/div[3]/div[2]/div[2]/div[2]/div[2]/div[{}]'.format(week + 1))))
        except TimeoutException:
            print ("Loading took too much time for week number!")
            return
        week_number.click()

    def select_stat_type(self, type):
        # TODO Not working for Projection
        if type == 'Projection':
            stat_num = 1
        elif type == 'Stats':
            stat_num = 2
            return # Set to stats by default
        else:
            raise ValueError("Must enter Projection or Stats")
        try:
            stat_type_button = WebDriverWait(self.driver, 25).until(EC.presence_of_element_located((By.XPATH, '//*[@id="root"]/div/div[1]/div[1]/div[3]/div/div[2]/div/div[3]/div[1]/div[1]/div[2]/div[{}]'.format(stat_num))))
        except:
            raise TimeoutException("Loading took too much time for stat type!")
        stat_type_button.click()

    def hide_owned_players(self):
        time.sleep(1)
        try:
            hide_owned = WebDriverWait(self.driver, 25).until(EC.presence_of_element_located((By.XPATH, '//*[@id="root"]/div/div[1]/div[1]/div[3]/div/div[2]/div/div[3]/div[2]/div[3]/div[2]')))
        except TimeoutException:
            print ("Loading took too much time for hide owned!")
        hide_owned.click()

    def select_player_type(self, player_type):
        switcher = {
                'All':(1,-1),
                'QB':(2,-1),
                'RB':(3,-1),
                'WR':(4,-1),
                'TE':(5,-1),
                'K':(6,-1),
                'DEF':(7,-1),
                'FLEX':(8,1),
                'ROOKIE':(8,2)
            }
        type_num = switcher.get(player_type, 'Invalid player type')
        try:
            player_type = WebDriverWait(self.driver, 25).until(EC.presence_of_element_located((By.XPATH, '//*[@id="root"]/div/div[1]/div[1]/div[3]/div/div[2]/div/div[3]/div[1]/div[2]/div[2]/div/div[{}]'.format(type_num[0]))))
            player_type.click()
        except:
            print ("Loading took too much time for player type!")
        if type_num[0] == 8:
            try:
                player_type_2 = WebDriverWait(self.driver, 25).until(EC.presence_of_element_located((By.XPATH, '//*[@id="root"]/div/div[1]/div[1]/div[3]/div/div[2]/div/div[3]/div[1]/div[2]/div[2]/div/div[8]/div/div/div[{}]'.format(1))))
                player_type_2.click()
            except:
                print ("Loading took too much time for player type part 2!")

    def get_top_x_player(self, rank):
        player = Player()
        try:
            player_name = WebDriverWait(self.driver, 3).until(EC.presence_of_element_located((By.XPATH, '//*[@id="root"]/div/div[1]/div[1]/div[3]/div/div[2]/div/div[5]/div/div[1]/div/div[1]/div/div/div[{}]/div/div[2]/div[2]/div[1]'.format(rank))))
            player_points = WebDriverWait(self.driver, 3).until(EC.presence_of_element_located((By.XPATH, '//*[@id="root"]/div/div[1]/div[1]/div[3]/div/div[2]/div/div[5]/div/div[1]/div/div[1]/div/div/div[{}]/div/div[6]'.format(rank))))
            player_projection = WebDriverWait(self.driver, 3).until(EC.presence_of_element_located((By.XPATH, '//*[@id="root"]/div/div[1]/div[1]/div[3]/div/div[2]/div/div[5]/div/div[1]/div/div[1]/div/div/div[{}]/div/div[5]'.format(rank))))
            player_position = WebDriverWait(self.driver, 3).until(EC.presence_of_element_located((By.XPATH, '//*[@id="root"]/div/div[1]/div[1]/div[3]/div/div[2]/div/div[5]/div/div[1]/div/div[1]/div/div/div[{}]/div/div[2]/div[3]/div[1]'.format(rank))))
        except TimeoutException:
            print ("Loading took too much time for select player!")
        player.name = player_name.text
        player.points = player_points.text
        player.projection = player_projection.text
        player.position = player_position.text
        return player

def make_list_top_players(scraper, playertype, top_x):
    scraper.select_player_type(playertype)
    players = []
    for count in range(top_x):
        players.append(scraper.get_top_x_player(rank=(count+1)))
    return players

if __name__ == "__main__":
    scraper = Webscraper('/Users/beaugrimmel/Documents/GitHub/fantasy-football-webscraper/chromedriver')
    scraper.goto_website('https://sleeper.app/login')
    scraper.login('', '')
    scraper.select_leaders_tab()
    # scraper.select_stat_type(type='Stats')
    # scraper.select_week(week=9)
    scraper.hide_owned_players()

    rbs = make_list_top_players(scraper, 'RB', 2)
    print(rbs[1].name)
    print(rbs[1].points)

    scraper.end_scraper()