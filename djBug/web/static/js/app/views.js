"use strict"

var app = app || {}

app.TicketView = Backbone.View.extend({
	className: 'item',
	template: _.template( $('#ticket-template').html() ),
	
	events: {
		"click .openButton": 'showDescription',
		"click .closeButton": 'hideDescription',
		"click .toApproveStateButton": 'setToApproveState',
		"click .approvedStateButton": 'setApprovedState',
		"click .closedStateButton": 'setClosedState',
		"click .notabugStateButton": 'setNotABugState',
		"click .wontfixStateButton": 'setWontFixState',
		"click .edit": 'showDescriptionArea',
		"blur .editable": 'savedescr'
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
		this.hideDescriptionArea();
	},
	
	showDescriptionArea: function() {
		this.$(".form").show();
		this.$(".statictext").hide();
		this.$(".edit").hide();
	},
	
	hideDescriptionArea: function() {
		this.$(".form").hide();
		this.$(".statictext").show();
		this.$(".edit").show();
	},
	
	savedescr: function() {
		this.model.set("description", this.$(".editable").val());
		this.hideDescriptionArea();
		this.model.save();
	},
	
	setToApproveState: function() {
		this.model.set("state", "to_approve");
		this.model.save();
	},
	
	setApprovedState: function() {
		this.model.set("state", "approved");
		this.model.save();
	},
	
	setClosedState: function() {
		this.model.set("state", "closed");
		this.model.save();
	},
	
	setNotABugState: function() {
		this.model.set("state", "not_a_bug");
		this.model.save();
	},
	
	setWontFixState: function() {
		this.model.set("state", "wontfix");
		this.model.save();
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
