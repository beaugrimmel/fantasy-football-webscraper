import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

class Player():
    def __init__(self):
        self.name = ''
        self.points = ''
        self.pos = ''

driver = webdriver.Chrome(executable_path='/Users/beaugrimmel/Documents/fantasy-football-webscraper/chromedriver')
driver.get('https://sleeper.app/login')

# Find and input username
user_box = driver.find_element(By.XPATH, '//*[@id="landing"]/div/div/div[2]/div/div[2]/div[2]/div[1]/div[1]/input')
user_box.send_keys('<UserName>')
user_box.send_keys(Keys.RETURN)

# Find and input password
time.sleep(.25)
password_box = driver.find_element(By.XPATH, '//*[@id="landing"]/div/div/div[2]/div/div[2]/div[2]/div[2]/div[1]/input')
password_box.send_keys('<Password>')
password_box.send_keys(Keys.RETURN)

# Select which league you want to look at
# TODO

# Click on leaders tab
time.sleep(2)
leaders_box = driver.find_element(By.XPATH, '//*[@id="root"]/div/div[1]/div[1]/div[3]/div/div[1]/a[3]')
leaders_box.click()

# Click on dropdown menu for weeks
time.sleep(.25)
week_dropdown = driver.find_element(By.XPATH, '//*[@id="root"]/div/div[1]/div[1]/div[3]/div/div[2]/div/div[3]/div[2]/div[2]/div[2]')
week_dropdown.click()

# Select the week your looking for
time.sleep(.25)
week = 11
week_dropdown = driver.find_element(By.XPATH, '//*[@id="root"]/div/div[1]/div[1]/div[3]/div/div[2]/div/div[3]/div[2]/div[2]/div[2]/div[2]/div[{}]'.format(week + 1))
week_dropdown.click()

# Hide owned players
time.sleep(.25)
hide_owned = driver.find_element(By.XPATH, '//*[@id="root"]/div/div[1]/div[1]/div[3]/div/div[2]/div/div[3]/div[2]/div[3]/div[2]')
hide_owned.click()

top_player_name =  '//*[@id="root"]/div/div[1]/div[1]/div[3]/div/div[2]/div/div[5]/div/div[1]/div/div[1]/div/div/div[{}]/div/div[2]/div[2]/div[1]'
top_player_points = '//*[@id="root"]/div/div[1]/div[1]/div[3]/div/div[2]/div/div[5]/div/div[1]/div/div[1]/div/div/div[{}]/div/div[6]'
top_player_pos = '//*[@id="root"]/div/div[1]/div[1]/div[3]/div/div[2]/div/div[5]/div/div[1]/div/div[1]/div/div/div[{}]/div/div[2]/div[3]/div[1]'

# Select QB
time.sleep(.25)
qb_button = driver.find_element(By.XPATH, '//*[@id="root"]/div/div[1]/div[1]/div[3]/div/div[2]/div/div[3]/div[1]/div[2]/div[2]/div/div[{}]'.format(2))
qb_button.click()

qb = Player()

top_name = driver.find_element(By.XPATH, top_player_name.format(1))
top_points = driver.find_element(By.XPATH, top_player_points.format(1))
top_pos = driver.find_element(By.XPATH, top_player_pos.format(1))
qb.name = top_name.text
qb.points = top_points.text
qb.pos = top_pos.text

# Select RB
time.sleep(.25)
rb_button = driver.find_element(By.XPATH, '//*[@id="root"]/div/div[1]/div[1]/div[3]/div/div[2]/div/div[3]/div[1]/div[2]/div[2]/div/div[{}]'.format(3))
rb_button.click()

rbs = []
for x in range(2):
    rbs.append(Player())

for count,rb in enumerate(rbs):
    top_name = driver.find_element(By.XPATH, top_player_name.format(count + 1))
    top_points = driver.find_element(By.XPATH, top_player_points.format(count + 1))
    top_pos = driver.find_element(By.XPATH, top_player_pos.format(count + 1))
    rb.name = top_name.text
    rb.points = top_points.text
    rb.pos = top_pos.text 

# Select WR
time.sleep(.25)
wr_button = driver.find_element(By.XPATH, '//*[@id="root"]/div/div[1]/div[1]/div[3]/div/div[2]/div/div[3]/div[1]/div[2]/div[2]/div/div[{}]'.format(4))
wr_button.click()

