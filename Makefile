BASEDIR:=$(shell dirname $(realpath $(firstword $(MAKEFILE_LIST))))

PORT ?= 8080

all: 3rdparty

.PHONY: 3rdparty
3rdparty:
	$(MAKE) -C 3rdparty

.PHONY: distclean
distclean:
	$(MAKE) -C 3rdparty clean

run: 3rdparty
	DOCROOT=${BASEDIR}/www/ PORT=$(PORT) \
		${BASEDIR}/3rdparty/lighttpd/sbin/lighttpd -D -f ${BASEDIR}/3rdparty/lighttpd.conf
