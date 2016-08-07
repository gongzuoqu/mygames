var WormishTheGame = window.WormishTheGame || {};
WormishTheGame.ui = (function($){
	var ui = {
	    ROW_HEIGHT: 50,
        FLOWER_DIMS : 50,

        WORM_DIMS : 50,

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

        updateWormPosition : function (worm) {
            var coord = worm.getXAndY() ;
            var left = coord.x  - ui.WORM_DIMS / 2 ;
            var top = coord.y - ui.WORM_DIMS / 2 ;
            worm.getSprite().css({
                top: top,
                left: left
            }) ;
            // gameArea.append(worm.getSprite())
        },

		moveWormTo : function(worm, coords, duration) {
            var complete = function () {
                console.log("moveWormTo completed")
                worm.setXAndY(newX, newY);
                worm.getSprite().css(Modernizr.prefixed("transition"),"") ;
                worm.getSprite().css({
                    left: worm.getTopAndLeft().left - ui.WORM_DIMS / 2,
                    top: worm.getTopAndLeft().top - ui.WORM_DIMS / 2
                });
                worm.setMove(false);
            }

            worm.setMove(true) ;
            var newX = worm.getXAndY().x + coords.x ;
            var newY = worm.getXAndY().y + coords.y ;
            if (Modernizr.csstransitions) {
                console.log("csstransitions")
                worm.getSprite().css(Modernizr.prefixed("transition"),"all "+(duration/1000)+"s linear") ;
                worm.getSprite().css({
                    left: newX - ui.WORM_DIMS / 2,
                    top: newY - ui.WORM_DIMS / 2
                }) ;
                setTimeout(complete, duration) ;
            } else {
                console.log("animate")
                worm.getSprite().animate({
                        left: newX - ui.WORM_DIMS / 2,
                        top: newY - ui.WORM_DIMS / 2
                    },
                    {
                        duration: duration,
                        easing: "linear",
                        complete: complete
                    })
            }
		},

		hideDialog : function () {
			$(".dialog").fadeOut(300);
		}
	};
	return ui;
})(jQuery);