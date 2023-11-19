from django import template

register = template.Library()


@register.inclusion_tag("core/__simple_table_button.html")
def simple_table_button(custom_class="", href="", id="", color_class="", icon="", bootstrap_icon=False):
    return {
        "custom_class": custom_class,
        "href": href,
        "id": id,
        "color_class": color_class,
        "icon": icon,
        "bootstrap_icon": bootstrap_icon,
    }
