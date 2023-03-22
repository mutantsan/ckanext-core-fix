from __future__ import annotations

from enum import Enum, auto

import ckan.plugins.toolkit as tk


CONF_DISABLE_FIXES = "ckanext.core_fix.disable_fix"


def get_disabled_fixes() -> list[str]:
    return tk.aslist(tk.config.get(CONF_DISABLE_FIXES, []))


class Fixes(Enum):
    dashboard_activity = auto()
    markdown_macro = auto()
    fontawesome_icons = auto()
    secondary_order = auto()
    button_icon_text_gap = auto()
    mobile_layout_breakpoint = auto()


FIXES_WITH_TEMPLATES = [
    Fixes.mobile_layout_breakpoint,
    Fixes.markdown_macro,
]
