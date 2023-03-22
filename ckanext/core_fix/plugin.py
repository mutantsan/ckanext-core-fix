import logging

import ckan.plugins as p
import ckan.plugins.toolkit as tk

import ckanext.core_fix.config as conf
import ckanext.core_fix.utils as utils
import ckanext.core_fix.helpers as helper


log = logging.getLogger(__name__)


class CoreFixPlugin(p.SingletonPlugin):
    p.implements(p.IConfigurer)
    p.implements(p.ITemplateHelpers)

    # IConfigurer

    def update_config(self, config_: tk.CKANConfig):
        utils.check_disabled_fixes()
        utils.notify()

        tk.add_template_directory(config_, "templates")
        tk.add_public_directory(config_, "public")
        tk.add_resource("assets", "core_fix")

        if not utils.is_fix_disabled(conf.Fixes.markdown_macro):
            tk.add_template_directory(
                config_, f"templates/{conf.Fixes.markdown_macro.name}/"
            )

    # ITemplateHelpers

    def get_helpers(self):
        return helper.get_helpers()
