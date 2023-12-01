(ns aoc-2023.day01-test
  (:require [clojure.test :as t]
            [aoc-2023.day01 :as sol]))

(def test-input "./input/day01_test")
(def test-input2 "./input/day01_test2")
(def actual-input "./input/day01")

(t/deftest part1-test
  (t/are [expected input] (= expected (sol/part1 input))
    142 test-input
    54331 actual-input))

(t/deftest part2-test
  (t/are [expected input] (= expected (sol/part2 input))
    281 test-input2
    54518 actual-input))
