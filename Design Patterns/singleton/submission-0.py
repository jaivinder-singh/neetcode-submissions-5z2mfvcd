class Singleton:
    _unique_instance = None

    # In python consider this method as the 'getInstance'
    def __new__(cls):

        if cls._unique_instance is None:
            cls._unique_instance = super(Singleton, cls).__new__(cls)
            cls._unique_instance._init_singleton()
        
        return cls._unique_instance

    def _init_singleton(self):
        return self._unique_instance

    def getValue(self) -> str:
        return self.value

    def setValue(self, value: str):
        self.value = value
