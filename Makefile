NAME	=	 pbrain-gomoku-ai

$(NAME):
	cp main.py $(NAME)
	chmod +x $(NAME)

build: $(NAME)

clean:
	rm -rf **/__pycache__
	rm -rf build
	rm -rf dist

fclean: clean
	rm -f $(NAME)

re: fclean all $(NAME)

.PHONY: all clean fclean re $(NAME)