(ns aoc-2021.day03-test
  (:require [clojure.test :as t]
            [aoc-2021.day03 :as sol]))

(def test-input "./input/day03_test")
(def actual-input "./input/day03")

(t/deftest part1-test
  (t/are [expected input] (= expected (sol/part1 input))
    198 test-input
    1540244 actual-input))

(t/deftest part2-test
  (t/are [expected input] (= expected (sol/part2 input))
    230 test-input
    4203981 actual-input))
