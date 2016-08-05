var WormishTheGame = window.WormishTheGame || {};
WormishTheGame.Game = (function($){
	var Game = function(){
		this.init = function(){
			$(".but_start_game").bind("click",startGame);
			var board
		};
		 var startGame = function(){
			$(".but_start_game").unbind("click");
			WormishTheGame.ui.hideDialog();
			board = new WormishTheGame.Board();
			WormishTheGame.ui.drawBoard(board);
		};
	};
	return Game;
})(jQuery);