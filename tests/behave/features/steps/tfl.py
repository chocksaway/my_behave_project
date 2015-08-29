from behave import *

@step('I should receive a "{numeric}" response')
def step_impl(context, numeric):
    """
    :type context behave.runner.Context
    """
    pass


@given('that the TFL connections endpoint is available for "{endpoint_type}" line')
def step_impl(context, endpoint_type):
    """
    :type context behave.runner.Context
    """
    pass


@when("I make a request")
def step_impl(context):
    """
    :type context behave.runner.Context
    """
    pass


@then('I should receive "{data_type}" data')
def step_impl(context, data_type):
    """
    :type context behave.runner.Context
    """
    pass