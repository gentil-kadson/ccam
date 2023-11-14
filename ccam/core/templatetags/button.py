from django import template

register = template.Library()


@register.inclusion_tag("core/__button.html")
def button(
    button_text,
    custom_class="",
    type="submit",
    form_id="",
    id="",
    bootstrap_icon=False,
    image_icon=False,
    icon_path="",
    icon_style="outlined",
    icon="",
    color_class="green-svg",
):
    return {
        "button_text": button_text,
        "icon": icon,
        "bootstrap_icon": bootstrap_icon,
        "icon_style": icon_style,
        "image_icon": image_icon,
        "icon_path": icon_path,
        "custom_class": custom_class,
        "type": type,
        "form_id": form_id,
        "id": id,
        "color_class": color_class,
    }
