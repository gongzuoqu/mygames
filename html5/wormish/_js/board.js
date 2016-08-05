/**
 * Created by LionelB1 on 8/5/2016.
 */
var WormishTheGame = window.WormishTheGame || {};
WormishTheGame.Board = (function($){
    var NUM_ROWS = 10 ;
    var NUM_COLS = 16 ;
    var Board = function() {
        var that = this ;
        var rows = createLayout() ;
        this.getRows = function () { return rows ; }
        return this ;
    } ;

    var createLayout = function () {
        var rows = [] ;
        for(var i=0; i<NUM_ROWS ; i++) {
            var row = []
            for(var j=0; j<NUM_COLS ; j++) {
                var type = Math.floor(Math.random() * 4);
                var cell = WormishTheGame.Flower.create(i, j, type)
                row[j] = cell
            }
            rows.push(row) ;
        }
        return rows ;
    };
	return Board;
})(jQuery);