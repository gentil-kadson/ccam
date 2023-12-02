from __future__ import annotations

import typing

from allauth.account.adapter import DefaultAccountAdapter
from allauth.socialaccount.adapter import DefaultSocialAccountAdapter
from django.conf import settings
from django.http import HttpRequest
from django.urls import reverse_lazy

from ccam.core.constants import COURSE_COORDINATOR_GROUP_NAME, SEAC_COORDINATOR_GROUP_NAME, STUDENT_GROUP_NAME

if typing.TYPE_CHECKING:
    from allauth.socialaccount.models import SocialLogin

    from ccam.users.models import User


class AccountAdapter(DefaultAccountAdapter):
    def is_open_for_signup(self, request: HttpRequest) -> bool:
        return getattr(settings, "ACCOUNT_ALLOW_REGISTRATION", True)


class SocialAccountAdapter(DefaultSocialAccountAdapter):
    def is_open_for_signup(self, request: HttpRequest, sociallogin: SocialLogin) -> bool:
        return getattr(settings, "ACCOUNT_ALLOW_REGISTRATION", True)

    def populate_user(self, request: HttpRequest, sociallogin: SocialLogin, data: dict[str, typing.Any]) -> User:
        """
        Populates user information from social provider info.

        See: https://django-allauth.readthedocs.io/en/latest/advanced.html?#creating-and-populating-user-instances
        """
        user = sociallogin.user
        if name := data.get("name"):
            user.name = name
        elif first_name := data.get("first_name"):
            user.name = first_name
            if last_name := data.get("last_name"):
                user.name += f" {last_name}"
        return super().populate_user(request, sociallogin, data)


class PeopleAccountAdapter(AccountAdapter):
    GROUPS_HOME_URLS = {
        SEAC_COORDINATOR_GROUP_NAME: reverse_lazy("people:managers:home"),
        COURSE_COORDINATOR_GROUP_NAME: reverse_lazy("people:coordinators:home"),
        STUDENT_GROUP_NAME: reverse_lazy("people:students:home"),
    }

    def get_login_redirect_url(self, request):
        user_group = request.user.groups.first()
        return self.GROUPS_HOME_URLS[user_group.name] if user_group else "/"

    def get_logout_redirect_url(self, request):
        return "/accounts/login/"
