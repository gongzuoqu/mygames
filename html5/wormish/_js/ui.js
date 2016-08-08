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
            var allCells = worm.getAllCells()
            for (var i=0;i<allCells.length;i++) {
                var cell = allCells[i]
                var newPos = ui.calculateNewPos(cell)
                cell.getSprite().css({
                    left: newPos.left,
                    top: newPos.top
                });
            }
            // gameArea.append(worm.getSprite())
        },

		moveWormTo : function(worm, duration) {
            var complete = function (allPos) {
                console.log("moveWormTo completed:"+allPos.length)
                var allCells = worm.getAllCells() ;
                for (var i=0;i<allCells.length;i++) {
                    var cell = allCells[i];
                    var newPos = allPos[i];
                    cell.setXAndY(newPos.x, newPos.y);
                    cell.getSprite().css(Modernizr.prefixed("transition"), "");
                    cell.getSprite().css({
                        left: newPos.left,
                        top: newPos.top
                    });
                }
                worm.setMove(false);
            }

            worm.setMove(true) ;
            var allCells = worm.getAllCells() ;
            if (Modernizr.csstransitions) {
                console.log("csstransitions")
                var allCells = worm.getAllCells()
                var last = false
                var allPos = []
                var delay = 0 ;
                for (var i=0;i<allCells.length;i++) {
                    var cell = allCells[i]
                    var newPos = ui.calculateNewPos(cell)
                    cell.getSprite().css(Modernizr.prefixed("transition"), "all " + (duration / 1000) + "s linear " + delay + "s");
                    cell.getSprite().css({
                        left: newPos.left,
                        top: newPos.top
                    });
                    console.log("Value i:"+i) ;
                    allPos[i] = newPos ;
                    delay += (duration / 2000) ;
                }
                console.log("delay is:"+delay)
                setTimeout(function() {complete(allPos) ;}, duration+(delay*1000));
            } else {
                console.log("animate")
                var allCells = worm.getAllCells()
                var last = false
                for (var i=0;i<allCells.length;i++) {
                    if (i==(allCells.length-1))
                        last = true
                    var cell = allCells[i]
                    var newPos = ui.calculateNewPos(cell)
                    cell.getSprite().animate({
                            left: newPos.left,
                            top: newPos.top
                        },
                        {
                            duration: duration,
                            easing: "linear",
                            complete: function() {complete(cell, newPos, last)}
                        })
                    }
                }
		},

        calculateNewPos: function(cell) {
		    var d = cell.getDirection() ;
            var newCoor = { x:0, y:0 } ;
            var curCoor = cell.getXAndY() ;

            switch(d) {
                case 1:
                    newCoor.x = curCoor.x ;
                    newCoor.y = curCoor.y - ui.WORM_DIMS ;
                    break ;
                case 2:
                    newCoor.x = curCoor.x + ui.WORM_DIMS ;
                    newCoor.y = curCoor.y ;
                    break ;
                case 3:
                    newCoor.x = curCoor.x ;
                    newCoor.y = curCoor.y + ui.WORM_DIMS ;
                    break ;
                case 4:
                    newCoor.x = curCoor.x - ui.WORM_DIMS ;
                    newCoor.y = curCoor.y ;
                    break ;
            }

            newCoor.left = newCoor.x - ui.WORM_DIMS / 2 ;
            newCoor.top = newCoor.y - ui.WORM_DIMS / 2 ;

            return newCoor ;
        },

		hideDialog : function () {
			$(".dialog").fadeOut(300);
		}
	};
	return ui;
})(jQuery);