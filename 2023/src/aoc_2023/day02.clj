(ns aoc-2023.day02
  (:require [clojure.string :as str]))

(defn parse-input [input]
  (->> (slurp input)
       (str/split-lines)))

(def maximum-cubes (hash-map :red 12 :green 13 :blue 14))

(defn parse-game [line]
  (let [[_ game-num & boxes] (re-seq #"\w+" line)]
    {:game-num (read-string game-num)
     :cubes    (reduce (fn [acc [n cube]] (update acc (keyword cube) max (read-string n)))
                       {:red 0, :green 0, :blue 0}
                       (partition 2 boxes))}))

(defn playable? [{:keys [cubes]}]
  (= cubes (merge-with min cubes maximum-cubes)))

(defn part1 [input_file]
  (transduce (comp (map parse-game) (filter playable?) (map :game-num)) + (parse-input input_file)))

(defn cube-power [game]
  (->> game :cubes vals (apply *)))

(defn part2 [input_file]
  (transduce (map (comp cube-power parse-game)) + (parse-input input_file)))

(defn -main []
  (let [input_file "./input/day02"]
    (println (part1 input_file))
    (println (part2 input_file))))