#app/tasks/base.py
import sqlalchemy
from app.core.celery_app import  celery_app

from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import scoped_session
from app.db.session import engine


class WPSTask(celery_app.Task):

    def __call__(self, *args, **kwargs):
        self.engine = engine
        session_factory = sessionmaker(bind=self.engine)
        self.session = scoped_session(session_factory)
        return super().__call__(*args, **kwargs)

    def after_return(self, status, retval, task_id, args, kwargs, einfo):
        if hasattr(self, 'session'):
            self.session.remove()
        if hasattr(self, 'engine'):
            self.engine.engine.dispose()