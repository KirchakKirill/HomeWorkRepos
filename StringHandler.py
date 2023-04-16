class StringHandler:
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