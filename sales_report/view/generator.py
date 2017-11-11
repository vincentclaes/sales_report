from jinja2 import Environment, BaseLoader


def render_template_from_string(template_vars, template_path):
    """
    Renders a HTML template via Jinja2 using the provided template variables and the template itself.

    :param template_vars: (dict) Variable pool which Jinja2 uses to generate dynamic content.
    :param template_str: (str) Template in string form.
    :return: (Template) Populated HTML template.
    """
    template_string = open(template_path).read()
    # Creates the template from template string
    template = Environment(loader=BaseLoader).from_string(template_string)
    # Populates the template with values retrieves from the DataFrame
    rendered_template = template.render(template_vars)
    with open('/home/vagrant/Desktop/axa_test/axa_test/view/output/output.html', "w") as text_file:
        text_file.write(rendered_template)