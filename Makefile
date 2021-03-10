PROJECT_NAME=guild_bot

# Make sure poetry virtual env is active
local:
	python ./guild_bot

build:
	docker build -t $(PROJECT_NAME) .

run:
	docker run $(PROJECT_NAME)

# Go into the container
inspect:
	docker run -it /bin/bash
