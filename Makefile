CC=g++
CFLAGS=-Wall
LDFLAGS= -lpqxx -lpq

all: src/main.cpp build/
	$(CC) src/main.cpp $(CFLAGS) $(LDFLAGS) -o build/main

build/:
	mkdir build
