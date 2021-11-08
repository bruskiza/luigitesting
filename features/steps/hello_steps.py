from behave import given, when, then
import requests
from structlog import get_logger

log = get_logger()

@given(u'there is a {url}')
def step_impl(context, url):
    context.url = url


@when(u'we go there')
def step_impl(context):
    log.info("In here")
    context.result = requests.get(context.url)


@then(u'it returns {status_code}')
def step_impl(context, status_code):
    log.info(context.result.status_code)
    log.info(status_code)
    assert context.result.status_code == int(status_code)

