(ns aoc-2023.day05-test
  (:require [clojure.test :as t]
            [aoc-2023.day05 :as sol]))

(def test-input (slurp "./input/day05_test"))
(def actual-input (slurp "./input/day05"))

(t/deftest part1-test
  (t/are [expected input] (= expected (sol/part1 input))
    35 test-input
    346433842 actual-input))

(t/deftest part2-test
  (t/are [expected input] (= expected (sol/part2 input))
    46 test-input
    60294664 actual-input))
