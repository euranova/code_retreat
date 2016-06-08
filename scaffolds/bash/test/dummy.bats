#!/usr/bin/env bats

load test_helper
source "${BATS_TEST_DIRNAME}/../lib/dummy.sh"

@test "dummy prints \"hello world!\"" {
  run hello
  assert_success
  assert_output "hello world!"
}
