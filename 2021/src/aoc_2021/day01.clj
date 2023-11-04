(ns aoc-2021.day01
  (:require [clojure.string :as str]))

(defn parse-measurements [input]
  (->> (slurp input)
       (str/split-lines)
       (map #(Integer/parseInt %))))

(defn part1 [input_file]
  (->> (parse-measurements input_file)
       (partition 2 1)
       (filter (partial apply <))
       count))

(defn part2 [input_file]
  (->> (parse-measurements input_file)
       (partition 3 1)
       (map (partial apply +))
       (partition 2 1)
       (filter (partial apply <))
       count))

(defn -main []
  (let [input_file "./input/day01"]
    (println (part1 input_file))
    (println (part2 input_file))))