wrs = []
for x in range(2):
    wrs.append(Player())

for count,wr in enumerate(wrs):
    top_name = driver.find_element(By.XPATH, top_player_name.format(count + 1))
    top_points = driver.find_element(By.XPATH, top_player_points.format(count + 1))
    top_pos = driver.find_element(By.XPATH, top_player_pos.format(count + 1))
    wr.name = top_name.text
    wr.points = top_points.text
    wr.pos = top_pos.text 

# Select TE
time.sleep(.25)
te_button = driver.find_element(By.XPATH, '//*[@id="root"]/div/div[1]/div[1]/div[3]/div/div[2]/div/div[3]/div[1]/div[2]/div[2]/div/div[{}]'.format(5))
te_button.click()

te = Player()

top_name = driver.find_element(By.XPATH, top_player_name.format(1))
top_points = driver.find_element(By.XPATH, top_player_points.format(1))
top_pos = driver.find_element(By.XPATH, top_player_pos.format(1))
te.name = top_name.text
te.points = top_points.text
te.pos = top_pos.text

# Select K
time.sleep(.25)
k_button = driver.find_element(By.XPATH, '//*[@id="root"]/div/div[1]/div[1]/div[3]/div/div[2]/div/div[3]/div[1]/div[2]/div[2]/div/div[{}]'.format(6))
k_button.click()

k = Player()

top_name = driver.find_element(By.XPATH, top_player_name.format(1))
top_points = driver.find_element(By.XPATH, top_player_points.format(1))
top_pos = driver.find_element(By.XPATH, top_player_pos.format(1))
k.name = top_name.text
k.points = top_points.text
k.pos = top_pos.text

# Select D
time.sleep(.25)
D_button = driver.find_element(By.XPATH, '//*[@id="root"]/div/div[1]/div[1]/div[3]/div/div[2]/div/div[3]/div[1]/div[2]/div[2]/div/div[{}]'.format(7))
D_button.click()

d = Player()

top_name = driver.find_element(By.XPATH, top_player_name.format(1))
top_points = driver.find_element(By.XPATH, top_player_points.format(1))
top_pos = driver.find_element(By.XPATH, top_player_pos.format(1))
d.name = top_name.text
d.points = top_points.text
d.pos = top_pos.text

# Select Flex
# Pull in top 7 flex players
time.sleep(.25)
more_button = driver.find_element(By.XPATH, '//*[@id="root"]/div/div[1]/div[1]/div[3]/div/div[2]/div/div[3]/div[1]/div[2]/div[2]/div/div[{}]'.format(8))
more_button.click()

flex_button = driver.find_element(By.XPATH, '//*[@id="root"]/div/div[1]/div[1]/div[3]/div/div[2]/div/div[3]/div[1]/div[2]/div[2]/div/div[8]/div/div/div[1]')
flex_button.click()

fs = []
for x in range(7):
    fs.append(Player())

for count,f in enumerate(fs):
    top_name = driver.find_element(By.XPATH, top_player_name.format(count + 1))
    top_points = driver.find_element(By.XPATH, top_player_points.format(count + 1))
    top_pos = driver.find_element(By.XPATH, top_player_pos.format(count + 1))
    f.name = top_name.text
    f.points = top_points.text
    f.pos = top_pos.text 

# Append player objects to starter list
starters = []
starters.append(qb)
for rb in rbs:
    starters.append(rb)
for wr in wrs:
    starters.append(wr)
starters.append(te)

# append those starters names to a list
starter_names = []
for starter in starters:
    starter_names.append(starter.name)

# Add the two correct flex players
for flex in fs:
    if (flex.name not in starter_names):
        starters.append(flex)
        starter_names.append(flex.name)

# Add kicker and def
starters.append(k)
starters.append(d)
starter_names.append(k.name)
starter_names.append(d.name)

output = ''
total_points = 0
for player in starters:
    total_points += float(player.points)
    output = output + player.name + ' ' + player.pos + ' ' + str(player.points) + '\n'
output = output + 'Total points: ' + str(total_points)

print(output)

# Some code for if you want to enter results into league chat
# input_box = driver.find_element(By.XPATH, '//*[@id="root"]/div/div[1]/div[1]/div[2]/div[2]/div[2]/div/div/div[2]/div[3]/div/div/textarea')
# input_box.send_keys(output)

driver.quit()