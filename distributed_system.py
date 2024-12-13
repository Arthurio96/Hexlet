class Server:
    def __init__(self, id):
        self.id = id
        self.current_task = None
        self.remaining_time = 0
        
    def assign_task(self, task):
        self.current_task = task
        self.remaining_time = task["time"]

    def tick(self):
        if self.remaining_time > 0:
            self.remaining_time -= 1
        if self.remaining_time == 0:
            self.current_task = None

    def is_free(self):
        return self.current_task is None

    def __repr__(self):
        if self.current_task:
            return f"Server {self.id}: выполняет задание с приоритетом {self.current_task['priority']} (осталось {self.remaining_time} сек.)"
        else:
            return f"Server {self.id}: пусто"

class TaskQueue:
    def __init__(self):
        self.queue = []

    def add_task(self, task):
        self.queue.append(task)
        self.queue.sort(key=lambda x: x["priority"], reverse=True)

    def get_next_task(self):
        return self.queue.pop(0) if self.queue else None

    def __repr__(self):
        return f"Очередь заданий: {[(task['time'], task['priority']) for task in self.queue] if self.queue else 'нет'}"

class DistributedSystem:
    def __init__(self, num_servers):
        self.servers = [Server(i + 1) for i in range(num_servers)]
        self.task_queue = TaskQueue()

    def add_task(self, task):
        free_server = min(self.servers, key=lambda s: s.remaining_time if not s.is_free() else 0)
        if free_server.is_free():
            free_server.assign_task(task)
            print(f"Задание с {task['time']} секундами выполнения и приоритетом {task['priority']} направлено на Сервер {free_server.id}.")
        else:
            self.task_queue.add_task(task)
            print(f"Задание с {task['time']} секундами выполнения и приоритетом {task['priority']} добавлено в очередь.")

    def tick(self):
        for server in self.servers:
            server.tick()

        for server in self.servers:
            if server.is_free():
                next_task = self.task_queue.get_next_task()
                if next_task:
                    server.assign_task(next_task)

    def display_status(self):
        for server in self.servers:
            print(server)
        print(self.task_queue)

if __name__ == "__main__":
    print("Добро пожаловать в симулятор распределенной системы.")
    num_servers = int(input("Введите количество серверов: "))
    system = DistributedSystem(num_servers)

    while True:
        command = input("Команда (добавить <время> <приоритет>, тик, статус, выход): ")
        if command.startswith("добавить"):
            _, time, priority = command.split()
            system.add_task({"time": int(time), "priority": int(priority)})
        elif command == "тик":
            system.tick()
        elif command == "статус":
            system.display_status()
        elif command == "выход":
            break
        else:
            print("Неизвестная команда.")