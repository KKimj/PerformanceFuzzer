class Benchmark:
    def __init__(self)-> None:
        self.task_clock = None
        self.CPUs_utilized = None

        self.context_switches = None
        self.cpu_migrations = None
        self.page_faults = None

        self.cyces = None
        self.instructions = None
        self.branches = None
        self.branch_misses = None

        self.time = None
        self.user_time = None
        self.sys_time = None