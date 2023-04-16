class StringHandler:

    def camel(self, st):
        tmp = None
        res = st[0]
        for value in st:
            if (tmp != None):
                if (tmp.islower()):
                    res += value.upper()
                else:
                    res += value.lower()
            tmp = res[-1]
        print(res)

str = StringHandler()
str.camel('Утром!! было! солнечно!!!!')