from framework.webapp import webapp


class NewFeed():
    instance = None

    @classmethod
    def get_instance(cls):
        if cls.instance is None:
            cls.instance = NewFeed()
        return cls.instance

    def __init__(self):
        self.driver = webapp.get_driver()

    def verify_status(self, row):
        print('Verifying dashboard status..')

    def verify_refresh(self):
        print('Verifying dashboard refresh component..')

    def verify_battery_status(self):
        print('Verifying Battery status..')

    def verify_battery_refresh(self):
        print('Verifying battery refresh..')

    def verify_gps_setting(self, row):
        print('Verifying GPS setting..')


newfeed = NewFeed.get_instance()
