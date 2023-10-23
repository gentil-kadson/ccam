from django import template

register = template.Library()


@register.inclusion_tag("core/_breadcrumb_item.html")
def breadcrumb_item(
    text: str, icon: str, href="", bootstrap_icon=False, active=False, icon_style="outlined", last_item=False
):
    return {
        "text": text,
        "icon": icon,
        "bootstrap_icon": bootstrap_icon,
        "active": active,
        "icon_style": icon_style,
        "last_item": last_item,
        "href": href,
    }
