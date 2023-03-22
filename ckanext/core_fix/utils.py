from __future__ import annotations

import logging

from ckanext.core_fix.config import Fixes, get_disabled_fixes
from ckanext.core_fix.exceptions import CoreFixException

log = logging.getLogger(__name__)


def notify() -> None:
    """Notify about disabled/enabled fixes on startup"""
    for fix in Fixes:
        notify_disabled(fix) if is_fix_disabled(fix) else notify_enabled(fix)


def notify_enabled(fix: Fixes) -> None:
    log.info(f"The `{fix}` fix has been enabled")


def notify_disabled(fix: Fixes) -> None:
    log.info(f"The `{fix}` fix has been disabled")


def check_disabled_fixes() -> None:
    """Check if all fixes listed as disabled are actually exists"""
    available_fixes: list[str] = Fixes._member_names_

    for fix in get_disabled_fixes():
        if is_fix_exist(fix):
            continue

        raise CoreFixException(
            f"The fix `{fix}` doesn't exists. List of available fixes: {available_fixes}"
        )


def is_fix_disabled(fix: Fixes | str) -> bool:
    """Check if fix is disabled"""
    fix_name: str = fix.name if isinstance(fix, Fixes) else fix
    available_fixes: list[str] = Fixes._member_names_

    if fix_name not in available_fixes:
        raise CoreFixException(
            f"The fix `{fix}` doesn't exists. List of available fixes: {available_fixes}"
        )

    return fix_name in get_disabled_fixes()


def is_fix_exist(fix: str) -> bool:
    return fix in Fixes._member_names_
