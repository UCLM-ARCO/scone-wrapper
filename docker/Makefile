MAKEFLAGS += --warn-undefined-variables
HOW_TO_LOGIN=https://docs.github.com/es/packages/using-github-packages-with-your-projects-ecosystem/configuring-docker-for-use-with-github-packages
GITHUB_TOKEN=~/.github-token-package

HUB=docker.pkg.github.com
VERSION=latest
NAME=scone-wrapper
IMAGE=${HUB}/uclm-arco/${NAME}/${NAME}:${VERSION}

login:
	@test ! -z "${GITHUB_USERNAME}" || (echo "ERROR: Define var GITHUB_USERNAME"; false)
	@test ! -f "${GITHUB_TOKEN}" || (echo "ERROR: Need a token. See $${HOW_TO_LOGIN}"; false)
	@cat ~/.github-token-packages | docker login ${HUB} -u ${GITHUB_USERNAME} --password-stdin

build:
	docker build . -t ${NAME}

push: build login
	docker tag ${NAME} ${IMAGE}
	docker push ${IMAGE}

version:
	docker run -v $(shell dirname $$PWD):/github/workspace ${NAME} dpkg -l scone-wrapper
