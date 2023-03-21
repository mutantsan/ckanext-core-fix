from __future__ import annotations

import ckan.plugins.toolkit as tk


CONF_DISABLE_FIXES = "ckanext.core_fix.disable_fix"


def get_disabled_fixes() -> list[str]:
    return tk.aslist(tk.config.get(CONF_DISABLE_FIXES, []))
