(ns aoc-2021.day01-test
  (:require [clojure.test :as t]
            [aoc-2021.day01 :as sol]))

(def test-input "./input/day01_test")
(def actual-input "./input/day01")

(t/deftest part1-test
  (t/are [expected input] (= expected (sol/part1 input))
    7 test-input
    1559 actual-input))

(t/deftest part2-test
  (t/are [expected input] (= expected (sol/part2 input))
    5 test-input
    1600 actual-input))
