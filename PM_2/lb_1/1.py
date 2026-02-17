class SettingsManager:


    _instance = None  
    
    def __new__(cls):
        """Переопределяем создание объекта — всегда возвращаем один и тот же экземпляр"""
        if cls._instance is None:
            print("Создаётся первый (и единственный) экземпляр SettingsManager")
            cls._instance = super(SettingsManager, cls).__new__(cls)
            cls._instance._initialize_defaults()
        return cls._instance
    
    def _initialize_defaults(self):
        """Устанавливает значения настроек по умолчанию"""
        self.theme = "light"              
        self.language = "ru"              
        self.config_path = "config.json"
        self.window_width = 1280
        self.window_height = 720
        self.auto_save = True
        self.font_size = 14
    
    def set_theme(self, theme: str):
        if theme in ["light", "dark"]:
            self.theme = theme
            print(f"Тема изменена на: {theme}")
        else:
            print("Ошибка: поддерживаются только 'light' и 'dark'")
    
    def set_language(self, lang: str):
        self.language = lang
        print(f"Язык изменён на: {lang}")
    
    def set_config_path(self, path: str):
        self.config_path = path
        print(f"Путь к конфигурации: {path}")
    
    def get_all_settings(self):
        """Возвращает словарь со всеми текущими настройками"""
        return {
            "theme": self.theme,
            "language": self.language,
            "config_path": self.config_path,
            "window_width": self.window_width,
            "window_height": self.window_height,
            "auto_save": self.auto_save,
            "font_size": self.font_size
        }
    
    def __str__(self):
        return f"SettingsManager(theme={self.theme}, lang={self.language}, config={self.config_path})"



if __name__ == "__main__":
    print("Демонстрация паттерна Singleton (вариант 1)\n")
    
   
    settings1 = SettingsManager()
    print("settings1:", settings1)
    
   
    settings2 = SettingsManager()
    print("settings2:", settings2)
    
    print("\nПроверка идентичности объектов:")
    print("settings1 is settings2 →", settings1 is settings2)
    
    
    settings1.set_theme("dark")
    settings1.set_language("en")
    settings1.window_width = 1440
