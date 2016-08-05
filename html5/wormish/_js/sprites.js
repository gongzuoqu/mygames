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
        this.getSprite = function() { return sprite ; }
        this.getSize = function() { return size ; }
        this.increaseSize =function() { size +=1 ;}
        this.getDirection = function () { return direction ;}
        this.goUp = function () { direction = DIRECTION_UP ;}
        this.goRight = function () { direction = DIRECTION_RIGHT ;}
        this.goDown = function () { direction = DIRECTION_DOWN ;}
        this.goLeft = function () { direction = DIRECTION_LEFT ;}
        this.getTop = function () { return top ;}
        this.getLeft = function () { return left ;}
        this.setTopAndLeft = function (t, l) { top=t ; left = l;}
        this.getCol = function () { return col ;}
        this.getRow = function () { return row ;}
        this.setColAndRow = function (c, r) { col = c ; row = r ;}
        this.setXAndY = function (x, y) { xPos = x ; yPos = y ;}
        this.getXPos = function () { return xPos ; }
        this.getYPos = function () { return yPos ; }
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

