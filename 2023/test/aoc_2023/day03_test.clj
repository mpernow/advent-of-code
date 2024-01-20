(ns aoc-2023.day03-test
  (:require [clojure.test :as t]
            [aoc-2023.day03 :as sol]))

(def test-input (slurp "./input/day03_test"))
(def actual-input (slurp "./input/day03"))

(t/deftest part1-test
  (t/are [expected input] (= expected (sol/part1 input))
    4361 test-input
    538046 actual-input))

(t/deftest part2-test
  (t/are [expected input] (= expected (sol/part2 input))
    467835 test-input
    81709807 actual-input))
