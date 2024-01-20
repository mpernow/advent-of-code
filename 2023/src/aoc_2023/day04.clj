(ns aoc-2023.day04
  (:require [clojure.string :as str]
            [clojure.set :as set]))

(defn parse-input [input]
  (->> (slurp input)
       (str/split-lines)))

(defn parse-card [line]
  (let [[_ winning actual] (str/split line #"\||:")]
    {:winning (set (map read-string (re-seq #"\d+" winning)))
     :actual   (set (map read-string (re-seq #"\d+" actual)))}))

(defn number-correct [card]
  (count (set/intersection (get card :winning) (get card :actual))))

(defn compute-score [num]
  (if (> num 0) (int (Math/pow 2 (- num 1))) 0))

(defn part1 [input_file]
  (->> (parse-input input_file)
       (map parse-card)
       (map number-correct)
       (map compute-score)
       (reduce +)))

(defn part2 [input_file]
  (last (reduce (fn [[cards row acc] line]
                  (let [wins (number-correct line)
                        num-cards-here (inc (get cards row 0))
                        future-cards (reduce #(assoc %1 (+ %2 row) num-cards-here) {} (range 1 (inc wins)))]
                    [(merge-with + cards future-cards) (inc row) (+ acc num-cards-here)]))
                [{} 1 0]
                (map parse-card (parse-input input_file)))))

(defn -main []
  (let [input_file "./input/day04"]
    (println (part1 input_file))
    (println (part2 input_file))))