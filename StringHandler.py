class StringHandler:

    def shortener(self,st):
        while '(' in st or ')' in st:
            left = st.rfind('(')
            right = st.find(')', left)
            st = st.replace(st[left:right + 1], '')
        return st


str = StringHandler()
print(str.shortener('123(xyz(568)9)zvq'))