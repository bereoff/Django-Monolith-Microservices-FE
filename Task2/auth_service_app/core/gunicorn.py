import multiprocessing
import os

bind = "0.0.0.0:8000"
workers = int(os.getenv("WEB_CONCURRENCY", multiprocessing.cpu_count() * 2))
threads = int(os.getenv("PYTHON_MAX_THREADS", 1))
worker_class = "gthread"

# Arquivos de log
accesslog = "-"
access_log_format = "%(h)s %(l)s %(u)s %(t)s '%(r)s' %(s)s %(b)s '%(f)s' '%(a)s' in %(D)sµs"  # noqa: E501

reload = os.getenv("WEB_RELOAD", "").lower() in ("1", "true")

# Configurações adicionais específicas do seu aplicativo podem ser adicionadas aqui
# Exemplo: preload = True

# O nome do arquivo da aplicação WSGI
# Deve ser no formato 'nome_do_modulo:nome_do_objeto'
# Se o seu arquivo WSGI está em 'core/wsgi.py', então seria 'core.wsgi:application'
# application é o objeto WSGI padrão
# Caso você tenha uma instância diferente, substitua 'application' por ela
# Exemplo: 'core.wsgi:my_custom_application'
# application = "core.wsgi:application"
