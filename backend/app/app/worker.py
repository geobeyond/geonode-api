# from raven import Client

from typing import List
from pydantic import UUID4, UrlStr

from app.db_models.job import Job
from app.core.celery_app import celery_app
from app.tasks.base import WPSTask
from app.api.utils.processes.buffer.buffer import Buffer
from app.api.utils.processes.hello.hello import getResult

from app.models.job import statusEnum
from app.models.common import link as Link
from app.core.config import (
    StatusMessage,
    ApplicationType,
    WPSRel,
    Lang,
    Title
)

# client_sentry = Client(config.SENTRY_DSN)

import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


@celery_app.task(acks_late=True)
def test_celery(word: str):
    return f"test task return {word}"


@celery_app.task(
    bind=True,
    base=WPSTask,
    name="async_buffer",
    acks_late=True
)
def async_buffer(self, job_jid: UUID4, location: UrlStr):
    logger.info("======> Let's try to execute the query")
    logger.info(f"======> The unique value of UUID for the job is {job_jid}")
    job = self.session.query(Job).get(job_jid)
    logger.info(f"======> Status for the job is {job.status}")
    self_link = Link(
        href=f"{location}",
        rel=WPSRel.SELF.value,
        type=ApplicationType.JSON.value,
        hreflang=Lang.EN.value,
        title=Title.SELF.value
    )
    logger.info(f"======> Self link is {self_link}")
    job_links = [self_link.dict()]
    job.links = job_links
    self.session.commit()
    p = Buffer(inputs=job.inputs, outputs=job.outputs)
    # p.run()
    # save result in the Job model
    logger.info("======> Let's try to save the result")
    result = getResult() # p.result
    if result:
        result_link = Link(
            href=f"{location}/result",
            rel=WPSRel.RESULT.value,
            type=ApplicationType.JSON.value,
            hreflang=Lang.EN.value,
            title=Title.RESULT.value
        )
        job.progress = 100
        job.status = statusEnum.SUCCESSFUL.value
        job.message = StatusMessage.SUCCESSFUL.value
        job_links = job_links + [result_link.dict()]
        logger.info(f"======> job_links has value {job_links}")
        job.links = job_links
        job.result = result.dict()
        self.session.commit()
        json_result = result.json()
        logger.info(f"======> Job record refreshed")
        logger.info(f"======> The new value for the status of the job is {job.status}")
        logger.info(f"======> Result dictionary for the job {job_jid} is \n{json_result}")
    return f"async buffer finished"