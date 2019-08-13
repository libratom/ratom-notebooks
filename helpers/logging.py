import logging

import ipywidgets as widgets
from IPython.display import display


# https://ipywidgets.readthedocs.io/en/stable/examples/Output%20Widget.html#Integrating-output-widgets-with-the-logging-module
class OutputWidgetHandler(logging.Handler):
    """ Custom logging handler sending logs to an output widget """

    def __init__(self, *args, **kwargs):
        super(OutputWidgetHandler, self).__init__(*args, **kwargs)
        layout = {
            'display': 'flex',
            'border': '1px solid lightgray',
        }
        self.out = widgets.Output(layout=layout)

    def emit(self, record):
        """ Overload of logging.Handler method """
        new_output = {
            'name': 'stdout',
            'output_type': 'stream',
            'text': f'{self.format(record)}\n'
        }
        self.out.outputs = (new_output, ) + self.out.outputs

    def show_logs(self):
        """ Show the logs """
        display(self.out)

    def clear_logs(self):
        """ Clear the current logs """
        self.out.clear_output()
