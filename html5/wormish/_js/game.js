var WormishTheGame = window.WormishTheGame || {};
WormishTheGame.Game = (function($){
	var Game = function(){
		this.init = function(){
			$(".but_start_game").bind("click",startGame);
			$(".but_refresh_map").bind("click",refreshMap);
			var board ;
            var worm ;
		};
		 var startGame = function(){
			$(".but_start_game").unbind("click");
			WormishTheGame.ui.hideDialog();
			board = new WormishTheGame.Board();
            worm = createAndSetWorm() ;
			WormishTheGame.ui.drawBoard(board);
			WormishTheGame.ui.updateWormPosition(worm);
		};

		var refreshMap = function() {
			board.clearAllFlowers();
            board = new WormishTheGame.Board();
			WormishTheGame.ui.drawBoard(board);
        }

        var createAndSetWorm = function() {
			var worm = WormishTheGame.Worm.create();
			worm.getSprite().addClass("worm");
			$("#board").append(worm.getSprite());
            board.updateWormPosition(worm) ;
			return worm;
        }
	};
	return Game;
})(jQuery);