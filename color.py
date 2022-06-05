"""
Return RGB in format (int, int, int) when ask certain color(Ref, Green ats)
"""


class Color:
    @staticmethod
    def red():
        return 255, 0, 0

    @staticmethod
    def green():
        return 0, 255, 0

    @staticmethod
    def blue():
        return 0, 0, 255

    @staticmethod
    def white():
        return 255, 255, 255

    @staticmethod
    def black():
        return 0, 0, 0
