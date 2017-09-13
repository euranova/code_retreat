cxxtestgen := cxxtestgen

src-files := \
  src/module.cpp

include := include
header-files := \
  include/module.h

test := test
test-file := $(test)/tests.h

build = build
test-runner-src := $(build)/test-runner.cpp
test-runner-exe := $(build)/test-runner

.PHONY: all clean test

all: test

$(test-runner-src): $(test-file)
	mkdir -p $(build)
	$(cxxtestgen) --fog-parser --runner=ParenPrinter -o $(test-runner-src) $(test-file)

$(test-runner-exe): $(test-runner-src) $(src-files) $(header-files)
	g++ -o $(test-runner-exe) -std=c++11 -I$(CXXTEST) -I$(include) $(test-runner-src) $(src-files)

test: $(test-runner-exe)
	$(test-runner-exe)

clean:
	rm -rf $(build)
