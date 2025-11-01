"""
pyp_iniparser - Primitive (seriously!) Python Ini File Parser.

Adam Kubiak @2024
"""


class PYP_Iniparser:
    def __init__(self):
        self.filename = ""
        self.data = {}
        self._lines = []

    def _read(self, filename):
        """
        Parameters
        ----------
        filename : string

        Returns
        -------
        bool
            True on success
            False on error
        """
        try:
            with open(filename, "r") as file:
                lines = file.readlines()
                for line in lines:
                    if line[0].isalpha():
                        self._lines.append(line.strip())
        except IOError:
            return False

        return True

    def _force_type(self, word):
        """
        Parameters
        ----------
        word : list to process

        Returns
        -------
        list
            processed list, only int, float, bool and string are supported
        """
        a = ""
        if len(word) > 2:
            word[1] = "=".join(word[1::]).strip()
            return word
        if word[1].lower() == "true":
            word[1] = True
            return word
        if word[1].lower() == "false":
            word[1] = False
            return word
        try:
            a = int(word[1])
        except ValueError:
            try:
                a = float(word[1])
            except ValueError:
                a = str(word[1])
        finally:
            word[1] = a
        return word

    def parse(self, filename, strict=False):
        """
        Parameters
        ----------
        filename : string
            valid path to file
        strict : Bool, optional
            determines if typechecking is enabled
            default False

        Returns
        -------
        bool
            True of success
            False on error (only in case of IO errors!)
        """
        if not self._read(filename):
            return False
        for line in self._lines:
            if "=" not in line or not line[0].isalpha():
                continue
            word = line.split("=")

            if len(word) > 2:
                self.data[word[0].strip()] = "=".join(word[1::]).strip()

            else:
                if strict:
                    word = self._force_type(word)
                    if isinstance(word[1], str):
                        self.data[word[0].strip()] = word[1].strip()
                        continue

                    self.data[word[0].strip()] = word[1]
                    continue
                self.data[word[0].strip()] = word[1].strip()
        return True


def main():
    import sys

    sys.exit("This is a module file")


if __name__ == "__main__":
    main()
