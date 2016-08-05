var WormishTheGame = window.WormishTheGame || {};
WormishTheGame.Game = (function($){
	var Game = function(){
		this.init = function(){
			$(".but_start_game").bind("click",startGame);
			$(".but_refresh_map").bind("click",refreshMap);
			var board
		};
		 var startGame = function(){
			$(".but_start_game").unbind("click");
			WormishTheGame.ui.hideDialog();
			board = new WormishTheGame.Board();
			WormishTheGame.ui.drawBoard(board);
		};
		var refreshMap = function () {
			board.clearAllFlowers();
            board = new WormishTheGame.Board();
			WormishTheGame.ui.drawBoard(board);
        }
	};
	return Game;
})(jQuery);