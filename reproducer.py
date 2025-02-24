from app import dummy_task

dummy_task.delay("hello, world")  # Will be successfully scheduled and executed.

# Now we'll do the same with 20MB of data, the publish will fail but the
# following call will succeed nonetheless. We'll be able to see that there's no
# corresponding execution message in the worker's logs.
dummy_task.delay("@" * 20_000_000)


# The following call is where we'll get the PRECONDITION_FAILED exception for
# the previous message publish operation.
dummy_task.delay("hello, world")
