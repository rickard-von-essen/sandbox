from locust import HttpLocust, TaskSet


def index(l):
    l.client.get("/")


def status(l):
    l.client.get("/status/")


def crash(l):
    l.client.get("/crash/")


class UserBehavior(TaskSet):
    tasks = {index: 10, status: 75, crash: 1}

    # def on_start(self):
    #    login(self)


class WebsiteUser(HttpLocust):
    task_set = UserBehavior
    min_wait = 5000
    max_wait = 9000
