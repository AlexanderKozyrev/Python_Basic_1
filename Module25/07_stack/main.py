class Stack:
    def __init__(self):
        self.__elem = []

    def __str__(self):
        return '; '.join(self.__elem)

    def addendum(self, element):
        self.__elem.append(element)

    def removal(self):
        if len(self.__elem) == 0:
            return None
        return self.__elem.pop()


class TaskManager:
    def __init__(self):
        self.task = dict()

    def __str__(self):
        display = []
        if self.task:
            for i_priority in sorted(self.task.keys()):
                display.append('{prior} {task}\n'.format(
                    prior=str(i_priority),
                    task=self.task[i_priority]
                )
            )

        return ''.join(display)

    def new_task(self, task, priority):
        if priority not in self.task:
            self.task[priority] = Stack()
        self.task[priority].addendum(task)


manager = TaskManager()
manager.new_task("сделать уборку", 4)
manager.new_task("помыть посуду", 4)
manager.new_task("отдохнуть", 1)
manager.new_task("поесть", 2)
manager.new_task("сдать дз", 2)
print(manager)
