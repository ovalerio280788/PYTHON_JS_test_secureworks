class BasePage:
    """
    This class contains all of the common functions used for the pages.
    """

    def __init__(self, context):
        self.driver = context.driver
        self.context = context

    @property
    def url(self):
        return self.context.config.userdata.get('app_url')

    @property
    def get_title(self):
        return self.driver.title

    @property
    def get_current_url(self):
        return self.driver.current_url
