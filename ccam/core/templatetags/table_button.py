from django import template

register = template.Library()


@register.inclusion_tag("core/__table_button.html")
def table_button(
    button_text,
    icon="",
    href="",
    custom_class="",
    bootstrap_icon=False,
    image_icon=False,
    color_class="green-svg",
    icon_style="outlined",
    icon_path="",
    abs_url="",
):
    return {
        "button_text": button_text,
        "icon": icon,
        "href": href,
        "custom_class": custom_class,
        "bootstrap_icon": bootstrap_icon,
        "image_icon": image_icon,
        "color_class": color_class,
        "icon_style": icon_style,
        "icon_path": icon_path,
        "abs_url": abs_url,
    }
