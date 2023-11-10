(ns aoc-2021.day02-test
  (:require [clojure.test :as t]
            [aoc-2021.day02 :as sol]))

(def test-input "./input/day02_test")
(def actual-input "./input/day02")

(t/deftest part1-test
  (t/are [expected input] (= expected (sol/part1 input))
    150 test-input
    1488669 actual-input))

(t/deftest part2-test
  (t/are [expected input] (= expected (sol/part2 input))
    900 test-input
    1176514794 actual-input))
