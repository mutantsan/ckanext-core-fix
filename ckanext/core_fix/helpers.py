from __future__ import annotations

import logging
from typing import Callable, Any

import ckan.plugins.toolkit as tk

import ckanext.core_fix.config as conf
import ckanext.core_fix.utils as utils


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
    helpers: dict[str, Callable[..., Any]] = {
        "dashboard_activity_stream": dashboard_activity_stream,
        "cf_is_fix_disabled": lambda x: utils.is_fix_disabled(x),
    }

    if utils.is_fix_disabled(conf.Fixes.dashboard_activity):
        helpers.pop("dashboard_activity_stream")
        utils.notify_disabled(conf.Fixes.dashboard_activity)
    else:
        utils.notify_enabled(conf.Fixes.dashboard_activity)

    return helpers
