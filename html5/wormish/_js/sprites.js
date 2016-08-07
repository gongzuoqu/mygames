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

WormishTheGame.Worm = (function($) {
    var DIRECTION_UP = 1 ;
    var DIRECTION_RIGHT = 2 ;
    var DIRECTION_DOWN = 3 ;
    var DIRECTION_LEFT = 4 ;

    var Worm = function(sprite) {
        var that = this ;
        var size = 1 ;
        var direction = DIRECTION_RIGHT ;
        var top, left ;
        var col, row ;
        var xPos, yPos ;
        var isMoving = false ;
        this.getSprite = function() { return sprite ; }
        this.setMove = function (bool) { isMoving = bool ; }
        this.isMoving = function () { return isMoving ; }
        this.getSize = function() { return size ; }
        this.increaseSize =function() { size +=1 ;}
        this.getDirection = function () { return direction ;}
        this.goUp = function () { direction = DIRECTION_UP ;}
        this.goRight = function () { direction = DIRECTION_RIGHT ;}
        this.goDown = function () { direction = DIRECTION_DOWN ;}
        this.goLeft = function () { direction = DIRECTION_LEFT ;}
        this.getTopAndLeft = function () {
            var coord = {
                Top: top ,
                Left: left } ;
                return coord ; }
        this.setTopAndLeft = function (t, l) { top=t ; left = l;}
        this.getColAndRow = function () {
            var coord = {
                Col: col ,
                Row: row } ;
                return coord ; }
        this.setColAndRow = function (c, r) { col = c ; row = r ;}
        this.getXAndY = function () {
            var coord = {
                x: xPos ,
                y: yPos } ;
                return coord ; }
        this.setXAndY = function (x, y) { console.log("X:"+x+" Y:"+y) ; xPos = x ; yPos = y ;}
    }

    Worm.create = function() {
        var sprite = $(document.createElement("div")) ;
        sprite.addClass("worm") ;
        var w = new Worm(sprite) ;
        w.setXAndY(175,175)
        return w ;
    }

    return Worm ;
})(jQuery) ;

