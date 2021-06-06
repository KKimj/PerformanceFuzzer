from models.mutation_model import Mutation
import random

class MutationController:
    def __init__(self, vector_max_num = 10, *args) -> None:
        # print(files)
        self.mutation = Mutation(vector_max_num = vector_max_num)
        self.map = self.mutation.map

    def __call__(self) -> None:
        pass

    def insert(self):
        function_rand_num = random.randrange(10)
        label_rand_num = random.randrange(10)
        count_rand_num = random.randrange(10)
        
        vector = {
                'function_num' : function_rand_num,
                'label_num' : label_rand_num,
                'code' : 'call void asm sideeffect "NOP;", ""()\n',
                'count' : count_rand_num,
            }
        # {
        #     'function_num' : 0,
        #     'label_num' : 0,
        #     'code' : 'call void asm sideeffect "NOP;", ""()\n',
        #     'count' : 1,
        # }
        self.map['vectors_num'] += 1
        self.map['vectors'].append(vector)
        pass

    def drop_out(self):
        rand_index = random.randrange(self.map['vectors_num'])
        self.map['vectors'].pop(rand_index)

        self.map['vectors_num'] -= 1


