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
        self.proj = ''
        self.pos = ''

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
        try:
            week_dropdown = WebDriverWait(self.driver, 25).until(EC.presence_of_element_located((By.XPATH, '//*[@id="root"]/div/div[1]/div[1]/div[3]/div/div[2]/div/div[3]/div[2]/div[2]/div[2]')))
            week_dropdown.click()
        except:
            print ("Loading took too much time for week dropdown!")
        try:
            week_number = WebDriverWait(self.driver, 25).until(EC.presence_of_element_located((By.XPATH, '//*[@id="root"]/div/div[1]/div[1]/div[3]/div/div[2]/div/div[3]/div[2]/div[2]/div[2]/div[2]/div[{}]'.format(week + 1))))
            week_number.click()
        except:
            print ("Loading took too much time for week number!")

    def select_stat_type(self, type):
        if type == 'Projection':
            stat_num = 1
        elif type == 'Stats':
            stat_num = 2
            return # Set to stats by default
        else:
            raise ValueError("Must enter Projection or Stats")
        try:
            stat_type_button = WebDriverWait(self.driver, 25).until(EC.presence_of_element_located((By.XPATH, '//*[@id="root"]/div/div[1]/div[1]/div[3]/div/div[2]/div/div[3]/div[1]/div[1]/div[2]/div[{}]'.format(stat_num))))
            stat_type_button.click()
        except:
            print ("Loading took too much time for stat type!")

    def hide_owned_players(self):
        try:
            hide_owned = WebDriverWait(self.driver, 25).until(EC.presence_of_element_located((By.XPATH, '//*[@id="root"]/div/div[1]/div[1]/div[3]/div/div[2]/div/div[3]/div[2]/div[3]/div[2]')))
            hide_owned.click()
        except:
            print ("Loading took too much time for hide owned!")

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

if __name__ == "__main__":
    scraper = Webscraper('/Users/beaugrimmel/Documents/GitHub/fantasy-football-webscraper/chromedriver')
    scraper.goto_website('https://sleeper.app/login')
    scraper.login('', '')
    scraper.select_leaders_tab()
    scraper.select_stat_type(type='Stats')
    scraper.select_week(week=12)
    scraper.hide_owned_players()
    scraper.select_player_type('FLEX')
    time.sleep(5)
    scraper.end_scraper()

# top_player_name =  '//*[@id="root"]/div/div[1]/div[1]/div[3]/div/div[2]/div/div[5]/div/div[1]/div/div[1]/div/div/div[{}]/div/div[2]/div[2]/div[1]'
# top_player_points = '//*[@id="root"]/div/div[1]/div[1]/div[3]/div/div[2]/div/div[5]/div/div[1]/div/div[1]/div/div/div[{}]/div/div[6]'
# top_player_proj = '//*[@id="root"]/div/div[1]/div[1]/div[3]/div/div[2]/div/div[5]/div/div[1]/div/div[1]/div/div/div[{}]/div/div[5]'
# top_player_pos = '//*[@id="root"]/div/div[1]/div[1]/div[3]/div/div[2]/div/div[5]/div/div[1]/div/div[1]/div/div/div[{}]/div/div[2]/div[3]/div[1]'

# # Select QB
# time.sleep(.25)
# qb_button = driver.find_element(By.XPATH, '//*[@id="root"]/div/div[1]/div[1]/div[3]/div/div[2]/div/div[3]/div[1]/div[2]/div[2]/div/div[{}]'.format(2))
# qb_button.click()

# qb = Player()

# top_name = driver.find_element(By.XPATH, top_player_name.format(1))
# top_points = driver.find_element(By.XPATH, top_player_points.format(1))
# top_proj = driver.find_element(By.XPATH, top_player_proj.format(1))
# top_pos = driver.find_element(By.XPATH, top_player_pos.format(1))
# qb.name = top_name.text
# qb.points = top_points.text
# qb.proj = top_proj.text
# qb.pos = top_pos.text

# # Select RB
# time.sleep(.25)
# rb_button = driver.find_element(By.XPATH, '//*[@id="root"]/div/div[1]/div[1]/div[3]/div/div[2]/div/div[3]/div[1]/div[2]/div[2]/div/div[{}]'.format(3))
# rb_button.click()

# rbs = []
# for x in range(2):
#     rbs.append(Player())

# for count,rb in enumerate(rbs):
#     top_name = driver.find_element(By.XPATH, top_player_name.format(count + 1))
#     top_points = driver.find_element(By.XPATH, top_player_points.format(count + 1))
#     top_proj = driver.find_element(By.XPATH, top_player_proj.format(count + 1))
#     top_pos = driver.find_element(By.XPATH, top_player_pos.format(count + 1))
#     rb.name = top_name.text
#     rb.points = top_points.text
#     rb.proj = top_proj.text
#     rb.pos = top_pos.text

# # Select WR
# time.sleep(.25)
# wr_button = driver.find_element(By.XPATH, '//*[@id="root"]/div/div[1]/div[1]/div[3]/div/div[2]/div/div[3]/div[1]/div[2]/div[2]/div/div[{}]'.format(4))
# wr_button.click()

# wrs = []
# for x in range(2):
#     wrs.append(Player())

