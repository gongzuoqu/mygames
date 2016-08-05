var WormishTheGame = window.WormishTheGame || {};
WormishTheGame.ui = (function($){
	var ui = {
	    ROW_HEIGHT: 50,
        FLOWER_DIMS : 50,

		init : function () {
		},

        drawBoard: function(board) {
            var rows = board.getRows() ;
            var gameArea = $("#board") ;
            for(var i=0; i<rows.length; i++) {

                var row = rows[i] ;

                for(var j=0; j<row.length; j++) {

                    var flower = row[j] ;
                    if (flower) {
                        var flowerSprite = flower.getSprite();
                        var left = j * ui.FLOWER_DIMS;
                        var top = i * ui.ROW_HEIGHT;
                        flowerSprite.css({
                            left: left,
                            top: top
                        });
                        gameArea.append(flowerSprite)
                    }
                }
            }
        },

		hideDialog : function () {
			$(".dialog").fadeOut(300);
		}
	};
	return ui;
})(jQuery);