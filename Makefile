build:
	docker build -t andrequeiroz2/api-auth:latest .

push:
	docker push andrequeiroz2/api-auth:latest

pull:
	docker pull andrequeiroz2/api-auth:latest

run:
	docker run -p 6000:6000 andrequeiroz2/api-auth:latest