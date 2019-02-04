class Locators (object):
    def __init__(self, myDriver):
        self.driver = myDriver

    cookies_button = '//*[@id="layerAcceptCookie"]/a'
    login = '//*[@id="app"]/div/main/div/div/div[2]/header/nav/a[2]'
    email = ':nth-child(2) > :nth-child(1) > .v-input__control > .v-input__slot > .v-text-field__slot > input'
    password = ':nth-child(2) > .v-input__control > .v-input__slot > .v-text-field__slot > input'
    singin = '/html/body/div/div/main/div/div/div[2]/div/div/div/form[1]/button'

    new_app_button = 'button.theme--dark:nth-child(1)'
    new_app_button2 = 'button.speed-dial__button:nth-child(4)'
    app_name = '.v-form > :nth-child(1) > .v-input__control > .v-input__slot > .v-text-field__slot > input'
    select_os = '.chipOS_selected > .v-chip__content > span'
    bundle_id = ':nth-child(4) > .v-input__control > .v-input__slot > .v-text-field__slot > input'
    description = 'div.v-input:nth-child(5) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > textarea:nth-child(2)'
    image = 'filepond--browser'
    create_button = 'button.white--text:nth-child(3)'

    apps = '.v-list > :nth-child(2) > .v-list__tile > .v-list__tile__content > .v-list__tile__title'
    edit = 'div.v-menu__content:nth-child(3) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1)'
    tabla = '.v-datatable'

    '/html/body/div/div[22]/main/div/div/div[2]/div/div[1]/div/div[2]/div/table/tbody/tr[3]/td[1]/div/span'
    '/html/body/div/div[22]/main/div/div/div[2]/div/div[1]/div/div[2]/div/table/tbody/tr[4]/td[1]/div/span'
    editar = '/html/body/div/div[22]/main/div/div/div[2]/div/div[1]/div/div[2]/div/table/tbody/tr[4]/td[1]/div/div/div/a'
    '/html/body/div/div[22]/main/div/div/div[2]/div/div[1]/div/div[2]/div/table/tbody/tr[3]/td[1]/div/div/div/a'

    edit_button = ('.menuable__content__active > .v-list > :nth-child(1) > .v-list__tile')

    edit_app_name = '.v-form > div:nth-child(1) > div:nth-child(1) > div:nth-child(1)'