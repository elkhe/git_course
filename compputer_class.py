class CPU:
    def __init__(self, name, fr) -> None:
        self.name = name
        self.fr = fr


class Memory:
    def __init__(self, name, volume) -> None:
        self.name = name
        self.volume = volume


class MotherBoard:

    def __init__(self, name, cpu, *mem_slots) -> None:
        self.name = name
        self.cpu = cpu
        self.total_mem_slots = 4
        self.mem_slots = mem_slots[:self.total_mem_slots]


    def _describe_memory(self, mem):
        return '; '.join([f'{x.name} - {x.volume}' for x in mem])


    def get_config(self):
        return [f'Материнская плата: {self.name}', f'Центральный процессор: {self.cpu.name}, {self.cpu.fr}',
                f'Слотов памяти: {self.total_mem_slots}', f'Память: {self._describe_memory(self.mem_slots)}']  

c = CPU('Elbrus', 2)
m1 = Memory('SSD1', 250)
m2 = Memory('HDD', 500)
mb = MotherBoard('MotherB', c, m1, m2)

print(mb.get_config())