import logging

from ckanext.core_fix.config import Fixes, get_disabled_fixes


log = logging.getLogger(__name__)


def is_fix_disabled(fix: Fixes) -> bool:
    """Check if fix is disabled"""
    return fix.name in get_disabled_fixes()


def notify_enabled(fix: Fixes) -> None:
    log.info(f"The `{fix}` fix has been enabled")


def notify_disabled(fix: Fixes) -> None:
    log.info(f"The `{fix}` fix has been disabled")
