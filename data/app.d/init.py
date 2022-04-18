"""
init.py

A very simple example of initializing a Deephaven server through application mode.

This script simply makes a table with 5 values in it.

@copyright Deephaven Data Labs LLC
"""
from deephaven import empty_table
from deephaven.appmode import ApplicationState, get_app_state

from typing import Callable

ApplicationState = jpy.get_type("io.deephaven.appmode.ApplicationState")

#Non ApplicationState examples. These global variables are available for use within Deephaven
def hello():
    print("Hello world")

source = empty_table(5)
result = source.update(["Values = i"])

#ApplicationState examples. These variables are scoped to the application mode function, and
#only become global variables during the app[<variable>] assignment.
def start(app: ApplicationState):
    table = empty_table(5)
    table = table.update(["Values = i"])

    app["table"] = table

def initialize(func: Callable[[ApplicationState], None]):
  app = get_app_state()
  func(app)

initialize(start)
