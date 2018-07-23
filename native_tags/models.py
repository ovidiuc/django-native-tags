import settings

if 'native_tags.templatetags.native' in settings.BUILTIN_TAGS:
    try:
        try:
            # django >=1,8,<1.9
            from django.template.base import add_to_builtins
        except ImportError:
            # django<1.8
            from django.template import add_to_builtins
    except ImportError:
        # django>=1.9, not tested at all
        def add_to_builtins(module):
            if settings.TEMPLATES:
                for template_settings in settings.TEMPLATES:
                    template_settings['OPTIONS']['builtins'] += [mod]
    add_to_builtins('native_tags.templatetags.native')
