class Cache:
    NUMEROS_CACHED = []

    def get_from_cache(self):
        return self.NUMEROS_CACHED

    def set_to_cache(self, numeros):
        self.NUMEROS_CACHED = numeros  # no-lint
