{
    'name': "Calendar Event Email Restrict",
    'version': '9.0.1.0.0',
    'depends': [
        'calendar',
        'calendar_event_tag_color',
    ],
    'author': "Valentin THIRION, Jason PINDAT @ AbAKUS it-solutions SARL",
    'website': "http://www.abakusitsolutions.eu",
    'category': 'Calendar',
    'description': """
        Calendar Event Email Restrict

        Restricts automatic mail sending to clients by adding choices in the event form.

        The module is depends of calendar_event_tag_color in order to stack the modules extensions.
        If the module independency is needed, replace
        "var CalendarView = require('calendar_event_tag_color.CalendarViewColor');"
        by
        "var CalendarView = require('web_calendar.CalendarView');"
        in the JavaScript file

        This module has been developed by Valentin THIRION & Jason PINDAT @ AbAKUS it-solutions.
    """,
    'data': [
        'views/calendar_views.xml',
    ],
}
