# ckanext-core-fix

This extensions comes to provide temprorary fixes to CKAN core that isn't yet applied, but will be (probably) applied soon.

By default, all the fixes are enabled. Check the **Config settings** section to understand how to disabled specific fix.

All the fixes must be associated with a PR to the CKAN core.

## Requirements

Compatibility with core CKAN versions:

| CKAN version    | Compatible?   |
| --------------- | ------------- |
| 2.7 and earlier             | not tested    |
| 2.8             | not tested    |
| 2.9             | not tested    |
| 2.10.0             | yes    |

## Installation

I suggest using `pip install ckanext-core-fix` to install package. If you want to install it from github, you probably know what to do.

Add `core_fix` to `ckan.plugins` to enable the plugin.

## List of fixes
1. Fix dashboard activity page (`dashboard_activity`)
	Fix call of `dashboard_activity_stream` helper.
	https://github.com/ckan/ckan/pull/7482


## Config settings

	# Provide a list of fixes names to disable it
	# (optional, default: None).
	ckanext.core_fix.disable_fix = dashboard_activity

## Tests

To run the tests, do:

    pytest --ckan-ini=test.ini

## License

[AGPL](https://www.gnu.org/licenses/agpl-3.0.en.html)
