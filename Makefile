.PHONY: help build up down logs shell test clean

help:
	@echo "Available commands:"
	@echo "  make build    - Build Docker images"
	@echo "  make up       - Start containers"
	@echo "  make down     - Stop containers"
	@echo "  make logs     - View logs"
	@echo "  make shell    - Open shell in app container"
	@echo "  make clean    - Remove containers and volumes"

build:
	docker-compose build

up:
	docker-compose up -d

down:
	docker-compose down

logs:
	docker-compose logs -f

shell:
	docker-compose exec app bash

clean:
	docker-compose down -v
	docker system prune -f
