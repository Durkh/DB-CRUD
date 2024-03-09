CXX=g++
INC_DIR=include 
CXXFLAGS=-Wall -I$(INC_DIR)
LDFLAGS=-lpqxx -lpq
DEPS = src/*.cpp 


all: build/ $(DEPS)
	$(CXX) $(DEPS) $(CXXFLAGS) $(LDFLAGS) -o build/main

build/:
	mkdir build

clean:
	rm -rf build
