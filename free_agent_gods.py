import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from tabulate import tabulate
from secrets import username, password

class Player():
    def __init__(self):
        self.name = ''
        self.points = ''
        self.projection = ''
        self.position = ''
    
    def __eq__(self, other):
        return self.name==other.name
    
    def __hash__(self):
        return hash(self.name)

class Webscraper():
    def __init__(self, chromedriver_path):
        self.chromedriver_path = chromedriver_path
        self.driver = webdriver.Chrome(chromedriver_path)
    
    def end_scraper(self):
        self.driver.quit()

    def goto_website(self, website_url):
        self.driver.get(website_url)

    def login(self, username, password):
        user_box = self.driver.find_element_by_xpath('//*[@id="landing"]/div/div/div[2]/div/div[2]/div[2]/div[1]/div[1]/input')
        user_box.send_keys(username)
        user_box.send_keys(Keys.RETURN)

        password_box = WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="landing"]/div/div/div[2]/div/div[2]/div[2]/div[2]/div[1]/input')))
        password_box.send_keys(password)
        password_box.send_keys(Keys.RETURN)

    def select_league(self):
        pass # TODO Implement function to select league

    def select_leaders_tab(self):
        leaders_box = WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="root"]/div/div[1]/div[1]/div[3]/div/div[1]/a[3]')))
        leaders_box.click()

    def select_week(self, week):
        week_dropdown = WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="root"]/div/div[1]/div[1]/div[3]/div/div[2]/div/div[3]/div[2]/div[2]/div[2]')))
        week_dropdown.click()

        week_number = WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="root"]/div/div[1]/div[1]/div[3]/div/div[2]/div/div[3]/div[2]/div[2]/div[2]/div[2]/div[{}]'.format(week + 1))))
        week_number.click()

    def select_stat_type(self, type):
        # TODO Look into why theres sometimes timeout issues
        if type == 'Projection':
            stat_num = 1
        elif type == 'Stats':
            stat_num = 2
        else:
            raise ValueError("Must enter Projection or Stats")
        stat_type_button = WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="root"]/div/div[1]/div[1]/div[3]/div/div[2]/div/div[3]/div[1]/div[1]/div[2]/div[{}]'.format(stat_num))))
        stat_type_button.click()

    def hide_owned_players(self):
        hide_owned = WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="root"]/div/div[1]/div[1]/div[3]/div/div[2]/div/div[3]/div[2]/div[3]/div[2]')))
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

        player_type = WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="root"]/div/div[1]/div[1]/div[3]/div/div[2]/div/div[3]/div[1]/div[2]/div[2]/div/div[{}]'.format(type_num[0]))))
        player_type.click()

        if type_num[0] == 8:
            player_type_2 = WebDriverWait(self.driver, 5).until(EC.presence_of_element_located((By.XPATH, '//*[@id="root"]/div/div[1]/div[1]/div[3]/div/div[2]/div/div[3]/div[1]/div[2]/div[2]/div/div[8]/div/div/div[{}]'.format(type_num[1]))))
            player_type_2.click()

    def get_top_x_player(self, rank):
        player = Player()
        player_name = WebDriverWait(self.driver, 3).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="root"]/div/div[1]/div[1]/div[3]/div/div[2]/div/div[5]/div/div[1]/div/div[1]/div/div/div[{}]/div/div[2]/div[2]/div[1]'.format(rank))))
        player_points = WebDriverWait(self.driver, 3).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="root"]/div/div[1]/div[1]/div[3]/div/div[2]/div/div[5]/div/div[1]/div/div[1]/div/div/div[{}]/div/div[6]'.format(rank))))
        player_projection = WebDriverWait(self.driver, 3).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="root"]/div/div[1]/div[1]/div[3]/div/div[2]/div/div[5]/div/div[1]/div/div[1]/div/div/div[{}]/div/div[5]'.format(rank))))
        player_position = WebDriverWait(self.driver, 3).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="root"]/div/div[1]/div[1]/div[3]/div/div[2]/div/div[5]/div/div[1]/div/div[1]/div/div/div[{}]/div/div[2]/div[3]/div[1]'.format(rank))))
        player.name = player_name.text
        player.points = player_points.text
        player.projection = player_projection.text
        player.position = player_position.text
        return player

    def make_list_top_players(self, playertype, top_x):
        scraper.select_player_type(playertype)
        players = []
        for count in range(top_x):
            players.append(scraper.get_top_x_player(rank=(count+1)))
        return players

if __name__ == "__main__":
    scraper = Webscraper('/Users/beaugrimmel/Documents/GitHub/fantasy-football-webscraper/chromedriver')
    scraper.goto_website('https://sleeper.app/login')
    scraper.login(username, password)
    scraper.select_leaders_tab()
    scraper.select_week(week=13)
    scraper.hide_owned_players()
    scraper.select_stat_type(type='Stats')

    qb = scraper.make_list_top_players('QB', 1)
    rb = scraper.make_list_top_players('RB', 2)
    wr = scraper.make_list_top_players('WR', 2)
    te = scraper.make_list_top_players('TE', 1)
    flex = scraper.make_list_top_players('FLEX', 7)
    k = scraper.make_list_top_players('K', 1)
    d = scraper.make_list_top_players('DEF', 1)
    starters = qb + rb + wr + te 

    flexs_added = 0
    for flex in flex:
        if flexs_added == 2:
            break
        if flex not in starters:
            starters.append(flex)
            flexs_added += 1

    starters = starters + k + d

    # Print results nicely formatted
    starters_print = []
    total_points = 0
    for starter in starters:
        starters_print.append([starter.name, starter.position, starter.points])
        total_points += round(float(starter.points),2)
    print(tabulate(starters_print, headers=['Name', 'Pos/Team', 'Points']))
    print('Total points: {}'.format(round(total_points)))

    time.sleep(1)
    scraper.end_scraper()