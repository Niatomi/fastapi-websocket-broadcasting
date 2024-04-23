up: dev
start: dev
dev: 
	docker compose -f docker-compose.dev.yml up --build -d --force-recreate

prod:
	docker compose -f docker-compose.yml up --build -d --force-recreate

stop:
	docker compose stop

exec:
	docker exec -u 0 -it broadcast_api bash 

logs:
	docker logs -f broadcast_api

sn:
	sudo systemctl stop nginx

ssn:
	sudo systemctl start nginx
