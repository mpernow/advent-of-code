(ns aoc-2023.day01
  (:require [clojure.string :as str]))

(defn parse-input [input]
  (->> (slurp input)
       (str/split-lines)))

(defn get-first-and-last [numbers]
  (str (first numbers) (last numbers)))

(defn part1 [input_file]
  (->> (parse-input input_file)
       (map (partial re-seq #"\d"))
       (map get-first-and-last)
       (map read-string)
       (reduce +)))

(def letters-to-nums (hash-map :one 1 :two 2 :three 3 :four 4 :five 5 :six 6 :seven 7 :eight 8 :nine 9 :1 1 :2 2 :3 3 :4 4 :5 5 :6 6 :7 7 :8 8 :9 9))

(defn convert-and-get-first-and-last [numbers]
  (str (get letters-to-nums (keyword (first numbers))) (get letters-to-nums (keyword (last numbers)))))

(defn replace-with-extended [line]
  (str/replace (str/replace (str/replace (str/replace line #"one" "one1one") #"two" "two2two") #"three" "tree3three") #"eight" "eight8eight"))

(defn part2 [input_file]
  (->> (parse-input input_file)
       (map replace-with-extended)
       (map (partial re-seq #"one|two|three|four|five|six|seven|eight|nine|\d"))
       (map convert-and-get-first-and-last)
       (map read-string)
       (reduce +)))

(defn -main []
  (let [input_file "./input/day01"]
    (println (part1 input_file))
    (println (part2 input_file))))