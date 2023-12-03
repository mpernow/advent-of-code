(ns aoc-2023.day02-test
  (:require [clojure.test :as t]
            [aoc-2023.day02 :as sol]))

(def test-input "./input/day02_test")
(def actual-input "./input/day02")

(t/deftest part1-test
  (t/are [expected input] (= expected (sol/part1 input))
    8 test-input
    2076 actual-input))

(t/deftest part2-test
  (t/are [expected input] (= expected (sol/part2 input))
    2286 test-input
    70950 actual-input))
