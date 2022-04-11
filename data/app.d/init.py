"""
init.py

A very simple example of initializing a Deephaven server through application mode.

This script simply makes a table with 5 values in it.

@author Jake Mulford
@copyright Deephaven Data Labs LLC
"""
import jpy
from deephaven import empty_table
from typing import Callable

ApplicationState = jpy.get_type("io.deephaven.appmode.ApplicationState")

#Non ApplicationState examples
def hello():
    print("Hello world")

source = empty_table(5)
result = source.update(["Values = i"])

#ApplicationState examples
def start(app: ApplicationState):
    table = empty_table(5)
    table = table.update(["Values = i"])

    app.setField("table", table.j_object)

def initialize(func: Callable[[ApplicationState], None]):
  app = jpy.get_type("io.deephaven.appmode.ApplicationContext").get()
  func(app)

initialize(start)
