(ns aoc-2023.day03
  (:require [clojure.string :as str]
            [aoc-2023.utils :as utils]))

(defn engine-symbol? [c] (not (or (utils/digit? c) (utils/space? c))))
(defn gear-symbol [c] (= c \*))

(defn parse-line [line y]
  (let [m (re-matcher #"\d+" line)]
    (loop [acc ()]
      (if (.find m)
        (recur (conj acc {:value  (read-string (.group m))
                          :points (set (map #(vector % y) (range (.start m) (.end m))))}))
        acc))))

(defn parse-input
  ([input] (->> (str/split-lines input)
                (map-indexed #(parse-line %2 %1))
                (apply concat))))

(defn parse-symbols [input]
  (keep (fn [[p v]] (when (engine-symbol? v) {:value v :point p}))
        (utils/parse-grid-chars-to-coords-map input)))


(defn symbol-adjacencies [symbols numbers]
  (map (fn [{:keys [point] :as m}]
         (let [surr (utils/surrounding point)]
           (assoc m :adjacent-numbers (filter #(some (:points %) surr) numbers))))
       symbols))

(defn part1 [input]
  (->> (symbol-adjacencies (parse-symbols input) (parse-input input))
       (mapcat :adjacent-numbers)
       (set)
       (map :value)
       (apply +)))

(defn part2 [input]
  (->> (symbol-adjacencies (parse-symbols input) (parse-input input))
       (keep (fn [{:keys [value adjacent-numbers]}] (when (and (gear-symbol value)
                                                               (= (count adjacent-numbers) 2))
                                                      (transduce (map :value) * adjacent-numbers))))
       (apply +)))

(defn -main []
  (let [input_file (slurp "./input/day03")]
    (println (part1 input_file))
    (println (part2 input_file))))