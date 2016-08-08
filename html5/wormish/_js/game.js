var WormishTheGame = window.WormishTheGame || {};
WormishTheGame.Game = (function($){
	var Game = function(){
	    var fps = 60 ;
		this.init = function(){
			$(".but_start_game").bind("click",startGame);
			$(".but_refresh_map").bind("click",refreshMap);
			var board ;
            var worm ;
		};

        var startGame = function(){
			$(".but_start_game").unbind("click");
            $(document).keydown(keyPressed);
			WormishTheGame.ui.hideDialog();
			board = new WormishTheGame.Board();
            worm = createAndSetWorm() ;
			WormishTheGame.ui.drawBoard(board);
			WormishTheGame.ui.updateWormPosition(worm);
            setInterval(gameTick, 1000 / fps);
		};

		var refreshMap = function() {
			board.clearAllFlowers();
            board = new WormishTheGame.Board();
			WormishTheGame.ui.drawBoard(board);
        } ;

        var createAndSetWorm = function() {
			var worm = WormishTheGame.Worm.create();
            worm.goRight() ;
            var allCells = worm.getAllCells()
            for (var i=0;i<allCells.length;i++) {
                var cell = allCells[i]
                console.log("cell: "+cell)
    			$("#board").append(cell.getSprite());
            }
            board.updateWormPosition(worm) ;
			return worm;
        } ;

        var gameTick = function() {
            console.log("game tick") ;

            if (!worm.isMoving()) {
                console.log("game tick moving") ;
                // var dir = worm.getDirection() ;
                // switch(dir) {
                //     case 1: // Up
                //         console.log("to Up")
                //         coord = { x:0, y:-WormishTheGame.ui.WORM_DIMS} ;
                //         break ;
                //     case 2: // Right
                //         console.log("to Right")
                //         coord = { x:WormishTheGame.ui.WORM_DIMS, y:0} ;
                //         break ;
                //     case 3: // Down
                //         console.log("to Down")
                //         coord = { x:0, y:WormishTheGame.ui.WORM_DIMS} ;
                //         break ;
                //     case 4: // Left
                //         console.log("to Left")
                //         coord = { x:-WormishTheGame.ui.WORM_DIMS, y:0} ;
                //         break ;
                // }
                WormishTheGame.ui.moveWormTo(worm, 250);
                board.updateWormPosition(worm) ;
            }
        }

        var keyPressed = function (event) {
            var coord ;
            switch(event.which) {
                case 37: // left
                    console.log("to Left")
                    worm.goLeft() ;
                break;

                case 38: // up
                    console.log("to Up")
                    worm.goUp() ;
                break;

                case 39: // right
                    console.log("to Right")
                    worm.goRight() ;
                break;

                case 40: // down
                    console.log("to Down")
                    worm.goDown() ;
                break;

                default: return; // exit this handler for other keys
            }
            event.preventDefault(); // prevent the default action (scroll / move caret)
        }
	};
    return Game;
})(jQuery);