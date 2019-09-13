{
    'name': "Calendar Event Tag Color",
    'version': '9.0.1.0.0',
    'depends': [
        'calendar',
        'web_widget_color',
    ],
    'author': "Valentin THIRION, Jason PINDAT @ AbAKUS it-solutions SARL",
    'website': "http://www.abakusitsolutions.eu",
    'category': 'Calendar',
    'description': """
        Calendar Event Tag Color

        Restricts event tagging to 1 tag par event.
        Event colorization is defined by tags.

        The module is depends of web_calendar_time_limit in order to stack the modules extensions.
        If the module independency is needed, replace
        "var CalendarView = require('web_calendar_time_limit.CalendarViewTimeLimit');"
        by
        "var CalendarView = require('web_calendar.CalendarView');"
        in the JavaScript file

        This module has been developed by Valentin THIRION & Jason PINDAT @ AbAKUS it-solutions.
    """,
    'data': [
        'views/calendar_views.xml',
        'data/groups.xml',
        'security/ir.model.access.csv'
    ],
}
