import re


class Parser:
    """
    Use to parse user's input
    """
    def parser(self, q):
        """
        Parse user element to being usable on wikipedia
        """

        q = q.lower()
        p = re.compile(
            "ou est \s*([^.?:;]*)$|"
            "où est \s*([^.?:;]*)$|"
            "ou se trouve\s*([^.?:;]*)$|"
            "où se trouve\s*([^.?:;]*)$|"
            "l’adresse de\s*([^.?:;]*)$|"
            "ladresse de\s*([^.?:;]*)$|"
            "l adresse de\s*([^.?:;]*)$|"
            "ou se situe\s*([^.?:;]*)$|"
            "où se situe\s*([^.?:;]*)$"
            )
        match = p.match(q)

        if match:
            result = [group for group in match.groups() if group is not None]
            return result

        return None
