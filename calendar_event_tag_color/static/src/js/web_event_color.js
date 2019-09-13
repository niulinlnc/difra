odoo.define('calendar_event_tag_color.CalendarViewColor', function (require) {
    "use strict";

    var core = require('web.core');
    var CalendarView = require('web.CalendarView');

    var CalendarViewColor = CalendarView.extend({
        
        event_data_transform: function(event) {

            var hex_value = event.hex_value ? event.hex_value : '#9E9E9E';

            return $.extend(this._super.apply(this, arguments), {
                backgroundColor: hex_value,
                borderColor: hex_value
            });
        }
    });

    core.view_registry.add('calendar', CalendarViewColor);

    return CalendarViewColor;
});