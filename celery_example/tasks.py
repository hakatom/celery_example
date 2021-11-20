from celery_example.celery import app
@app.task
def add(x, y):
    res = x+y
    message=f"result is {res}"
