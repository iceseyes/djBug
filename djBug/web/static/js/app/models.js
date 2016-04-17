"use strict"

var app = app || {};

app.TicketModel = Backbone.Model.extend({});

app.TicketCollection = Backbone.Model.extend({
	url: app.api.tickets.base_url,
	model: app.TicketModel,
	
	parse: function (data) {
		this.page_count = data.count;
		this.next_url = data.next;
		this.prev_url = data.previous;
		
		return data.results;
	}
});

$(function () {
	app.tickets = new app.TicketCollection();
})