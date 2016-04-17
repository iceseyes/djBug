"use strict"

var app = app || {};

app.TicketModel = Backbone.Model.extend({
});

app.TicketCollection = Backbone.Collection.extend({
	url: app.tickets_url,
	model: app.TicketModel,
	
	parse: function (data) {
		this.page_count = data.count;
		this.next_url = data.next;
		this.prev_url = data.previous;

		return data.results;
	}
});
