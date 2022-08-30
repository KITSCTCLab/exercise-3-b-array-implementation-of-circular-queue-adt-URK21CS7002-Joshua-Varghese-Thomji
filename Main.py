class MyCircularQueue:
    def __init__(self, size: int):
        self.size = size
        self.queue = []
        self.front = self.rear = -1

    def enqueue(self, value: int) -> bool:
        if not(is_full()):
            rear = (rear+1)%size
            queue[rear] = value
            if front == -1:
                front += 1
            return True

    def dequeue(self) -> bool:
        if not(is_empty()):
            x = queue[front]
            if rear == front:
                rear = front = -1
            else:
                front = (front+1)%size
            return True

    def get_front(self) -> int:
        if is_empty():
            return -1
        else:
            return(queue[front])

    def get_rear(self):
        if is_empty():
            return -1
        else:
            return(queue[rear])

    def is_empty(self):
        return(front == -1)

    def is_full(self):
        return((self.rear + 1) % self.size == self.front)


# Do not change the following code
operations = []
for specific_operation in input().split(','):
    operations.append(specific_operation.strip())
data = []
for item in input().split(','):
    item = item.strip()
    if item == '-':
        data.append([])
    else:
        data.append([int(item)])
obj = MyCircularQueue(data[0][0])
result = []
for i in range(len(operations)):
    if i == 0:
        result.append(None)
    elif operations[i] == "enqueue":
        result.append(obj.enqueue(data[i][0]))
    elif operations[i] == "get_rear":
        result.append(obj.get_rear())
    elif operations[i] == "get_front":
        result.append(obj.get_front())
    elif operations[i] == "dequeue":
        result.append(obj.dequeue())
    elif operations[i] == "is_full":
        result.append(obj.is_full())
    elif operations[i] == "is_empty":
        result.append(obj.is_empty())

print(result)
