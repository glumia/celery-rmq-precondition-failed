from celery import Celery

app = Celery(broker="amqp://guest:guest@rmq:5672//")


@app.task
def dummy_task(data: str):
    print(f"executing dummy task with data: {data}")
