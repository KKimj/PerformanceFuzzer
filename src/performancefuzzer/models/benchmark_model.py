class Benchmark:
    def __init__(self) -> None:
        self.task_clock = None
        self.context_switches = None
        self.cpu_migrations = None
        self.cycles = None
        self.instructions = None
        self.branches = None
        self.branch_misses = None

        self.CPUs_utilized = None

        self.user_time = None
        self.sys_time = None

    # getter time elapsed, user_time + sys_time
    pass