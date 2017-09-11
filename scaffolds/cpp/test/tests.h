#include <cxxtest/TestSuite.h>

#include "module.h"

class Tests : public CxxTest::TestSuite {
public:
  void test_returnTrue_should_return_true(void) {
    Module module;
    TS_ASSERT_EQUALS(true, module.returnTrue());
  }
};
