from django import template

register = template.Library()


@register.inclusion_tag("core/__anchor.html")
def anchor(icon, href, anchor_text, bootstrap_icon=False, color_class="green-text", custom_class=""):
    return {
        "icon": icon,
        "href": href,
        "anchor_text": anchor_text,
        "bootstrap_icon": bootstrap_icon,
        "color_class": color_class,
        "custom_class": custom_class,
    }
