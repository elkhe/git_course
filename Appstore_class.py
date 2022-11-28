class AppStore:
    def __init__(self) -> None:
        self.app_dict = {}

    def add_application(self, app):
        if app.name not in self.app_dict:
            self.app_dict[app.name] = app


    def remove_application(self, app):
        if app.name in self.app_dict:
            del self.app_dict[app.name]
        


    def block_application(self, app):
        if app.name in self.app_dict:
            self.app_dict[app.name].blocked = True


    def total_apps(self):
        return len(self.app_dict)


class Application:
    def __init__(self, name) -> None:
        self.name = name
        self.blocked = False


store = AppStore()
app_youtube = Application("Youtube")
store.add_application(app_youtube)
store.block_application(app_youtube)
print(store.app_dict, store.app_dict["Youtube"].blocked)
store.remove_application(app_youtube)
print(store.app_dict)