A sample Celery app to reproduce the `PRECONDITION_FAILED` error when
scheduling a new task.

The cause of this is the lack of [publisher
confirms](https://www.rabbitmq.com/docs/confirms#publisher-confirms) by default on
celery's rabbitmq messages.

What happens is that a `.delay`/`.apply_async` call where we try to schedule a
task with a lot of data (more than [rabbitmq's `max_message_size`
config](https://www.rabbitmq.com/docs/configure#config-items)) returns
successfully, the connection goes into an error state, and then we get an
exception as soon as we do the next `.delay`/`.apply_async` call.

To reproduce, run rabbitmq and the worker with:
```bash
docker compose up
```

Wait a bit until you see the `... celery@{hash} ready` message, then in another
shell run:
```bash
docker compose exec worker python reproducer.py
```
