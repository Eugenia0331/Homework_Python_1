class StringUtils:
    def capitalize(self, string):
        if string is None or string == "":
            return string
        if not isinstance(string, str):
            return string
        if not string[0].isalpha():
            return string
        return string[0].upper() + string[1:].lower()

    def trim(self, string):
        if string is None:
            return None
        if not isinstance(string, str):
            return string
        stripped = string.lstrip(' ')
        return "" if stripped == "" else stripped

    def contains(self, string, symbol):
        if string is None or symbol is None:
            return False
        if not isinstance(string, str):
            return False
        return symbol in string

    def delete_symbol(self, string, symbol):
        if string is None or symbol is None:
            return string
        if not isinstance(string, str):
            return string
        if symbol == "":
            return string
        return string.replace(symbol, "")

    def starts_with(self, string, prefix):
        if string is None or prefix is None:
            return False
        if not isinstance(string, str):
            return False
        return string.startswith(prefix)

    def to_list(self, string, delimiter):
        if string is None:
            return None
        if not isinstance(string, str):
            return None
        if string == "":
            return []
        return string.split(delimiter)
