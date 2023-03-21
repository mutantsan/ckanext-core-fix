from __future__ import annotations

import logging
from typing import Callable, Any

import ckan.plugins.toolkit as tk

from ckanext.core_fix.config import get_disabled_fixes


log = logging.getLogger(__name__)


@tk.chained_helper
def dashboard_activity_stream(
    next_func: Callable[..., Any], *args, **kw: Any  # type: ignore
) -> list[dict[str, Any]]:
    """
    Insert `offset` positional argument
    If kw isn't empty, we are started to pass kw args properly

    https://github.com/ckan/ckan/pull/7482
    """

    if not kw:
        args: list[Any] = list(args)
        args.insert(3, 0)

    return next_func(*args, **kw)


def get_helpers():
    disabled: list[str] = get_disabled_fixes()
    helpers: dict[str, Callable[..., Any]] = {
        "dashboard_activity_stream": dashboard_activity_stream
    }

    if "dashboard_activity" in disabled:
        helpers.pop("dashboard_activity_stream")
        log.warning("The `dashboard_activity` fix has been disabled")

    return helpers
