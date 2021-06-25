'''Muation controller'''
import random
# Models
from models.action_model import Action
from models.mutation_model import Mutation

class MutationController:
    def __init__(self, capacity = 10, files_num = 0) -> None:
        self.mutation = Mutation(capacity = capacity)

        self.files_num = 0 
        self.IRs = []


    @property
    def actions_num(self):
        return len(self.mutation.actions)


    def toJson(self) -> dict:
        actions = []
        for action in self.mutation.actions:
            actions.append({
                'file_num' : action.file_num,
                'function_num' : action.function_num,
                'label_num' : action.label_num,
                
                'method_num' : action.method_num,
                'method_count' : action.method_count,
                
                'code' : action.code,
            })

        json = {
            'action_space' : self.mutation.action_space,
            'capacity' : self.mutation.capacity,
            'actions' : actions
        }
        return json

    def fromJson(self, json) -> None:
        self.mutation.action_space = json['action_space']
        self.mutation.capacity = json['capacity']

        actions = json['actions']
        self.mutation.actions = []
        for action in actions:
            self.mutation.actions.append(
                Action(
                    file_num = action['file_num'], 
                    function_num = action['function_num'], 
                    label_num = action['label_num'], 
                    method_num = action['method_num'], 
                    method_count = action['method_count'], 
                    code = action['code'])
            )


    def insert(self, index, action):
        self.mutation.actions.insert(index, action)

    def append(self, action):
        self.mutation.actions.append(action)

    def drop_out(self):
        rand_index = random.randrange(self.actions_num)
        self.mutation.actions.pop(rand_index)
    
    def sample(self):
        rand_file = random.randrange(self.files_num)

        rand_function = 0
        rand_label = 0
        
        rand_method = 0
        rand_count = 0
        

        action = Action(file_num = rand_file,
                        function_num = rand_function,
                        labe_num = rand_label,
                        method_num = rand_method,
                        method_count = rand_count,
                        code = '')
        return action

    def reset(self):
        self.mutation.actions.clear()

    def add_file(self):
        pass
        
if __name__ == '__main__':
    mutationController = MutationController()
