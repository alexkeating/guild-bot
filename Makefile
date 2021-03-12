PROJECT_NAME=guild_bot

# Make sure poetry virtual env is active
local:
	poetry run python ./guild_bot

build:
	docker build -t $(PROJECT_NAME) . 

run:
	docker run -e API_TOKEN=$(API_TOKEN) \
			   -e SUGGESTION_CHANNEL=$(SUGGESTION_CHANNEL) \
			   -e CLIENT_ID=$(CLIENT_ID) \
			   -e GUILD_ID=$(GUILD_ID) \
			   $(PROJECT_NAME) $(cmd)

# Go into the container
inspect:
	docker run -it /bin/bash

generate_oauth:
	$(MAKE) run CLIENT_ID=$(CLIENT_ID) \
		        GUILD_ID=$(GUILD_ID) \
				cmd="poetry run python ./scripts/generate_oauth.py"
