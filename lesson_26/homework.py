import requests

username = "aaa"
passwd = "bb"

url = f"https://{username}:{passwd}@qauto2.forstudy.space"

xpath_1 = "//button[@class='hero-descriptor_btn btn btn-primary' and text()='Sign up']"
xpath_2 = "//button[@class='header-link -guest' and text()='Guest log in']"
xpath_3 = "//button[@class='btn btn-outline-white header_signin' and text()='Sign In']"
xpath_4 = "//a[@class='btn header-link -active' and text()='Home']"
xpath_5 = "//button[@class='btn header-link' and text()='About']"
xpath_6 = "//button[@class='btn header-link' and text()='Contacts']"
xpath_7 = "//div[@class='html5-video-container']/video[@class='video-stream html5-main-video']"
xpath_8 = "//span[@class='socials_icon icon icon-facebook']"
xpath_9 = "//span[@class='socials_icon icon icon-telegram']"
xpath_10 = "//span[@class='socials_icon icon icon-youtube']"
xpath_11 = "//span[@class='socials_icon icon icon-instagram']"
xpath_12 = "//span[@class='socials_icon icon icon-linkedin']"
xpath_13 = "//a[@class='contacts_link display-4' and text()='ithillel.ua']"
xpath_14 = "//a[@class='contacts_link h4' and text()='support@ithillel.ua']"
xpath_15 = "//a[@class='footer_logo']"
xpath_16 = "//a[@class='btn header-link -active' and text()='Garage']"
xpath_17 = "//a[@class='btn header-link' and text()='Fuel expenses']"
xpath_18 = "//a[@class='btn header-link' and text()='Instructions']"
xpath_19 = "//a[@class='btn btn-white btn-sidebar sidebar_btn']/span[@class='icon icon-garage']"
xpath_20 = "//a[@class='btn btn-white btn-sidebar sidebar_btn']/span[@class='icon icon-fuel']"
xpath_21 = "//a[@class='btn btn-white btn-sidebar sidebar_btn']/span[@class='icon icon-instructions']"
xpath_22 = "//a[@class='btn btn-link text-danger btn-sidebar sidebar_btn']"
xpath_23 = "//button[@class='btn btn-primary' and text()='Add car']"
xpath_24 = "//button[@id='userNavDropdown']"
xpath_25 = "//div[@class='user-nav show dropdown']/nav[@class='user-nav_menu dropdown-menu show']/a[@class='dropdown-item btn btn-link user-nav_link' and text()='Fuel expenses']"
xpath_26 = "//div[@class='user-nav show dropdown']/nav[@class='user-nav_menu dropdown-menu show']/a[@class='dropdown-item btn btn-link user-nav_link' and text()='Instructions']"
xpath_27 = "//div[@class='user-nav show dropdown']/nav[@class='user-nav_menu dropdown-menu show']/a[@class='dropdown-item btn btn-link user-nav_link' and text()='Garage']"
xpath_28 = "//div[@class='user-nav show dropdown']/nav[@class='user-nav_menu dropdown-menu show']/button[@class='dropdown-item btn btn-link user-nav_link' and text()='Logout']"
xpath_29 = "//div[@class='item-group']/button[@class='btn btn-primary' and text()='Add an expense']"
xpath_30 = "//button[@class='instructions-search-controls_search btn btn-primary' and text()='Search']"
xpath_31 = "//button[@id='brandSelectDropdown']"
xpath_32 = "//button[@id='modelSelectDropdown']"
xpath_33 = "//a[@class='instruction-link']/p[@class='instruction-link_description' and text()='Front windshield wipers on Audi TT']"
xpath_34 = "//a[@class='instruction-link']/p[@class='instruction-link_description' and text()='Rear anti roll bar links on Audi TT']"
xpath_35 = "//a[@class='instruction-link']/p[@class='instruction-link_description' and text()='Rear coil springs on Audi TT']"
xpath_36 = "//a[@class='instruction-link']/p[@class='instruction-link_description' and text()='Rear suspension lower control arm on Audi TT']"
xpath_37 = "//a[@class='instruction-link']/p[@class='instruction-link_description' and text()='Rear suspension strut on Audi TT']"
xpath_38 = "//a[@class='instruction-link']/p[@class='instruction-link_description' and text()='Spark plugs on Audi TT']"
xpath_39 = "//button[text()='Login']",
xpath_40 = "//input[@name='email' and @type='text']",
xpath_41 = "//input[@name='password' and @type='password']",
xpath_42 = "//button[@type='submit' and text()='Login']",
xpath_43 = "//h1[text()='Your Garage']",
xpath_44 =  "//button[@class='btn btn-dark' and contains(text(),'Add car')]",
xpath_45 = "//select[@name='carBrand']",
xpath_46 = "//select[@name='carModel']",
xpath_47 = "//select[@name='carFuelType']",
xpath_48 = "//input[@name='carRegistration']",
xpath_49 = "//button[@type='submit' and text()='Add']",
xpath_50 = "//h1[text()='Your Garage']"