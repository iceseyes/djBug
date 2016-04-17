"use strict"

var app = app || {}

app.TicketView = Backbone.View.extend({
	className: 'item',
	template: _.template( $('#ticket-template').html() ),
	
	events: {
		"click .openButton": 'showDescription',
		"click .closeButton": 'hideDescription',
	},
	
	initialize: function() {
		this.listenTo(this.model, 'change', this.render);
	},
	
	render: function() {
		this.$el.html( this.template( this.model.attributes ) );
		this.hideDescription();
		return this;
	},
	
	showDescription: function() {
		this.$(".item-descr").show();
		this.$(".openButton").hide();
		this.$(".closeButton").show();
	},
	
	hideDescription: function() {
		this.$(".item-descr").hide();
		this.$(".openButton").show();
		this.$(".closeButton").hide();
	}
});

app.HomeView = Backbone.View.extend({
	el: '#tickets',
	tickets: new app.TicketCollection(),
	
	initialize: function() {
		this.listenTo(this.tickets, 'add', this.addOne);
		this.listenTo(this.tickets, 'reset', this.addAll);
		
		this.tickets.fetch();
	},
	
	
	addOne: function(ticket) {
		var view = new app.TicketView({ model: ticket });
		this.$('#ticket-list').append( view.render().el );
	},
	
	addAll: function() {
		this.$('#ticket-list').html('');
		_.each(this.tickets, this.addOne, this);
	}
});
