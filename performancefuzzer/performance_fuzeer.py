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
    IR_controller = IRController()
    mutation_controller = MutationController()

    resource_manager = ResourceManager()
    
