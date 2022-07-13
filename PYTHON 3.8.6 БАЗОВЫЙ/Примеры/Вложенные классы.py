class Women:
    title = 'object title'
    photo = 'object photo'
    ordering = 'object ordering'

    def __init__(self, user, psw):
        self.user = user
        self.psw = psw
        self.meta = self.Meta(user + '@' + psw)

    class Meta:
        object = ['id']

        def __init__(self, access):
            self.access = access


w = Women('root', '12345')
print(w.ordering)
print(w.Meta.object)
print(w.__dict__)
print(w.meta.__dict__)
