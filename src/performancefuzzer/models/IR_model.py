class IRModel:
    def __init__(self) -> None:
        self.scope = Scope()
        self.source_name = 'test.ll'
        self.target_name = 'test.ll'
        


class Scope:
    def __init__(self):
        self.scope = {'global' : False, 'function' : False, 'label' : False }

if __name__ == '__main__':
    s1 = Scope()

    print(s1.scope)