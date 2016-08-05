/**
 * Created by LionelB1 on 8/5/2016.
 */
var WormishTheGame = window.WormishTheGame || {};

WormishTheGame.Flower = (function($) {
    var Flower = function(row, col, type, sprite) {
        var that = this ;
        this.getRow = function() { return row ; }
        this.getCol = function() { return col ; }
        this.getType = function() { return type ; }
        this.getSprite = function() { return sprite ; }
    }

    Flower.create = function(row, col, type) {
        var sprite = $(document.createElement("div")) ;
        sprite.addClass("flower") ;
        sprite.addClass("flower_"+type) ;
        var f = new Flower(row, col, type, sprite) ;
        return f ;
    }
    return Flower ;
})(jQuery) ;

WormishTheGame.WormCell = (function($) {
    var WormCell = function(sprite) {
        var that = this ;
        this.getSprite = function() { return sprite ; }
    }

    WormCell.create = function() {
        var sprite = $(document.createElement("div")) ;
        sprite.addClass("worm") ;
        var w = new WormCell(sprite) ;
        return w ;
    }
    return WormCell ;
})(jQuery) ;

