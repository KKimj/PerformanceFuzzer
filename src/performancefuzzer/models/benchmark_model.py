class Benchmark:
    def __init__(self, task_clock = None, **kwargs) -> None:
        self.task_clock = None
        self.context_switches = None
        self.cpu_migrations = None
        self.cycles = None
        self.instructions = None
        self.branches = None
        self.branch_misses = None

        self.CPUs_utilized = None

        self.time = None
        self.user_time = None
        self.sys_time = None
        
        # self.update(kwargs)
