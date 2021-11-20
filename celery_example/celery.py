from celery import Celery

app = Celery('tasks', broker='amqp://', backend='rpc://', task_default_queue="app",include=["celery_example.tasks"])
app.conf.update(
    task_routs={
                'celery_example.*': {'queue': 'app'}
                }
)
#{'tasks':'celery_example.tasks.add','id':'54086c5e-6¬193-4575-8308-dbab76798756','args':[1,2]}
# {"tasks":"celery_example.tasks.add","id":"54086c5e-6193-4575-8308-dbab76798756","args":[1,2]}