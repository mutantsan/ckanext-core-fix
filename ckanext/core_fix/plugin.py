import ckan.plugins as plugins
import ckan.plugins.toolkit as tk


from ckanext.core_fix.helpers import get_helpers

class CoreFixPlugin(plugins.SingletonPlugin):
    plugins.implements(plugins.IConfigurer)
    plugins.implements(plugins.ITemplateHelpers)

    # IConfigurer

    def update_config(self, config_: tk.CKANConfig):
        tk.add_template_directory(config_, "templates")
        tk.add_public_directory(config_, "public")
        tk.add_resource("assets", "core_fix")

    # ITemplateHelpers

    def get_helpers(self):
        return get_helpers()
