up: dev
start: dev
dev: 
	docker compose -f docker-compose.dev.yml up --build -d --force-recreate

prod:
	docker compose -f docker-compose.yml up --build -d --force-recreate

stop:
	docker compose stop

exec:
	docker exec -u 0 -it broadcastAPI bash 

logs:
	docker logs -f broadcastAPI

sn:
	sudo systemctl stop nginx

ssn:
	sudo systemctl start nginx
