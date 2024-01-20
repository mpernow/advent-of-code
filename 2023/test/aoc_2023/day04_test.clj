(ns aoc-2023.day04-test
  (:require [clojure.test :as t]
            [aoc-2023.day04 :as sol]))

(def test-input "./input/day04_test")
(def actual-input "./input/day04")

(t/deftest part1-test
  (t/are [expected input] (= expected (sol/part1 input))
    13 test-input
    26426 actual-input))

(t/deftest part2-test
  (t/are [expected input] (= expected (sol/part2 input))
    30 test-input
    6227972 actual-input))
