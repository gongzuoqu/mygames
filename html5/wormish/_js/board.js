/**
 * Created by LionelB1 on 8/5/2016.
 */
var WormishTheGame = window.WormishTheGame || {};
WormishTheGame.Board = (function($){
    var NUM_ROWS = 10 ;
    var NUM_COLS = 16 ;
    var NBR_FLOWERS = 10 ;
    var Board = function() {
        var that = this ;
        var rows = createLayout() ;
        var listFlowers = createAllFlowers(NBR_FLOWERS, rows) ;

        this.getRows = function () { return rows ; }

        this.clearAllFlowers = function () {
            console.log("delete called")
            for(var i=0;i<listFlowers.length;i++) {
                listFlowers[i].getSprite().remove()
            }
        }

        this.updateWormPosition = function (worm) {

            var coord = worm.getXAndY() ;
            var col =  coord.x / NUM_ROWS ;
            var row =  coord.y / NUM_COLS ;
            worm.setColAndRow(col, row) ;
        }

        return this ;
    } ;

    var createLayout = function () {
        var rows = [] ;
        for(var i=0; i<NUM_ROWS ; i++) {
            var row = []
            for(var j=0; j<NUM_COLS ; j++) {
                // var type = Math.floor(Math.random() * 4);
                // var cell = WormishTheGame.Flower.create(i, j, type)
                // row[j] = cell
                row[j] = null ;
            }
            rows.push(row) ;
        }

        console.log("map created")
        return rows ;
    };

    var createAllFlowers = function(nbrOfFlowers, rows) {
        var flowers = []
        for (var i=0; i<nbrOfFlowers; i++) {
            var col = Math.floor(Math.random() * NUM_COLS);
            var row = Math.floor(Math.random() * NUM_ROWS);
            var type = Math.floor(Math.random() * 4);
            var f = WormishTheGame.Flower.create(col, row, type)
            var row = rows[row]
            row[col] = f
            flowers.push(f)
        }
        return flowers ;
    }

	return Board;
})(jQuery);