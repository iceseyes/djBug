"use strict"

var app = app || {};

app.TicketModel = Backbone.Model.extend({
	initialize: function() {
		if(this.get("state")==="to_approve") {
			this.set("state_icon", "folder open");
		} else if(this.get("state")==="closed") {
			this.set("state_icon", "close");
		} else if(this.get("state")==="not_a_bug") {
			this.set("state_icon", "Thumbs Down");
		} else {
			this.set("state_icon", "bug");
		}
	}
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
