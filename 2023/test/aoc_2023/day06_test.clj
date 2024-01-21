(ns aoc-2023.day06-test
  (:require [clojure.test :as t]
            [aoc-2023.day06 :as sol]))

(def test-input1 [[7 9] [15 40] [30 200]])
(def test-input2 [[71530 940200]])
(def actual-input1 [[48 261] [93 1192] [84 1019] [66 1063]])
(def actual-input2 [[48938466 261119210191063]])

(t/deftest part1-test
  (t/are [expected input] (= expected (sol/solve input))
    288 test-input1
    1312850 actual-input1))

(t/deftest part2-test
  (t/are [expected input] (= expected (sol/solve input))
    71503 test-input2
    36749103 actual-input2))