# for count,wr in enumerate(wrs):
#     top_name = driver.find_element(By.XPATH, top_player_name.format(count + 1))
#     top_points = driver.find_element(By.XPATH, top_player_points.format(count + 1))
#     top_proj = driver.find_element(By.XPATH, top_player_proj.format(count + 1))
#     top_pos = driver.find_element(By.XPATH, top_player_pos.format(count + 1))
#     wr.name = top_name.text
#     wr.points = top_points.text
#     wr.proj = top_proj.text
#     wr.pos = top_pos.text 

# # Select TE
# time.sleep(.25)
# te_button = driver.find_element(By.XPATH, '//*[@id="root"]/div/div[1]/div[1]/div[3]/div/div[2]/div/div[3]/div[1]/div[2]/div[2]/div/div[{}]'.format(5))
# te_button.click()

# te = Player()

# top_name = driver.find_element(By.XPATH, top_player_name.format(1))
# top_points = driver.find_element(By.XPATH, top_player_points.format(1))
# top_proj = driver.find_element(By.XPATH, top_player_proj.format(count + 1))
# top_pos = driver.find_element(By.XPATH, top_player_pos.format(1))
# te.name = top_name.text
# te.points = top_points.text
# te.proj = top_proj.text
# te.pos = top_pos.text

# # Select K
# time.sleep(.25)
# k_button = driver.find_element(By.XPATH, '//*[@id="root"]/div/div[1]/div[1]/div[3]/div/div[2]/div/div[3]/div[1]/div[2]/div[2]/div/div[{}]'.format(6))
# k_button.click()

# k = Player()

# top_name = driver.find_element(By.XPATH, top_player_name.format(1))
# top_points = driver.find_element(By.XPATH, top_player_points.format(1))
# top_proj = driver.find_element(By.XPATH, top_player_proj.format(count + 1))
# top_pos = driver.find_element(By.XPATH, top_player_pos.format(1))
# k.name = top_name.text
# k.points = top_points.text
# k.proj = top_proj.text
# k.pos = top_pos.text

# # Select D
# time.sleep(.25)
# D_button = driver.find_element(By.XPATH, '//*[@id="root"]/div/div[1]/div[1]/div[3]/div/div[2]/div/div[3]/div[1]/div[2]/div[2]/div/div[{}]'.format(7))
# D_button.click()

# d = Player()

# top_name = driver.find_element(By.XPATH, top_player_name.format(1))
# top_points = driver.find_element(By.XPATH, top_player_points.format(1))
# top_proj = driver.find_element(By.XPATH, top_player_proj.format(count + 1))
# top_pos = driver.find_element(By.XPATH, top_player_pos.format(1))
# d.name = top_name.text
# d.points = top_points.text
# d.proj = top_proj.text
# d.pos = top_pos.text

# # Select Flex
# # Pull in top 7 flex players
# time.sleep(.25)
# more_button = driver.find_element(By.XPATH, '//*[@id="root"]/div/div[1]/div[1]/div[3]/div/div[2]/div/div[3]/div[1]/div[2]/div[2]/div/div[{}]'.format(8))
# more_button.click()

# flex_button = driver.find_element(By.XPATH, '//*[@id="root"]/div/div[1]/div[1]/div[3]/div/div[2]/div/div[3]/div[1]/div[2]/div[2]/div/div[8]/div/div/div[1]')
# flex_button.click()

# fs = []
# for x in range(7):
#     fs.append(Player())

# for count,f in enumerate(fs):
#     top_name = driver.find_element(By.XPATH, top_player_name.format(count + 1))
#     top_points = driver.find_element(By.XPATH, top_player_points.format(count + 1))
#     top_proj = driver.find_element(By.XPATH, top_player_proj.format(count + 1))
#     top_pos = driver.find_element(By.XPATH, top_player_pos.format(count + 1))
#     f.name = top_name.text
#     f.points = top_points.text
#     f.proj = top_proj.text
#     f.pos = top_pos.text 

# # Append player objects to starter list
# starters = []
# starters.append(qb)
# for rb in rbs:
#     starters.append(rb)
# for wr in wrs:
#     starters.append(wr)
# starters.append(te)

# # append those starters names to a list
# starter_names = []
# for starter in starters:
#     starter_names.append(starter.name)

# # Add the two correct flex players
# for flex in fs:
#     if (flex.name not in starter_names):
#         starters.append(flex)
#         starter_names.append(flex.name)

# # Add kicker and def
# starters.append(k)
# starters.append(d)
# starter_names.append(k.name)
# starter_names.append(d.name)

# if (Projection):
#     output = ''
#     total_points = 0
#     for player in starters:
#         # print(player.name)
#         # print(player.proj)
#         # print(type(player.proj))
#         total_points += float(player.proj)
#         output = output + player.name + ' ' + player.pos + ' ' + str(player.proj) + '\n'
#     output = output + 'Total projected points: ' + str(total_points)
# else:
#     output = ''
#     total_points = 0
#     for player in starters:
#         total_points += float(player.points)
#         output = output + player.name + ' ' + player.pos + ' ' + str(player.points) + '\n'
#     output = output + 'Total points: ' + str(total_points)

# print(output)

# # Some code for if you want to enter results into league chat
# # input_box = driver.find_element(By.XPATH, '//*[@id="root"]/div/div[1]/div[1]/div[2]/div[2]/div[2]/div/div/div[2]/div[3]/div/div/textarea')
# # input_box.send_keys(output)

# driver.quit()