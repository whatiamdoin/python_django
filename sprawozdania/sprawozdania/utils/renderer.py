from string import Template


def render_html(html, message=''):
    templated_html = Template(html)
    filled_templated_html = templated_html.substitute(message=f"{message}")
    return filled_templated_html
