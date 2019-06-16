from raven import Client

from pydantic import UUID4

from app.core import config
from app.db_models.job import Job
from app.core.celery_app import celery_app
from app.tasks.base import WPSTask
from app.api.utils.processes.buffer import Buffer

from app.models.job import statusEnum
from app.core.config import StatusMessage

client_sentry = Client(config.SENTRY_DSN)


@celery_app.task(acks_late=True)
def test_celery(word: str):
    return f"test task return {word}"


@celery_app.task(bind=True, base=WPSTask, name='async_buffer', acks_late=True)
def async_buffer(self, job_jid: UUID4):
    job = self.session.query(Job).filter(Job.jid == job_jid).first()
    p = Buffer(inputs=job.inputs, outputs=job.outputs)
    p.run()
    # save p.result in the Job model
    result = p.result
    if result:
        job.update(
            progress=100,
            status=statusEnum.SUCCESSFUL.value,
            message=StatusMessage.SUCCESSFUL.value,
            result=result
        )
    return f"async buffer scheduled"