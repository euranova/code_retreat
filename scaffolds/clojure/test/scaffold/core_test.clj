(ns scaffold.core-test
  (:require [clojure.test :refer :all]
            [scaffold.core :refer :all]))

(deftest a-test
  (testing "This obviously works"
    (is (= 1 1)))
  (testing "Testing foo"
    (is (= "A Hello, World!" (foo "A")))))
