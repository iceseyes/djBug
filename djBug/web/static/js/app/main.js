"use strict"

var app = app || {};

app.Router = Backbone.Router.extend({
    routes: {
        "": "home",
    },

    initialize: function () {},

    home: function () {
        if (!this.homeView) {
            this.homeView = new app.HomeView();
        } 
        
        this.homeView.render();
    }
});