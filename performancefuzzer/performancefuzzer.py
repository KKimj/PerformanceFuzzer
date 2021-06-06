from controllers import IR_controller
from controllers import mutation_controller
from controllers.benchmark_controller import BenchmarkController
from controllers.IR_controller import IRController
from controllers.mutation_controller import MutationController
from managers import resource_manager

from managers.resource_manager import ResourceManager

class PerformanceFuzzer:
    def __init__(self, source_file_name) -> None:

        # Resource manager
            # C source file -> IR file

        # Mutation
        # Benchmark
        pass
    
    def __call__(self) -> None:
        pass

if __name__ == '__main__':
    print('performance fuzzer')
    benchmark_controller = BenchmarkController()
    
    IR_controller = IRController(
        path = '/home/kkimj/PerformanceFuzzer/tests/helloworld/',
        source_name = 'main.c', target_name = 'main_opt', compile_option = '', execute_arguments = '',)

    IR_controller = IRController()
    
    mutation_controller = MutationController()

    resource_manager = ResourceManager()

    IR_controller.profiling()
    IR_controller.append(label_num = 4, code_count = 4)
    IR_controller.insert(label_num = 4, code_count = 4)
    IR_controller.insert(label_num = 0, code_count = 2)


    
    
