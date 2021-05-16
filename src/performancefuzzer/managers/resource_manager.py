class ResourceManager:
    def __init__(self) -> None:
        self.scheduler = None
        self.source = ''

        self.mutaionControllers = []
        self.benchmarkControleers = []