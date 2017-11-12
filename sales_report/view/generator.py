import os
from jinja2 import Environment, BaseLoader
import logging


def create_html_report(template_vars, template_path, path, name='output.html'):
    """
    Renders a HTML template via Jinja2 using the provided template variables and the template itself.

    :param template_vars: (dict) Variable pool which Jinja2 uses to generate dynamic content.
    :param template_str: (str) Template in string form.
    :return: (Template) Populated HTML template.
    """
    logging.info('render report ...')
    template_string = open(template_path).read()
    # Creates the template from template string
    template = Environment(loader=BaseLoader).from_string(template_string)
    # Populates the template with values retrieves from the DataFrame
    rendered_template = template.render(template_vars)
    output_path = os.path.join(path, name)
    logging.info('write report to {}'.format(output_path))
    with open(output_path, "w") as text_file:
        text_file.write(rendered_template)
