from django import template

register = template.Library()


@register.inclusion_tag("core/__anchor.html")
def anchor(icon, anchor_text, bootstrap_icon=False, color_class="green-text", custom_class="", abs_url="", href=""):
    return {
        "icon": icon,
        "href": href,
        "anchor_text": anchor_text,
        "bootstrap_icon": bootstrap_icon,
        "color_class": color_class,
        "custom_class": custom_class,
        "abs_url": abs_url,
    }
