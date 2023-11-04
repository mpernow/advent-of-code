(ns aoc-2021.core-test
  (:require [clojure.test :as t]
            [aoc-2021.core :as sut]))

(t/deftest basic-tests
  (t/testing "it says hello to everyone"
    (t/is (= (with-out-str (sut/-main)) "Merry Christmas!\n"))))