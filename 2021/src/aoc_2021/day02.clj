(ns aoc-2021.day02
  (:require [clojure.string :as str]))

(defn parse-instruction [input]
  (let [[a b] (str/split input #" ")]
    [(keyword a) (read-string b)]))

(defn parse-input [input]
  (->> (slurp input)
       (str/split-lines)
       (map parse-instruction)))

(def initial-submarine {:pos 0 :depth 0 :aim 0})

(defn final-position [{:keys [pos depth]}]
  (* pos depth))

(defn create-mover [forward-fn down-fn up-fn]
  (fn [submarine [dir amount]]
    (let [op (dir {:forward forward-fn, :down down-fn, :up up-fn})]
      (op submarine amount))))

(def part1-mover (create-mover (fn [submarine amount] (update submarine :pos + amount))
                               (fn [submarine amount] (update submarine :depth + amount))
                               (fn [submarine amount] (update submarine :depth - amount))))
(def part2-mover (create-mover (fn [{aim :aim :as submarine} amount] (-> (update submarine :pos + amount)
                                                                         (update :depth + (* aim amount))))
                               (fn [submarine amount] (update submarine :aim + amount))
                               (fn [submarine amount] (update submarine :aim - amount))))

(defn solve [mover input_file]
  (->> (parse-input input_file)
       (reduce mover initial-submarine)
       final-position))

(defn part1 [input_file]
  (->> (solve part1-mover input_file)))

(defn part2 [input_file]
  (->> (solve part2-mover input_file)))

(defn -main []
  (let [input_file "./input/day02"]
    (println (part1 input_file))
    (println (part2 input_file))))