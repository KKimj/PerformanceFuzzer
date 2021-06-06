class Mutation:
    def __init__(self, vector_max_num = 10):

        self.vector_max_num = vector_max_num
        self.vectors_num = 0
        self.vectors = [
            # {
            #     'function_num' : 0,
            #     'label_num' : 0,
            #     'code' : 'call void asm sideeffect "NOP;", ""()\n',
            #     'count' : 1,
            # }
        ]

        self.map = {
            'vector_max_num' : self.vector_max_num,
            'vectors_num' : self.vectors_num,
            'vectors' : self.vectors
        }
    
    # def map(self):
    #     return {
    #         'vector_max_num' : self.vector_max_num,
    #         'vectors_num' : self.vectors_num,
    #         'vectors' : self.vectors
    #     }


if __name__ == '__main__':
    muation = Mutation()
    
    print(muation.map)
    muation.vectors.append({
                'function_num' : 0,
                'label_num' : 0,
                'code' : 'call void asm sideeffect "NOP;", ""()\n',
                'count' : 1,
            })
    muation.map['vectors_num'] += 1
    muation.map['vector_max_num'] += 1
    print(muation.map)
