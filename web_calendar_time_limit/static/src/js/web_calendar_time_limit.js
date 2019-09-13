odoo.define('web_calendar_time_limit.CalendarViewTimeLimit', function (require) {
	"use strict";

	var core = require('web.core');
	var CalendarView = require('web.AgendaView'); //AgendaView

	var CalendarViewTimeLimit = CalendarView.extend({

		init: function() {

			return $.extend(this._super.apply(this, arguments), {
				minTime: 7,
				maxTime: 19
			});
		}
	});

	core.view_registry.add('calendar', CalendarViewTimeLimit);

	return CalendarViewTimeLimit;
});