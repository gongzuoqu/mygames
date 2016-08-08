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


    var DIRECTIONS = {
        DIRECTION_UP : 1 ,
        DIRECTION_RIGHT : 2 ,
        DIRECTION_DOWN : 3 ,
        DIRECTION_LEFT : 4
    } ;

    var INIT_SIZE = 5 ;
    var INIT_DIRECTION = DIRECTIONS.DIRECTION_RIGHT ;

    var WormCell = function(sprite, x, y, direct) {
        var top, left ;
        var col, row ;
        var xPos = x, yPos= y ;
        var direction = direct ;
        this.getSprite = function() { return sprite ; }
        this.getDirection = function () { return direction ;}
        this.goUp = function () { direction = DIRECTIONS.DIRECTION_UP ;}
        this.goRight = function () { direction = DIRECTIONS.DIRECTION_RIGHT ;}
        this.goDown = function () { direction = DIRECTIONS.DIRECTION_DOWN ;}
        this.goLeft = function () { direction = DIRECTIONS.DIRECTION_LEFT ;}

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

    var Worm = function(allCells) {
        var that = this ;
        var size = allCells.length ;
        var isMoving = false ;
        var allBodyCell = allCells

        this.setMove = function (bool) { isMoving = bool ; }
        this.isMoving = function () { return isMoving ; }
        this.getSize = function() { return size ; }
        this.getAllCells = function () { return allBodyCell ; }
        this.goUp = function () { allBodyCell[0].goUp() ;}
        this.goRight = function () { allBodyCell[0].goRight() ;}
        this.goDown = function () { allBodyCell[0].goDown() ;}
        this.goLeft = function () { allBodyCell[0].goLeft() ;}

    }

    Worm.create = function() {
        var x = 175, y= 175 ;
        var allCells = [] ;
        for (var i=0;i<INIT_SIZE; i++) {
            var wc = Worm.createWormCell(x, y, INIT_DIRECTION)
            allCells[i] = wc ;
            // x -= WormishTheGame.ui.WORM_DIMS + (WormishTheGame.ui.WORM_DIMS/4) ;
            x -= (WormishTheGame.ui.WORM_DIMS/4) * 1.5 ;
        }

        var w = new Worm(allCells) ;
        return w ;
    }

    Worm.createWormCell = function(x, y, direct) {
        var sprite = $(document.createElement("div")) ;
        sprite.addClass("worm") ;
        var wc = new WormCell(sprite, x, y, direct) ;
        return wc ;
    }

    return Worm ;
})(jQuery) ;

