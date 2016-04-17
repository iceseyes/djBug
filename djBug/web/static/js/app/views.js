"use strict"

var app = app || {}

app.HomeView = Backbone.View.extend({
	el: '#tickets',
	template: _.template( $('#tickets-template').html() ),
	
	initialize: function() {
		this.listenTo(app.tickets, 'add', this.addOne);
		this.listenTo(app.tickets, 'reset', this.addAll);
		this.render();
	},
	
	render: function() {
		var content = this.template();
		this.$el.html(content);
		app.tickets.fetch();
	},
	
	addOne: function(ticket) {
		var view = new app.TicketView();
		this.$('#ticket-list').append( view.render().el );
	},
	
	addAll: function() {
		this.$('#ticket-list').html('');
		app.Tickets.each(this.addOne, this);
	}
});