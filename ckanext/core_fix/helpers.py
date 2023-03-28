from __future__ import annotations

import logging
from typing import Callable, Any

import ckan.plugins as p
import ckan.plugins.toolkit as tk

import ckanext.core_fix.config as conf
import ckanext.core_fix.utils as utils


log = logging.getLogger(__name__)


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


def get_fixes_with_css() -> list[str]:
    """Return a list of fixes name that include CSS changes"""
    return [fix.name for fix in conf.FIXES_WITH_CSS]


def get_helpers():
    helpers: dict[str, Callable[..., Any]] = {
        "cf_is_fix_disabled": lambda x: utils.is_fix_disabled(x),
        "cf_get_fixes_with_css": get_fixes_with_css,
    }

    if p.plugin_loaded("activity"):
        tk.chained_helper(dashboard_activity_stream)

        helpers["dashboard_activity_stream"] = dashboard_activity_stream

        if utils.is_fix_disabled(conf.Fixes.dashboard_activity):
            helpers.pop("dashboard_activity_stream")

    return helpers
