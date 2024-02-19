import multiprocessing
import os

bind = "0.0.0.0:8001"
workers = int(os.getenv("WEB_CONCURRENCY", multiprocessing.cpu_count() * 2))
threads = int(os.getenv("PYTHON_MAX_THREADS", 1))
worker_class = "gthread"

accesslog = "-"
access_log_format = "%(h)s %(l)s %(u)s %(t)s '%(r)s' %(s)s %(b)s '%(f)s' '%(a)s' in %(D)sµs"  # noqa: E501

reload = os.getenv("WEB_RELOAD", "").lower() in ("1", "true")
