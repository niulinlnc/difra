odoo.define('calendar_event_email_restrict.CalendarViewDisplay', function (require) {
    "use strict";

    var core = require('web.core');
    var CalendarView = require('calendar_event_tag_color.CalendarViewColor');

    var CalendarViewDisplay = CalendarView.extend({
        
        event_data_transform: function(event) {

            var vals = this._super.apply(this, arguments);

            vals.title = '<div style="font-style:italic;">(' + event.mode_text + ')</div>' + vals.title;

            return vals;
        }
    });

    core.view_registry.add('calendar', CalendarViewDisplay);

    return CalendarViewDisplay;
});