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
            
str = StringHandler()
str.search_substr('Кол', 'коЛокОл')
str.search_substr('Колобок', 'колобоК')
str.search_substr('Кол', 'Плов')

