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
        
    def search_substr(self, subst, st):
        resault = st.lower().find(subst.lower())
        if (resault != -1):
            print("Есть контакт!")
        else:
            print("Мимо!")
    def shortener(self,st):
        while '(' in st or ')' in st:
            left = st.rfind('(')
            right = st.find(')', left)
            st = st.replace(st[left:right + 1], '')
        return st       
                
str = StringHandler()
str.search_substr('Кол', 'коЛокОл')
str.search_substr('Колобок', 'колобоК')
str.search_substr('Кол', 'Плов')
str.camel('Утром!! было! солнечно!!!!')
print(str.shortener('123(xyz(568)9)zvq'))


   




